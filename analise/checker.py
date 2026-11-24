#!/usr/bin/env python3
"""Checker independente das workbooks: reavalia cada formula gerada
(COUNTIFS/SUMIFS/IF/SUM e aritmetica) contra os dados reais das abas,
comparando com valores recalculados de final_rows.json. Sai 'CLEAN' quando ok.
"""
import json
import re
import sys
from collections import defaultdict
from datetime import datetime, timedelta

from openpyxl import load_workbook

ROWS_JSON = "/workspace/analise_coleta/data/final_rows.json"
OUTDIR = "/workspace/github__tayanevsena__analise-tempo-clientes/entrega"

MONTHS = [("2026-08", "ago"), ("2026-09", "set"), ("2026-10", "out"), ("2026-11", "nov")]
DIAS_UTEIS_MES = {"ago": 11, "set": 21, "out": 21, "nov": 9}
DIAS_UTEIS_TOTAL = 62
EXPEDIENTE = 540

# ---------------------------------------------------------------- dados reais
rows = json.load(open(ROWS_JSON, encoding="utf-8"))


def local_day(dt_iso):
    return (datetime.strptime(dt_iso, "%Y-%m-%dT%H:%M:%SZ") - timedelta(hours=3)).date().isoformat()


def cli_stats(rows, cli=None, month=None, require_contado=True):
    d = o = dem = rec = env = minu = 0
    for r in rows:
        if sit_ok(r, cli, month, require_contado):
            minu += r["minutos"]
            if r["tipo"] == "Enviado":
                env += 1
            else:
                rec += 1
                cls = r["class"]
                if cls == "Doc":
                    d += 1
                elif cls == "Demanda":
                    dem += 1
                else:
                    o += 1
    return {"Doc": d, "Demanda": dem, "Outros": o, "Rec": rec, "Env": env, "min": minu}


def sit_ok(r, cli, month, contado=True):
    if cli is not None and r["client"] != cli:
        return False
    if month is not None and r["date"][:7] != month:
        return False
    if contado and r["sit"] != "Contado":
        return False
    return True


ALL_CLIENTS = sorted({r["client"] for r in rows})
ALL_14 = ["CARGILL", "BERNECK", "BRX", "CEVA", "ARGOFRUTA", "APL",
          "PERNOD RICARD", "NISSAN", "UNILEVER", "GROSFILLEX",
          "NATURAL ONE", "CAN PACK", "ED&F MAN", "DSV"]
minutos_cli = {}
for c in ALL_14:
    minutos_cli[c] = cli_stats(rows, c)["min"]
ORDER = sorted(ALL_14, key=lambda c: (-minutos_cli[c], c))

dias_cli = defaultdict(set)
for r in rows:
    if r["sit"] == "Contado":
        dias_cli[r["client"]].add(local_day(r["date"]))
DIAS_ATIV_CLI = {c: len(dias_cli[c]) for c in ALL_14}
DIAS_ATIV_TOTAL = len(set().union(*dias_cli.values()))
DIAS_ATIV_MES = {c: {lbl: len({local_day(r["date"]) for r in rows
                               if r["client"] == c and r["date"][:7] == m and r["sit"] == "Contado"})
                     for m, lbl in MONTHS} for c in ALL_14}
MIN_MES = {c: {lbl: cli_stats(rows, c, m)["min"] for m, lbl in MONTHS} for c in ALL_14}

# ---------------------------------------------------------------- mini parser
TOK = re.compile(r"""
    (?P<sheetrange>(?:'[^']+'|[A-Za-z_][\w.]{0,30})!\$?[A-Z]{1,3}\$?:\$?[A-Z]{1,3})
  | (?P<localrange>\$?[A-Z]{1,3}\$?\d+:\$?[A-Z]{1,3}\$?\d+)
  | (?P<cell>(?:'[A-Za-z_][\w.]{0,30}'|[A-Za-z_][\w.]{0,30})!\$?[A-Z]{1,2}\$?\d+|\$?[A-Z]{1,2}\$?\d+)
  | (?P<num>\d+(?:\.\d+)?)
  | (?P<str>"[^"]*")
  | (?P<ident>[A-Za-z_][A-Za-z0-9_.]*)
  | (?P<op><>|>=|<=|[=+*/(),<>-])
  | (?P<ws>\s+)
""", re.X)

ERRORS = []


def tokenize(f):
    toks, i = [], 0
    while i < len(f):
        m = TOK.match(f, i)
        if not m:
            ERRORS.append(f"tokenize fail at {f[i:i+20]!r} in {f!r}")
            return None
        i = m.end()
        if m.lastgroup == "ws":
            continue
        toks.append((m.lastgroup, m.group(0)))
    return toks


class Ctx:
    def __init__(self, values, cache=None):
        self.vals = values      # {(sheet, row, col): value}
        self.sh = None          # sheet atual
        self.frames = {}        # memo formulas: (sheet,row,col) -> value
        self.stack = set()
        self.cache = cache if cache is not None else {}
        self.maxrows = defaultdict(int)
        for (s, r, _c) in values:
            self.maxrows[s] = max(self.maxrows[s], r)

    def cell(self, sheet, row, col):
        key = (sheet, row, col)
        if key in self.stack:
            return 0
        if key in self.frames:
            return self.frames[key]
        raw = self.vals.get(key)
        if raw is None:
            return 0
        if isinstance(raw, str) and raw.startswith("="):
            self.stack.add(key)
            v = eval_formula(raw[1:], self, sheet, row, col)
            self.stack.discard(key)
            self.frames[key] = v
            return v
        if isinstance(raw, str):
            try:
                return float(raw)
            except ValueError:
                return raw
        return raw


def col_letter_to_num(s):
    n = 0
    for ch in s.strip("$"):
        n = n * 26 + ord(ch) - 64
    return n


def parse_range(sheet, spec):
    a, b = spec.split(":")
    if "!" in spec:
        sheet_name, rng = spec.split("!")
        sheet_name = sheet_name.strip("'")
        a, b = rng.split(":")
    else:
        sheet_name = sheet
    ca = re.match(r"\$?([A-Z]{1,3})", a).group(1)
    cb = re.match(r"\$?([A-Z]{1,3})", b).group(1)
    c1, c2 = col_letter_to_num(ca), col_letter_to_num(cb)
    ma = re.search(r"(\d+)", a)
    mb = re.search(r"(\d+)", b)
    r1 = int(ma.group(1)) if ma else None
    r2 = int(mb.group(1)) if mb else None
    return sheet_name, c1, c2, r1, r2


def criteria_match(val, crit):
    if isinstance(crit, str):
        return isinstance(val, str) and val.strip().lower() == crit.strip().lower()
    if isinstance(val, (int, float)) and isinstance(crit, (int, float)):
        return abs(val - crit) < 1e-9
    return False


class Parser:
    def __init__(self, toks, ctx):
        self.t = toks
        self.i = 0
        self.ctx = ctx

    def peek(self):
        return self.t[self.i] if self.i < len(self.t) else (None, None)

    def eat(self, val=None):
        kind, tok = self.peek()
        if val is not None and tok != val:
            raise ValueError(f"expected {val} got {tok}")
        self.i += 1
        return kind, tok

    # expr := comparison
    def expr(self):
        left = self.additive()
        while self.peek()[1] in ("=", "<>", "<", ">", "<=", ">="):
            op = self.eat()[1]
            right = self.additive()
            a, b = left, right
            if op == "=":
                left = criteria_match(a, b) or (isinstance(a, (int, float)) and isinstance(b, (int, float)) and abs(a - b) < 1e-9)
            elif op == "<>":
                left = not (a == b)
            else:
                try:
                    left = {"<": a < b, ">": a > b, "<=": a <= b, ">=": a >= b}[op]
                except TypeError:
                    left = False
            left = bool(left) * 1  # bool->num (TRUE/FALSE when printed, here numeric)
            if isinstance(left, int) and left in (0, 1):
                left = float(left)
        return left

    def additive(self):
        left = self.term()
        while self.peek()[1] in ("+", "-"):
            op = self.eat()[1]
            right = self.term()
            left = left + right if op == "+" else left - right
        return left

    def term(self):
        left = self.factor()
        while self.peek()[1] in ("*", "/"):
            op = self.eat()[1]
            right = self.factor()
            if op == "*":
                left = left * right
            else:
                left = left / right if right != 0 else 0
        return left

    def factor(self):
        kind, tok = self.peek()
        if tok == "(":
            self.eat()
            v = self.expr()
            self.eat(")")
            return v
        if tok == "-":
            self.eat()
            return -self.factor()
        if kind == "num":
            self.eat()
            return float(tok)
        if kind == "str":
            self.eat()
            return tok.strip('"')
        if kind == "sheetrange":
            self.eat()
            return ("range",) + parse_range(None, tok)
        if kind == "localrange":
            self.eat()
            return ("range",) + parse_range(self.ctx.sh, tok)
        if kind == "cell":
            self.eat()
            sh, coord = self.ctx.sh, tok
            if "!" in tok:
                sh, coord = tok.split("!")
                sh = sh.strip("'")
            m = re.match(r"\$?([A-Z]{1,2})\$?(\d+)", coord)
            return self.ctx.cell(sh, int(m.group(2)), col_letter_to_num(m.group(1)))
        if kind == "ident":
            self.eat()
            name = tok.upper()
            if name in ("TRUE", "FALSE"):
                return 1.0 if name == "TRUE" else 0.0
            self.eat("(")
            args = []
            if self.peek()[1] != ")":
                args.append(self.expr())
                while self.peek()[1] == ",":
                    self.eat()
                    args.append(self.expr())
            self.eat(")")
            return self.call(name, args)
        raise ValueError(f"unexpected token {tok}")

    def call(self, name, args):
        if name == "IF":
            cond = args[0]
            return args[1] if cond else (args[2] if len(args) > 2 else 0)
        if name == "SUM":
            tot = 0
            for a in args:
                tot += self.rangesum(a)
            return tot
        if name == "COUNTIFS":
            pairs = [(args[i], args[i + 1]) for i in range(0, len(args), 2)]
            return float(self.countifs(pairs))
        if name == "SUMIFS":
            sumr = args[0]
            pairs = [(args[i], args[i + 1]) for i in range(1, len(args), 2)]
            anchor_rows = self.range_rows(pairs[0][0])
            tot = 0
            for r in anchor_rows:
                if all(self.range_match(rng, r, crit) for rng, crit in pairs):
                    v = self.range_val(sumr, r)
                    if isinstance(v, (int, float)):
                        tot += v
            return tot
        if name in ("ROUND", "ABS"):
            v = args[0]
            if name == "ABS":
                return abs(v)
            return round(v, int(args[1])) if len(args) > 1 else round(v)
        raise ValueError(f"func {name} not supported")

    def range_rows(self, rng):
        """dict row -> lista de valores avaliados do intervalo, por linha."""
        if not (isinstance(rng, tuple) and rng and rng[0] == "range"):
            raise ValueError(f"not a range: {rng}")
        _, sh, c1, c2, r1, r2 = rng
        lo = r1 or 1
        hi = r2 if r2 is not None else self.ctx.maxrows.get(sh, 0)
        if r1 is not None:
            hi = r2
        key = ("C", sh, c1, c2, lo, r2)
        if key in self.ctx.cache:
            return self.ctx.cache[key]
        out = {}
        for r in range(lo, hi + 1):
            vals = []
            for c in range(c1, c2 + 1):
                raw = self.ctx.vals.get((sh, r, c))
                if raw is not None:
                    vals.append(self.ctx.cell(sh, r, c))
            if vals:
                out[r] = vals
        self.ctx.cache[key] = out
        return out

    def range_val(self, rng, r):
        v = self.range_rows(rng).get(r)
        return v[0] if isinstance(v, list) else v

    def range_match(self, rng, r, crit):
        v = self.range_rows(rng).get(r)
        if not v:
            return False
        return any(criteria_match(x, crit) for x in v)

    def range_cells(self, rng):
        rows = self.range_rows(rng)
        _, sh, c1, c2, _r1, _r2 = rng
        out = []
        for r in sorted(rows):
            for c in range(c1, c2 + 1):
                if (sh, r, c) in self.ctx.vals:
                    out.append(((sh, r, c), rows[r]))
                    break
        return out

    def countifs(self, pairs):
        anchor_rows = self.range_rows(pairs[0][0])
        cnt = 0
        for r in anchor_rows:
            if all(self.range_match(rng, r, crit) for rng, crit in pairs):
                cnt += 1
        return float(cnt)

    def rangesum(self, rng):
        rows = self.range_rows(rng)
        return sum(x for vals in rows.values() for x in vals
                   if isinstance(x, (int, float)))


def eval_formula(f, ctx, sheet, row, col):
    toks = tokenize(f)
    if toks is None:
        return None
    old = ctx.sh
    ctx.sh = sheet
    try:
        p = Parser(toks, ctx)
        return p.expr()
    except Exception as e:
        ERRORS.append(f"eval error {sheet}!{row},{col}: {e} :: {f}")
        return None
    finally:
        ctx.sh = old


def load_values(wb):
    vals = {}
    for sh in wb.sheetnames:
        ws = wb[sh]
        for row in ws.iter_rows():
            for cell in row:
                if cell.value is not None:
                    vals[(sh, cell.row, cell.column)] = cell.value
    return vals


# ---------------------------------------------------------------- verificacoes
def close(a, b, tol=1e-6):
    try:
        return abs(float(a) - float(b)) <= tol
    except (TypeError, ValueError):
        return a == b


FAILS = []


def check(where, label, got, want):
    if got is None or not close(got, want):
        FAILS.append(f"{where}: {label} got={got!r} want={want!r}")


def check_wb(path, kind):
    print(f"\n=== {path} ({kind}) ===")
    wb = load_workbook(path)
    need = {"RESUMO", "BASE", "MENSAL", "METODOLOGIA"} | {f"DET_{c}" for c in
           ["CARGILL", "BERNECK", "BRX", "CEVA", "ARGOFRUTA", "APL", "PERNOD", "NISSAN", "UNILEVER", "GROSFILLEX"]}
    missing = need - set(wb.sheetnames)
    if missing:
        FAILS.append(f"{path}: abas ausentes {missing}")

    ctx = Ctx(load_values(wb), None)
    ctx.sh = "RESUMO"

    # BASE: linhas = todas as 1098 rows (incl. dup/apagadas)
    wsB = wb["BASE"]
    n_base = wsB.max_row - 1
    if n_base != len(rows):
        FAILS.append(f"{path}: BASE rows {n_base} != {len(rows)}")
    wsH = wb["METODOLOGIA"]
    met_text = " ".join(str(wsH.cell(row=i, column=1).value or "") for i in range(1, wsH.max_row + 2))
    base_lbl_want = "Base: dias com atividade" if kind == "dias_com_atividade" else "Base: dias úteis"
    if "Base de dias desta versão" not in met_text:
        FAILS.append(f"{path}: METODOLOGIA sem linha 'Base de dias desta versão'")
    elif f"Base de dias desta versão: {base_lbl_want}" not in met_text:
        FAILS.append(f"{path}: METODOLOGIA documenta base errada (esperado {kind})")
    if "road-southeast" not in met_text or "road-northeast" not in met_text:
        FAILS.append(f"{path}: METODOLOGIA sem escopo das listas road-*")

    # DET sheets: contagem por cliente
    det_map = {"CARGILL": "DET_CARGILL", "BERNECK": "DET_BERNECK", "BRX": "DET_BRX",
               "CEVA": "DET_CEVA", "ARGOFRUTA": "DET_ARGOFRUTA", "APL": "DET_APL",
               "PERNOD RICARD": "DET_PERNOD", "NISSAN": "DET_NISSAN",
               "UNILEVER": "DET_UNILEVER", "GROSFILLEX": "DET_GROSFILLEX"}
    for cli, shn in det_map.items():
        n_want = sum(1 for r in rows if r["client"] == cli)
        n_got = wb[shn].max_row - 1
        if n_got != n_want:
            FAILS.append(f"{path}/{shn}: rows {n_got} != {n_want}")

    # RESUMO
    ws = wb["RESUMO"]
    seen_labels = []
    r = 5
    while True:
        name = ws.cell(row=r, column=1).value
        if name is None or name == "TOTAL":
            break
        seen_labels.append(name)
        s = cli_stats(rows, name)
        dias_ref = DIAS_ATIV_CLI.get(name, 0) if kind == "dias_com_atividade" else DIAS_UTEIS_TOTAL
        check(f"RESUMO {name} r{r}", "Doc", ctx.cell("RESUMO", r, 2), s["Doc"])
        check(f"RESUMO {name} r{r}", "Demanda", ctx.cell("RESUMO", r, 3), s["Demanda"])
        check(f"RESUMO {name} r{r}", "Outros", ctx.cell("RESUMO", r, 4), s["Outros"])
        check(f"RESUMO {name} r{r}", "Recebidos", ctx.cell("RESUMO", r, 5), s["Rec"])
        check(f"RESUMO {name} r{r}", "Enviados", ctx.cell("RESUMO", r, 6), s["Env"])
        check(f"RESUMO {name} r{r}", "Minutos", ctx.cell("RESUMO", r, 7), s["min"])
        check(f"RESUMO {name} r{r}", "Horas", ctx.cell("RESUMO", r, 8), round(s["min"] / 60, 6))
        check(f"RESUMO {name} r{r}", "Min/dia", ctx.cell("RESUMO", r, 9),
              round(s["min"] / dias_ref, 6) if dias_ref else 0)
        check(f"RESUMO {name} r{r}", "%exp", ctx.cell("RESUMO", r, 10), round(s["min"] / EXPEDIENTE, 9))
        check(f"RESUMO {name} r{r}", "Dias(K)", ctx.cell("RESUMO", r, 11), dias_ref)
        r += 1
    total_row = r
    if ws.cell(row=total_row, column=1).value != "TOTAL":
        FAILS.append(f"{path}: linha TOTAL nao encontrada na row {total_row}")
    tot_min = sum(minutos_cli[c] for c in ORDER)
    check(f"{path} TOTAL", "Minutos", ctx.cell("RESUMO", total_row, 7), tot_min)
    for j in range(2, 7):
        want = sum(cli_stats(rows, c)[["Doc", "Demanda", "Outros", "Rec", "Env"][j - 2]] for c in ALL_CLIENTS)
        check(f"{path} TOTAL col{j}", "sum", ctx.cell("RESUMO", total_row, j), want)
    dias_tot_ref = DIAS_ATIV_TOTAL if kind == "dias_com_atividade" else DIAS_UTEIS_TOTAL
    check(f"{path} TOTAL", "Horas", ctx.cell("RESUMO", total_row, 8), round(tot_min / 60, 6))
    check(f"{path} TOTAL", "Min/dia", ctx.cell("RESUMO", total_row, 9), round(tot_min / dias_tot_ref, 6))
    check(f"{path} TOTAL", "%exp", ctx.cell("RESUMO", total_row, 10), round(tot_min / EXPEDIENTE, 9))
    check(f"{path} TOTAL", "Dias", ctx.cell("RESUMO", total_row, 11), dias_tot_ref)

    if seen_labels != ORDER:
        FAILS.append(f"{path}: ordenacao RESUMO {seen_labels} != {ORDER}")

    # Indicador mensal
    mh = total_row + 3
    if ws.cell(row=mh, column=1).value != "Cliente":
        FAILS.append(f"{path}: indicador mensal fora da row {mh}")
    ridx = mh + 1
    for cli in ORDER:
        for m, lbl in MONTHS:
            dias_m = (DIAS_ATIV_MES[cli][lbl] if kind == "dias_com_atividade" else DIAS_UTEIS_MES[lbl])
            mm = cli_stats(rows, cli, m)["min"]
            check(f"IND {cli}/{lbl}", "Dias", ctx.cell("RESUMO", ridx, 3), dias_m)
            check(f"IND {cli}/{lbl}", "Min", ctx.cell("RESUMO", ridx, 4), mm)
            check(f"IND {cli}/{lbl}", "Horas", ctx.cell("RESUMO", ridx, 5), round(mm / 60, 6))
            check(f"IND {cli}/{lbl}", "Min/dia", ctx.cell("RESUMO", ridx, 6),
                  round(mm / dias_m, 6) if dias_m else 0)
            check(f"IND {cli}/{lbl}", "%dia", ctx.cell("RESUMO", ridx, 7),
                  round(mm / (EXPEDIENTE * dias_m), 9) if dias_m else 0)
            ridx += 1

    # MENSAL
    wsM = wb["MENSAL"]
    rM = 4
    for cli in ORDER:
        if wsM.cell(row=rM, column=1).value != cli:
            FAILS.append(f"{path}/MENSAL: cliente {cli} fora da row {rM}")
            break
        for j, (m, lbl) in enumerate(MONTHS, 2):
            check(f"MENSAL {cli}/{lbl}", "Min", ctx.cell("MENSAL", rM, j), cli_stats(rows, cli, m)["min"])
        check(f"MENSAL {cli}/Total", "Min", ctx.cell("MENSAL", rM, 6), minutos_cli[cli])
        if kind == "dias_com_atividade":
            dias_ref_m = DIAS_ATIV_MES[cli]
        else:
            dias_ref_m = {lbl: DIAS_UTEIS_MES[lbl] for _, lbl in MONTHS}
        for j, (m, lbl) in enumerate(MONTHS, 2):
            check(f"MENSAL {cli}/{lbl}", "Dias", ctx.cell("MENSAL", rM + 1, j), dias_ref_m[lbl])
        tot_d = sum(dias_ref_m.values())
        check(f"MENSAL {cli}/Total", "Dias", ctx.cell("MENSAL", rM + 1, 6), tot_d)
        for j in range(2, 6):
            L = chr(64 + j)
            dm = dias_ref_m[MONTHS[j - 2][1]]
            mn = cli_stats(rows, cli, MONTHS[j - 2][0])["min"]
            check(f"MENSAL {cli}/{MONTHS[j-2][1]}", "min/dia", ctx.cell("MENSAL", rM + 2, j),
                  round(mn / dm, 6) if dm else 0)
        mm_tot = minutos_cli[cli]
        check(f"MENSAL {cli}/Total", "min/dia", ctx.cell("MENSAL", rM + 2, 6),
              round(mm_tot / tot_d, 6) if tot_d else 0)
        rM += 4

    print(f"  sheets={len(wb.sheetnames)} BASE_rows={n_base} TOTAL_row={total_row}")


if __name__ == "__main__":
    for path, kind in [
        (f"{OUTDIR}/tempo_clientes_sul_sudeste_dias_com_atividade.xlsx", "dias_com_atividade"),
        (f"{OUTDIR}/tempo_clientes_sul_sudeste_dias_uteis.xlsx", "dias_uteis"),
    ]:
        check_wb(path, kind)
    if ERRORS:
        print("\nERROS DE AVALIACAO:")
        for e in ERRORS[:15]:
            print(" -", e)
    if FAILS:
        print(f"\nFALHAS: {len(FAILS)}")
        for f in FAILS[:40]:
            print(" -", f)
        print("STATUS: NOT CLEAN")
        sys.exit(1)
    print("\nSTATUS: CLEAN — todas as formulas e valores conferem com final_rows.json")
