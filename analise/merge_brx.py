import json
IDB2="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
IDB3="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAABNAAWW_bO3AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ME="bmn.tsena@cma-cgm.com"
S="FW: [CMA CGM] SOLICITA\u00c7\u00c3O DE FORNECEDOR | ITAQUAQUECETUBA/SP x SANTOS/SP | CLIENTE BRX INTERNATIONAL"
rows=[
 (IDB2,"R4KAAA=",S,"Juliane.MARQUES@mercosul-line.com.br","2026-11-09T20:42:03Z",ME,""),
 (IDB3,"RMTAAA=",S,"Juliane.MARQUES@mercosul-line.com.br","2026-11-09T20:42:03Z",ME,""),
]
out="/workspace/analise_coleta/raw/brx_all.jsonl"
import os
if not os.path.exists(out): open(out,"w").close()
have=set()
for l in open(out): have.add(json.loads(l)["id"])
new=0
with open(out,"a") as f:
    for r in rows:
        idb,suf,s,fr,d,to,cc=r
        id_=idb+suf
        if id_ in have: continue
        f.write(json.dumps({"id":id_,"folder":"main","date":d,"subject":s,"from":fr,"to":to,"cc":cc},ensure_ascii=False)+"\n")
        have.add(id_); new+=1
print("new:",new,"total:",len(have))
