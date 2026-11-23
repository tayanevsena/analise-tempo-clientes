import json, collections
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ME="bma.road-southeast@cma-cgm.com"
JUL="Juliane.MARQUES@mercosul-line.com.br"; THA="thaina.santos@mercosul-line.com.br"
SO3="operacional3@guarujaterminais.com.br"; SO4="operacional4@guarujaterminais.com.br"; CO="coordenador@guarujaterminais.com.br"
CC_UNI1=",".join(["laiza.may@uni.com.br","katny.barros@uni.com.br","helio@uni.com.br","cac@unitradinglog.com.br","faturamento.sts@uni.com.br",ME,"valerio.carvalho@uni.com.br","giovanna.reis@unitradinglog.com.br"])
CASC="Casc_Impo@cargill.com"; GRAZ="graziela.braga@pibernat.com.br"; PPAL="Paula_Palazzo@cargill.com"; GETH="gethelp@cargill.com"
GIO="Giovana_Santos1@cargill.com"; WES="Wesley_Delisolasantos@cargill.com"; TFA="Tiago_Faria@cargill.com"
AGRO="-AGROQUIMICOS-CROPINPUT@Cargill.com"; AGRO2="AGROQUIMICOS-CROPINPUT@cargill.com"; CSIMP="-CASC-GTOC-IMP@exch.cargill.com"
ITRG="impo.cargill.rgd@pibernat.com.br"; TEALL="-CASC-IMPORTS-TE-ALL@Cargill.com"; BSVC="bra.service@cma-cgm.com"
FINCUST="-finance-customs-cargillonly@Cargill.com"; NBAR="Natalia_Barreto@cargill.com"; CLF="Clara_Fernanda@cargill.com"; JAC="Jaciara_Marquesdesouza@cargill.com"
UNI3=",".join(["atendimentoaocliente.sts@uni.com.br","operacional.sts@uni.com.br"])
S_ESTA="SOLICITA\u00c7\u00c3O // ESTADIA // CMA CGM //  CARGIL - BOOKING: 26BR00018962212 / 26BR00019033762 - CHN3839530  - CHN3831374"
S_YM152=" LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001903376-2 | CHLORFENAPYR - RIO VERDE | CASC0141/26, PO 521715Z366 | YN2026WM152-2 (CHN3839530)"
S_GHYD276=" LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001879016-0 | DSA | CASC0139/26, PO 521715Z361 | GLIFOSATO NGC - RIO VERDE | GHYD260276 (CHN3831443)"
S_GHYD275=" LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001889833-6 | DSA| CASC0137/26, PO 521715Z359 | GLIFOSATO NGC - RIO VERDE | GHYD260275 (CHN3831378) *CARGA DSA*"
S_PROG="[CMA CGM] BRSSZ | Programa\u00e7\u00e3o CARGILL | UNITRADING - CHN3839530"
S_IMP_NS="BRSSZ | PROGRAMA\u00c7\u00c3O IMPORTA\u00c7\u00c3O | CARGILL x UNITRADING | CHN3831443"
S_IMP_378="BRSSZ | PROGRAMA\u00c7\u00c3O IMPORTA\u00c7\u00e3O | CARGILL x UNITRADING | CHN3831378".replace("\u00e7\u00e3o","Ã\u0087\u00c3O")
S_IMP_378="[CMA CCGM] BRSSZ | PROGRAMA\u00c7\u00c3O IMPORTA\u00c7\u00c3O | CARGILL x UNITRADING | CHN3831378"
S_AND0="Corre\u00e7\u00e3o  [CMA CGM] Cadastros | Guaruj\u00e1 Terminais x CARGILL"
rows=[
 (B4,"Rm5AAA=",S_ESTA,"fellipe.xavier@unitradinglog.com.br","2026-10-21T20:04:40Z",JUL,CC_UNI1),
 (B4,"RnGAAA=",S_YM152,THA,"2026-10-21T17:17:19Z",",".join([CASC,JUL,GRAZ,PPAL,ME,BSVC]),",".join([GIO,AGRO,ITRG,CSIMP,WES,TFA,FINCUST,NBAR,CLF,JAC])),
 (B4,"RnOAAA=",S_PROG,"giovanna.reis@unitradinglog.com.br","2026-10-21T13:46:41Z",",".join([THA])+","+UNI3,ME),
 (B4,"RnTAAA=",S_GHYD276,THA,"2026-10-21T12:58:10Z",",".join([CASC,JUL,GRAZ,GETH,ME,BSVC,AGRO2,PPAL,WES,TEALL]),",".join([GIO,AGRO,ITRG,CSIMP,TFA])),
 (B4,"RnVAAA=",S_GHYD275,THA,"2026-10-21T12:49:28Z",",".join([CASC,JUL,GRAZ,GETH,PPAL,ME,BSVC,GIO]),",".join([AGRO,ITRG,CSIMP,WES,TFA,TEALL])),
 (B4,"RnXAAA=",S_PROG,THA,"2026-10-21T12:23:46Z","giovanna.reis@unitradinglog.com.br,"+UNI3,ME),
 (B4,"RnZAAA=",S_PROG,"giovanna.reis@unitradinglog.com.br","2026-10-21T11:54:02Z",THA+","+UNI3,ME),
 (B4,"RnaAAA=",S_IMP_NS,"giovanna.reis@unitradinglog.com.br","2026-10-21T11:53:59Z",",".join(["felipe.lopes@uni.com.br",THA,JUL])+","+UNI3.split(",")[0],",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RncAAA=",S_IMP_378,"giovanna.reis@unitradinglog.com.br","2026-10-21T11:44:40Z",THA+","+JUL+","+"atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RngAAA=","RES: "+S_IMP_NS,"felipe.lopes@uni.com.br","2026-10-20T21:55:36Z","thaina.santos@mercosul-line.com.br,giovanna.reis@unitradinglog.com.br,Juliane.MARQUES@mercosul-line.com.br,atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RnjAAA=","RE: "+S_IMP_NS,THA,"2026-10-20T21:09:18Z","giovanna.reis@unitradinglog.com.br,Juliane.MARQUES@mercosul-line.com.br,atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"Rn2AAA=",S_AND0,SO4,"2026-10-20T14:26:35Z",",".join([JUL,CO,SO3]),ME),
 (B4,"Rn9AAA=",S_IMP_378,THA,"2026-10-20T13:17:33Z","giovanna.reis@unitradinglog.com.br,Juliane.MARQUES@mercosul-line.com.br,atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"Rn_AAA=","RE: "+S_IMP_NS,THA,"2026-10-20T13:12:49Z","giovanna.reis@unitradinglog.com.br,Juliane.MARQUES@mercosul-line.com.br,atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RoMAAA=",S_IMP_NS,"giovanna.reis@unitradinglog.com.br","2026-10-20T11:59:08Z",THA+","+JUL+","+"atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RoNAAA=",S_IMP_378,"giovanna.reis@unitradinglog.com.br","2026-10-20T11:55:49Z",THA+","+JUL+","+"atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RoeAAA=",S_PROG,THA,"2026-10-19T20:46:22Z","giovanna.reis@unitradinglog.com.br,atendimentoaocliente.sts@uni.com.br,operacional.sts@uni.com.br",ME),
 (B4,"RoiAAA=","RE: LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001889833-6 | DSA| CASC0137/26, PO 521715Z359 | GLIFOSATO NGC - RIO VERDE | GHYD260275 (CHN3831378) *CARGA DSA*",THA,"2026-10-19T20:13:45Z",",".join([CASC,JUL,GRAZ,GETH,PPAL,ME,BSVC,GIO]),",".join([AGRO,ITRG,CSIMP,WES,TFA,TEALL])),
 (B4,"RojAAA=","RE: LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001879016-0 | DSA | CASC0139/26, PO 521715Z361 | GLIFOSATO NGC - RIO VERDE | GHYD260276 (CHN3831443)",THA,"2026-10-19T20:11:02Z",",".join([CASC,JUL,GRAZ,GETH,ME,BSVC,AGRO2,PPAL,WES,TEALL]),",".join([GIO,AGRO,ITRG,CSIMP,TFA])),
 (B4,"RooAAA=",S_IMP_378,"giovanna.reis@unitradinglog.com.br","2026-10-19T19:48:06Z",THA+","+JUL+","+"atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
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
