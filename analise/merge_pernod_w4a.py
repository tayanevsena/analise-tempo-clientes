# merge PERNOD w4a [21/10-26/10] — 11 novas
import json, os
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
NAA = "ssz.naalves@cma-cgm.com"

SK = "[INTERNO] [Kick off Operacional] - CMA CGM x PRB"
SKR = "RE: " + SK

rows = []

def R(sfx, date, subject, frm, to, cc):
    rows.append({"id": ID1 + sfx, "folder": "main", "date": date, "subject": subject, "from": frm, "to": to, "cc": cc})

R("Rk-AAA=", "2026-10-23T19:05:07Z", SKR, BRA, [THA], [JBAT, RS, NLEY, DARO, ILN, JUL])
R("RlEAAA=", "2026-10-23T18:22:20Z", SKR, BRA, [THA], [JUL, JBAT, RS, NLEY, DARO, ILN])
R("RlHAAA=", "2026-10-23T18:10:58Z", SK, THA, [BRA], [JUL, NAA, JBAT, RS, NLEY, DARO, ILN])
R("RlMAAA=", "2026-10-23T17:13:59Z", SKR, THA, [BRA], [JUL, NAA, JBAT, RS, NLEY, DARO, ILN])
R("RlPAAA=", "2026-10-23T16:24:22Z", SKR, BRA, [THA], [JUL, NAA, JBAT, RS, NLEY, DARO, ILN])
R("RlhAAA=", "2026-10-23T12:23:55Z", SK, THA, [BRA], [JUL, JBAT, RS, NLEY, DARO, ILN, NAA])
R("RlkAAA=", "2026-10-23T12:05:17Z", SKR, BRA, [THA], [JUL, JBAT, RS, NLEY, DARO, ILN, NAA])
R("RllAAA=", "2026-10-23T11:57:43Z", SKR, THA, [BRA, JUL], [JBAT, RS, NLEY, DARO, ILN])
R("RlmAAA=", "2026-10-23T11:55:17Z", SKR, BRA, [THA], [JUL, JBAT, RS, NLEY, DARO, ILN])
R("RmmAAA=", "2026-10-22T13:55:33Z", SK, THA, [BRA, JUL], [JBAT, RS, NLEY, DARO, ILN])
R("RmuAAA=", "2026-10-22T12:00:52Z", SKR, BRA, [JUL], [JBAT, RS, THA, NLEY, DARO, ILN])

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
