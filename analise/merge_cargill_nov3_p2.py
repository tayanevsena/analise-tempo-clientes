import json, os
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
FTX="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ME="bma.road-southeast@cma-cgm.com"; BCG="bra.cgr@cma-cgm.com"; BSVC="BRA.SERVICE@CMA-CGM.COM"
JUL="Juliane.MARQUES@mercosul-line.com.br"
ISK="isadora_alonso@cargill.com"; ADB="Adriano_Dasilvabomtempo@cargill.com"; PED="Pedrohenrique_Defreitas@cargill.com"; AND="andressa_nunes@cargill.com"
VRA="Vitoria_Raiane@cargill.com"; SMA="Sandielle_Maia@cargill.com"; GT="cotton_gtocbr@cargill.com"; WAL="waldemar_henriquedeoliveira@cargill.com"
SO3="operacional3@guarujaterminais.com.br"; SO4="operacional4@guarujaterminais.com.br"; CO="coordenador@guarujaterminais.com.br"; TRN="transporte@guarujaterminais.com.br"
EXPX="contato@expurgaguacu.com.br"
BAR="barbara@mediterraneanlogistica.com.br"; ALE="alexandre@mediterraneanlogistica.com.br"; LAI="laiza@mediterraneanlogistica.com.br"; MED="mediterranean@mediterraneanlogistica.com.br"; VINM="vinicius@mediterraneanlogistica.com.br"
CAM="camila.alonso@agsurveyors.com"; MIC="micael.santiago@agsurveyors.com"; COTAG="cotton@agsurveyors.com"; VCA="vinicius.calazans@agsurveyors.com"; GFR="giovanna.freitas@agsurveyors.com"
PLGC="-port-logistics-cotton@Cargill.com"; CDocs="cotton-br-docs@cargill.com"; PAC="-port-allocation-cotton@exch.cargill.com"
TKR0="joana.santos@tkrinspection.com"; TKR1="Skarlatty.Boden@tkrinspection.com"; TKR2="renato.costa@tkrinspection.com"; TKR3="kelly.lopes@tkrinspection.com"; TKR4="carlos.osman@tkrinspection.com"; TKR5="cotton@tkrinspection.com"
PRE712="S51907.A01 - BKG SSZ1859739 - 12HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026  M-3762/26"
PRE15="S51907.A01 - BKG SSZ1859739 - 15HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026  M-3762/26"
S_PAE="PENDENTE AERA\u00c7\u00c3O 19/11 - AGENDAMENTO CHEIOS | "+PRE712
S_FUM="PENDENTE MAPA - FUMIGA\u00c7\u00c3O - NFS & DUE | APROVADA | PLANILHA DE PESO PARCIAL | "+PRE712
S_FATU="****URGENTE**** FATURAMENTO \u2013 Exporta\u00e7\u00e3o Indireta \u2013 ALGCTCOT  \u2013 Instru\u00e7\u00e3o: S00701.A05 \u2013 PLACA: EHH8B86 \u2013 NF: 46322"
S_DRAFT15="BRSSZ | DRAFT PARCIAL & ATUALIZA\u00c7\u00c3O DE DESCARGA | "+PRE15
CC_PAP=",".join([PLGC,CDocs,PAC]); CC_PAPB=",".join([PLGC,CDocs,PAC,BSVC])
A=["contabilidade@grupocinpak.com.br","ian_marques@cargill.com","Crisla_Leite@cargill.com","Harielly_Dasilvabatista@cargill.com","marialuiza.puerar@cooperuniaolrv.com.br","ctcottonlrv@hotmail.com","lucas.strassi@g10transportes.com.br"]
BB=["Vitoria_Raiane@cargill.com","anderson.godas@g10transportes.com.br","bahia@g10transportes.com.br","comercial.matopiba@g10transportes.com.br","cotton.g10@g10transportes.com.br","joao.bosco@g10transportes.com.br","josevan.oliveira@g10transportes.com.br","algodoeira@ctcotton.com.br","faturamento@cooperuniaolrv.com.br","mateus.munhoz@cooperuniaolrv.com.br","-CASC-COTTON-ULA@cargill.com","cotton_ctl@Cargill.com","Matheus_Yure@cargill.com","cotton_faturamento@cargill.com","Paulo_Carvalho@cargill.com","cotton_ctl@Cargill.com","cotton_faturamento@cargill.com","-cbs-uberlandia-fss-itp-originacaocotton-cargillonly@exch.cargill.com","cotton_ctl@Cargill.com","-CASC-COTTON-ULA@cargill.com","LAURIANE_GONCALVES@CRGL-THIRDPARTY.COM","JENNIFER_PERIS@CRGL-THIRDPARTY.COM",TKR2,TKR4,TKR3,"renato.sobral@tkrinspection.com",TKR5,ME,JUL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com","thaina.santos@mercosul-line.com.br","bma.mcastro@cma-cgm.com","joao.bosco@g10transportes.com.br","comercial.cotton@g10transportes.com.br","josevan.oliveira@g10transportes.com.br","rondonopolis.cotton@g10transportes.com.br","bahia@g10transportes.com.br"]
ANT="antony.goncalves@g10transportes.com.br"; CIN="contabilidade@grupocinpak.com.br"; IAN="ian_marques@cargill.com"; CRI="Crisla_Leite@cargill.com"
TO_ANT=",".join(A+[ANT]+BB)
TO_CIN=",".join([IAN,CRI,"Harielly_Dasilvabatista@cargill.com","marialuiza.puerar@cooperuniaolrv.com.br","ctcottonlrv@hotmail.com","lucas.strassi@g10transportes.com.br",ANT]+BB)
TO_IAN=",".join([CRI,CIN,"Harielly_Dasilvabatista@cargill.com","marialuiza.puerar@cooperuniaolrv.com.br","ctcottonlrv@hotmail.com","lucas.strassi@g10transportes.com.br",ANT]+BB)
TO_CRI=",".join([CIN,"Harielly_Dasilvabatista@cargill.com","marialuiza.puerar@cooperuniaolrv.com.br","ctcottonlrv@hotmail.com","lucas.strassi@g10transportes.com.br",ANT]+BB)
CC_G10A=",".join(["carlos.cordeiro@g10transportes.com.br","cleyton.ferraz@g10transportes.com.br","fayla.lendengues@g10transportes.com.br","gilney.goncalves@g10transportes.com.br","maykon.bastos@g10transportes.com.br","rikaro.leao@g10transportes.com.br"])
CC_G10B=CC_G10A+",rondonopolis.cotton@g10transportes.com.br,algodoeira@ctcotton.com.br"
S_LL=",".join([EXPX,ALE,AND,CAM,BAR,MIC,ISK,LAI,"luizjunior@hiperconterminais.com.br",MED,COTAG,VCA,GFR,ME,SO3,CO,SO4,GT,TRN])
S_LL2=",".join([AND,CAM,BAR,MIC,ISK,LAI,"luizjunior@hiperconterminais.com.br",MED,COTAG,VCA,GFR,ME,SO3,CO,SO4,GT,TRN])
S_LL3=",".join([AND,CAM,BAR,MIC,ISK,LAI,"luizjunior@hiperconterminais.com.br",MED,COTAG,VCA,GFR,ME,SO3,CO,SO4,GT])
CC_3PL=",".join([PLGC,CDocs,PAC,VCA,GFR,ME])
rows=[
 (B4,"S0vAAA=","RE: "+S_FATU,ANT,"2026-11-18T20:40:18Z",TO_ANT,CC_G10A),
 (B4,"S0yAAA=","RE: "+S_PAE,JUL,"2026-11-18T20:19:17Z",",".join([ISK,EXPX,ALE,AND,CAM,BAR,MIC,LAI,"luizjunior@hiperconterminais.com.br",MED,COTAG,VCA,GFR,ME,SO3,CO,SO4,GT,TRN,BSVC,BCG]),CC_PAP),
 (B4,"S0zAAA=","RES: "+S_PAE,ISK,"2026-11-18T20:15:08Z",",".join([JUL,EXPX,ALE,AND,CAM,BAR,MIC,LAI,"luizjunior@hiperconterminais.com.br",MED,COTAG,VCA,GFR,ME,SO3,CO,SO4,GT,TRN,BSVC]),CC_PAP),
 (B4,"S01AAA=","RE: "+S_PAE,JUL,"2026-11-18T20:03:10Z",S_LL,CC_PAPB),
 (B4,"S0tAAA=","RES: "+S_PAE,EXPX,"2026-11-18T19:57:15Z",",".join([JUL,ALE,AND,CAM,BAR,MIC,ISK,LAI,"luizjunior@hiperconterminais.com.br",MED,COTAG,VCA,GFR,ME,SO3,CO,SO4,GT,TRN]),CC_PAPB),
 (B4,"S0rAAA=",S_PAE,JUL,"2026-11-18T19:55:52Z",S_LL,CC_PAPB),
 (B4,"S0pAAA=","RES: "+S_FATU,CIN,"2026-11-18T19:54:24Z",TO_CIN,CC_G10B),
 (B4,"S0oAAA=","RES: "+S_FUM,EXPX,"2026-11-18T19:27:30Z",",".join([ALE,JUL,AND,CAM,BAR,MIC,ISK,LAI,"luizjunior@hiperconterminais.com.br",MED,COTAG,VCA,GFR,ME,SO3,CO,SO4,GT,TRN]),CC_PAPB),
 (B4,"S0jAAA=","RES: "+S_FUM,ALE,"2026-11-18T19:24:35Z",",".join([JUL,AND,CAM,BAR,MIC,ISK,LAI,"luizjunior@hiperconterminais.com.br",MED,COTAG,VCA,GFR,ME,SO3,CO,SO4,GT,TRN,EXPX]),CC_PAPB),
 (B4,"S0gAAA=","FATURAMENTO GUARUJA TERMINAIS X CMA - NF 7541 VENCIMENTO 18/12/2026- BOOKING SSZ1862967","faturamento2@guarujaterminais.com.br","2026-11-18T18:47:01Z","bma.faturamento@cma-cgm.com",",".join(["financeiro@vilavelhaterminais.com.br",ME,JUL,"financeiro2@vilavelhaterminais.com.br","financeiro1@vilavelhaterminais.com.br","faturamento@guarujaterminais.com.br",CO,"gerencia@guarujaterminais.com.br"])),
 (B4,"SMGAAA=","RES: ENTREGA CNTRS DUE 26BR002121542-0 -DESEMBARA\u00c7ADA / UNITIZADA : PLANILHA DE PESO - "+S_DRAFT15,SO4,"2026-11-18T18:16:03Z",",".join([ALE,JUL,VINM,BAR,CAM,MIC,ISK,LAI,PED,ADB,VRA,SMA,MED,COTAG,AND,EXPX,CO,SO3]),",".join([CC_3PL,WAL,GT])),
 (B4,"SMHAAA=","RE: DEMONSTRATIVO PARA FATURAMENTO - GUARUJA TERMINAIS X CMA - BOOKING SSZ1862967 - REF S51504.B01",JUL,"2026-11-18T17:42:13Z",",".join(["faturamento2@guarujaterminais.com.br",ME]),",".join(["faturamento@guarujaterminais.com.br","gerencia@guarujaterminais.com.br",CO])),
 (B4,"SMIAAA=","RE: "+S_FUM,JUL,"2026-11-18T17:37:25Z",S_LL2,CC_PAPB),
 (B4,"SMLAAA=","ENTREGA CNTRS DUE 26BR002121542-0 -DESEMBARA\u00c7ADA : PLANILHA DE PESO - "+S_DRAFT15,ALE,"2026-11-18T17:16:18Z",",".join([SO4,JUL,VINM,BAR,CAM,MIC,ISK,LAI,PED,ADB,VRA,SMA,MED,COTAG,AND,EXPX,CO,SO3]),",".join([CC_3PL,WAL,GT])),
 (FTX,"StxAAA=","PROGRAMA\u00c7\u00c3O DE ENTREGAS \u2013 MERCOSUL \u2013 19/11/2026","RAYNARA.SANTOS@MERCOSUL-LINE.COM.BR","2026-11-18T15:59:06Z",",".join(["roselma@rrtransporte.com","operacional@rrtransporte.com","intermodalmanaus@mercosul-line.com.br","jhonnespinheiro@rrtransporte.com","Thiago.Negreiros@mercosul-line.com.br"]),""),
 (B4,"S0RAAA=","RES: "+S_FATU,IAN,"2026-11-18T15:09:24Z",TO_IAN,CC_G10B),
 (B4,"S0SAAA=",S_FATU,CRI,"2026-11-18T14:51:47Z",TO_CRI,CC_G10B),
 (B4,"S0aAAA=",S_FUM,JUL,"2026-11-18T14:13:39Z",S_LL3,CC_PAPB),
 (B4,"S0bAAA=","RE: POSICIONAMENTO DE CONTEINER -  PLANILHA DE PESO - "+S_DRAFT15,JUL,"2026-11-18T14:12:17Z",",".join([ISK,SO4,VINM,BAR,CAM,MIC,LAI,PED,ADB,VRA,SMA,MED,COTAG,AND,EXPX,CO,SO3]),",".join([CC_3PL,BSVC])),
 (B4,"S0cAAA=","RES: [CMA CGM] BRSSZ | CROSS DOCKING - COTTON | CARGILL x GUARUJ\u00c1 TERMINAIS | S51907.A01 - BKG SSZ1859739 - 15HCs",SO4,"2026-11-18T14:10:35Z",",".join([JUL,SO3,CO]),ME),
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
