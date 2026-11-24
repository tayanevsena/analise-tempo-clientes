# merge PERNOD w3 [01/10-16/10] — 8 novas (kick-off PRB)
import json, os
from collections import Counter

OUT = "/workspace/analise_coleta/raw/pernod_all.jsonl"

ID1 = "AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"

ME = "bmn.tsena@cma-cgm.com"
RS = "bma.road-southeast@cma-cgm.com"

BRA = "BRA.SERVICE@CMA-CGM.COM"
JUL = "Juliane.MARQUES@mercosul-line.com.br"
THA = "thaina.santos@mercosul-line.com.br"
NLEY = "BMA.NLEY@cma-cgm.com"
JBAT = "BMA.JBATISTA@cma-cgm.com"
DARO = "BMA.DARODRIGUES@cma-cgm.com"
ILN = "bma.ils_newbusiness@cma-cgm.com"

SK = "[INTERNO] [Kick off Operacional] - CMA CGM x PRB"
SKR = "Re: " + SK
SKRE = "RE: " + SK

rows = []

def R(idb, sfx, date, subject, frm, to, cc):
    rows.append({
        "id": (idb + sfx) if idb else sfx,
        "folder": "main",
        "date": date,
        "subject": subject,
        "from": frm,
        "to": to,
        "cc": cc,
    })

R(ID1, "RtXAAA=", "2026-10-13T17:36:05Z", SK, THA, [BRA, JUL, NLEY], [JBAT, RS, DARO, ILN])
R(ID1, "RtZAAA=", "2026-10-13T16:37:09Z", SKR, BRA, [JUL, NLEY], [JBAT, RS, DARO, ILN])
R(ID1, "RwwAAA=", "2026-10-05T17:36:57Z", SKR, BRA, [NLEY, JUL], [JBAT, RS, DARO, ILN])
R(ID1, "RwyAAA=", "2026-10-05T17:28:28Z", SKR, NLEY, [JUL, BRA], [JBAT, RS, DARO, ILN])
R(ID1, "Rw_AAA=", "2026-10-05T13:15:42Z", SKRE, JUL, [BRA, NLEY], [JBAT, RS, DARO, ILN])
R(ID1, "RxUAAA=", "2026-10-02T18:31:09Z", SKRE, BRA, [JUL], [JBAT, RS, NLEY, DARO, ILN])
R(ID1, "RxcAAA=", "2026-10-02T14:55:06Z", SKRE, BRA, [JUL], [JBAT, RS, NLEY, DARO, ILN, "ssz.naalves@cma-cgm.com"])
R(ID1, "RxdAAA=", "2026-10-02T14:48:47Z", SK, JUL, [BRA, NLEY], [JBAT, DARO, RS, ILN])

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
