#!/usr/bin/env python3
"""Consolida a coleção: exclusões, gate final, tipo, classificação 3/5/10/20,
dedupe 45min, itens apagados, atribuição multi-cliente.

Saída: data/final_rows.json  (linhas classificadas por cliente)
"""
import json, glob, os, re, unicodedata
from collections import defaultdict
from datetime import datetime, timedelta

RAW = "/workspace/analise_coleta/raw"
OUT = "/workspace/analise_coleta/data/final_rows.json"
os.makedirs(os.path.dirname(OUT), exist_ok=True)

ME = "bmn.tsena@cma-cgm.com"

CLIENT_FILES = {
    "APL": ["apl_all.jsonl"],
    "ARGOFRUTA": ["argofruta_all.jsonl"],
    "BERNECK": ["berneck_all.jsonl"],
    "BRX": ["brx_all.jsonl"],
    "CAN PACK": ["canpack_oct.jsonl", "canpack_nov.jsonl"],
    "CARGILL": ["cargill_oct.jsonl", "cargill_nov.jsonl", "cargill_nov2.jsonl", "cargill_nov3.jsonl"],
    "CEVA": ["cartocor_all.jsonl"],
    "DSV": ["dsv_w1_w2.jsonl", "dsv_w1_w2b.jsonl", "dsv_w3.jsonl", "dsv_w4.jsonl",
            "dsv_w5a.jsonl", "dsv_w5b.jsonl", "dsv_w5c.jsonl", "dsv_w6.jsonl", "dsv_w7.jsonl"],
    "ED&F MAN": ["edfman_oct.jsonl", "edfman_nov.jsonl"],
    "NATURAL ONE": ["natone_all.jsonl"],
    "NISSAN": ["nissan_p1.jsonl", "nissan_p2.jsonl", "nissan_p3.jsonl", "nissan_p4.jsonl", "nissan_p5.jsonl"],
    "PERNOD RICARD": ["pernod_all.jsonl"],
    "UNILEVER": ["unilever_w1_p1.jsonl", "unilever_w1_p2.jsonl", "unilever_w1_p3.jsonl",
                 "unilever_w1_p4.jsonl", "unilever_w2_p1.jsonl", "unilever_w2_p2.jsonl",
                 "unilever_w2_p4.jsonl", "unilever_p1.jsonl", "unilever_p2.jsonl",
                 "unilever_p3.jsonl", "unilever_p4.jsonl"],
}
DELETED_FILES = {"DSV": ["dsv_del.jsonl"]}

DOMAIN_CLIENTS = {"NATURAL ONE": "natone", "CAN PACK": "canpack", "ED&F MAN": "edfman", "DSV": "dsv"}

# palavra-chave (subjects/addresses) — grafias alternativas
KEYWORDS = {
    "NATURAL ONE": ["natone", "natural one"],
    "CAN PACK": ["canpack", "can pack"],
    "ED&F MAN": ["edfman", "edf man", "edf-br"],
    "DSV": ["dsv"],
    "CARGILL": ["cargill"],
    "BERNECK": ["berneck"],
    "BRX": ["brx"],
    "CEVA": ["cartocor", "ceva"],
    "ARGOFRUTA": ["argofruta"],
    "APL": ["perfilor", "perfiler"],
    "PERNOD RICARD": ["pernod", "pernord"],
    "NISSAN": ["nissan"],
    "UNILEVER": ["unilever"],
    "GROSFILLEX": ["grosfillex", "grofillex"],
}

OUTROS = ["resposta automatica", "automatic reply", "status", "newsletter", "digest",
          "agradec", "welcome", "webinar", "ajuste", "cadastro"]
DOCS = ["nota fiscal", "notas fiscais", "comprovante", "instrucao documentaria", "fatura", "nfs"]
DEM = ["programacao", "coleta", "pre nomeacao", "booking", "liberacao", "vazio", "estufagem",
       "pre stacking", "safra", "draft", "aceite", "carregamento", "agendamento", "ovacao",
       "devolucao", "embarque", "ddl"]
DOCS_WORD = [r"\bnf\b", r"\bnf.\b", r"\bxml\b", r"\bdue\b"]
DEM_WORD = [r"\bord\b|\bordem|\bordens\b", r"\bddl\b"]

EXCL_SUBJ = re.compile(
    r"^(accepted|declined|tentative|atualizado|atualizacao):\s|undeliverable|undeliverable:"
    r"|indicadores sul|indicadores sd|notificacao automatica", re.I)
EXCL_FROM = re.compile(r"postmaster|@thread\.v2|no-reply|noreply", re.I)


def as_list(v):
    if v is None:
        return []
    if isinstance(v, list):
        return [x.strip() for x in v if isinstance(x, str) and x.strip()]
    if isinstance(v, str):
        return [x.strip() for x in re.split(r"[,;]", v) if x.strip()]
    return []


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def strip_prefixes(s):
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r"^\s*(re|res|fw|fwd|enc|r[i]|res:)\s*:\s*", "", s, flags=re.I)
    return s.strip()


def classify(subject_norm_full):
    n = subject_norm_full
    for k in OUTROS:
        if k in n:
            return "Outros"
    for pat in DOCS_WORD:
        if re.search(pat, n):
            return "Doc"
    for k in DOCS:
        if k in n:
            return "Doc"
    for pat in DEM_WORD:
        if re.search(pat, n):
            return "Demanda"
    for k in DEM:
        if k in n:
            return "Demanda"
    return "Outros"


def clean_subject_display(s):
    return norm(s)


def subject_key(subject):
    return strip_prefixes(norm(subject))


def client_match_in_subject(norm_subj, client):
    for kw in KEYWORDS[client]:
        if kw in norm_subj:
            return True
    return False


def addr_matches(client, row):
    addrs = [row["from"]] + as_list(row.get("to")) + as_list(row.get("cc"))
    dom = DOMAIN_CLIENTS.get(client)
    if dom is not None:
        return any(a and dom in a.lower() for a in addrs)
    kws = KEYWORDS[client]
    return any(any(kw in (a or "").lower() for kw in kws) for a in addrs)


def first_kw_pos(norm_subj, client):
    best = position = None
    for kw in KEYWORDS[client]:
        p = norm_subj.find(kw)
        if p >= 0 and (position is None or p < position):
            position = p
    return position if position is not None else 10**9


# ---------- load pool ----------
pool = {}          # id -> row (main)
deleted = {}       # key(date,subj_norm,from) -> True
for cli, files in CLIENT_FILES.items():
    for fname in files:
        path = os.path.join(RAW, fname)
        if not os.path.exists(path):
            continue
        for line in open(path, encoding="utf-8"):
            if not line.strip():
                continue
            row = json.loads(line)
            if "from" not in row:
                continue  # registro de skip/log, não é um e-mail
            pool.setdefault(row["id"], row)

for cli, files in DELETED_FILES.items():
    for fname in files:
        path = os.path.join(RAW, fname)
        for line in open(path, encoding="utf-8"):
            if not line.strip():
                continue
            row = json.loads(line)
            if "from" not in row:
                continue
            deleted[(row["date"], subject_key(row["subject"]), (row["from"] or "").lower())] = True
            main_exists = False
            pool.setdefault(row["id"], row)
            pool[row["id"]]["deleted"] = True

# gate final + client membership
gated = defaultdict(list)
gate_fail = 0
for _id, row in pool.items():
    addrs = {(a or "").lower() for a in [row["from"]] + as_list(row.get("to")) + as_list(row.get("cc"))}
    if not (ME in addrs or "bma.road-southeast@cma-cgm.com" in addrs or "bma.road-south@cma-cgm.com" in addrs):
        gate_fail += 1
        continue
    ns = norm(row["subject"])
    matched = []
    for cli in CLIENT_FILES:
        if cli in KEYWORDS and client_match_in_subject(ns, cli):
            matched.append(cli)
        elif cli in DOMAIN_CLIENTS and addr_matches(cli, row):
            matched.append(cli)
    if not matched:
        continue

    ipos = 10**9
    for cli in matched:
        if cli in DOMAIN_CLIENTS:
            isub = dfound = None
            isub = ns
            p = 10**9
            for kw in KEYWORDS.get(cli, [DOMAIN_CLIENTS[cli]]):
                q = ns.find(kw)
                if q >= 0:
                    p = min(p, q)
            ip = p
        else:
            ip = first_kw_pos(ns, cli)
        if ip < ipos:
            ipos = ip
    best = 10**9
    best_cli = None
    for cli in matched:
        p = first_kw_pos(ns, cli) if cli not in DOMAIN_CLIENTS else min(
            [ns.find(kw) for kw in KEYWORDS.get(cli, []) if ns.find(kw) >= 0] or [10**9])
        if p < best:
            best = p
            best_cli = cli
    if best == 10**9:
        best_cli = sorted(matched)[0]
    gated[best_cli].append(row)

# exclusões + tipo + classificação
final = []
excluded = []
for cli, rows in gated.items():
    for row in rows:
        ns_full = norm(row["subject"])
        ns_key = subject_key(row["subject"])
        if EXCL_SUBJ.search(ns_full) or EXCL_FROM.search(row["from"] or ""):
            excluded.append((cli, row["date"], row["subject"]))
            continue
        is_sent = (row["from"] or "").lower() == ME
        cls = classify(ns_full)
        final.append({
            "client": cli,
            "id": row["id"],
            "folder": row.get("folder", "main"),
            "date": row["date"],
            "nm_from": norm(row["from"] or ""),
            "from": row["from"],
            "to": as_list(row.get("to")),
            "cc": as_list(row.get("cc")),
            "subject": row["subject"],
            "subj_key": ns_key,
            "tipo": "Enviado" if is_sent else "Recebido",
            "class": cls if not is_sent else None,
            "minutos": 10 if is_sent else {"Doc": 3, "Demanda": 20, "Outros": 5}[cls],
            "sit": "Contado",
            "deleted": bool(row.get("deleted")),
        })

# dedupe 45min por assunto normalizado (com fusão de réplicas idênticas)
by_cli_key = defaultdict(list)
for r in final:
    by_cli_key[(r["client"], r["subj_key"])].append(r)

dupes = 0
for (cli, _k), grp in by_cli_key.items():
    grp.sort(key=lambda r: r["date"])
    seen_dt = []
    for r in grp:
        dt = datetime.strptime(r["date"], "%Y-%m-%dT%H:%M:%SZ")
        near = any(abs((dt - d).total_seconds()) <= 45 * 60 for d in seen_dt)
        near_exact = any((dt - d).total_seconds() == 0 for d in seen_dt)
        if r.get("deleted"):
            r["minutos"] = 0
            r["sit"] = "Apagado (fora da contagem)"
            continue
        if near:
            r["minutos"] = 0
            r["sit"] = "Duplicado (fora da contagem)"
            dupes += 1
        else:
            seen_dt.append(dt)

with open(OUT, "w", encoding="utf-8") as f:
    json.dump(final, f, ensure_ascii=False, indent=1)

# --------- summary ---------
summary = defaultdict(lambda: {"Doc": 0, "Demanda": 0, "Outros": 0, "Recebidos": 0, "Enviados": 0, "min": 0})
days_cli = defaultdict(set)
for r in final:
    if r["sit"] != "Contado" or r["deleted"]:
        continue
    d = (datetime.strptime(r["date"], "%Y-%m-%dT%H:%M:%SZ") - timedelta(hours=3)).date().isoformat()
    days_cli[r["client"]].add(d)
    s = summary[r["client"]]
    s["min"] += r["minutos"]
    if r["tipo"] == "Enviado":
        s["Enviados"] += 1
    else:
        s["Recebidos"] += 1
        s[r["class"]] += 1

print("rows:", len(final), "| gate_fail:", gate_fail, "| excluded:", len(excluded), "| dupes:", dupes)
for cli in sorted(summary, key=lambda c: -summary[c]["min"]):
    s = summary[cli]
    print(f"{cli:14s} doc={s['Doc']:4d} dem={s['Demanda']:4d} oth={s['Outros']:4d} "
          f"rec={s['Recebidos']:4d} env={s['Enviados']:4d} min={s['min']:5d} days={len(days_cli[cli])}")
tot = sum(s["min"] for s in summary.values())
all_days = set().union(*days_cli.values()) if days_cli else set()
print("TOTAL min:", tot, "=", tot // 60, "h", tot % 60, "| dias com atividade (qualquer cliente):", len(all_days))
print("excluded:", excluded[:5])
