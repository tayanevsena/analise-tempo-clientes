# merge PERNOD w4b [26/10-01/11] — 7 novas (kick-off PRB Santos Brasil)
import json
from collections import Counter

OUT = "/workspace/analise_coleta/raw/pernod_all.jsonl"

ID1 = "AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"

RS = "bma.road-southeast@cma-cgm.com"
BRA = "BRA.SERVICE@CMA-CGM.COM"
JUL = "Juliane.MARQUES@mercosul-line.com.br"
THA = "thaina.santos@mercosul-line.com.br"
NLEY = "BMA.NLEY@cma-cgm.com"
JBAT = "BMA.JBATISTA@cma-cgm.com"
DARO = "BMA.DARODRIGUES@cma-cgm.com"
ILN = "bma.ils_newbusiness@cma-cgm.com"
ANDS = "anderson.siqueira@santosbrasil.com.br"
GIO = "giovanna.jesus@santosbrasil.com.br"
COB = "cobranca@santosbrasil.com.br"
LUA = "luanda.pitombo@santosbrasil.com.br"
VAN = "vanessa.amaral@santosbrasil.com.br"

SKR = "RE: RES: [INTERNO] [Kick off Operacional] - CMA CGM x PRB"
SK8 = "RES: [INTERNO] [Kick off Operacional] - CMA CGM x PRB"
SK = "[INTERNO] [Kick off Operacional] - CMA CGM x PRB"
SKRE = "RE: " + SK

rows = []

def R(sfx, date, subject, frm, to, cc):
    rows.append({"id": ID1 + sfx, "folder": "main", "date": date, "subject": subject, "from": frm, "to": to, "cc": cc})

R("RjzAAA=", "2026-10-26T19:04:04Z", SKR, THA, [ANDS, GIO, LUA, COB], [JUL, BRA, VAN, JBAT, RS, NLEY, DARO, ILN])
R("Rj2AAA=", "2026-10-26T18:02:13Z", SKR, BRA, [ANDS], [JUL, LUA, VAN, JBAT, GIO, RS, COB, NLEY, THA, DARO, ILN])
R("Rj8AAA=", "2026-10-26T17:43:33Z", SK8, ANDS, [COB, GIO], [JBAT, RS, NLEY, DARO, ILN, JUL, LUA, VAN, THA, BRA])
R("Rj_AAA=", "2026-10-26T17:30:50Z", SK, THA, [BRA, ANDS], [JBAT, RS, NLEY, DARO, ILN, JUL])
R("RkCAAA=", "2026-10-26T16:18:07Z", SKRE, BRA, [THA], [JBAT, RS, NLEY, DARO, ILN, JUL])
R("RkHAAA=", "2026-10-26T14:49:58Z", SKRE, BRA, [THA], [JUL, JBAT, RS, NLEY, DARO, ILN])
R("RkJAAA=", "2026-10-26T14:07:07Z", SKRE, THA, [BRA, "bma.macosta@cma-cgm.com"], [JBAT, RS, NLEY, DARO, ILN, JUL])

with open(OUT, "r", encoding="utf-8") as f:
    seen = {json.loads(l)["id"] for l in f if l.strip()}

new = 0
with open(OUT, "a", encoding="utf-8") as f:
    for r_ in rows:
        if r_["id"] in seen:
            continue
        f.write(json.dumps(r_, ensure_ascii=False) + "\n")
        seen.add(r_["id"])
        new += 1

with open(OUT, "r", encoding="utf-8") as f:
    all_lines = [json.loads(l) for l in f if l.strip()]
print(f"new: {new} total: {len(all_lines)}")
print("by day:", Counter(x["date"][:10] for x in all_lines))
