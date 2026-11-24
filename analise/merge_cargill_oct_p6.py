import json, collections
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ME="bma.road-southeast@cma-cgm.com"
JUL="Juliane.MARQUES@mercosul-line.com.br"; THA="thaina.santos@mercosul-line.com.br"
ADB="Adriano_Dasilvabomtempo@cargill.com"; PED="Pedrohenrique_Defreitas@cargill.com"
SO3="operacional3@guarujaterminais.com.br"; SO4="operacional4@guarujaterminais.com.br"; CO="coordenador@guarujaterminais.com.br"
CCTL="cotton_ctl@Cargill.com"; CDocs="cotton-br-docs@cargill.com"; GT="cotton_gtocbr@cargill.com"
CASC="Casc_Impo@cargill.com"; GRAZ="graziela.braga@pibernat.com.br"; PPAL="Paula_Palazzo@cargill.com"; GETH="gethelp@cargill.com"
GIO="Giovana_Santos1@cargill.com"; WES="Wesley_Delisolasantos@cargill.com"; TFA="Tiago_Faria@cargill.com"
AGRO="-AGROQUIMICOS-CROPINPUT@Cargill.com"; AGRO2="AGROQUIMICOS-CROPINPUT@cargill.com"; CSIMP="-CASC-GTOC-IMP@exch.cargill.com"
ITRG="impo.cargill.rgd@pibernat.com.br"; TEALL="-CASC-IMPORTS-TE-ALL@Cargill.com"; BSVC="bra.service@cma-cgm.com"
FINCUST="-finance-customs-cargillonly@Cargill.com"; NBAR="Natalia_Barreto@cargill.com"; CLF="Clara_Fernanda@cargill.com"; JAC="Jaciara_Marquesdesouza@cargill.com"
UNI3=",".join(["atendimentoaocliente.sts@uni.com.br","operacional.sts@uni.com.br"])
CC_ESTU=",".join(["-COTTON-BR-PLANNING@Cargill.com","Beatriz_Carvalho@cargill.com","Jose_americo@cargill.com","Karoline_Dasilvapereira@cargill.com","Luciana_Calegari@cargill.com","bma.mcastro@cma-cgm.com","RCE.JLIMA@cma-cgm.com",THA,"Eduardo.FIGUEIRA@mercosul-line.com.br",CDocs,GT,"BMA.NLEY@cma-cgm.com","Renato_Magalhaes@cargill.com",CCTL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com",ME])
S_EST2="RE: Planejamento Estufagem Cargill - CMA STS & SSA - Crop 2026"
S_EST0="Planejamento Estufagem Cargill - CMA STS & SSA - Crop 2026"
S_PROG="[CMA CGM] BRSSZ | Programa\u00e7\u00e3o CARGILL | UNITRADING - CHN3839530"
S_IMP_NS="[CMA CCGM] BRSSZ | PROGRAMA\u00c7\u00c3O IMPORTA\u00c7\u00c3O | CARGILL x UNITRADING | CHN3831443"
S_IMP_378="[CMA CCGM] BRSSZ | PROGRAMA\u00c7\u00c3O IMPORTA\u00e7\u00c3O".replace("\u00e7\u00e3o IMPORTA","Ã\u0087\u00c3O IMPORTA")
S_IMP_378="[CMA CCGM] BRSSZ | PROGRAMA\u00c7\u00c3O IMPORTA\u00c7\u00c3O | CARGILL x UNITRADING | CHN3831378"
S_YM="LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001903376-2 | CHLORFENAPYR - RIO VERDE | CASC0141/26, PO 521715Z366 | YN2026WM152-2 (CHN3839530)"
S_G276="LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001879016-0 | DSA | CASC0139/26, PO 521715Z361 | GLIFOSATO NGC - RIO VERDE | GHYD260276 (CHN3831443)"
S_G275="LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001889833-6 | DSA| CASC0137/26, PO 521715Z359 | GLIFOSATO NGC - RIO VERDE | GHYD260275 (CHN3831378) *CARGA DSA*"
CC_YM=",".join([GIO,AGRO,ITRG,CSIMP,WES,TFA,FINCUST,NBAR,CLF,JAC])
CC_YMc=",".join([GIO,AGRO,CASC,ITRG,CSIMP,WES,TFA,FINCUST,NBAR,CLF,JAC])
T_JUL=",".join([JUL,"Paulo_Carvalho@cargill.com","Karen_Morotti@cargill.com",PED,"Lucas_Simoes@cargill.com","Rafael_Felicissimo@cargill.com","Thairony_Souza@cargill.com"])
rows=[
 (B4,"RopAAA=",S_IMP_NS,"giovanna.reis@unitradinglog.com.br","2026-10-19T19:46:37Z",THA+","+JUL+","+"atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RovAAA=",S_EST0,THA,"2026-10-19T19:38:33Z",",".join([ADB,JUL,"Paulo_Carvalho@cargill.com","Karen_Morotti@cargill.com",PED,"Lucas_Simoes@cargill.com","Rafael_Felicissimo@cargill.com","Thairony_Souza@cargill.com"]),CC_ESTU),
 (B4,"Ro5AAA=",S_YM,THA,"2026-10-19T18:32:45Z",",".join([CASC,JUL,GRAZ,PPAL,ME,BSVC]),CC_YM),
 (B4,"Ro6AAA=",S_PROG,THA,"2026-10-19T18:28:31Z","giovanna.reis@unitradinglog.com.br,"+UNI3,ME),
 (B4,"Ro7AAA=",S_PROG,"giovanna.reis@unitradinglog.com.br","2026-10-19T18:25:53Z",THA+","+UNI3,ME),
 (B4,"RpEAAA=","RES: "+S_EST0,ADB,"2026-10-19T16:45:26Z",T_JUL,CC_ESTU),
 (B4,"RpFAAA=","RES: "+S_YM,CASC,"2026-10-19T16:30:16Z",",".join([JUL,GRAZ,PPAL,ME,BSVC]),CC_YMc),
 (B4,"RpIAAA=",S_YM,THA,"2026-10-19T16:12:44Z",",".join([JUL,GRAZ,PPAL,ME,BSVC,"leticia_campos@cargill.com"]),CC_YMc),
 (B4,"RpKAAA=",S_PROG,THA,"2026-10-19T15:24:45Z","giovanna.reis@unitradinglog.com.br,atendimentoaocliente.sts@uni.com.br,operacional.sts@uni.com.br",ME),
 (B4,"RpNAAA=","RE: "+S_YM,JUL,"2026-10-19T14:13:35Z",",".join([GRAZ,PPAL,ME,BSVC]),CC_YMc),
 (B4,"RpOAAA=","RE: "+S_G275,THA,"2026-10-19T13:37:18Z",",".join([CASC,JUL,GRAZ,GETH,PPAL,ME,BSVC,GIO]),",".join([AGRO,ITRG,CSIMP,WES,TFA,TEALL])),
 (B4,"RpQAAA=",S_G276,THA,"2026-10-19T13:31:53Z",",".join([CASC,JUL,GRAZ,GETH,ME,BSVC,AGRO2,PPAL,WES,TEALL]),",".join([GIO,AGRO,ITRG,CSIMP,TFA])),
 (B4,"RpRAAA=",S_IMP_378,"giovanna.reis@unitradinglog.com.br","2026-10-19T13:27:09Z",THA+","+JUL+","+"atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RpjAAA=",S_IMP_NS,"giovanna.reis@unitradinglog.com.br","2026-10-19T11:41:05Z",THA+","+JUL+","+"atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RpkAAA=",S_IMP_378,"giovanna.reis@unitradinglog.com.br","2026-10-19T11:31:14Z",THA+","+JUL+","+"atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RqAAAA=",S_EST2,JUL,"2026-10-18T17:43:29Z",",".join(["Paulo_Carvalho@cargill.com","Karen_Morotti@cargill.com",ADB,PED,"Lucas_Simoes@cargill.com","Rafael_Felicissimo@cargill.com","Thairony_Souza@cargill.com"]),CC_ESTU),
 (B4,"RqCAAA=","[CMA CGM] Cadastros | Guaruj\u00e1 Terminais x CARGILL",JUL,"2026-10-18T17:37:31Z",",".join([CO,SO3,SO4]),ME),
 (B4,"RqhAAA=",S_IMP_NS,"giovanna.reis@unitradinglog.com.br","2026-10-17T14:49:29Z",THA+","+JUL+","+"atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RqkAAA=",S_IMP_378,"giovanna.reis@unitradinglog.com.br","2026-10-17T12:23:38Z",THA+","+JUL+","+"atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RqsAAA=","RE: "+S_YM,JUL,"2026-10-16T21:11:39Z",",".join([GRAZ,PPAL,ME,BSVC]),CC_YMc),
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
