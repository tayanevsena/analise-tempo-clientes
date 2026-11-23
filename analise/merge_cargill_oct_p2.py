import json, os
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
FTX="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ME="bma.road-southeast@cma-cgm.com"
JUL="Juliane.MARQUES@mercosul-line.com.br"; THA="thaina.santos@mercosul-line.com.br"
ISK="isadora_alonso@cargill.com"; ADB="Adriano_Dasilvabomtempo@cargill.com"; PED="Pedrohenrique_Defreitas@cargill.com"
SO3="operacional3@guarujaterminais.com.br"; SO4="operacional4@guarujaterminais.com.br"; CO="coordenador@guarujaterminais.com.br"
COTAG="cotton@agsurveyors.com"; VCA="vinicius.calazans@agsurveyors.com"; GFR="giovanna.freitas@agsurveyors.com"; MART="marcela.correia@agsurveyors.com"; CERT="certificate@agsurveyors.com"; MIC="micael.santiago@agsurveyors.com"
PLGC="-port-logistics-cotton@Cargill.com"; CDocs="cotton-br-docs@cargill.com"; PAC="-port-allocation-cotton@exch.cargill.com"; CCTL="cotton_ctl@Cargill.com"; CAS="-CASC-COTTON-ULA@cargill.com"; COTFAT="cotton_faturamento@cargill.com"; CBD="-cbs-uberlandia-fss-itp-originacaocotton-cargillonly@exch.cargill.com"; NFE="Nfe@cargill.com"
LGG="LAURIANE_GONCALVES@CRGL-THIRDPARTY.COM"
LIB="BMA.LIBERACAO@cma-cgm.com"; CCIS="ssz.customerservice@ccis-network.com"
NAT="Natalia_Queiroz@cargill.com"; IAN="ian_marques@cargill.com"
SO4T=",".join([JUL,SO3,CO]); T_CRO2=",".join([SO4,SO3,CO])
CC_ACE=",".join([PLGC,CDocs,PAC,VCA,COTAG,GFR,ME])
CC_ACE2=",".join([PLGC,CDocs,PAC,VCA,GFR])
S_ACES719="PR\u00c9-NOMEA\u00c7\u00c3O - S51907.A01 - BKG SSZ1859739 - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
S_DCD="BRSSZ | DADOS DE CONTAINERS | PR\u00c9-NOMEA\u00c7\u00e3O - S51504.B01 - BKG SSZ1862967 - SANTOS / HAIPHONG (CMA-CGM/ZIRANLOG) - CASA | Safra 2026".replace("CONTAI","CONTAINERS | PR\u00c9-NOMEA")
S_DCD="BRSSZ | DADOS DE CONTAINERS | PR\u00c9-NOMEA\u00c7\u00c3O - S51504.B01 - BKG SSZ1862967 - SANTOS / HAIPHONG (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
S_ACE186="BRSSZ | ACEITE | PR\u00c9-NOMEA\u00c7\u00c3O - S51504.B01 - BKG SSZ1862967 - SANTOS / HAIPHONG (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
S_LCV7="RE: [CMA CGM] BRSSZ | Libera\u00e7\u00e3o de vazio - CARGILL | COTTON | SSZ1862967 (LR)"
CC_LC=",".join(["liza.may@uni.com.br"])
T_RR=",".join(["roselma@rrtransporte.com","operacional@rrtransporte.com","intermodalmanaus@mercosul-line.com.br","jhonnespinheiro@rrtransporte.com","Thiago.Negreiros@mercosul-line.com.br"])
CC_UNI1=",".join(["laiza.may@uni.com.br","katny.barros@uni.com.br","helio@uni.com.br","cac@unitradinglog.com.br","faturamento.sts@uni.com.br",ME,"valerio.carvalho@uni.com.br","giovanna.reis@unitradinglog.com.br"])
CC_UNI2=",".join(["tatiana.ranieri@uni.com.br"]+CC_UNI1.split(","))
BMF=["geronimo@bomfrete.com.br","cotton_cargill@bomfrete.com.br"]
CC_UDT=",".join(["ctecotton@bomfrete.com.br","willyan.souza@algceleste.com","thiago.feitosa@algceleste.com","durvacil.assis@algceleste.com",NFE,CCTL,CAS,COTFAT,CBD,CCTL,CAS,LGG,LGG,LGG,LGG,COTAG,CERT,MART,MIC,ME,JUL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com",THA,"bma.mcastro@cma-cgm.com"]+BMF+["gerenciamentoderisco@bomfrete.com.br"]+BMF+["g.ricardo@bomfrete.com.br","wellington.lima@bomfrete.com.br"])
T_LCE7=",".join([IAN,"faturamento@cooami.com.br","fiscal@gpcagro.com","jessica.tristao@algceleste.com","cotton@cooami.com.br","jaison@cooami.com.br"])
T_LCE3=",".join(["faturamento@cooami.com.br","fiscal@gpcagro.com","jessica.tristao@algceleste.com","cotton@cooami.com.br","jaison@cooami.com.br"])
S_UDT="FATURAMENTO \u2013 Exporta\u00e7\u00e3o Indireta \u2013 ALGCELES  \u2013 Instru\u00e7\u00e3o: S51504.B01 \u2013 PLACA: UDT4I05 \u2013 NF: 228092 / 228091"
rows=[
 (B4,"Rh_AAA=","BRSSZ | ACEITE | PR\u00c9-NOMEA\u00c7\u00c3O - S51907.A01 - BKG SSZ1859739 - 15HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026",JUL,"2026-10-29T18:25:01Z",ADB,CC_ACE),
 (B4,"RiBAAA=",S_ACES719,ADB,"2026-10-29T16:40:11Z",",".join([THA,ME,JUL]),",".join([PLGC,CDocs,PAC,VCA,COTAG,GFR])),
 (FTX,"QrBAAA=","PROGRAMA\u00c7\u00c3O DE ENTREGAS \u2013 MERCOSUL \u2013 30/10/2026","RAYNARA.SANTOS@MERCOSUL-LINE.COM.BR","2026-10-28T23:13:25Z",T_RR,""),
 (B4,"RinAAA=",S_DCD,JUL,"2026-10-28T17:56:37Z",",".join([PED,MART,ADB,ME,COTAG]),",".join([PLGC,CDocs,PAC,VCA,GFR])),
 (B4,"RipAAA=","RES: [CMA CGM] BRSSZ | CROSS DOCKING - COTTON | CARGILL x GUARUJ\u00c1 TERMINAIS | S51504.B01 - BKG SSZ1862967 10HCs",SO4,"2026-10-28T17:47:04Z",SO4T,ME),
 (B4,"Ri1AAA=","RES: [CMA CGM] BRSSZ | CROSS DOCKING - COTTON | CARGILL x GUARUJ\u00c1 TERMINAIS | S51504.B01 - BKG SSZ1862967 10HCs",SO4,"2026-10-27T21:36:43Z",SO4T,ME),
 (B4,"Ri3AAA=","RE: [CMA CGM] BRSSZ | CROSS DOCKING - COTTON | CARGILL x GUARUJ\u00c1 TERMINAIS | S51504.B01 - BKG SSZ1862967 10HCs",JUL,"2026-10-27T21:20:39Z",T_CRO2,ME),
 (B4,"Ri4AAA=","RE: SOLICITA\u00c7\u00c3O // ESTADIA // CMA CGM //  CARGIL - BOOKING: 26BR00018962212 / 26BR00019033762 - CHN3839530  - CHN3831374",JUL,"2026-10-27T21:14:19Z","fellipe.xavier@unitradinglog.com.br",CC_UNI1),
 (B4,"Ri6AAA=","RE: SOLICITA\u00c7\u00c3O // ESTADIA // CMA CGM //  CARGIL - BOOKING: 26BR00018962212 - CHN3831374",JUL,"2026-10-27T21:05:17Z","fellipe.xavier@unitradinglog.com.br",CC_UNI2),
 (B4,"Ri7AAA=","RES: SOLICITA\u00c7\u00c3O // ESTADIA // CMA CGM //  CARGIL - BOOKING: 26BR00018962212 / 26BR00019033762 - CHN3839530  - CHN3831374","fellipe.xavier@unitradinglog.com.br","2026-10-27T21:04:50Z",JUL,CC_UNI1),
 (B4,"Ri-AAA=",S_LCV7,LIB,"2026-10-27T20:35:35Z",",".join([JUL,CCIS]),ME),
 (B4,"RjBAAA=","[CMA CGM] BRSSZ | Libera\u00e7\u00e3o de vazio - CARGILL | COTTON | SSZ1862967",JUL,"2026-10-27T20:21:25Z",LIB,ME),
 (B4,"RjGAAA=","RES: "+S_ACE186,PED,"2026-10-27T18:28:00Z",",".join([JUL,MART,ADB,ME,COTAG]),",".join([PLGC,CDocs,PAC,VCA,GFR])),
 (B4,"RjHAAA=","RE: "+S_ACE186,JUL,"2026-10-27T18:23:32Z",",".join([MART,ADB,ME,COTAG]),",".join([PLGC,CDocs,PAC,VCA,GFR])),
 (B4,"RjRAAA=","RES: "+S_UDT,NAT,"2026-10-27T14:55:22Z",T_LCE7,CC_UDT),
 (B4,"RjZAAA=","RE: SDL-DOC - [CMA CGM] BRSSZ | INTERNO | ROAD | AJUSTE DE TAXAS | CARGILL - CHN3839530","bra.service@cma-cgm.com","2026-10-27T13:43:55Z",JUL,ME),
 (B4,"RjaAAA=","RE: SDL-DOC - [CMA CGM] BRSSZ | INTERNO | ROAD | AJUSTE DE TAXAS | CARGILL - CHN3831443","bra.service@cma-cgm.com","2026-10-27T13:39:59Z",JUL,ME),
 (B4,"RjbAAA=","RE: SDL-DOC - [CMA CGM] BRSSZ | INTERNO | ROAD | AJUSTE DE TAXAS | CARGILL - CHN3831374","bra.service@cma-cgm.com","2026-10-27T13:37:33Z",JUL,ME),
 (B4,"RjdAAA=","RE: SDL-DOC - [CMA CGM] BRSSZ | INTERNO | ROAD | AJUSTE DE TAXAS | CARGILL - CHN3831378","bra.service@cma-cgm.com","2026-10-27T13:33:11Z",JUL,ME),
 (B4,"RjgAAA=","RES: "+S_UDT,"embarquecotton1@bomfrete.com.br","2026-10-27T13:10:10Z",",".join([IAN,NAT])+","+T_LCE3,CC_UDT),
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
import collections
c=collections.Counter(json.loads(l)["date"][:10] for l in open(out))
print("by day:",sorted(c.items()))
