import json, os
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ME="bma.road-southeast@cma-cgm.com"; BSVC="BRA.SERVICE@CMA-CGM.COM"; PLE="SSZ.PLETTRA@cma-cgm.com"; RSA="ssz.rsantos@cma-cgm.com"
JUL="Juliane.MARQUES@mercosul-line.com.br"; THA="thaina.santos@mercosul-line.com.br"
ISK="isadora_alonso@cargill.com"; ADB="Adriano_Dasilvabomtempo@cargill.com"; PED="Pedrohenrique_Defreitas@cargill.com"; AND="andressa_nunes@cargill.com"
VRA="Vitoria_Raiane@cargill.com"; SMA="Sandielle_Maia@cargill.com"; GT="cotton_gtocbr@cargill.com"
SO3="operacional3@guarujaterminais.com.br"; SO4="operacional4@guarujaterminais.com.br"; CO="coordenador@guarujaterminais.com.br"
EXPX="contato@expurgaguacu.com.br"
BAR="barbara@mediterraneanlogistica.com.br"; ALE="alexandre@mediterraneanlogistica.com.br"; LAI="laiza@mediterraneanlogistica.com.br"; MED="mediterranean@mediterraneanlogistica.com.br"; VINM="vinicius@mediterraneanlogistica.com.br"
CAM="camila.alonso@agsurveyors.com"; MIC="micael.santiago@agsurveyors.com"; COTAG="cotton@agsurveyors.com"; VCA="vinicius.calazans@agsurveyors.com"; GFR="giovanna.freitas@agsurveyors.com"
PLGC="-port-logistics-cotton@Cargill.com"; CDocs="cotton-br-docs@cargill.com"; PAC="-port-allocation-cotton@exch.cargill.com"
TKR2="renato.costa@tkrinspection.com"; TKR3="kelly.lopes@tkrinspection.com"; TKR4="carlos.osman@tkrinspection.com"; TKR5="cotton@tkrinspection.com"; TSB="renato.sobral@tkrinspection.com"
PRE712="S51907.A01 - BKG SSZ1859739 - 12HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026  M-3762/26"
PRE15="S51907.A01 - BKG SSZ1859739 - 15HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026  M-3762/26"
S_CRO="RES: [CMA CGM] BRSSZ | CROSS DOCKING - COTTON | CARGILL x GUARUJ\u00c1 TERMINAIS | S51907.A01 - BKG SSZ1859739 - 15HCs"
S_POS="POSICIONAMENTO DE CONTEINER -  PLANILHA DE PESO - BRSSZ | DRAFT PARCIAL & ATUALIZA\u00c7\u00c3O DE DESCARGA | "+PRE15
S_PLA="PLANILHA DE PESO - BRSSZ | DRAFT PARCIAL & ATUALIZA\u00c7\u00c3O DE DESCARGA | "+PRE15
S_SDL="SDL-DOC | BRSSZ | AJUSTE DE BOOKING MULTIMODAL | CARGILL | COTTON"
S_FUM="PENDENTE MAPA - FUMIGA\u00c7\u00c3O - NFS & DUE | APROVADA | PLANILHA DE PESO PARCIAL | "+PRE712
S_APR="APROVADA | PLANILHA DE PESO PARCIAL | "+PRE712
S_FOUT="FATURAMENTO \u2013 Exporta\u00e7\u00e3o Indireta \u2013 ALGCTCOT  \u2013 Instru\u00e7\u00e3o: S00701.A05 \u2013 PLACA: OUT9D43 \u2013 NF: 46245"
CC_PAP=",".join([PLGC,CDocs,PAC,BSVC]); CC_3PL=",".join([PLGC,CDocs,PAC,VCA,GFR,ME])
T_CRO=",".join([JUL,SO3,CO]); T_CRO2=",".join([SO4,SO3,CO])
LUZ="luizjunior@hiperconterminais.com.br"
CCTL="cotton_ctl@Cargill.com"; CAS="-CASC-COTTON-ULA@cargill.com"; COTFAT="cotton_faturamento@cargill.com"; CBD="-cbs-uberlandia-fss-itp-originacaocotton-cargillonly@exch.cargill.com"
LGG="LAURIANE_GONCALVES@CRGL-THIRDPARTY.COM"; JPR="JENNIFER_PERIS@CRGL-THIRDPARTY.COM"
G10=["ian_marques@cargill.com","Crisla_Leite@cargill.com","lucas.pivetta@cooperuniaolrv.com.br","contabilidade@grupocinpak.com.br","Harielly_Dasilvabatista@cargill.com","ctcottonlrv@hotmail.com","lucas.strassi@g10transportes.com.br","rondonopolis.cotton@g10transportes.com.br",CCTL,CAS,"mateus.munhoz@cooperuniaolrv.com.br","faturamento@cooperuniaolrv.com.br",COTFAT,CBD,CCTL,CAS,LGG,JPR,TKR2,TKR4,TKR3,TSB,TKR5,ME,JUL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com",THA,"bma.mcastro@cma-cgm.com","joao.bosco@g10transportes.com.br","comercial.cotton@g10transportes.com.br","josevan.oliveira@g10transportes.com.br","rondonopolis.cotton@g10transportes.com.br","bahia@g10transportes.com.br"]
CC_G10=",".join(["algodoeira@ctcotton.com.br","rodrigo.bonatto@g10transportes.com.br"])
CC_3PL_SO=",".join([PLGC,CDocs,PAC,VCA,GFR,ME,SO3,CO,SO4])
rows=[
 (B4,"SLjAAA=",S_CRO,SO4,"2026-11-18T13:20:23Z",T_CRO,ME),
 (B4,"SLmAAA=",S_CRO,SO4,"2026-11-18T13:06:43Z",T_CRO,ME),
 (B4,"SLnAAA=","RE: "+S_CRO,JUL,"2026-11-18T13:05:20Z",T_CRO2,ME),
 (B4,"SLpAAA=","RES: "+S_POS,ISK,"2026-11-18T12:55:34Z",",".join([JUL,SO4,VINM,BAR,CAM,MIC,LAI,PED,ADB,VRA,SMA,MED,COTAG,AND,EXPX,CO,SO3]),CC_3PL),
 (B4,"SLqAAA=","RE: "+S_CRO,JUL,"2026-11-18T12:38:27Z",T_CRO2,ME),
 (B4,"SLsAAA=","RE: "+S_SDL,RSA,"2026-11-18T12:30:25Z",",".join([THA,JUL,BSVC]),",".join([ME,PLE])),
 (B4,"SLtAAA=","RE: "+S_POS,JUL,"2026-11-18T12:19:46Z",",".join([ISK,SO4,VINM,BAR,CAM,MIC,LAI,PED,ADB,VRA,SMA,MED,COTAG,AND,EXPX,CO,SO3]),CC_3PL),
 (B4,"SLiAAA=",S_SDL,THA,"2026-11-18T12:05:24Z",",".join([RSA,JUL,BSVC]),",".join([ME,PLE])),
 (B4,"SLuAAA=","RES: "+S_APR,AND,"2026-11-18T11:58:55Z",",".join([CAM,BAR,MIC,ISK,JUL,LAI,LUZ,MED,COTAG,VCA,GFR,ME,SO3,CO,SO4,GT]),",".join([PLGC,CDocs,PAC])),
 (B4,"SLvAAA=","RES: "+S_PLA,ISK,"2026-11-18T11:29:14Z",",".join([BAR,CAM,MIC,JUL,LAI,PED,ADB,VRA,SMA,MED,COTAG,AND]),CC_3PL_SO),
 (B4,"SLxAAA=","RES: "+S_POS,ISK,"2026-11-18T11:05:42Z",",".join([SO4,JUL,VINM,BAR,CAM,MIC,LAI,PED,ADB,VRA,SMA,MED,COTAG,AND,EXPX,CO,SO3]),CC_3PL),
 (B4,"SL1AAA=","RE: "+S_FOUT,"guilherme.queiroz@g10transportes.com.br","2026-11-17T22:20:08Z",",".join(["antony.goncalves@g10transportes.com.br"]+G10+["guilherme.queiroz@g10transportes.com.br"]),CC_G10),
 (B4,"SL3AAA=","RE: "+S_FOUT,"antony.goncalves@g10transportes.com.br","2026-11-17T22:03:13Z",",".join(G10+["guilherme.queiroz@g10transportes.com.br"]),CC_G10),
 (B4,"S10AAA=","RE: "+S_SDL,RSA,"2026-11-17T20:54:16Z",",".join([JUL,BSVC]),",".join([ME,PLE])),
 (B4,"S1yAAA=","RES: "+S_POS,SO4,"2026-11-17T20:29:44Z",",".join([JUL,VINM,BAR,CAM,MIC,ISK,LAI,PED,ADB,VRA,SMA,MED,COTAG,AND,EXPX,CO,SO3]),CC_3PL),
 (B4,"SLhAAA=","RE: "+S_SDL,JUL,"2026-11-17T20:06:33Z",",".join([BSVC,RSA]),",".join([ME,PLE])),
 (B4,"SLOAAA=","RES: "+S_POS,EXPX,"2026-11-17T20:00:30Z",",".join([VINM,BAR,CAM,MIC,ISK,JUL,LAI,PED,ADB,VRA,SMA,MED,COTAG,AND,SO4,CO,SO3]),CC_3PL),
 (B4,"SLPAAA=","RE: "+S_POS,JUL,"2026-11-17T19:55:43Z",",".join([VINM,BAR,CAM,MIC,ISK,LAI,PED,ADB,VRA,SMA,MED,COTAG,AND,EXPX,SO4,CO,SO3]),CC_3PL),
 (B4,"SLSAAA=",S_POS,VINM,"2026-11-17T19:48:29Z",",".join([BAR,CAM,MIC,ISK,JUL,LAI,PED,ADB,VRA,SMA,MED,COTAG,AND,EXPX,SO4,CO,SO3]),CC_3PL),
 (B4,"SLTAAA=","RES: "+S_PLA,BAR,"2026-11-17T19:44:15Z",",".join([CAM,MIC,ISK,JUL,LAI,PED,ADB,VRA,SMA,LUZ,MED,COTAG,AND]),CC_3PL_SO),
]
out="/workspace/analise_coleta/raw/cargill_nov3.jsonl"
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
