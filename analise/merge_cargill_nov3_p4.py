import json, os
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ME="bma.road-southeast@cma-cgm.com"
JUL="Juliane.MARQUES@mercosul-line.com.br"; THA="thaina.santos@mercosul-line.com.br"
ISK="isadora_alonso@cargill.com"; ADB="Adriano_Dasilvabomtempo@cargill.com"; PED="Pedrohenrique_Defreitas@cargill.com"; AND="andressa_nunes@cargill.com"
VRA="Vitoria_Raiane@cargill.com"; SMA="Sandielle_Maia@cargill.com"; GT="cotton_gtocbr@cargill.com"
SO3="operacional3@guarujaterminais.com.br"; SO4="operacional4@guarujaterminais.com.br"; CO="coordenador@guarujaterminais.com.br"
BAR="barbara@mediterraneanlogistica.com.br"; LAI="laiza@mediterraneanlogistica.com.br"; MED="mediterranean@mediterraneanlogistica.com.br"
CAM="camila.alonso@agsurveyors.com"; MIC="micael.santiago@agsurveyors.com"; COTAG="cotton@agsurveyors.com"; VCA="vinicius.calazans@agsurveyors.com"; GFR="giovanna.freitas@agsurveyors.com"; LUZ="luizjunior@hiperconterminais.com.br"
CCTL="cotton_ctl@Cargill.com"; CAS="-CASC-COTTON-ULA@cargill.com"; COTFAT="cotton_faturamento@cargill.com"; CBD="-cbs-uberlandia-fss-itp-originacaocotton-cargillonly@exch.cargill.com"; NFE="Nfe@cargill.com"
LGG="LAURIANE_GONCALVES@CRGL-THIRDPARTY.COM"; JPR="JENNIFER_PERIS@CRGL-THIRDPARTY.COM"
TKR2="renato.costa@tkrinspection.com"; TKR3="kelly.lopes@tkrinspection.com"; TKR4="carlos.osman@tkrinspection.com"; TKR5="cotton@tkrinspection.com"; TSB="renato.sobral@tkrinspection.com"
PRE15="S51907.A01 - BKG SSZ1859739 - 15HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026  M-3762/26"
S_PLA="PLANILHA DE PESO - BRSSZ | DRAFT PARCIAL & ATUALIZA\u00c7\u00c3O DE DESCARGA | "+PRE15
S_DRA="BRSSZ | DRAFT PARCIAL & ATUALIZA\u00c7\u00c3O DE DESCARGA | "+PRE15
S_PLU="PLANILHA ATUALIZADA  ///S51907.A01 - BKG SSZ1859739 - 15HCs"
S_SPD="CCe - FATURAMENTO \u2013 Exporta\u00e7\u00e3o Indireta \u2013 ALGTRESC  \u2013 Instru\u00e7\u00e3o: S51907.A01 \u2013 PLACA: SPD0A75 \u2013 NF: 228882"
S_OUT="FATURAMENTO \u2013 Exporta\u00e7\u00e3o Indireta \u2013 ALGCTCOT  \u2013 Instru\u00e7\u00e3o: S00701.A05 \u2013 PLACA: OUT9D43 \u2013 NF: 46245"
T_CRO=",".join([JUL,SO3,CO]); T_CRO2=",".join([SO4,SO3,CO])
CC_3PL_SO=",".join(["-port-logistics-cotton@Cargill.com","cotton-br-docs@cargill.com","-port-allocation-cotton@exch.cargill.com",VCA,GFR,ME,SO3,CO,SO4])
CC_3PL_A=",".join(["-port-logistics-cotton@Cargill.com","cotton-br-docs@cargill.com","-port-allocation-cotton@exch.cargill.com",VCA,COTAG,GFR,ME,SO3,CO,SO4])
TMID=[ISK,JUL,BAR,LAI,PED,ADB,VRA,SMA,LUZ,MED,COTAG]
T_COOP=",".join(["faturamento@cooami.com.br","comercial3@trescoqueiros.com","jaison@cooami.com.br","cotton@cooami.com.br","cotton@cooami.com.br",CCTL,NFE,VRA,"Itamar_Filho@cargill.com",CAS,COTFAT,CBD,CCTL,CAS,LGG,JPR,COTAG,"certificate@agsurveyors.com","marcela.correia@agsurveyors.com",MIC,ME,JUL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com",THA,"bma.mcastro@cma-cgm.com","Renan_Ruani@cargill.com","Itamar_Filho@cargill.com","cbs-uberlandia-ctl-cdm-all@exch.cargill.com"])
CC_COOP=",".join(["administrativoalg2@trescoqueiros.com","financeiro3@trescoqueiros.com","administrativoalg3@trescoqueiros.com","administrativoalg@trescoqueiros.com","comercial2@trescoqueiros.com","comercial5@trescoqueiros.com","comercial@trescoqueiros.com","controladoria@trescoqueiros.com","comercial4@trescoqueiros.com","thomas@trescoqueiros.com","financeiro4@trescoqueiros.com","financeiro5@trescoqueiros.com","aprendizfinanceiro@trescoqueiros.com"])
LP="lucas.pivetta@cooperuniaolrv.com.br"; CIN="contabilidade@grupocinpak.com.br"; HAR="Harielly_Dasilvabatista@cargill.com"; CRI="Crisla_Leite@cargill.com"; IAN="ian_marques@cargill.com"
LUV="ctcottonlrv@hotmail.com"; LST="lucas.strassi@g10transportes.com.br"; RCO="rondonopolis.cotton@g10transportes.com.br"
CC_G10=",".join(["algodoeira@ctcotton.com.br","rodrigo.bonatto@g10transportes.com.br"])
T_OUT_BASE=[LP,CIN,HAR,VRA,LUV,LST,RCO,CCTL,CAS,"mateus.munhoz@cooperuniaolrv.com.br","faturamento@cooperuniaolrv.com.br",COTFAT,CBD,CCTL,CAS,LGG,JPR,TKR2,TKR4,TKR3,TSB,TKR5,ME,JUL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com",THA,"bma.mcastro@cma-cgm.com","joao.bosco@g10transportes.com.br","Comercial.cotton@g10transportes.com.br","Josevan.oliveira@g10transportes.com.br",RCO,"bahia@g10transportes.com.br"]
T_OUT_IAN=",".join([CRI]+T_OUT_BASE)
T_OUT_CRI=",".join(T_OUT_BASE)
rows=[
 (B4,"SLWAAA=",S_PLA,CAM,"2026-11-17T19:31:04Z",",".join([BAR,MIC,ISK,JUL,LAI,PED,ADB,VRA,SMA,LUZ,MED,COTAG,AND]),CC_3PL_SO),
 (B4,"SLIAAA=","RES: "+S_DRA,BAR,"2026-11-17T17:54:26Z",",".join([MIC,ISK,JUL,LAI,PED,ADB,VRA,SMA,LUZ,MED,COTAG]),CC_3PL_SO),
 (B4,"SLHAAA=","RES: "+S_PLU,SO4,"2026-11-17T17:44:23Z",T_CRO,ME),
 (B4,"SLEAAA=","RE: "+S_PLU,JUL,"2026-11-17T17:10:36Z",T_CRO2,ME),
 (B4,"SLFAAA=","RES: "+S_PLU,SO4,"2026-11-17T16:20:16Z",T_CRO,ME),
 (B4,"SLCAAA=","RES: CCe - "+S_SPD,IAN,"2026-11-17T15:30:22Z",",".join([HAR,CAM,CRI])+","+T_COOP,CC_COOP),
 (B4,"SLBAAA=","RES: CCe - "+S_SPD,HAR,"2026-11-17T15:20:29Z",",".join([CAM,IAN,CRI])+","+T_COOP,CC_COOP),
 (B4,"SK-AAA=","RE: "+S_PLU,JUL,"2026-11-17T15:18:17Z",T_CRO2,ME),
 (B4,"SLAAAA=","CCe - "+S_SPD,CAM,"2026-11-17T15:18:10Z",",".join([IAN,CRI])+","+T_COOP,CC_COOP),
 (B4,"SItAAA=","RES: "+S_DRA,MIC,"2026-11-17T14:50:17Z",",".join(TMID),CC_3PL_SO),
 (B4,"SIxAAA=","RES: "+S_DRA,MIC,"2026-11-17T14:24:41Z",",".join(TMID),CC_3PL_SO),
 (B4,"SI8AAA=","RES: "+S_DRA,MIC,"2026-11-17T12:59:07Z",",".join(TMID),CC_3PL_SO),
 (B4,"SI-AAA=","RE: "+S_DRA,JUL,"2026-11-17T12:51:55Z",",".join([ISK]+TMID[2:]),CC_3PL_A),
 (B4,"SJFAAA=","RES: "+S_DRA,ISK,"2026-11-17T12:31:15Z",",".join([JUL]+TMID[2:]),CC_3PL_A),
 (B4,"SJGAAA=","RES: "+S_PLU,SO4,"2026-11-17T12:28:25Z",T_CRO,ME),
 (B4,"SJHAAA=","RES: "+S_OUT,IAN,"2026-11-17T11:59:56Z",T_OUT_IAN,CC_G10),
 (B4,"SJKAAA=",S_OUT,CRI,"2026-11-17T11:41:09Z",T_OUT_CRI,CC_G10),
 (B4,"SJSAAA=","RES: "+S_DRA,BAR,"2026-11-16T21:47:33Z",",".join([JUL,LAI,PED,ISK,ADB,VRA,SMA,LUZ,MED]),CC_3PL_A),
 (B4,"SImAAA=","RE: "+S_DRA,JUL,"2026-11-16T17:23:20Z",",".join([BAR,LAI,PED,ISK,ADB,VRA,SMA,LUZ,MED]),CC_3PL_A),
 (B4,"SIoAAA=","RES: "+S_DRA,BAR,"2026-11-16T15:59:47Z",",".join([LAI,PED,ISK,JUL,ADB,VRA,SMA,LUZ,MED]),CC_3PL_A),
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
