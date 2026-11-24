import json, collections
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
FTX="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ME="bma.road-southeast@cma-cgm.com"
JUL="Juliane.MARQUES@mercosul-line.com.br"; THA="thaina.santos@mercosul-line.com.br"
ADB="Adriano_Dasilvabomtempo@cargill.com"; PED="Pedrohenrique_Defreitas@cargill.com"
IAN="ian_marques@cargill.com"; NAT="Natalia_Queiroz@cargill.com"; CRI="Crisla_Leite@cargill.com"; REN="Renata_Lima@cargill.com"
COTAG="cotton@agsurveyors.com"; MART="marcela.correia@agsurveyors.com"; CERT="certificate@agsurveyors.com"; MIC="micael.santiago@agsurveyors.com"
VCA="vinicius.calazans@agsurveyors.com"; GFR="giovanna.freitas@agsurveyors.com"
PLGC="-port-logistics-cotton@Cargill.com"; CDocs="cotton-br-docs@cargill.com"; PAC="-port-allocation-cotton@exch.cargill.com"
CCTL="cotton_ctl@Cargill.com"; CAS="-CASC-COTTON-ULA@cargill.com"; COTFAT="cotton_faturamento@cargill.com"; CBD="-cbs-uberlandia-fss-itp-originacaocotton-cargillonly@exch.cargill.com"; NFE="Nfe@cargill.com"
LGG="LAURIANE_GONCALVES@CRGL-THIRDPARTY.COM"; GT="cotton_gtocbr@cargill.com"
SO3="operacional3@guarujaterminais.com.br"; SO4="operacional4@guarujaterminais.com.br"; CO="coordenador@guarujaterminais.com.br"
CC_PG=",".join([PLGC,CDocs,PAC,VCA,GFR])
TRES=["administrativoalg2@trescoqueiros.com","financeiro3@trescoqueiros.com","administrativoalg3@trescoqueiros.com","administrativoalg@trescoqueiros.com","comercial2@trescoqueiros.com","comercial5@trescoqueiros.com","comercial@trescoqueiros.com","controladoria@trescoqueiros.com","comercial4@trescoqueiros.com","thomas@trescoqueiros.com"]
TRES3=TRES+["financeiro4@trescoqueiros.com","financeiro5@trescoqueiros.com","aprendizfinanceiro@trescoqueiros.com"]
CC_UNI1=",".join(["laiza.may@uni.com.br","katny.barros@uni.com.br","helio@uni.com.br","cac@unitradinglog.com.br","faturamento.sts@uni.com.br",ME,"valerio.carvalho@uni.com.br","giovanna.reis@unitradinglog.com.br"])
CC_ESTU=",".join(["-COTTON-BR-PLANNING@Cargill.com","Beatriz_Carvalho@cargill.com","Jose_americo@cargill.com","Karoline_Dasilvapereira@cargill.com","Luciana_Calegari@cargill.com","bma.mcastro@cma-cgm.com","RCE.JLIMA@cma-cgm.com","Eduardo.FIGUEIRA@mercosul-line.com.br",CDocs,GT,"BMA.NLEY@cma-cgm.com","Renato_Magalhaes@cargill.com",CCTL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com",ME])
TKR=["renato.costa@tkrinspection.com","kelly.lopes@tkrinspection.com","carlos.osman@tkrinspection.com","cotton@tkrinspection.com","drafts@tkrinspection.com"]
CASC="Casc_Impo@cargill.com"; GRAZ="graziela.braga@pibernat.com.br"; PPAL="Paula_Palazzo@cargill.com"; GETH="gethelp@cargill.com"
GIO="Giovana_Santos1@cargill.com"; WES="Wesley_Delisolasantos@cargill.com"; TFA="Tiago_Faria@cargill.com"
AGRO="-AGROQUIMICOS-CROPINPUT@Cargill.com"; CSIMP="-CASC-GTOC-IMP@exch.cargill.com"; TEALL="-CASC-IMPORTS-TE-ALL@Cargill.com"; ITRG="impo.cargill.rgd@pibernat.com.br"; BSVC="bra.service@cma-cgm.com"
S_ACE186="BRSSZ | ACEITE | PR\u00c9-NOMEA\u00c7\u00c3O - S51504.B01 - BKG SSZ1862967 - SANTOS / HAIPHONG (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
S_PNS515="PR\u00c9-NOMEA\u00c7\u00c3O - S51504.B01 - BKG SSZ1862967 - SANTOS / HAIPHONG (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
S_EST2="RE: Planejamento Estufagem Cargill - CMA STS & SSA - Crop 2026"
S_EST0="Planejamento Estufagem Cargill - CMA STS & SSA - Crop 2026"
S_ESTA="RES: SOLICITA\u00c7\u00c3O // ESTADIA // CMA CGM //  CARGIL - BOOKING: 26BR00018962212 / 26BR00019033762 - CHN3839530  - CHN3831374"
S_DVS="FATURAMENTO \u2013 Exporta\u00e7\u00e3o Indireta \u2013 ALGTRESC  \u2013 Instru\u00e7\u00e3o: S51504.B01 \u2013 PLACA: DVS4I70 \u2013 NF: 227883"
S_GXA="FATURAMENTO \u2013 Exporta\u00e7\u00e3o Indireta \u2013 ALGTRESC  \u2013 Instru\u00e7\u00e3o: S51504.B01 \u2013 PLACA: GXA9992 \u2013 NF: 227876"
CC_DVSR=",".join(TRES+[COTFAT,CBD,CCTL,CAS,LGG,LGG,LGG,LGG,COTAG,CERT,MART,MIC,ME,JUL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com",THA,"bma.mcastro@cma-cgm.com","geronimo@bomfrete.com.br","cotton_cargill@bomfrete.com.br","financeiro5@trescoqueiros.com","aprendizfinanceiro@trescoqueiros.com","jeniffer@bomfrete.com.br","jackeline@bomfrete.com.br"])
CC_DVSN=",".join(TRES+[COTFAT,CBD,CCTL,CAS,LGG,LGG,LGG,LGG,COTAG,CERT,MART,MIC,ME,JUL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com",THA,"bma.mcastro@cma-cgm.com","geronimo@bomfrete.com.br","cotton_cargill@bomfrete.com.br","financeiro5@trescoqueiros.com","aprendizfinanceiro@trescoqueiros.com"])
CC_GXA=",".join(TRES3)
FATC=[COTFAT,CBD,CCTL,CAS,LGG,"geronimo@bomfrete.com.br","cotton_cargill@bomfrete.com.br",COTFAT,CBD,CCTL,CAS,LGG,COTAG,CERT,MART,MIC,ME,JUL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com",THA,"bma.mcastro@cma-cgm.com","geronimo@bomfrete.com.br","cotton_cargill@bomfrete.com.br"]
T_GXA_A=",".join([REN,CRI,"faturamento@cooami.com.br","comercial3@trescoqueiros.com","jaison@cooami.com.br","cotton@cooami.com.br","cotton@cooami.com.br",CCTL,NFE,"ctecotton@bomfrete.com.br"]+FATC)
T_GXA_B=",".join([CRI,"faturamento@cooami.com.br","comercial3@trescoqueiros.com","jaison@cooami.com.br","cotton@cooami.com.br","cotton@cooami.com.br",CCTL,NFE,"ctecotton@bomfrete.com.br"]+FATC)
T_GXA_C=T_GXA_B+","+NAT
T_GXA_D=",".join(["faturamento@cooami.com.br","comercial3@trescoqueiros.com","jaison@cooami.com.br","cotton@cooami.com.br","cotton@cooami.com.br",CCTL,NFE,"ctecotton@bomfrete.com.br"]+FATC)
T_DVS_cte=",".join([IAN,NAT,"faturamento@cooami.com.br","comercial3@trescoqueiros.com","jaison@cooami.com.br","cotton@cooami.com.br","cotton@cooami.com.br",CCTL])
T_DVS_ian=",".join([NAT,"faturamento@cooami.com.br","comercial3@trescoqueiros.com","jaison@cooami.com.br","cotton@cooami.com.br","cotton@cooami.com.br",CCTL,"ctecotton@bomfrete.com.br"])
T_DVS_nat=",".join(["faturamento@cooami.com.br","comercial3@trescoqueiros.com","jaison@cooami.com.br","cotton@cooami.com.br","cotton@cooami.com.br",CCTL,NFE,"ctecotton@bomfrete.com.br"])
LBT=" [CMA CGM] BRSSZ | Programa\u00e7\u00e3o CARGILL | UNITRADING - CHN3839530"
rows=[
 (B4,"RknAAA=","BRSSZ | ACEITE | PR\u00c9-NOMEA\u00c7\u00c3O - S51504.B01 - BKG SSZ1862967 - SANTOS / HAIPHONG (CMA-CGM/ZIRANLOG) - CASA | Safra 2026",JUL,"2026-10-24T14:02:24Z",",".join([MART,ADB,THA,ME,COTAG]),CC_PG),
 (B4,"RkvAAA=","RES: "+S_DVS,"ctecotton@bomfrete.com.br","2026-10-23T21:58:59Z",T_DVS_cte,CC_DVSR),
 (B4,"RkyAAA=","RES: "+S_PNS515,MART,"2026-10-23T21:11:20Z",",".join([ADB,THA,ME,JUL,COTAG]),CC_PG),
 (B4,"Rk0AAA=","RES: "+S_GXA,"embarquecotton1@bomfrete.com.br","2026-10-23T21:00:09Z",T_GXA_A,CC_GXA),
 (B4,"Rk2AAA=",S_ESTA,"fellipe.xavier@unitradinglog.com.br","2026-10-23T20:23:14Z",JUL,CC_UNI1),
 (B4,"Rk3AAA=","RES: "+S_PNS515,ADB,"2026-10-23T20:10:35Z",",".join([THA,ME,JUL,COTAG]),CC_PG),
 (B4,"Rk4AAA=","RES: "+S_PNS515,ADB,"2026-10-23T20:07:53Z",",".join([THA,ME,JUL]),",".join([PLGC,CDocs,PAC]+TKR)),
 (B4,"Rk8AAA=",S_PNS515,ADB,"2026-10-23T19:42:27Z",",".join([THA,ME,JUL]),",".join([PLGC,CDocs,PAC]+TKR)),
 (B4,"RlAAAA=","RES: "+S_DVS,IAN,"2026-10-23T18:51:48Z",T_DVS_ian,CC_DVSN),
 (B4,"RlBAAA=","RES: "+S_GXA,REN,"2026-10-23T18:46:06Z",T_GXA_B,CC_GXA),
 (B4,"RlGAAA=","RES: "+S_GXA,"wellington.lima@bomfrete.com.br","2026-10-23T18:12:56Z",T_GXA_C,CC_GXA),
 (B4,"RlIAAA=",S_EST2,"Karen_Morotti@cargill.com","2026-10-23T18:01:34Z",",".join([THA,ADB,JUL,"Paulo_Carvalho@cargill.com",PED,"Lucas_Simoes@cargill.com","Rafael_Felicissimo@cargill.com","Thairony_Souza@cargill.com"]),CC_ESTU),
 (B4,"RlTAAA=",S_DVS,NAT,"2026-10-23T14:15:03Z",T_DVS_nat,CC_DVSN),
 (B4,"RlUAAA=",S_EST0,THA,"2026-10-23T14:14:06Z",",".join([ADB,JUL,"Paulo_Carvalho@cargill.com","Karen_Morotti@cargill.com",PED,"Lucas_Simoes@cargill.com","Rafael_Felicissimo@cargill.com","Thairony_Souza@cargill.com"]),CC_ESTU),
 (B4,"RlZAAA=",S_GXA,CRI,"2026-10-23T13:49:17Z",T_GXA_D,CC_GXA),
 (B4,"RlaAAA=","[CMA CCGM] BRSSZ | PROGRAMA\u00c7\u00c3O IMPORTA\u00c7\u00c3O | CARGILL x UNITRADING | CHN3831443","giovanna.reis@unitradinglog.com.br","2026-10-23T13:43:18Z",",".join(["felipe.lopes@uni.com.br",THA,JUL,"atendimentoaocliente.sts@uni.com.br"]),",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RlpAAA=","RES:  LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001889833-6 | DSA| CASC0137/26, PO 521715Z359 | GLIFOSATO NGC - RIO VERDE | GHYD260275 (CHN3831378) *CARGA DSA*",CASC,"2026-10-23T11:32:46Z",",".join([THA,JUL,GRAZ,GETH,PPAL,ME,BSVC,GIO]),",".join([AGRO,ITRG,CSIMP,WES,TFA,TEALL])),
 (B4,"RmlAAA=","[CMA CGM] BRSSZ | Programa\u00e7\u00e3o CARGILL | UNITRADING - CHN3839530","giovanna.reis@unitradinglog.com.br","2026-10-22T13:56:39Z",",".join([THA,"atendimentoaocliente.sts@uni.com.br","operacional.sts@uni.com.br"]),ME),
 (B4,"RmoAAA=",LBT,THA,"2026-10-22T13:31:57Z",",".join(["giovanna.reis@unitradinglog.com.br","atendimentoaocliente.sts@uni.com.br","operacional.sts@uni.com.br"]),ME),
 (FTX,"QGoAAA=","PROGRAMA\u00c7\u00c3O DE ENTREGAS \u2013 MERCOSUL \u2013 23/10/2026","RAYNARA.SANTOS@MERCOSUL-LINE.COM.BR","2026-10-22T12:58:30Z",",".join(["roselma@rrtransporte.com","operacional@rrtransporte.com","intermodalmanaus@mercosul-line.com.br","jhonnespinheiro@rrtransporte.com","Thiago.Negreiros@mercosul-line.com.br"]),""), 
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
