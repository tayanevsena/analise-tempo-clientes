# merge CARTOCOR (CEVA) rows into raw/cartocor_all.jsonl
import json, os

OUT = "/workspace/analise_coleta/raw/cartocor_all.jsonl"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "a").close()  # ensure exists

ID1 = "AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ID2 = "AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
AQB = "AQMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAADSrFV1ygwrEK1d5Xhoqs19gcA-qQhS5nsYUyT70hlqAkATQAAAgEJAAAA-qQhS5nsYUyT70hlqAkATQAGLZEH"
AQJ = "AQMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAADSrFV1ygwrEK1d5Xhoqs19gcA-qQhS5nsYUyT70hlqAkATQAFlvmzuAAAAP6kIUuZ7GFMk_9IZagJAE0ABi2RIwAAAQ=="

ME = "bmn.tsena@cma-cgm.com"
M1 = "bma.road-southeast@cma-cgm.com"
LIB = "BMA.LIBERACAO@cma-cgm.com"
ADR = "adriana.souza@coopercarga.com.br"
KAY = "kayron@coopercarga.com.br"
FAB = "fabiola.santos@coopercarga.com.br"
MAY = "mayara.santos@coopercarga.com.br"
ISA = "isabelly.claudino@coopercarga.com.br"
CAB = "cabotagem@coopercarga.com.br"
CAS = "cassiano@coopercarga.com.br"
CAI = "caique.santos@coopercarga.com.br"
JUL = "Juliane.MARQUES@mercosul-line.com.br"
SSZ = "ssz.customerservice@ccis-network.com"
LUC = "lucas.silva@lechman.com.br"
CMALE = "cma.lechman@lechman.com.br"
DOC = "documentacao@mercosul-line.com.br"
TRADE = "TRADE@mercosul-line.com.br"
TAX = "tax@mercosul-line.com.br"
ATT = "atendimento@mercosul-line.com.br"
VIT = "vitoria.ferreira@coopercarga.com.br"
RAF = "rafael.teixeira@coopercarga.com.br"
O365 = "Office365Reports@microsoft.com"

S_PG47 = "[CMA CGM] BRSSZ | Programação CEVA (CARTOCOR) | COOPERCARGA | WK 47"
S_PG47RE = "RE: [CMA CGM] BRSSZ | Programação CEVA (CARTOCOR) | COOPERCARGA | WK 47"
S_PG48 = "[CMA CGM] BRSSZ | Programação CEVA (CARTOCOR) | COOPERCARGA | WK 48"
S_LV041LE = "RE: [CMA CGM] BRSSZ | Liberação de vazio - CEVA (CARTOCOR) | CUR0274941 (LE)"
S_LV041LERES = "RES: [CMA CGM] BRSSZ | Liberação de vazio - CEVA (CARTOCOR) | CUR0274941 (LE)"
S_LV041 = "[CMA CGM] BRSSZ | Liberação de vazio - CEVA (CARTOCOR) | CUR0274941"
S_LV038 = "[CMA CGM] BRSSZ | Liberação de vazio - CEVA (CARTOCOR) | CUR0274938"
S_LV040 = "[CMA CGM] BRSSZ | Liberação de vazio - CEVA (CARTOCOR) | CUR0274940"
S_LV040LR = "RE: [CMA CGM] BRSSZ | Liberação de vazio - CEVA (CARTOCOR) | CUR0274940 (LR)"
S_LV040LRRES = "RES: [CMA CGM] BRSSZ | Liberação de vazio - CEVA (CARTOCOR) | CUR0274940 (LR)"
S_LV038LR = "RE: [CMA CGM] BRSSZ | Liberação de vazio - CEVA (CARTOCOR) | CUR0274938 (LR)"
S_LV038LRRES = "RES: [CMA CGM] BRSSZ | Liberação de vazio - CEVA (CARTOCOR) | CUR0274938 (LR)"
S_APR = "RE: [CMA CGM] BRSSZ | Aprovação de material de peçação CEVA (CARTOCOR) | COOPERCARGA | WK 47"
S_APR0 = "[CMA CGM] BRSSZ | Aprovação de material de peçação CEVA (CARTOCOR) | COOPERCARGA | WK 47"
S_RECALL = "Relatório de Recall de Mensagem para a mensagem: \"[CMA CGM] BRSSZ | Programação CEVA (CARTOCOR) | COOPERCARGA | WK 48\""
S_CUSTOS = "RE: SDL-DOC - [CMA CGM] BRSSZ | CUSTOS ADICIONAIS | CEVA (CARTOCOR) | CUR0274347 - CUR0274348 - CUR0274339"
S_CUSTOS0 = "SDL-DOC - [CMA CGM] BRSSZ | CUSTOS ADICIONAIS | CEVA (CARTOCOR) | CUR0274347 - CUR0274348 - CUR0274339"

def R(idb, sfx, date, subject, frm, to, cc):
    return {
        "id": (idb + sfx) if idb is not None else sfx,
        "folder": "main",
        "date": date,
        "subject": subject,
        "from": frm,
        "to": ",".join(to),
        "cc": ",".join(cc),
    }

rows = [
    R(ID1, "S1kAAA=", "2026-11-19T12:53:37Z", S_PG47RE, ADR, [KAY, ME, FAB, MAY, ISA, CAB, JUL], [M1, CAS]),
    R(ID1, "S0wAAA=", "2026-11-18T20:33:42Z", S_LV041LE, SSZ, [ME], [M1, LIB]),
    R(ID1, "S0xAAA=", "2026-11-18T20:33:29Z", S_LV041LERES, SSZ, [ME], [M1, LIB]),
    R(ID1, "S1qAAA=", "2026-11-18T19:33:24Z", S_PG48, ME, [CAB], [M1]),
    R(ID2, "Su5AAA=", "2026-11-18T19:33:02Z", S_RECALL, O365, [ME], []),
    R(AQB, "qgAAAA==", "2026-11-18T19:33:00Z", S_PG48, ME, [CAB], [M1]),
    R(AQB, "qQAAAA==", "2026-11-18T19:28:00Z", S_PG48, ME, [CAB], [M1]),
    R(AQB, "RwAAAA==", "2026-11-18T19:28:00Z", S_PG48, ME, [CAB], [M1]),
    R(ID1, "S1rAAA=", "2026-11-18T18:53:30Z", S_LV041LE, ME, [SSZ], [M1, LIB]),
    R(AQB, "qAAAAA==", "2026-11-18T18:53:00Z", S_LV041LE, ME, [SSZ], [M1, LIB]),
    R(ID1, "SLyAAA=", "2026-11-18T09:53:06Z", S_PG47RE, KAY, [ADR, ME, FAB, MAY, ISA, CAB, JUL], [M1, CAS]),
    R(ID1, "SL0AAA=", "2026-11-17T22:20:29Z", S_PG47RE, ADR, [ME, FAB, MAY, KAY, ISA, CAB, JUL], [M1, CAS]),
    R(ID1, "SLQAAA=", "2026-11-17T19:54:41Z", S_PG47RE, ME, [ADR, FAB, MAY, KAY, ISA, CAB, JUL], [M1, CAS]),
    R(AQB, "pAAAAA==", "2026-11-17T19:52:00Z", S_PG47RE, ME, [ADR, FAB, MAY, KAY, ISA, CAB, JUL], [M1, CAS]),
    R(ID1, "SLUAAA=", "2026-11-17T19:42:32Z", S_APR, FAB, [ME, MAY, KAY, ADR, ISA, CAB, JUL, VIT, RAF], [M1, CAS]),
    R(ID1, "SLZAAA=", "2026-11-17T19:20:55Z", S_APR0, ME, [FAB, MAY, KAY, ADR, ISA, CAB, JUL], [M1, CAS]),
    R(AQB, "owAAAA==", "2026-11-17T19:20:00Z", S_APR0, ME, [FAB, MAY, KAY, ADR, ISA, CAB, JUL], [M1, CAS]),
    R(ID1, "S1wAAA=", "2026-11-17T19:16:07Z", S_LV041LERES, LIB, [ME, SSZ], [M1]),
    R(ID1, "SMCAAA=", "2026-11-17T18:15:38Z", S_PG47RE, ADR, [FAB, MAY, KAY, ISA, ME, CAB, JUL], [M1, CAS]),
    R(None, AQJ, "2026-11-17T18:06:50Z", S_PG47RE, ADR, [FAB, MAY, KAY, ISA, ME, CAB, JUL], [M1, CAS]),
    R(ID1, "SL_AAA=", "2026-11-17T17:56:31Z", S_PG47RE, FAB, [MAY, KAY, ADR, ISA, ME, CAB, JUL], [M1, CAS]),
    R(ID1, "SL8AAA=", "2026-11-17T17:31:13Z", S_LV041, ME, [LIB], [M1]),
    R(AQB, "nAAAAA==", "2026-11-17T17:31:00Z", S_LV041, ME, [LIB], [M1]),
    R(ID1, "SI6AAA=", "2026-11-17T13:31:14Z", S_PG47RE, MAY, [ADR, CAI, ISA, ME, KAY, CAB], [M1]),
    R(ID1, "SI7AAA=", "2026-11-17T13:24:08Z", S_PG47RE, ADR, [CAI, ISA, ME, MAY, KAY, CAB], [M1]),
    R(ID1, "SJAAAA=", "2026-11-17T12:49:38Z", S_PG47RE, ADR, [CAI, ISA, ME, MAY, KAY, CAB], [M1]),
    R(ID1, "SJDAAA=", "2026-11-17T12:42:24Z", S_PG47RE, ADR, [CAI, ISA, ME, MAY, KAY, CAB], [M1]),
    R(ID1, "SJMAAA=", "2026-11-17T09:55:01Z", S_PG47RE, CAI, [ISA, ME, MAY, KAY, ADR, CAB], [M1]),
    R(ID1, "SJOAAA=", "2026-11-17T02:30:17Z", S_PG47RE, CAI, [ISA, ME, MAY, KAY, ADR, CAB], [M1]),
    R(ID1, "SJRAAA=", "2026-11-16T21:49:21Z", S_PG47RE, ISA, [ME, MAY, KAY, ADR, CAB], [M1]),
    R(ID1, "SJgAAA=", "2026-11-16T18:32:31Z", S_PG47RE, ME, [ISA, MAY, KAY, ADR, CAB], [M1]),
    R(AQB, "jAAAAA==", "2026-11-16T18:32:00Z", S_PG47RE, ME, [ISA, MAY, KAY, ADR, CAB], [M1]),
    R(ID1, "SJsAAA=", "2026-11-16T15:32:27Z", S_PG47RE, ISA, [MAY, KAY, ADR, ME, CAB], [M1]),
    R(ID1, "SKIAAA=", "2026-11-16T12:21:56Z", S_PG47RE, MAY, [KAY, ADR, ISA, ME, CAB], [M1]),
    R(ID1, "SKOAAA=", "2026-11-16T09:38:48Z", S_PG47RE, KAY, [ADR, ISA, ME, CAB], [M1]),
    R(ID1, "SKQAAA=", "2026-11-15T22:29:08Z", S_PG47RE, ADR, [ISA, KAY, ME, CAB], [M1]),
    R(ID1, "SKSAAA=", "2026-11-15T12:34:44Z", S_PG47RE, ADR, [ISA, KAY, ME, CAB], [M1]),
    R(ID1, "SKVAAA=", "2026-11-14T18:43:56Z", S_PG47RE, ISA, [KAY, ME, CAB], [M1]),
    R(ID1, "SKWAAA=", "2026-11-14T18:35:15Z", S_PG47RE, ISA, [KAY, ME, CAB], [M1]),
    R(ID1, "SKkAAA=", "2026-11-14T09:00:20Z", S_PG47RE, KAY, [ME, CAB], [M1]),
    R(ID1, "SF3AAA=", "2026-11-11T20:39:54Z", S_PG47, ME, [CAB], [M1]),
    R(AQB, "cQAAAA==", "2026-11-11T20:39:00Z", S_PG47, ME, [CAB], [M1]),
    R(ID1, "SF-AAA=", "2026-11-11T19:16:46Z", S_LV040LRRES, LUC, [LIB, ME, CMALE], [M1]),
    R(ID1, "SGAAAA=", "2026-11-11T19:15:56Z", S_LV038LRRES, LUC, [LIB, ME, CMALE], [M1]),
    R(ID1, "SFpAAA=", "2026-11-11T15:15:07Z", S_LV040LR, LIB, [ME, CMALE, LUC], [M1]),
    R(ID1, "SFqAAA=", "2026-11-11T15:14:33Z", S_LV038LR, LIB, [ME, LUC, CMALE], [M1]),
    R(ID1, "SE6AAA=", "2026-11-11T13:24:03Z", S_LV040, ME, [LIB], [M1]),
    R(ID1, "SE7AAA=", "2026-11-11T13:23:16Z", S_LV038, ME, [LIB], [M1]),
    R(AQB, "ZAAAAA==", "2026-11-11T13:23:00Z", S_LV038, ME, [LIB], [M1]),
    R(AQB, "ZQAAAA==", "2026-11-11T13:23:00Z", S_LV040, ME, [LIB], [M1]),
    R(ID1, "SHUAAA=", "2026-11-10T19:09:38Z", S_CUSTOS, DOC, [JUL], [TRADE, M1]),
    R(ID1, "RyDAAA=", "2026-11-09T14:12:47Z", S_CUSTOS, JUL, [DOC, TRADE], [M1]),
    R(ID1, "RyEAAA=", "2026-11-09T14:09:33Z", S_CUSTOS, DOC, [JUL, TRADE], [M1]),
    R(ID1, "RxvAAA=", "2026-11-06T20:59:12Z", S_CUSTOS, DOC, [JUL, TAX], [M1]),
    R(ID1, "RxwAAA=", "2026-11-06T20:31:06Z", S_CUSTOS0, JUL, [DOC], [M1, ATT]),
]

existing = set()
if os.path.exists(OUT):
    with open(OUT, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                existing.add(json.loads(line)["id"])

new = 0
with open(OUT, "a", encoding="utf-8") as f:
    for r in rows:
        if r["id"] in existing:
            continue
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
        existing.add(r["id"])
        new += 1

print(f"new: {new} total: {len(existing)}")

from collections import Counter
by_day = Counter()
with open(OUT, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            by_day[json.loads(line)["date"][:10]] += 1
for d in sorted(by_day):
    print(d, by_day[d])
