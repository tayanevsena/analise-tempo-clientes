import json, os
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
BS="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAbGqrRHAAA="
ME="bma.road-southeast@cma-cgm.com"; BCG="bra.cgr@cma-cgm.com"; BSVC="BRA.SERVICE@CMA-CGM.COM"
JUL="Juliane.MARQUES@mercosul-line.com.br"; THA="thaina.santos@mercosul-line.com.br"
ISK="isadora_alonso@cargill.com"; ADB="Adriano_Dasilvabomtempo@cargill.com"
PED="Pedrohenrique_Defreitas@cargill.com"; AND="andressa_nunes@cargill.com"
SO3="operacional3@guarujaterminais.com.br"; SO4="operacional4@guarujaterminais.com.br"; CO="coordenador@guarujaterminais.com.br"; TRN="transporte@guarujaterminais.com.br"
EXPX="contato@expurgaguacu.com.br"
BAR="barbara@mediterraneanlogistica.com.br"; ALE="alexandre@mediterraneanlogistica.com.br"; LAI="laiza@mediterraneanlogistica.com.br"; MED="mediterranean@mediterraneanlogistica.com.br"
CAM="camila.alonso@agsurveyors.com"; MIC="micael.santiago@agsurveyors.com"; COTAG="cotton@agsurveyors.com"; VCA="vinicius.calazans@agsurveyors.com"; GFR="giovanna.freitas@agsurveyors.com"
GT="cotton_gtocbr@cargill.com"; PLGC="-port-logistics-cotton@Cargill.com"; CDocs="cotton-br-docs@cargill.com"; PAC="-port-allocation-cotton@exch.cargill.com"; CCTL="cotton_ctl@Cargill.com"
MJR="Mariajulia_Ramos@cargill.com"; DAN="Danilo_Mendes@cargill.com"; THI="thierre.mendonca@pibernat.com.br"; EXPC="expo.cargill.cotton@pibernat.com.br"
TKR0="joana.santos@tkrinspection.com"; TKR1="Skarlatty.Boden@tkrinspection.com"; TKR2="renato.costa@tkrinspection.com"; TKR3="kelly.lopes@tkrinspection.com"; TKR4="carlos.osman@tkrinspection.com"; TKR5="cotton@tkrinspection.com"
PRE712="S51907.A01 - BKG SSZ1859739 - 12HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026  M-3762/26"
PRE702="S00702.A53 - BKG 256584712 - RONDONOPOLIS / CHATTOGRAM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
PRE_TBI="S00702.A53 - BKG TBI - SANTOS / CHATTOGRAM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
T_SALDO=",".join([SO4,JUL,PED,EXPX,ISK,SO3,CO,TRN])
S_CJAN="CAPTA\u00c7\u00c3O DE JANELAS | DDL CARGA ALTERADO P/ 19/11 17H | "+PRE712
S_CEX="CONFIRMA\u00c7\u00c3O DE EXTENS\u00c3O DE DDL CARGA | "+PRE712
S_CAE="CONFIRMA\u00c7\u00c3O DE AERA\u00c7\u00c3O 19/11 | "+PRE712
S_PAE="PENDENTE AERA\u00c7\u00c3O 19/11 - AGENDAMENTO CHEIOS | "+PRE712
S_PN702="PR\u00c9-NOMEA\u00c7\u00c3O - "+PRE702
S_PNTBI="CONSIDERAR ESTE | PR\u00c9-NOMEA\u00c7\u00c3O - "+PRE_TBI
S_HAI="RES: RELATORIO FOTOGRAFICO  TICKETS DE EMBARQUE  - S51504.B01 - BKG SSZ1862967 - SANTOS / HAIPHONG (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
CC_JAN=",".join([ALE,AND,CAM,BAR,MIC,LAI,MED,COTAG,VCA,GFR,ME,GT,BSVC,PLGC,CDocs,PAC])
CC_EXT=",".join([ALE,AND,CAM,BAR,MIC,LAI,MED,COTAG,VCA,GFR,ME,SO3,CO,SO4,GT,TRN,BSVC,PLGC,CDocs,PAC])
CC_LL=",".join([JUL,EXPX,ALE,AND,CAM,BAR,MIC,LAI,MED,COTAG,VCA,GFR,ME,SO3,CO,SO4,GT,TRN,BSVC,BCG,PLGC,CDocs,PAC])
CC_LL2=",".join([JUL,EXPX,ALE,AND,CAM,BAR,MIC,LAI,"luizjunior@hiperconterminais.com.br",MED,COTAG,VCA,GFR,ME,SO3,CO,SO4,GT,TRN,BSVC,BCG])
S_PN702_S="PR\u00c9-NOMEA\u00c7\u00c3O - "+PRE702
rows=[
 (B4,"S1oAAA=","INSTRUCAO DE SALDO //   S51907.A01 - BKG ??? - 03HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026  M-4104/26",BAR,"2026-11-19T21:10:13Z",T_SALDO,",".join([ALE,AND,CAM,MIC,MED,COTAG,VCA,GFR,ME,GT,BSVC,PLGC,CDocs,PAC])),
 (B4,"S1jAAA=","RES: "+S_CJAN,BAR,"2026-11-19T20:51:50Z",T_SALDO,",".join([ALE,AND,CAM,MIC,LAI,MED,COTAG,VCA,GFR,ME,GT,BSVC,PLGC,CDocs,PAC])),
 (B4,"S1nAAA=","RES: CONSIDERAR ESTE | "+PRE_TBI+" M-4101/26",BAR,"2026-11-19T19:36:23Z",",".join([JUL,ADB,ME]),",".join([PLGC,CDocs,PAC,VCA,COTAG,GFR,MED,BSVC])),
 (B4,"S14AAA=","RE: CONSIDERAR ESTE | "+PRE_TBI,JUL,"2026-11-19T17:42:05Z",",".join([ADB,ME]),",".join([PLGC,CDocs,PAC,VCA,COTAG,GFR,MED,BSVC])),
 (B4,"S1aAAA=",S_CJAN,SO4,"2026-11-19T16:26:12Z",",".join([JUL,PED,EXPX,ISK,SO3,CO,TRN]),CC_JAN),
 (B4,"S1dAAA=","RES: "+S_CJAN,SO4,"2026-11-19T15:18:31Z",",".join([JUL,PED,EXPX,ISK,SO3,CO,TRN]),CC_JAN),
 (B4,"S1eAAA=",S_CJAN,JUL,"2026-11-19T15:07:30Z",",".join([PED,EXPX,ISK,SO3,CO,SO4,TRN]),CC_JAN),
 (B4,"S1XAAA=","RES: "+S_CEX,PED,"2026-11-19T14:45:16Z",",".join([JUL,EXPX,ISK,BCG]),CC_EXT),
 (B4,"S1VAAA=",S_CEX,JUL,"2026-11-19T14:41:08Z",",".join([EXPX,ISK]),CC_EXT),
 (B4,"S1JAAA=","RES: "+S_CAE,EXPX,"2026-11-19T14:17:01Z",",".join([JUL,ISK]),CC_EXT),
 (B4,"S1IAAA=",S_CAE,JUL,"2026-11-19T14:13:51Z",",".join([ISK,EXPX]),CC_EXT),
 (B4,"S1KAAA=",S_HAI,"leticia.nascimento@tkrinspection.com","2026-11-19T13:52:22Z",",".join([SO4,JUL,DAN,MJR,TKR0,TKR1,ME,TKR2,TKR3,TKR4,TKR5,EXPC,GT,SO3,CO,TRN,THI]),",".join([PLGC,CDocs,PAC,CCTL,BSVC])),
 (B4,"S04AAA=",S_PNTBI,ADB,"2026-11-19T11:59:13Z",",".join([THA,ME,JUL]),",".join([PLGC,CDocs,PAC,VCA,COTAG,GFR,MED])),
 (B4,"S07AAA=","Re: RES: "+S_PAE,"luizjunior@hiperconterminais.com.br","2026-11-19T11:24:37Z",ISK,CC_LL),
 (B4,"S08AAA=","RES: "+S_PAE,ISK,"2026-11-19T11:17:44Z",CC_LL2,",".join([PLGC,CDocs,PAC])),
 (B4,"S09AAA=","PLANILHA ATUALIZADA  ///S51907.A01 - BKG SSZ1859739 - 15HCs",SO4,"2026-11-19T11:10:18Z",",".join([JUL,SO3,CO]),ME),
 (BS,"","ENVIO DOCS DE ENTREGA - R R DE ANDRADE LIMA SERVICOS DE TRANSPORTES EIRELI","rpa_no_reply@mercosul-line.com.br","2026-11-19T05:56:57Z","roselma@rrtransporte.com","doc.norte@mercosul-line.com.br"),
 (B4,"S1RAAA=","RES: COLETA DE SALDO / [CMA CGM] BRSSZ | CROSS DOCKING - COTTON | CARGILL x GUARUJ\u00c1 TERMINAIS | S51907.A01 - BKG SSZ1859739 - 15HCs",SO4,"2026-11-18T21:30:44Z",",".join([JUL,SO3,CO]),ME),
 (B4,"S1FAAA=","RES: "+S_PN702_S,ADB,"2026-11-18T21:07:18Z",",".join([THA,ME,JUL]),",".join([PLGC,CDocs,PAC,VCA,COTAG,GFR,MED])),
 (B4,"S1EAAA=",S_PN702_S,ADB,"2026-11-18T21:07:04Z",",".join([THA,ME,JUL]),",".join([PLGC,CDocs,PAC,VCA,COTAG,GFR,MED])),
]
out="/workspace/analise_coleta/raw/cargill_nov3.jsonl"
have=set()
if os.path.exists(out):
    for l in open(out): have.add(json.loads(l)["id"])
new=0
with open(out,"a") as f:
    for r in rows:
        idb,suf,s,fr,d,to,cc=r
        id_=(idb+suf) if suf else idb
        if id_ in have: continue
        f.write(json.dumps({"id":id_,"folder":"main","date":d,"subject":s,"from":fr,"to":to,"cc":cc},ensure_ascii=False)+"\n")
        have.add(id_); new+=1
print("new:",new,"total:",len(have))
