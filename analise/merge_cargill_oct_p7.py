import json, collections
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ME="bma.road-southeast@cma-cgm.com"
JUL="Juliane.MARQUES@mercosul-line.com.br"; THA="thaina.santos@mercosul-line.com.br"
CASC="Casc_Impo@cargill.com"; GRAZ="graziela.braga@pibernat.com.br"; PPAL="Paula_Palazzo@cargill.com"; GETH="gethelp@cargill.com"
GIO="Giovana_Santos1@cargill.com"; WES="Wesley_Delisolasantos@cargill.com"; TFA="Tiago_Faria@cargill.com"
AGRO="-AGROQUIMICOS-CROPINPUT@Cargill.com"; AGRO2="AGROQUIMICOS-CROPINPUT@cargill.com"; CSIMP="-CASC-GTOC-IMP@exch.cargill.com"
ITRG="impo.cargill.rgd@pibernat.com.br"; TEALL="-CASC-IMPORTS-TE-ALL@Cargill.com"; BSVC="bra.service@cma-cgm.com"
NBAR="Natalia_Barreto@cargill.com"
UNI3=",".join(["atendimentoaocliente.sts@uni.com.br","operacional.sts@uni.com.br"])
S_G276="LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001879016-0 | DSA | CASC0139/26, PO 521715Z361 | GLIFOSATO NGC - RIO VERDE | GHYD260276 (CHN3831443)"
S_G277="LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001896221-2 | DSA | CASC0138/26, PO 521715Z360 | GLIFOSATO NGC - DANFE SOLICITADA| GHYD260277 (CHN3831374)"
S_G275C="RES: LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001889833-6 | DSA| CASC0137/26, PO 521715Z359 | GLIFOSATO NGC - RIO VERDE | GHYD260275 (CHN3831378) *CARGA DSA*"
S_IMP_NS="[CMA CCGM] BRSSZ | PROGRAMA\u00c7\u00c3O IMPORTA\u00c7\u00c3O | CARGILL x UNITRADING | CHN3831443"
S_IMP_374="[CMA CCGM] BRSSZ | PROGRAMA\u00c7\u00c3O IMPORTA\u00c7\u00c3O | CARGILL x UNITRADING | CHN3831374"
S_IMP_378="[CMA CCGM] BRSSZ | PROGRAMA\u00c7\u00c3O IMPORTA\u00c7\u00c3O | CARGILL x UNITRADING | CHN3831378"
CC_277=",".join([GIO,AGRO,NBAR,ITRG,CSIMP,WES,TFA])
rows=[
 (B4,"RrCAAA=",S_G277,THA,"2026-10-16T19:13:27Z",",".join([CASC,JUL,GRAZ,PPAL,ME,BSVC,TEALL]),CC_277),
 (B4,"RrLAAA=",S_IMP_374,"giovanna.reis@unitradinglog.com.br","2026-10-16T18:48:22Z",JUL+","+"atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RrUAAA=","RE: "+S_IMP_NS,THA,"2026-10-16T18:35:39Z",JUL+","+UNI3.split(",")[0],",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RrVAAA="," "+S_IMP_374,THA,"2026-10-16T18:33:14Z",JUL+","+"giovanna.reis@unitradinglog.com.br,atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RrWAAA="," "+S_IMP_378,THA,"2026-10-16T18:30:13Z",JUL+","+"atendimentoaocliente.sts@uni.com.br,giovanna.reis@unitradinglog.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RrhAAA=","RES: "+S_G276,CASC,"2026-10-16T17:10:07Z",",".join([THA,JUL,GRAZ,GETH,ME,BSVC,AGRO2,PPAL,WES,TEALL]),",".join([GIO,AGRO,ITRG,CSIMP,TFA])),
 (B4,"RriAAA=","RES: "+S_G277,CASC,"2026-10-16T17:02:51Z",",".join([JUL,GRAZ,PPAL,ME,BSVC,TEALL]),CC_277),
 (B4,"RrjAAA=",S_G275C,CASC,"2026-10-16T17:00:03Z",",".join([JUL,GRAZ,GETH,PPAL,ME,BSVC,GIO]),",".join([AGRO,ITRG,CSIMP,WES,TFA,TEALL])),
]
out="/workspace/analise_coleta/raw/cargill_oct.jsonl"
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
c=collections.Counter(json.loads(l)["date"][:10] for l in open(out))
print("by day:",sorted(c.items()))
