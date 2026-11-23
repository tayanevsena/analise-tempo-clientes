import json, os
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ME="bma.road-southeast@cma-cgm.com"
PRE="S51907.A01 - BKG SSZ1859739 - 15HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
PRE2="S51504.B01 - BKG SSZ1862967 - SANTOS / HAIPHONG (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
S_CROSS="[CMA CGM] BRSSZ | CROSS DOCKING - COTTON | CARGILL x GUARUJÁ TERMINAIS | S51907.A01 - BKG SSZ1859739 - 15HCs"
S_DOC="Instrução Documentária - S51504.B01- BK SSZ1862967- CARGILL - SANTOS / HAIPHONG PORT, VIETNAM (CIP /EXW)"
JUL="Juliane.MARQUES@mercosul-line.com.br"
ISK="isadora_alonso@cargill.com"; ADB="Adriano_Dasilvabomtempo@cargill.com"; VRA="Vitoria_Raiane@cargill.com"; SMA="Sandielle_Maia@cargill.com"
SO3="operacional3@guarujaterminais.com.br"; SO4="operacional4@guarujaterminais.com.br"; CO="coordenador@guarujaterminais.com.br"
CCTL="cotton_ctl@cargill.com"; NFE="Nfe@cargill.com"; CAS="-CASC-COTTON-ULA@cargill.com"; COTFAT="cotton_faturamento@cargill.com"; CBD="-cbs-uberlandia-fss-itp-originacaocotton-cargillonly@exch.cargill.com"
LGG="LAURIANE_GONCALVES@CRGL-THIRDPARTY.COM"; JPR="JENNIFER_PERIS@CRGL-THIRDPARTY.COM"
AGFULL=",".join(["cotton@agsurveyors.com","certificate@agsurveyors.com","marcela.correia@agsurveyors.com","micael.santiago@agsurveyors.com"])
BMA=",".join([ME,JUL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com","thaina.santos@mercosul-line.com.br","bma.mcastro@cma-cgm.com"])
PLGC="-port-logistics-cotton@Cargill.com"; CDocs="cotton-br-docs@cargill.com"; PAC="-port-allocation-cotton@exch.cargill.com"
TKR=["joana.santos@tkrinspection.com","Skarlatty.Boden@tkrinspection.com","renato.costa@tkrinspection.com","kelly.lopes@tkrinspection.com","carlos.osman@tkrinspection.com","cotton@tkrinspection.com"]
MJR="Mariajulia_Ramos@cargill.com"; NAT="Natalia_Queiroz@cargill.com"; IAN="ian_marques@cargill.com"
YAS="yasmin.mello@pibernat.com.br"; EXPC="expo.cargill.cotton@pibernat.com.br"; GT="cotton_gtocbr@cargill.com"
TRN="transporte@guarujaterminais.com.br"
TJUL3=JUL+","+SO3+","+CO
OP3C=",".join([SO4,SO3,CO])
DRAFTTO=",".join([ISK,ADB,VRA,SMA,"luizjunior@hiperconterminais.com.br"])
DRAFTCC=",".join([PLGC,CDocs,PAC,AGFULL.replace("certificate","vinicius.calazans@agsurveyors.com").replace("marcela.correia","cotton").replace("micael.santiago","giovanna.freitas"),ME,SO3,CO,SO4])
FATIRLO="FATURAMENTO – Exportação Indireta – ALGTIRLO  – Instrução: S51907.A01 – PLACA: FHG6H51 – NF: 834"
FATLCE="FATURAMENTO – Exportação Indireta – ALGCELES  – Instrução: S51907.A01 – PLACA: DTP3J81 – NF: 229255"
CC_IRLO_1=",".join(["cotton_ctl@Cargill.com","geronimo@bomfrete.com.br","cotton_cargill@bomfrete.com.br","jackeline@bomfrete.com.br",COTFAT,CBD,"cotton_ctl@Cargill.com",CAS,LGG,LGG,JPR,AGFULL,BMA,"geronimo@bomfrete.com.br","cotton_cargill@bomfrete.com.br","jeniffer@bomfrete.com.br","jackeline@bomfrete.com.br"])
CC_IRLO_2=",".join(["cotton_ctl@Cargill.com","ctecotton@bomfrete.com.br","geronimo@bomfrete.com.br","cotton_cargill@bomfrete.com.br","jackeline@bomfrete.com.br",COTFAT,CBD,"cotton_ctl@Cargill.com",CAS,LGG,LGG,JPR,AGFULL,BMA,"geronimo@bomfrete.com.br","cotton_cargill@bomfrete.com.br"])
CC_LCE=",".join(["willyan.souza@algceleste.com","thiago.feitosa@algceleste.com","durvacil.assis@algceleste.com",NFE,"cotton_ctl@Cargill.com",CAS,COTFAT,CBD,"cotton_ctl@Cargill.com",CAS,LGG,LGG,JPR,AGFULL,BMA,"rondonopolis.cotton@g10transportes.com.br","bahia@g10transportes.com.br"])
LIB="BMA.LIBERACAO@cma-cgm.com"; CCIS="ssz.customerservice@ccis-network.com"
rows=[
 (B4,"SGSAAA=","RES: PLANILHA ATUALIZADA  ///"+PRE,SO4,"2026-11-12T15:23:50Z",TJUL3,ME),
 (B4,"SGWAAA=","RE: PLANILHA ATUALIZADA  ///"+PRE,JUL,"2026-11-12T15:16:33Z",OP3C,ME),
 (B4,"SGZAAA=","RE: BRSSZ | DRAFT PARCIAL & ATUALIZAÇÃO DE DESCARGA | "+PRE,JUL,"2026-11-12T15:13:42Z",DRAFTTO,DRAFTCC),
 (B4,"SGeAAA=","RES: PLANILHA ATUALIZADA  ///"+PRE,SO4,"2026-11-12T15:03:31Z",TJUL3,ME),
 (B4,"SGnAAA=","RES: "+FATIRLO,"ctecotton@bomfrete.com.br","2026-11-12T14:31:14Z",IAN+","+NAT+",faturamento@agrofibramt.com.br,armazensgeraistirloni@agrotirloni.com",CC_IRLO_1),
 (B4,"SGGAAA=","RES: "+FATLCE,"Renata_Lima@cargill.com","2026-11-12T13:32:34Z",NAT+",faturamento@cooami.com.br,fiscal@gpcagro.com,jaison@cooami.com.br,jessica.tristao@algceleste.com,cotton@cooami.com.br",CC_LCE),
 (B4,"SGDAAA=","RE: BRSSZ | DRAFT PARCIAL & ATUALIZAÇÃO DE DESCARGA | "+PRE,JUL,"2026-11-12T13:03:45Z",DRAFTTO,DRAFTCC),
 (B4,"SGJAAA=","RES: "+FATIRLO,IAN,"2026-11-12T12:51:42Z",NAT+",faturamento@agrofibramt.com.br,armazensgeraistirloni@agrotirloni.com",CC_IRLO_2),
 (B4,"SGCAAA=","APROVADA PLANILHA DE PESO | "+PRE2,MJR,"2026-11-12T12:27:17Z",",".join(TKR[:7]+[EXPC,GT]),",".join([PLGC,CDocs,PAC,"cotton_ctl@Cargill.com"])),
 (B4,"SG4AAA=",FATLCE,NAT,"2026-11-12T12:18:45Z","faturamento@cooami.com.br,fiscal@gpcagro.com,jaison@cooami.com.br,jessica.tristao@algceleste.com,cotton@cooami.com.br",CC_LCE),
 (B4,"SG8AAA=",FATIRLO,NAT,"2026-11-12T11:30:34Z","faturamento@agrofibramt.com.br,armazensgeraistirloni@agrotirloni.com",CC_IRLO_2),
 (B4,"SG9AAA=","RES: BRSSZ | DRAFT PARCIAL & ATUALIZAÇÃO DE DESCARGA | "+PRE,ISK,"2026-11-12T11:30:27Z",DRAFTTO,DRAFTCC),
 (B4,"SG_AAA=","PLANILHA ATUALIZADA  ///"+PRE,SO4,"2026-11-12T11:25:33Z",TJUL3,ME),
 (B4,"SFzAAA=","RES: "+S_JULCROSS if False else "RES: "+S_CROSS,SO4,"2026-11-11T21:07:31Z",TJUL3,ME),
 (B4,"SF1AAA=","RE: [CMA CGM] BRSSZ | Liberação de vazio - CARGILL | COTTON | SSZ1859739 (LS)",JUL,"2026-11-11T20:43:13Z",CCIS+","+LIB+","+OP3C+","+TRN,ME),
 (B4,"SF2AAA=","RES: [CMA CGM] BRSSZ | Liberação de vazio - CARGILL | COTTON | SSZ1859739 (LS)",CCIS,"2026-11-11T20:39:50Z",LIB+","+JUL,ME),
 (B4,"SF4AAA=","RE: [CMA CGM] BRSSZ | Liberação de vazio - CARGILL | COTTON | SSZ1859739 (LS)",LIB,"2026-11-11T20:30:07Z",JUL+","+CCIS,ME),
 (B4,"SF5AAA=","[CMA CGM] BRSSZ | Liberação de vazio - CARGILL | COTTON | SSZ1859739",JUL,"2026-11-11T20:18:44Z",LIB,ME),
 (B4,"SFeAAA=","***PLANILHA DE PESO*** "+S_DOC,"joana.santos@tkrinspection.com","2026-11-11T19:04:45Z",YAS+","+ISK,",".join([JUL,MJR,TKR[1],ME,TKR[2],TKR[3],TKR[4],TKR[5],"cotton_ctl@Cargill.com",EXPC,PLGC,CDocs,PAC])),
 (B4,"SFcAAA=","RES: ***PLANILHA DE PESO*** "+S_DOC,"kelly.lopes@tkrinspection.com","2026-11-11T19:03:10Z",YAS+","+ISK,",".join([JUL,MJR,TKR[0],TKR[1],ME,TKR[2],TKR[4],TKR[5],"cotton_ctl@Cargill.com",EXPC,PLGC,CDocs,PAC])),
]
rows=[r for r in rows if r[5] is not None]
out="/workspace/analise_coleta/raw/cargill_nov2.jsonl"
have=set()
if os.path.exists(out):
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
