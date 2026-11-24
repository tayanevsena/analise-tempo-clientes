#!/usr/bin/env python3
"""Gera as DUAS pastas de planilha (dias com atividade / dias úteis).

Estrutura por workbook: RESUMO, MENSAL, 10x DET_*, BASE, METODOLOGIA.
Fórmulas vivas: COUNTIFS/SUMIFS sobre as abas DET (clientes de palavra-chave)
e sobre a aba BASE (clientes por domínio + TOTAL).
"""
import json
import os
from datetime import datetime, timedelta

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter

ROWS_JSON = "/workspace/analise_coleta/data/final_rows.json"
OUTDIR = "/workspace/github__tayanevsena__analise-tempo-clientes/entrega"
os.makedirs(OUTDIR, exist_ok=True)

ME = "bmn.tsena@cma-cgm.com"

CLIENTS_BASE = ["CARGILL", "BERNECK", "BRX", "CEVA", "ARGOFRUTA", "APL",
                "PERNOD RICARD", "NISSAN", "UNILEVER", "GROSFILLEX"]
DOMAIN_CLIENTS = ["NATURAL ONE", "CAN PACK", "ED&F MAN", "DSV"]

DET_SHEET = {
    "CARGILL": "DET_CARGILL", "BERNECK": "DET_BERNECK", "BRX": "DET_BRX",
    "CEVA": "DET_CEVA", "ARGOFRUTA": "DET_ARGOFRUTA", "APL": "DET_APL",
    "PERNOD RICARD": "DET_PERNOD", "NISSAN": "DET_NISSAN",
    "UNILEVER": "DET_UNILEVER", "GROSFILLEX": "DET_GROSFILLEX",
}

MONTHS = [("2026-08", "ago"), ("2026-09", "set"), ("2026-10", "out"), ("2026-11", "nov")]
DIAS_UTEIS_MES = {"2026-08": 11, "2026-09": 21, "2026-10": 21, "2026-11": 9}

HEAD_FILL = PatternFill("solid", fgColor="1F4E78")
HEAD_FONT = Font(color="FFFFFF", bold=True)
TOT_FILL = PatternFill("solid", fgColor="D9E1F2")
EDIT_FILL = PatternFill("solid", fgColor="FFF2CC")
THIN = Side(style="thin", color="B0B0B0")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def local_date(dt_iso):
    return datetime.strptime(dt_iso, "%Y-%m-%dT%H:%M:%SZ") - timedelta(hours=3)


def fmt_de_para(r):
    de = r["from"] or ""
    para = "; ".join(x for x in (r.get("to") or []) if x)
    return de, para


def det_rows_for(rows, cli):
    out = []
    for r in rows:
        if r["client"] != cli:
            continue
        de, para = fmt_de_para(r)
        cc = "; ".join(x for x in (r.get("cc") or []) if x)
        cls = r["class"] if r["tipo"] == "Recebido" else "Enviado (10 min)"
        out.append([r["date"].replace("T", " ").replace("Z", ""), r["date"][:7],
                    r["tipo"], de, para, cc, r["subject"], cls, r["minutos"], r["sit"]])
    out.sort(key=lambda x: x[0])
    return out


def write_table(ws, header, data, widths, start_row=1):
    for j, h in enumerate(header, 1):
        c = ws.cell(row=start_row, column=j, value=h)
        c.fill, c.font, c.border = HEAD_FILL, HEAD_FONT, BORDER
        c.alignment = Alignment(vertical="center")
    for i, row in enumerate(data, start_row + 1):
        for j, v in enumerate(row, 1):
            c = ws.cell(row=i, column=j, value=v)
            c.border = BORDER
            if isinstance(v, str):
                c.alignment = Alignment(vertical="top", wrap_text=False)
    for j, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(j)].width = w
    ws.freeze_panes = ws.cell(row=start_row + 1, column=1)


def sumifs(col_sum, sheet, crits):
    pairs = []
    for col, crit in crits:
        pairs.append(f"'{sheet}'!${col}:${col}")
        pairs.append(crit)
    return f"SUMIFS('{sheet}'!${col_sum}:${col_sum},{','.join(pairs)})"


def countifs(sheet, pairs):
    parts = []
    for col, crit in pairs:
        parts.append(f"'{sheet}'!${col}:${col}")
        parts.append(crit)
    return f"COUNTIFS({','.join(parts)})"


def build(base_kind, rows, path):
    """base_kind: 'dias_com_atividade' | 'dias_uteis'"""
    wb = Workbook()

    counted = [r for r in rows if r["sit"] == "Contado" and not r.get("deleted")]

    minutos_cli = {}
    dias_cli = {}
    dias_mes = {c: {m: 0 for m, _ in MONTHS} for c in CLIENTS_BASE + DOMAIN_CLIENTS}
    min_mes = {c: {m: 0 for m, _ in MONTHS} for c in CLIENTS_BASE + DOMAIN_CLIENTS}
    for c in CLIENTS_BASE + DOMAIN_CLIENTS:
        cr = [r for r in counted if r["client"] == c]
        minutos_cli[c] = sum(r["minutos"] for r in cr)
        d = sorted({local_date(r["date"]).date().isoformat() for r in cr})
        dias_cli[c] = len(d)
        for m, _ in MONTHS:
            dias_mes[c][m] = len({local_date(r["date"]).date().isoformat()
                                  for r in cr if r["date"][:7] == m})
            min_mes[c][m] = sum(r["minutos"] for r in cr if r["date"][:7] == m)

    all_days = {local_date(r["date"]).date().isoformat() for r in counted}
    dias_total_union = len(all_days)

    if base_kind == "dias_uteis":
        dias_ref = {c: sum(DIAS_UTEIS_MES.values()) for c in CLIENTS_BASE + DOMAIN_CLIENTS}
        dias_total = 62
        dias_mes_ref = {c: dict(DIAS_UTEIS_MES) for c in CLIENTS_BASE + DOMAIN_CLIENTS}
    else:
        dias_ref = dict(dias_cli)
        dias_total = dias_total_union
        dias_mes_ref = {c: dict(dias_mes[c]) for c in CLIENTS_BASE + DOMAIN_CLIENTS}

    order = sorted(CLIENTS_BASE + DOMAIN_CLIENTS, key=lambda c: (-minutos_cli[c], c))

    # ---------------- DET tabs ----------------
    for cli in CLIENTS_BASE:
        ws = wb.create_sheet(DET_SHEET[cli])
        data = det_rows_for(rows, cli)
        write_table(ws, ["Data (UTC)", "Mês", "Tipo", "De", "Para", "CC", "Assunto",
                         "Classificação", "Minutos", "Situação"], data,
                    [17, 8, 10, 26, 40, 40, 60, 16, 8, 24])

    # ---------------- BASE ----------------
    ws = wb.create_sheet("BASE")
    base_data = []
    for r in sorted(rows, key=lambda x: (x["date"], x["client"])):
        de, para = fmt_de_para(r)
        cc = "; ".join(x for x in (r.get("cc") or []) if x)
        cls = r["class"] if r["tipo"] == "Recebido" else "Enviado (10 min)"
        base_data.append([r["client"], r["date"].replace("T", " ").replace("Z", ""), r["date"][:7],
                          r["tipo"], de, para, cc, r["subject"], cls, r["minutos"], r["sit"]])
    write_table(ws, ["Cliente", "Data (UTC)", "Mês", "Tipo", "De", "Para", "CC", "Assunto",
                     "Classificação", "Minutos", "Situação"], base_data,
                [14, 17, 8, 10, 26, 40, 40, 60, 16, 8, 24])

    # ---------------- RESUMO ----------------
    ws = wb.create_sheet("RESUMO", 0)
    ws.cell(row=1, column=1, value="Tempo dedicado por cliente – Sul/Sudeste")
    ws.cell(row=1, column=1).font = Font(bold=True, size=14)
    base_lbl = ("Base: dias com atividade (dias corridos UTC−3 com ≥1 e-mail contabilizado)"
                if base_kind == "dias_com_atividade" else
                "Base: dias úteis (15/08–15/11/2026, excl. fins de semana e feriados 07/09, 12/10 e 02/11 = 62 dias)")
    ws.cell(row=2, column=1, value=base_lbl + " | Expediente-padrão: 540 min")

    hdr = ["Cliente", "Doc", "Demanda", "Outros", "Recebidos", "Enviados", "Minutos", "Horas",
           "Min/dia", "% expediente", "Dias (referência)"]
    for j, h in enumerate(hdr, 1):
        c = ws.cell(row=4, column=j, value=h)
        c.fill, c.font, c.border = HEAD_FILL, HEAD_FONT, BORDER
    row_i, first_data_row = 5, 5
    for cli in order:
        if cli in DET_SHEET:
            sh = DET_SHEET[cli]
            doc = "=" + countifs(sh, [("H", '"Doc"'), ("J", '"Contado"')])
            dem = "=" + countifs(sh, [("H", '"Demanda"'), ("J", '"Contado"')])
            oth = "=" + countifs(sh, [("H", '"Outros"'), ("J", '"Contado"')])
            rec = "=" + countifs(sh, [("C", '"Recebido"'), ("J", '"Contado"')])
            env = "=" + countifs(sh, [("C", '"Enviado"'), ("J", '"Contado"')])
            mins = "=" + sumifs("I", sh, [("J", '"Contado"')])
        else:
            doc = "=" + countifs("BASE", [("A", f'"{cli}"'), ("I", '"Doc"'), ("K", '"Contado"')])
            dem = "=" + countifs("BASE", [("A", f'"{cli}"'), ("I", '"Demanda"'), ("K", '"Contado"')])
            oth = "=" + countifs("BASE", [("A", f'"{cli}"'), ("I", '"Outros"'), ("K", '"Contado"')])
            rec = "=" + countifs("BASE", [("A", f'"{cli}"'), ("D", '"Recebido"'), ("K", '"Contado"')])
            env = "=" + countifs("BASE", [("A", f'"{cli}"'), ("D", '"Enviado"'), ("K", '"Contado"')])
            mins = f'=SUMIFS(BASE!$J:$J,BASE!$A:$A,"{cli}",BASE!$K:$K,"Contado")'
        ws.cell(row=row_i, column=1, value=cli).border = BORDER
        for j, v in enumerate([doc, dem, oth, rec, env, mins], 2):
            ws.cell(row=row_i, column=j, value=v).border = BORDER
        c = ws.cell(row=row_i, column=8, value=f"=G{row_i}/60"); c.number_format = "0.00"; c.border = BORDER
        c = ws.cell(row=row_i, column=9, value=f"=IF(K{row_i}=0,0,G{row_i}/K{row_i})"); c.number_format = "0.0"; c.border = BORDER
        c = ws.cell(row=row_i, column=10, value=f"=G{row_i}/540"); c.number_format = "0.0%"; c.border = BORDER
        c = ws.cell(row=row_i, column=11, value=dias_ref[cli]); c.fill, c.border = EDIT_FILL, BORDER
        row_i += 1
    total_row = row_i
    ws.cell(row=total_row, column=1, value="TOTAL").font = Font(bold=True)
    for j in range(2, 8):
        L = get_column_letter(j)
        c = ws.cell(row=total_row, column=j,
                    value=f"=SUM({L}{first_data_row}:{L}{total_row-1})")
        c.font, c.fill, c.border = Font(bold=True), TOT_FILL, BORDER
    c = ws.cell(row=total_row, column=8, value=f"=G{total_row}/60")
    c.number_format = "0.00"; c.font, c.fill, c.border = Font(bold=True), TOT_FILL, BORDER
    c = ws.cell(row=total_row, column=9, value=f"=G{total_row}/K{total_row}")
    c.number_format = "0.0"; c.font, c.fill, c.border = Font(bold=True), TOT_FILL, BORDER
    c = ws.cell(row=total_row, column=10, value=f"=G{total_row}/540")
    c.number_format = "0.0%"; c.font, c.fill, c.border = Font(bold=True), TOT_FILL, BORDER
    c = ws.cell(row=total_row, column=11, value=dias_total)
    c.font, c.fill, c.border = Font(bold=True), TOT_FILL, BORDER
    for j in range(1, 12):
        ws.column_dimensions[get_column_letter(j)].width = {
            1: 15, 2: 6, 3: 8, 4: 7, 5: 10, 6: 9, 7: 9, 8: 8, 9: 8, 10: 12, 11: 16}.get(j, 12)

    # Indicador mensal
    ws.cell(row=total_row + 2, column=1, value="Indicador mensal").font = Font(bold=True, size=12)
    mh = total_row + 3
    for j, h in enumerate(["Cliente", "Mês", "Dias", "Minutos", "Horas", "Min/dia", "% do dia"], 1):
        c = ws.cell(row=mh, column=j, value=h)
        c.fill, c.font, c.border = HEAD_FILL, HEAD_FONT, BORDER
    r = mh + 1
    for cli in order:
        for mk, mlabel in MONTHS:
            if cli in DET_SHEET:
                mins_f = "=" + sumifs("I", DET_SHEET[cli], [("B", f'"{mk}"'), ("J", '"Contado"')])
            else:
                mins_f = (f'=SUMIFS(BASE!$J:$J,BASE!$A:$A,"{cli}",BASE!$K:$K,"Contado",'
                          f'BASE!$C:$C,"{mk}")')
            ws.cell(row=r, column=1, value=cli).border = BORDER
            ws.cell(row=r, column=2, value=mlabel).border = BORDER
            c = ws.cell(row=r, column=3, value=dias_mes_ref[cli][mk]); c.fill, c.border = EDIT_FILL, BORDER
            ws.cell(row=r, column=4, value=mins_f).border = BORDER
            c = ws.cell(row=r, column=5, value=f"=D{r}/60"); c.number_format = "0.00"; c.border = BORDER
            c = ws.cell(row=r, column=6, value=f"=IF(C{r}=0,0,D{r}/C{r})"); c.number_format = "0.0"; c.border = BORDER
            c = ws.cell(row=r, column=7, value=f"=IF(C{r}=0,0,D{r}/(540*C{r}))"); c.number_format = "0.0%"; c.border = BORDER
            r += 1
    ws.freeze_panes = "A5"

    # ---------------- MENSAL ----------------
    ws = wb.create_sheet("MENSAL")
    ws.cell(row=1, column=1, value="Minutos por cliente/mês — " + base_lbl).font = Font(bold=True, size=12)
    r = 3
    for j, h in enumerate(["Cliente", "ago", "set", "out", "nov", "Total"], 1):
        c = ws.cell(row=r, column=j, value=h)
        c.fill, c.font, c.border = HEAD_FILL, HEAD_FONT, BORDER
    r += 1
    dias_row_pos = {}
    for cli in order:
        lab = ws.cell(row=r, column=1, value=cli)
        lab.font = Font(bold=True); lab.border = BORDER
        for j, (mk, _) in enumerate(MONTHS, 2):
            if cli in DET_SHEET:
                f = "=" + sumifs("I", DET_SHEET[cli], [("B", f'"{mk}"'), ("J", '"Contado"')])
            else:
                f = (f'=SUMIFS(BASE!$J:$J,BASE!$A:$A,"{cli}",BASE!$K:$K,"Contado",'
                     f'BASE!$C:$C,"{mk}")')
            ws.cell(row=r, column=j, value=f).border = BORDER
        ws.cell(row=r, column=6, value=f"=SUM(B{r}:E{r})").border = BORDER
        ws.cell(row=r + 1, column=1, value="Dias (entrada editável)").border = BORDER
        for j, (mk, _) in enumerate(MONTHS, 2):
            c = ws.cell(row=r + 1, column=j, value=dias_mes_ref[cli][mk])
            c.fill, c.border = EDIT_FILL, BORDER
        c = ws.cell(row=r + 1, column=6, value=f"=SUM(B{r+1}:E{r+1})")
        c.fill, c.border, c.font = EDIT_FILL, BORDER, Font(bold=True)
        ws.cell(row=r + 2, column=1, value="Min/dia").border = BORDER
        for j in range(2, 6):
            L = get_column_letter(j)
            c = ws.cell(row=r + 2, column=j, value=f"=IF({L}{r+1}=0,0,{L}{r}/{L}{r+1})")
            c.number_format, c.border = "0.0", BORDER
        c = ws.cell(row=r + 2, column=6, value=f"=IF(F{r+1}=0,0,F{r}/F{r+1})")
        c.number_format, c.border, c.font = "0.0", BORDER, Font(bold=True)
        dias_row_pos[cli] = r + 1
        r += 4

    # ---------------- METODOLOGIA ----------------
    ws = wb.create_sheet("METODOLOGIA")
    ws.column_dimensions["A"].width = 130
    met = [
        "METODOLOGIA — Tempo dedicado por cliente – Sul/Sudeste (caixa bmn.tsena@cma-cgm.com)",
        "",
        f"Base de dias desta versão: {base_lbl}",
        "",
        "1. ESCOPO: caixa inteira (caixa de entrada + subpastas de arquivo + itens enviados + lixeira).",
        "2. GATE: e-mail entra se bmn.tsena@cma-cgm.com, bma.road-southeast@cma-cgm.com ou bma.road-south@cma-cgm.com estiver em Para/CC, ou se a remetente for a própria conta. E-mails só de bma.road-northeast ficam fora.",
        "3. PERÍODO: 15/08/2026 a 19/11/2026 para coleta; análise mensal ago/set/out/nov. Datas em UTC; conversão UTC−3 para contagem de dias locais.",
        "4. BUSCA: por domínio (NATURAL ONE/natone, CAN PACK/canpack, ED&F MAN/edfman, DSV/dsv) e por palavra-chave no assunto/remetente/destinatários/CC (CARGILL, BERNECK, BRX, CEVA/cartocor, ARGOFRUTA, APL/perfilar, PERNOD RICARD pernod/pernord/PRB, NISSAN, UNILEVER, GROSFILLEX grosfillex-grofillex).",
        "5. TETO DA BUSCA: teto silencioso de ~275 resultados por consulta; coleta dividida em janelas ([15/08–01/09], [01/09–01/10], [01/10–16/10], [16/10–01/11], [01/11–11/11], [11/11–19/11]) com paginação até o token acabar; janelas com ≥250 itens sem token foram reabertas ao meio.",
        "6. LIXEIRA (deleteditems): a mesma busca foi repetida na lixeira; message-ids de lá não são contabilizados (aparecem nas abas DET com Situação 'Apagado (fora da contagem)'). Único achado: 2 itens DSV de 19/11.",
        "7. REGRAS DE TEMPO: Enviado (remetente = eu) = 10 min fixos. Recebidos classificados pelo assunto normalizado (sem acento), ordem de teste Outros → Doc → Demanda:",
        "   • Doc = 3 min: nf, nfs, nota(s) fiscal(is), xml, fatura, due, comprovante, instrução documentária;",
        "   • Demanda = 20 min: programação, coleta, pré-nomeação, booking, liberação, vazio, estufagem, pré-stacking, safra, draft, ord(em), aceite, carregamento, agendamento, ovação, devolução, embarque, ddl;",
        "   • Outros = 5 min: resposta automática, automatic reply, status, newsletter, digest, agradec…, welcome, webinar, ajuste, cadastro e tudo que não se encaixa.",
        "8. MULTI-CLIENTE: quando vários clientes aparecem, o e-mail é atribuído ao primeiro citado no assunto.",
        "9. DUPLICADOS: mesmo assunto normalizado (sem prefixos RE/RES/FW/ENC) recebido em janela de até 45 min conta 1 vez; réplicas ficam listadas como 'Duplicado (fora da contagem)', sem minutos.",
        "10. EXCLUSÕES: bounces/undeliverable, postmaster, RSVPs de calendário (Accepted/Declined/Tentative), notificações de Teams/Threads (@thread.v2 sem assunto) e e-mails internos 'Indicadores SUL'/'Indicadores SD'.",
        "11. DIAS COM ATIVIDADE: dias corridos (UTC−3) com ≥1 e-mail contabilizado, incluindo sáb./dom./feriados; calculados do próprio resultado, por cliente/mês e total (união de dias entre clientes).",
        "12. DIAS ÚTEIS: 15/08 a 15/11/2026, excl. fins de semana e feriados nacionais 07/09, 12/10 e 02/11 = 62 dias (ago 11, set 21, out 21, nov 9). Linhas 'Dias' nas abas RESUMO/MENSAL são células de entrada editáveis (amarelo).",
        "13. AUDITORIA: abas DET listam item a item (10 clientes de palavra-chave); clientes por domínio ficam agregados na aba BASE; RESUMO/MENSAL usam fórmulas vivas SUMIFS/COUNTIFS sobre DET/BASE; % expediente = min/540.",
        "14. OBSERVAÇÕES: GROSFILLEX não retornou nenhum e-mail em toda a caixa no período (linha zerada); assuntos 'Kick off … PRB' e grafias 'PERNORD' tratados como PERNOD RICARD; 1 linha PERNOD 'O-n' (02/10 15:03) sem eu/RS/RST em Para/CC foi removida pelo gate nesta versão.",
    ]
    for i, line in enumerate(met, 1):
        ws.cell(row=i, column=1, value=line)
        ws.cell(row=i, column=1).alignment = Alignment(wrap_text=True, vertical="top")

    del wb["Sheet"]
    wb.save(path)
    return {"out": path, "order": order, "minutos": minutos_cli, "dias": dias_ref,
            "dias_total": dias_total, "dias_mes": dias_mes_ref, "min_mes": min_mes}


def main():
    rows = json.load(open(ROWS_JSON))
    res1 = build("dias_com_atividade", rows,
                 f"{OUTDIR}/tempo_clientes_sul_sudeste_dias_com_atividade.xlsx")
    res2 = build("dias_uteis", rows,
                 f"{OUTDIR}/tempo_clientes_sul_sudeste_dias_uteis.xlsx")
    totals = {k: res1["minutos"][k] for k in res1["order"]}
    for res in (res1, res2):
        print(res["out"], "clientes:", len(res["order"]))
    tt = sum(totals.values())
    print("TOTAL min:", tt, "=", tt // 60, "h", tt % 60)
    diag = {"order": res1["order"], "minutos": totals,
            "dias_ativ_cli": res1["dias"], "dias_ativ_total": res1["dias_total"],
            "dias_ut_mes": DIAS_UTEIS_MES, "min_mes": res1["min_mes"],
            "dias_mes_ativ": res1["dias_mes"]}
    json.dump(diag, open("/workspace/analise_coleta/data/resumo_diag.json", "w"),
              ensure_ascii=False, indent=1)
    print("diag salvo em data/resumo_diag.json")


if __name__ == "__main__":
    main()
