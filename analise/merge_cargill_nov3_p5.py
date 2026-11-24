import json, os
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ME="bma.road-southeast@cma-cgm.com"; BSVC="BRA.SERVICE@CMA-CGM.COM"; PLE="SSZ.PLETTRA@cma-cgm.com"; RSA="ssz.rsantos@cma-cgm.com"
JUL="Juliane.MARQUES@mercosul-line.com.br"
ISK="isadora_alonso@cargill.com"; ADB="Adriano_Dasilvabomtempo@cargill.com"; PED="Pedrohenrique_Defreitas@cargill.com"; AND="andressa_nunes@cargill.com"
VRA="Vitoria_Raiane@cargill.com"; SMA="Sandielle_Maia@cargill.com"; GT="cotton_gtocbr@cargill.com"
SO3="operacional3@guarujaterminais.com.br"; SO4="operacional4@guarujaterminais.com.br"; CO="coordenador@guarujaterminais.com.br"; TRN="transporte@guarujaterminais.com.br"
EXPX="contato@expurgaguacu.com.br"; SANTX="santos@expurgaguacu.com.br"
BAR="barbara@mediterraneanlogistica.com.br"; LAI="laiza@mediterraneanlogistica.com.br"; MED="mediterranean@mediterraneanlogistica.com.br"; LUIZ="luiz@mediterraneanlogistica.com.br"
CAM="camila.alonso@agsurveyors.com"; MIC="micael.santiago@agsurveyors.com"; COTAG="cotton@agsurveyors.com"; VCA="vinicius.calazans@agsurveyors.com"; GFR="giovanna.freitas@agsurveyors.com"; LUZ="luizjunior@hiperconterminais.com.br"
CCTL="cotton_ctl@Cargill.com"; PLGC="-port-logistics-cotton@Cargill.com"; CDocs="cotton-br-docs@cargill.com"; PAC="-port-allocation-cotton@exch.cargill.com"
MJR="Mariajulia_Ramos@cargill.com"; DAN="Danilo_Mendes@cargill.com"; THI="thierre.mendonca@pibernat.com.br"; EXPC="expo.cargill.cotton@pibernat.com.br"
TKR0="joana.santos@tkrinspection.com"; TKR1="Skarlatty.Boden@tkrinspection.com"; TKR2="renato.costa@tkrinspection.com"; TKR3="kelly.lopes@tkrinspection.com"; TKR4="carlos.osman@tkrinspection.com"; TKR5="cotton@tkrinspection.com"
PRE15="S51907.A01 - BKG SSZ1859739 - 15HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
S_DRA="BRSSZ | DRAFT PARCIAL & ATUALIZA\u00c7\u00c3O DE DESCARGA | "+PRE15
S_IDF="Instru\u00e7\u00e3o Document\u00e1ria FINAL - S51907.A01 - BK SSZ1859739 - INDIRETA - SANTOS / KARACHI  | Safra 2026 // M-3762/26"
S_IDP="Instru\u00e7\u00e3o Document\u00e1ria Provis\u00f3ria - S51907.A01 - BK SSZ1859739 - INDIRETA - SANTOS / KARACHI  | Safra 2026 // M-3762/26"
S_SDL="SDL-DOC | BRSSZ | AJUSTE DE BOOKING MULTIMODAL | CARGILL | COTTON"
S_DA="DRAFT ATUALIZADO  ///S51907.A01 - BKG SSZ1859739 - 15HCs"
S_DOC="Instru\u00e7\u00e3o Document\u00e1ria - S51504.B01- BK SSZ1862967- CARGILL - SANTOS / HAIPHONG PORT, VIETNAM (CIP /EXW)"
S_DEP="Confirma\u00e7\u00e3o de dep\u00f3sito dos cheios | DUE 26BR0020923722 DESEMBARA\u00c7ADA - S51504.B01 - BKG SSZ1862967 - SANTOS / HAIPHONG (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
T_TIQ=",".join([JUL,DAN,MJR,TKR0,TKR1,ME,TKR2,TKR3,TKR4,TKR5,EXPC,GT,SO3,CO,TRN,THI])
CC_TIQ=",".join([PLGC,CDocs,PAC,CCTL,BSVC])
CC_PL=",".join([PLGC,CDocs,PAC,VCA,COTAG,GFR,ME,SO3,CO,SO4])
CC_ID=",".join([PLGC,CDocs,GT])
rows=[
 (B4,"SIpAAA=","RES: "+S_DA,SO4,"2026-11-16T15:34:45Z",",".join([JUL,SO3,CO]),ME),
 (B4,"SJwAAA=","TICKETS DE EMBARQUE  - S51504.B01 - BKG SSZ1862967 - SANTOS / HAIPHONG (CMA-CGM/ZIRANLOG) - CASA | Safra 2026",SO4,"2026-11-16T15:06:41Z",T_TIQ,CC_TIQ),
 (B4,"SJzAAA=","RES: "+S_IDF,LUIZ,"2026-11-16T14:48:49Z",",".join([AND,LAI,JUL,VCA,COTAG,GFR,ME,MED,EXPX,SANTX]),CC_ID),
 (B4,"SJ0AAA=","RE: "+S_SDL,PLE,"2026-11-16T14:44:19Z",",".join([JUL,BSVC,RSA]),ME),
 (B4,"SJ1AAA=",S_IDF,AND,"2026-11-16T14:41:52Z",",".join([LAI,JUL,VCA,COTAG,GFR,ME,MED,EXPX,SANTX]),CC_ID),
 (B4,"SJ6AAA=","RES: "+S_DRA,LAI,"2026-11-16T14:29:33Z",",".join([PED,ISK,JUL,ADB,VRA,SMA,LUZ,BAR,MED]),CC_PL),
 (B4,"SJ8AAA=","RES: "+S_DRA,PED,"2026-11-16T14:19:25Z",",".join([ISK,JUL,ADB,VRA,SMA,LUZ,LAI,BAR]),CC_PL),
 (B4,"SJ9AAA=","RES: "+S_IDP,BAR,"2026-11-16T14:16:50Z",",".join([LAI,AND,JUL,VCA,COTAG,GFR,ME,MED,EXPX,SANTX,ISK,PED]),CC_ID),
 (B4,"SJ-AAA=","RE: "+S_DA,JUL,"2026-11-16T13:36:08Z",",".join([SO4,SO3,CO]),ME),
 (B4,"SKCAAA=","RES: "+S_IDP,BAR,"2026-11-16T13:28:23Z",",".join([LAI,AND,JUL,VCA,COTAG,GFR,ME,MED,EXPX,SANTX,ISK]),CC_ID),
 (B4,"SKDAAA=",S_SDL,JUL,"2026-11-16T13:21:24Z",",".join([BSVC,PLE,RSA]),ME),
 (B4,"SKFAAA=","RES: "+S_DRA,ISK,"2026-11-16T12:54:13Z",",".join([JUL,ADB,VRA,SMA,LUZ]),CC_PL),
 (B4,"SKGAAA=","RE: "+S_DOC,"marcos.sa@tkrinspection.com","2026-11-16T12:40:55Z",",".join([MJR,TKR0,JUL,TKR1,ME,TKR2,TKR3,TKR4,TKR5,CCTL,EXPC]),",".join([PLGC,CDocs,PAC])),
 (B4,"SKHAAA=",S_DEP,JUL,"2026-11-16T12:39:39Z",T_TIQ,CC_TIQ),
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
