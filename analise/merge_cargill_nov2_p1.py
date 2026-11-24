import json
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
BS="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
BE="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAbCebcYAAA="
ME="bma.road-southeast@cma-cgm.com"
PRE="S51907.A01 - BKG SSZ1859739 - 15HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
PRE2="S51504.B01 - BKG SSZ1862967 - SANTOS / HAIPHONG (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
IP="Instrução Documentária Provisória - S51907.A01 - BK SSZ1859739 - INDIRETA - SANTOS / KARACHI  | Safra 2026"
JUL="Juliane.MARQUES@mercosul-line.com.br"
ISK="isadora_alonso@cargill.com"; ADB="Adriano_Dasilvabomtempo@cargill.com"; VRA="Vitoria_Raiane@cargill.com"; SMA="Sandielle_Maia@cargill.com"
SO3="operacional3@guarujaterminais.com.br"; SO4="operacional4@guarujaterminais.com.br"; CO="coordenador@guarujaterminais.com.br"
CCTL="cotton_ctl@cargill.com"; NFE="Nfe@cargill.com"; CAS="-CASC-COTTON-ULA@cargill.com"; COTFAT="cotton_faturamento@cargill.com"; CBD="-cbs-uberlandia-fss-itp-originacaocotton-cargillonly@exch.cargill.com"
LGG="LAURIANE_GONCALVES@CRGL-THIRDPARTY.COM"; JPR="JENNIFER_PERIS@CRGL-THIRDPARTY.COM"
AGFULL=",".join(["cotton@agsurveyors.com","certificate@agsurveyors.com","marcela.correia@agsurveyors.com","micael.santiago@agsurveyors.com"])
BMA=",".join([ME,JUL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com","thaina.santos@mercosul-line.com.br","bma.mcastro@cma-cgm.com"])
PLGC="-port-logistics-cotton@Cargill.com"; CDocs="cotton-br-docs@cargill.com"; PAC="-port-allocation-cotton@exch.cargill.com"
TKR=["joana.santos@tkrinspection.com","Skarlatty.Boden@tkrinspection.com","renato.costa@tkrinspection.com","kelly.lopes@tkrinspection.com","carlos.osman@tkrinspection.com","cotton@tkrinspection.com"]
MJR="Mariajulia_Ramos@cargill.com"; DMN="Danilo_Mendes@cargill.com"; EXPC="expo.cargill.cotton@pibernat.com.br"; THR="thierre.mendonca@pibernat.com.br"; GT="cotton_gtocbr@cargill.com"
TRN="transporte@guarujaterminais.com.br"
COT=",".join([PLGC,CDocs,PAC])
AGS3=",".join(["vinicius.calazans@agsurveyors.com","cotton@agsurveyors.com","giovanna.freitas@agsurveyors.com"])
TJUL3=JUL+","+SO3+","+CO
DUEG=",".join([DMN,MJR]+TKR[:2]+[ME]+TKR[2:6]+[EXPC,GT])
CC_DUE=",".join([PLGC,CDocs,PAC,"cotton_ctl@Cargill.com","BRA.SERVICE@CMA-CGM.COM"])
DRAFTTO=",".join([ISK,ADB,VRA,SMA,"luizjunior@hiperconterminais.com.br"])
DRAFTCC=",".join([COT,AGS3,ME,SO3,CO,SO4])
FATDTP="FATURAMENTO – Exportação Indireta – ALGCELES – Instrução: S51907.A01 – PLACA: DTP3J81 – NF: 229255"
CC_DTP=",".join(["Natalia_Queiroz@cargill.com","faturamento@cooami.com.br","fiscal@gpcagro.com","jaison@cooami.com.br","cotton@cooami.com.br","willyan.souza@algceleste.com","thiago.feitosa@algceleste.com","durvacil.assis@algceleste.com",NFE,"cotton_ctl@Cargill.com",CAS,COTFAT,CBD,"LAURIANE_GONCALVES@crgl-thirdparty.com","JENNIFER_PERIS@crgl-thirdparty.com",AGFULL,BMA,"rondonopolis.cotton@g10transportes.com.br","bahia@g10transportes.com.br"])
rows=[
 (B4,"SKaAAA=","RES: DUE 26BR0020923722 DESEMBARAÇADA - "+PRE2,SO4,"2026-11-14T13:22:00Z",DUEG+","+SO3+","+CO+","+TRN+","+THR,CC_DUE),
 (BE,"","ENVIO DOCS DE ENTREGA - R R DE ANDRADE LIMA SERVICOS DE TRANSPORTES EIRELI","rpa_no_reply@mercosul-line.com.br","2026-11-14T08:13:09Z","roselma@rrtransporte.com","doc.norte@mercosul-line.com.br"),
 (B4,"SKpAAA=","RE: DUE 26BR0020923722 DESEMBARAÇADA - "+PRE2,JUL,"2026-11-13T21:45:23Z",DUEG+","+SO3+","+CO+","+TRN+","+THR+","+SO4,CC_DUE),
 (B4,"SKtAAA=","RE: BRSSZ | DRAFT PARCIAL & ATUALIZAÇÃO DE DESCARGA | "+PRE,JUL,"2026-11-13T21:18:13Z",DRAFTTO,DRAFTCC),
 (B4,"SIhAAA=","DUE 26BR0020923722 DESEMBARAÇADA - "+PRE2,JUL,"2026-11-13T20:31:31Z",DUEG+","+SO3+","+CO+","+TRN+","+THR,CC_DUE),
 (B4,"SIiAAA=","DUE 26BR0020923722 DESEMBARAÇADA - "+PRE2,THR,"2026-11-13T20:20:58Z",MJR,",".join(TKR[:2]+[JUL]+TKR[2:6]+[EXPC,GT,PLGC,CDocs,PAC,"cotton_ctl@Cargill.com"])),
 (B4,"SIfAAA=","RES: DRAFT ATUALIZADO  ///"+PRE,SO4,"2026-11-13T19:46:56Z",TJUL3,ME),
 (B4,"SK2AAA=","RE: PLANILHA ATUALIZADA  ///"+PRE,JUL,"2026-11-13T19:33:49Z","operacional4@guarujaterminais.com.br,operacional3@guarujaterminais.com.br,coordenador@guarujaterminais.com.br",ME),
 (B4,"SK4AAA=","RE: NFS DE EXPORTAÇÃO & DUE | APROVADA PLANILHA DE PESO | "+PRE2,DMN,"2026-11-13T19:28:52Z",JUL+","+DUEG,",".join([PLGC,CDocs,PAC,"cotton_ctl@Cargill.com",SO3,CO,TRN,"BRA.SERVICE@CMA-CGM.COM"])),
 (B4,"SIeAAA=","RES: BRSSZ | DRAFT PARCIAL & ATUALIZAÇÃO DE DESCARGA | "+PRE,ISK,"2026-11-13T19:25:53Z",DRAFTTO,DRAFTCC),
 (BS,"SXDAAA=","PROGRAMAÇÃO DE ENTREGAS – MERCOSUL – 16/11/2026","RAYNARA.SANTOS@MERCOSUL-LINE.COM.BR","2026-11-13T19:15:21Z","roselma@rrtransporte.com,operacional@rrtransporte.com,intermodalmanaus@mercosul-line.com.br,jhonnespinheiro@rrtransporte.com,Thiago.Negreiros@mercosul-line.com.br",""),
 (B4,"SITAAA=","NFS DE EXPORTAÇÃO & DUE | APROVADA PLANILHA DE PESO | "+PRE2,JUL,"2026-11-13T19:11:23Z",",".join([MJR]+TKR[:7]+[EXPC,GT]),",".join([PLGC,CDocs,PAC,"cotton_ctl@Cargill.com",SO3,CO,TRN,"BRA.SERVICE@CMA-CGM.COM"])),
 (B4,"SIWAAA=","RES: "+FATDTP,"fayla.lendengues@g10transportes.com.br","2026-11-13T19:09:59Z","jessica.tristao@algceleste.com,Renata_Lima@cargill.com",CC_DTP),
 (B4,"SH1AAA=","RES: PLANILHA ATUALIZADA  ///"+PRE,SO4,"2026-11-13T15:51:37Z",TJUL3,ME),
 (B4,"SHvAAA=","RES: "+IP+" // M-3762/26","barbara@mediterraneanlogistica.com.br","2026-11-13T15:29:10Z","laiza@mediterraneanlogistica.com.br,andressa_nunes@cargill.com,"+JUL+","+AGS3+","+ME+",mediterranean@mediterraneanlogistica.com.br,contato@expurgaguacu.com.br,santos@expurgaguacu.com.br","-port-logistics-cotton@Cargill.com,cotton-br-docs@cargill.com,cotton_gtocbr@cargill.com"),
 (B4,"SH-AAA=","RES: BRSSZ | DRAFT PARCIAL & ATUALIZAÇÃO DE DESCARGA | "+PRE,ISK,"2026-11-13T13:55:37Z",DRAFTTO,DRAFTCC),
 (B4,"SIJAAA=","Re: "+FATDTP,"jessica.tristao@algceleste.com","2026-11-12T21:35:20Z","Renata_Lima@cargill.com",CC_DTP),
 (B4,"SILAAA=","RES: PLANILHA ATUALIZADA  ///"+PRE,SO4,"2026-11-12T18:59:35Z",TJUL3,ME),
 (B4,"SIMAAA=","RE: PLANILHA ATUALIZADA  ///"+PRE,JUL,"2026-11-12T17:48:19Z","operacional4@guarujaterminais.com.br,operacional3@guarujaterminais.com.br,coordenador@guarujaterminais.com.br",ME),
 (B4,"SGKAAA=","RES: BRSSZ | DRAFT PARCIAL & ATUALIZAÇÃO DE DESCARGA | "+PRE,ISK,"2026-11-12T17:31:49Z",DRAFTTO,DRAFTCC),
]
out="/workspace/analise_coleta/raw/cargill_nov2.jsonl"
import os
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
import collections
c=collections.Counter(json.loads(l)["date"][:10] for l in open(out))
print("by day:",sorted(c.items()))
