import json, collections
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ME="bma.road-southeast@cma-cgm.com"
JUL="Juliane.MARQUES@mercosul-line.com.br"; THA="thaina.santos@mercosul-line.com.br"
ADB="Adriano_Dasilvabomtempo@cargill.com"; PED="Pedrohenrique_Defreitas@cargill.com"
SO3="operacional3@guarujaterminais.com.br"; SO4="operacional4@guarujaterminais.com.br"; CO="coordenador@guarujaterminais.com.br"
COTAG="cotton@agsurveyors.com"; MART="marcela.correia@agsurveyors.com"; CERT="certificate@agsurveyors.com"; MIC="micael.santiago@agsurveyors.com"
CCTL="cotton_ctl@Cargill.com"; CAS="-CASC-COTTON-ULA@cargill.com"; COTFAT="cotton_faturamento@cargill.com"; CBD="-cbs-uberlandia-fss-itp-originacaocotton-cargillonly@exch.cargill.com"; NFE="Nfe@cargill.com"
LGG="LAURIANE_GONCALVES@CRGL-THIRDPARTY.COM"; CDocs="cotton-br-docs@cargill.com"; GT="cotton_gtocbr@cargill.com"
NAT="Natalia_Queiroz@cargill.com"; IAN="ian_marques@cargill.com"; CRI="Crisla_Leite@cargill.com"
SO4T=",".join([JUL,SO3,CO]); T_CRO2=",".join([SO4,SO3,CO])
T_LCE3=",".join(["faturamento@cooami.com.br","fiscal@gpcagro.com","jessica.tristao@algceleste.com","cotton@cooami.com.br","jaison@cooami.com.br"])
S_UDT="FATURAMENTO \u2013 Exporta\u00e7\u00e3o Indireta \u2013 ALGCELES  \u2013 Instru\u00e7\u00e3o: S51504.B01 \u2013 PLACA: UDT4I05 \u2013 NF: 228092 / 228091"
CC_UDT=",".join(["ctecotton@bomfrete.com.br","willyan.souza@algceleste.com","thiago.feitosa@algceleste.com","durvacil.assis@algceleste.com",NFE,CCTL,CAS,COTFAT,CBD,CCTL,CAS,LGG,LGG,LGG,LGG,COTAG,CERT,MART,MIC,ME,JUL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com",THA,"bma.mcastro@cma-cgm.com","geronimo@bomfrete.com.br","cotton_cargill@bomfrete.com.br","gerenciamentoderisco@bomfrete.com.br","cotton_cargill@bomfrete.com.br","geronimo@bomfrete.com.br","g.ricardo@bomfrete.com.br","wellington.lima@bomfrete.com.br"])
T_ESTU=",".join(["Karen_Morotti@cargill.com",THA,ADB,"Paulo_Carvalho@cargill.com",PED,"Lucas_Simoes@cargill.com","Rafael_Felicissimo@cargill.com","Thairony_Souza@cargill.com","glaudeir_braga_ramos@cargill.com"])
CC_ESTU=",".join(["-COTTON-BR-PLANNING@Cargill.com","Beatriz_Carvalho@cargill.com","Jose_americo@cargill.com","Karoline_Dasilvapereira@cargill.com","Luciana_Calegari@cargill.com","bma.mcastro@cma-cgm.com","RCE.JLIMA@cma-cgm.com","Eduardo.FIGUEIRA@mercosul-line.com.br",CDocs,GT,"BMA.NLEY@cma-cgm.com","Renato_Magalhaes@cargill.com",CCTL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com",ME])
T_ESTU2=",".join(["Karen_Morotti@cargill.com",THA,ADB,"Paulo_Carvalho@cargill.com",PED,"Lucas_Simoes@cargill.com","Rafael_Felicissimo@cargill.com","Thairony_Souza@cargill.com"])
BSVC="bra.service@cma-cgm.com"
CASC="Casc_Impo@cargill.com"; GRAZ="graziela.braga@pibernat.com.br"; PPAL="Paula_Palazzo@cargill.com"; GETH="gethelp@cargill.com"
GIO="Giovana_Santos1@cargill.com"; WES="Wesley_Delisolasantos@cargill.com"; TFA="Tiago_Faria@cargill.com"
AGRO="-AGROQUIMICOS-CROPINPUT@Cargill.com"; AGRO2="AGROQUIMICOS-CROPINPUT@cargill.com"; CSIMP="-CASC-GTOC-IMP@exch.cargill.com"
FINCUST="-finance-customs-cargillonly@Cargill.com"; TEALL="-CASC-IMPORTS-TE-ALL@Cargill.com"
NBAR="Natalia_Barreto@cargill.com"; CLF="Clara_Fernanda@cargill.com"; JAC="Jaciara_Marquesdesouza@cargill.com"
ITRG="impo.cargill.rgd@pibernat.com.br"
SCL="-SCL-COTTON-ORIGEM@Cargill.com"; TOR="-TORRE-FARMERCARE-COTTON@Cargill.com"; MYU="Matheus_Yure@cargill.com"
T_COF1=",".join([CRI,"faturamento1@cooperfran.com.br",NAT,"balancasykue@catelan.agr.br","comercial@catelan.agr.br",COTFAT,CBD,CCTL,CAS,COTAG,CERT,MART,MIC,ME,JUL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com",THA,"bma.mcastro@cma-cgm.com","fribon.algodao@fribontransportes.com.br","algodao@fribontransportes.com.br","amanda.oliveira@fribontransportes.com.br"])
T_COF2=",".join(["faturamento1@cooperfran.com.br",NAT,"balancasykue@catelan.agr.br","comercial@catelan.agr.br",COTFAT,CBD,CCTL,CAS,COTAG,CERT,MART,MIC,ME,JUL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com",THA,"bma.mcastro@cma-cgm.com","fribon.algodao@fribontransportes.com.br","algodao@fribontransportes.com.br","amanda.oliveira@fribontransportes.com.br"])
CC_COF1=",".join([CCTL,CAS,SCL,TOR,MYU,"cooperfran.adm@cooperfran.com.br","faturamento2@cooperfran.com.br","leda@cooperfran.com.br","faturamento@cooperfran.com.br","faturamento3@cooperfran.com.br","comercial01@catelan.agr.br","Fribon@fribontransportes.com.br","lem.algodao@fribontransportes.com.br",LGG])
CC_COF3=",".join([SCL,TOR,MYU,"cooperfran.adm@cooperfran.com.br","faturamento2@cooperfran.com.br","faturamento@cooperfran.com.br","faturamento3@cooperfran.com.br","comercial01@catelan.agr.br","Fribon@fribontransportes.com.br","lem.algodao@fribontransportes.com.br"])
CC_COF4=",".join([CCTL,CAS,SCL,TOR,MYU,"cooperfran.adm@cooperfran.com.br","faturamento2@cooperfran.com.br","faturamento@cooperfran.com.br","faturamento3@cooperfran.com.br","comercial01@catelan.agr.br","Fribon@fribontransportes.com.br","lem.algodao@fribontransportes.com.br"])
S_CRO10="RE"+""+": [CMA CGM] BRSSZ | CROSS DOCKING - COTTON | CARGILL x GUARUJ\u00c1 TERMINAIS | S51504.B01 - BKG SSZ1862967 10HCs"
S_AND2="RE: Corre\u00e7\u00e3o  [CMA CGM] Cadastros | Guaruj\u00e1 Terminais x CARGILL"
S_EST2="RE: Planejamento Estufagem Cargill - CMA STS & SSA - Crop 2026"
S_TAX9530="SDL-DOC - [CMA CGM] BRSSZ | INTERNO | ROAD | AJUSTE DE TAXAS | CARGILL - CHN3839530"
S_TAX443="SDL-DOC - [CMA CGM] BRSSZ | INTERNO | ROAD | AJUSTE DE TAXAS | CARGILL - CHN3831443"
S_TAX374="SDL-DOC - [CMA CGM] BRSSZ | INTERNO | ROAD | AJUSTE DE TAXAS | CARGILL - CHN3831374"
S_TAX378="SDL-DOC - [CMA CGM] BRSSZ | INTERNO | ROAD | AJUSTE DE TAXAS | CARGILL - CHN3831378"
S_YM152="RE:  LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001903376-2 | CHLORFENAPYR - RIO VERDE | CASC0141/26, PO 521715Z366 | YN2026WM152-2 (CHN3839530)"
S_GHYD276="RE:  LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001879016-0 | DSA | CASC0139/26, PO 521715Z361 | GLIFOSATO NGC - RIO VERDE | GHYD260276 (CHN3831443)"
S_GHYD275="RE:  LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001889833-6 | DSA| CASC0137/26, PO 521715Z359 | GLIFOSATO NGC - RIO VERDE | GHYD260275 (CHN3831378) *CARGA DSA*"
rows=[
 (B4,"RjiAAA=","RES: "+S_UDT,IAN,"2026-10-27T12:12:30Z",",".join([NAT])+","+T_LCE3,CC_UDT),
 (B4,"RjjAAA=",S_UDT,NAT,"2026-10-27T11:39:04Z",T_LCE3,CC_UDT),
 (B4,"Rj9AAA=",S_EST2,JUL,"2026-10-26T17:38:49Z",T_ESTU,CC_ESTU),
 (B4,"RkBAAA=","LOGIN | Guaruj\u00e1 Terminais x CARGILL","operacional4@guarujaterminais.com.br","2026-10-26T16:40:34Z",",".join([JUL,CO,SO3]),ME),
 (B4,"RkOAAA=","RES: FATURAMENTO \u2013 Exporta\u00e7\u00e3o Indireta \u2013 ALGSLUIZ  \u2013 Instru\u00e7\u00e3o: S51504.B01 \u2013 PLACA: FSF9D09 \u2013 NF: 16030",IAN,"2026-10-26T11:58:41Z",T_COF1,CC_COF1),
 (B4,"RkPAAA=","FATURAMENTO \u2013 Exporta\u00e7\u00e3o Indireta \u2013 ALGSLUIZ  \u2013 Instru\u00e7\u00e3o: S51504.B01 \u2013 PLACA: FSF9D09 \u2013 NF: 16030",CRI,"2026-10-26T11:45:37Z",T_COF2,CC_COF1),
 (B4,"RkRAAA=",S_AND2,JUL,"2026-10-24T23:17:52Z",",".join([SO4,CO,SO3]),ME),
 (B4,"RkSAAA=",S_EST2,JUL,"2026-10-24T23:17:06Z",T_ESTU2,CC_ESTU),
 (B4,"RkWAAA=",S_TAX9530,JUL,"2026-10-24T20:44:33Z",BSVC,ME),
 (B4,"RkXAAA=",S_YM152,JUL,"2026-10-24T20:43:01Z",",".join([THA,CASC,GRAZ,PPAL,ME,BSVC]),",".join([GIO,AGRO,ITRG,CSIMP,WES,TFA,FINCUST,NBAR,CLF,JAC])),
 (B4,"RkYAAA=","RE: [CMA CGM] BRSSZ | Programa\u00e7\u00e3o CARGILL | UNITRADING - CHN3839530",JUL,"2026-10-24T20:41:21Z",",".join(["giovanna.reis@unitradinglog.com.br","atendimentoaocliente.sts@uni.com.br","operacional.sts@uni.com.br"]),ME),
 (B4,"RkZAAA=",S_GHYD276,JUL,"2026-10-24T20:37:34Z",",".join([THA,CASC,GRAZ,GETH,ME,BSVC,AGRO2,PPAL,WES,TEALL]),",".join([GIO,AGRO,ITRG,CSIMP,TFA])),
 (B4,"RkaAAA=",S_TAX443,JUL,"2026-10-24T20:37:25Z",BSVC,ME),
 (B4,"RkbAAA=",S_TAX374,JUL,"2026-10-24T20:31:45Z",BSVC,ME),
 (B4,"RkdAAA=","RE: FATURAMENTO \u2013 Exporta\u00e7\u00e3o Indireta \u2013 ALGSLUIZ  \u2013 Instru\u00e7\u00e3o: S51504.B01 \u2013 PLACA: RYQ3J58 \u2013 NF: 16022","Michele_Nunes@cargill.com","2026-10-24T19:58:41Z",T_COF1,CC_COF3),
 (B4,"RkgAAA=","FATURAMENTO \u2013 Exporta\u00e7\u00e3o Indireta \u2013 ALGSLUIZ  \u2013 Instru\u00e7\u00e3o: S51504.B01 \u2013 PLACA: RYQ3J58 \u2013 NF: 16022",CRI,"2026-10-24T18:05:45Z",T_COF2,CC_COF4),
 (B4,"RkjAAA=",S_GHYD275,JUL,"2026-10-24T15:39:24Z",",".join([CASC,THA,GRAZ,GETH,PPAL,ME,BSVC,GIO]),",".join([AGRO,ITRG,CSIMP,WES,TFA,TEALL])),
 (B4,"RkkAAA=",S_TAX378,JUL,"2026-10-24T15:36:04Z",BSVC,ME),
 (B4,"RklAAA=","RES: [CMA CGM] BRSSZ | CROSS DOCKING - COTTON | CARGILL x GUARUJ\u00c1 TERMINAIS | S51504.B01 - BKG SSZ1862967 10HCs",SO4,"2026-10-24T14:25:15Z",",".join([JUL,SO3,CO]),ME),
 (B4,"RkmAAA=","[CMA CGM] BRSSZ | CROSS DOCKING - COTTON | CARGILL x GUARUJ\u00c1 TERMINAIS | S51504.B01 - BKG SSZ1862967 10HCs",JUL,"2026-10-24T14:05:34Z",",".join([SO4,SO3,CO]),ME),
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
