# merge APL (PERFILOR) — 3 válidas, período 15/08-19/11
import json
from collections import Counter

OUT = "/workspace/analise_coleta/raw/apl_all.jsonl"
open(OUT, "w").close()

ID1 = "AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"

RS = "bma.road-southeast@cma-cgm.com"
JUL = "Juliane.MARQUES@mercosul-line.com.br"
FEL = "fellipe.xavier@unitradinglog.com.br"
GAB = "gabriel.carreira@unitradinglog.com.br"
CC_UNI = ["tatiana.ranieri@uni.com.br", "laiza.may@uni.com.br", "katny.barros@uni.com.br", "helio@uni.com.br", "cac@unitradinglog.com.br", "faturamento.sts@uni.com.br", RS]

SE1 = "RE: SOLICITA\u00c7\u00c3O // ESTADIA // CMA CGM //  APL (PERFILOR) - BOOKING SSZ1824415"
SE2 = "RES: SOLICITA\u00c7\u00c3O // ESTADIA // CMA CGM //  APL (PERFILOR) - BOOKING SSZ1822663"

rows = []

def R(sfx, date, subject, frm, to, cc):
    rows.append({"id": ID1 + sfx, "folder": "main", "date": date, "subject": subject, "from": frm, "to": to, "cc": cc})

R("Rw4AAA=", "2026-10-05T15:33:41Z", SE1, JUL, [FEL, GAB], CC_UNI)
R("RxNAAA=", "2026-10-02T20:00:52Z", SE2, FEL, [GAB, JUL], CC_UNI)
R("RxOAAA=", "2026-10-02T19:59:30Z", "RES: SOLICITA\u00c7\u00c3O // ESTADIA // CMA CGM //  APL (PERFILOR) - BOOKING SSZ1824415", FEL, [JUL, GAB], CC_UNI)

with open(OUT, "a", encoding="utf-8") as f:
    for r_ in rows:
        f.write(json.dumps(r_, ensure_ascii=False) + "\n")
print("total:", len(rows))
print("by day:", Counter(x["date"][:10] for x in rows))
