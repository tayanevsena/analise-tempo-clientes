import json
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
BS="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
BS2="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAa83z-SAAA="
AQM2="AQMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAADSrFV1ygwrEK1d5Xhoqs19gcA-qQhS5nsYUyT70hlqAkATQAFlvmzuAAAAP6kIUuZ7GFMk_9IZagJAE0ABi2RGAAAAQ=="
ME="bma.road-southeast@cma-cgm.com"
S_CROSS="[CMA CGM] BRSSZ | CROSS DOCKING - COTTON | CARGILL x GUARUJÁ TERMINAIS | S51907.A01 - BKG SSZ1859739 - 15HCs"
CROSS10="RES: [CMA CGM] BRSSZ | CROSS DOCKING - COTTON | CARGILL x GUARUJÁ TERMINAIS | S51504.B01 - BKG SSZ1862967 10HCs"
PRE="S51907.A01 - BKG SSZ1859739 - 15HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
PRE2="S51504.B01 - BKG SSZ1862967 - SANTOS / HAIPHONG (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
S_FAT="FATURAMENTO – Exportação Indireta – ALGTRESC  – Instrução: S51907.A01 – PLACA: RAT9G27 – NF: 228708"
STAX="SOLICITAÇÃO // ESTADIA // CMA CGM //  CARGIL - BOOKING: 26BR00018962212 / 26BR00019033762 - CHN3839530  - CHN3831374"
NFS2="NFS DE EXPORTAÇÃO & DUE + Confirmação MAPA | "+PRE2
JUL="Juliane.MARQUES@mercosul-line.com.br"
ISK="isadora_alonso@cargill.com"; ADB="Adriano_Dasilvabomtempo@cargill.com"; VRA="Vitoria_Raiane@cargill.com"
HAR="Harielly_Dasilvabatista@cargill.com"; RNR="Renan_Ruani@cargill.com"; ITF="Itamar_Filho@cargill.com"
IAN="ian_marques@cargill.com"; NAT="Natalia_Queiroz@cargill.com"; LCT="Luciana_Calegari@cargill.com"; PHF="Pedrohenrique_Defreitas@cargill.com"
CCTL="cotton_ctl@cargill.com"; NFE="Nfe@cargill.com"; COTFAT="cotton_faturamento@cargill.com"
CBD="-cbs-uberlandia-fss-itp-originacaocotton-cargillonly@exch.cargill.com"; CDD="cbs-uberlandia-ctl-cdm-all@exch.cargill.com"
SO3="operacional3@guarujaterminais.com.br"; SO4="operacional4@guarujaterminais.com.br"; CO="coordenador@guarujaterminais.com.br"
OP3C="operacional4@guarujaterminais.com.br,operacional3@guarujaterminais.com.br,coordenador@guarujaterminais.com.br"
FATCO="faturamento@cooami.com.br"; JAI="jaison@cooami.com.br"; COTCOO="cotton@cooami.com.br"
COO=",".join([FATCO,"comercial3@trescoqueiros.com",JAI,COTCOO,COTCOO])
TRESCO=",".join(["administrativoalg2@trescoqueiros.com","financeiro3@trescoqueiros.com","administrativoalg3@trescoqueiros.com","administrativoalg@trescoqueiros.com","comercial2@trescoqueiros.com","comercial5@trescoqueiros.com","comercial@trescoqueiros.com","controladoria@trescoqueiros.com","comercial4@trescoqueiros.com","thomas@trescoqueiros.com","financeiro4@trescoqueiros.com","financeiro5@trescoqueiros.com","aprendizfinanceiro@trescoqueiros.com"])
LGG="LAURIANE_GONCALVES@CRGL-THIRDPARTY.COM"; JPR="JENNIFER_PERIS@CRGL-THIRDPARTY.COM"
AGFULL=",".join(["cotton@agsurveyors.com","certificate@agsurveyors.com","marcela.correia@agsurveyors.com","micael.santiago@agsurveyors.com"])
BMA=",".join([ME,JUL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com","thaina.santos@mercosul-line.com.br","bma.mcastro@cma-cgm.com"])
PLGC="-port-logistics-cotton@Cargill.com"; CDocs="cotton-br-docs@cargill.com"; PAC="-port-allocation-cotton@exch.cargill.com"
TKR=["Skarlatty.Boden@tkrinspection.com","renato.costa@tkrinspection.com","kelly.lopes@tkrinspection.com","carlos.osman@tkrinspection.com","cotton@tkrinspection.com"]
DF26="drafts_ate_23-03-26@tkrinspection.com"; DF="drafts@tkrinspection.com"
CC_CAP=",".join([PLGC,CDocs,PAC,"vinicius.calazans@agsurveyors.com","cotton@agsurveyors.com","giovanna.freitas@agsurveyors.com",ME])
CC3=",".join([PLGC,CDocs,PAC])
DOCGRP=",".join([TKR[0],LCT,ISK,JUL,PHF,ADB,ME,TKR[1],TKR[2],TKR[3],TKR[4]])
UNI="laiza.may@uni.com.br,katny.barros@uni.com.br,helio@uni.com.br,cac@unitradinglog.com.br,faturamento.sts@uni.com.br,"+ME+",valerio.carvalho@uni.com.br,giovanna.reis@unitradinglog.com.br"
TONAV=FATCO+",comercial3@trescoqueiros.com,"+JAI+","+COTCOO+","+COTCOO+","+CCTL+","+NFE+","+VRA+","+ITF+",-CASC-COTTON-ULA@cargill.com,"+COTFAT+","+CBD+","+CCTL+",-CASC-COTTON-ULA@cargill.com,"+LGG+","+JPR+","+AGFULL+","+BMA+","+RNR+","+ITF+","+CDD
TJUL3=JUL+","+SO3+","+CO
rows=[
 (B4,"RezAAA=",S_FAT,HAR,"2026-11-04T20:29:32Z",FATCO+",comercial3@trescoqueiros.com,"+JAI+","+COTCOO+","+COTCOO+","+CCTL+","+NFE+","+VRA+","+ITF+",-CASC-COTTON-ULA@cargill.com,"+COTFAT+","+CBD+","+CCTL+",-CASC-COTTON-ULA@cargill.com,"+LGG+","+JPR+","+AGFULL+","+BMA+","+RNR+","+ITF+","+CDD,TRESCO),
 (B4,"Re6AAA=","RES: "+S_JULCROSS if False else "RES: "+S_CROSS,SO4,"2026-11-04T19:37:05Z",TJUL3,ME),
 (B4,"Re9AAA=","PLANILHA DE PESO |  "+NFS2,"joana.santos@tkrinspection.com","2026-11-04T18:26:03Z","Juliane.MARQUES@mercosul-line.com.br,"+NAT+","+",".join([JUL,NAT]+TKR[:1]+[LCT,ISK,PHF,ADB,ME]+TKR[1:5]+["cotton_ctl@Cargill.com"]),CC3),
 (B4,"RfAAAA=",NFS2,JUL,"2026-11-04T17:35:31Z","Natalia_Queiroz@cargill.com,"+",".join([TKR[0],LCT,ISK,PHF,ADB,ME,TKR[1],TKR[2],TKR[3],TKR[4],DF26,"cotton_ctl@Cargill.com"]),CC3),
 (B4,"RfCAAA=","RES: PLANILHA FINALIZADA //| S51504.B01 - BKG SSZ1862967 10HCs",SO4,"2026-11-04T17:01:25Z",TJUL3,ME),
 (B4,"RfDAAA=","RES: "+STAX,"fellipe.xavier@unitradinglog.com.br","2026-11-04T16:54:45Z",JUL,UNI),
 (B4,"RfNAAA=","RE: "+STAX,JUL,"2026-11-04T14:50:49Z","fellipe.xavier@unitradinglog.com.br",UNI),
 (B4,"RfOAAA=","RES: BRSSZ | ACEITE | PRÉ-NOMEAÇÃO - "+PRE,ISK,"2026-11-04T14:48:45Z",JUL+","+ADB,CC_CAP),
 (B4,"RfQAAA=","SDL-DOC - [CMA CGM] BRSSZ | INTERNO | ROAD | AJUSTE DE TAXAS | CARGILL - CHN3839530",JUL,"2026-11-04T14:45:10Z","BRA.SERVICE@CMA-CGM.COM",ME),
 (B4,"RfxAAA=","RES: URGENTE: Draft e Status Estufagem | "+PRE2,NAT,"2026-11-04T11:40:11Z",DOCGRP.replace(ISK+","+JUL,JUL+","+ISK).replace(",Skarlatty.Boden"+",",",Skarlatty.Boden"+",")+","+DF26+",cotton_ctl@Cargill.com" if False else ",".join([TKR[0],LCT,ISK,JUL,PHF,ADB,ME,TKR[1],TKR[2],TKR[3],TKR[4],DF26,"cotton_ctl@Cargill.com"]),CC3),
 (BS2,"","ENVIO DOCS DE ENTREGA - R R DE ANDRADE LIMA SERVICOS DE TRANSPORTES EIRELI","rpa_no_reply@mercosul-line.com.br","2026-11-04T05:36:29Z","roselma@rrtransporte.com","doc.norte@mercosul-line.com.br"),
 (B4,"Rf1AAA=","RES: URGENTE: Draft e Status Estufagem | "+PRE2,TKR[0],"2026-11-03T21:05:01Z",",".join([LCT,ISK,JUL,PHF,ADB,ME,TKR[1],TKR[2],TKR[3],TKR[4],DF26,NAT,"cotton_ctl@Cargill.com"]),CC3),
 (B4,"Rf2AAA=",CROSS10,SO4,"2026-11-03T20:59:10Z",TJUL3,ME),
 (B4,"Rf-AAA=","RE: "+CROSS10,JUL,"2026-11-03T20:14:04Z",OP3C,ME),
 (AQM2,"","URGENTE: Draft e Status Estufagem | "+PRE2,LCT,"2026-11-03T20:07:03Z",",".join([ISK,JUL,PHF,ADB,ME,TKR[1],TKR[2],TKR[3],TKR[4],DF]),CC3),
 (B4,"RgBAAA=","RES: PRÉ-NOMEAÇÃO - "+PRE2,LCT,"2026-11-03T20:06:54Z","Adriano_Dasilvabomtempo@cargill.com,thaina.santos@mercosul-line.com.br,"+ME+","+JUL,CC3+","+",".join([TKR[1],TKR[2],TKR[3],TKR[4],DF])),
 (B4,"RgGAAA=","RES: PLANILHA FINALIZADA //| S51504.B01 - BKG SSZ1862967 10HCs",SO4,"2026-11-03T18:27:51Z",TJUL3,ME),
 (B4,"RgIAAA=","RE: PLANILHA ATUALIZADA //| S51504.B01 - BKG SSZ1862967 10HCs",JUL,"2026-11-03T17:01:33Z",OP3C,ME),
 (BS,"Q8uAAA=","LISTA DE DESCARGA MERCOSUL FORTALEZA/BRA010N99N","RAYNARA.SANTOS@MERCOSUL-LINE.COM.BR","2026-11-03T16:05:41Z","MAO.AARAUJO@ccis-network.com,Thiago.Negreiros@mercosul-line.com.br,anacarolina.esteves@mercosul-line.com.br,mao.lgaia@ccis-network.com,MAO.TBARBOZA@ccis-network.com","multimodal.norte@mercosul-line.com.br"),
 (BS,"Q9JAAA=","PROGRAMAÇÃO DE ENTREGAS – MERCOSUL – 04/11/2026","RAYNARA.SANTOS@MERCOSUL-LINE.COM.BR","2026-11-03T15:10:00Z","roselma@rrtransporte.com,operacional@rrtransporte.com,intermodalmanaus@mercosul-line.com.br,jhonnespinheiro@rrtransporte.com,Thiago.Negreiros@mercosul-line.com.br",""),
 (BS,"RD6AAA=","PROGRAMAÇÃO DE ENTREGAS – MERCOSUL – 06/11/2026","RAYNARA.SANTOS@MERCOSUL-LINE.COM.BR","2026-11-05T15:17:31Z","roselma@rrtransporte.com,operacional@rrtransporte.com,intermodalmanaus@mercosul-line.com.br,jhonnespinheiro@rrtransporte.com,Thiago.Negreiros@mercosul-line.com.br",""),
 (BS,"z-SAAA=","ENVIO DOCS DE ENTREGA - R R DE ANDRADE LIMA SERVICOS DE TRANSPORTES EIRELI","rpa_no_reply@mercosul-line.com.br","2026-11-04T05:36:29Z","roselma@rrtransporte.com","doc.norte@mercosul-line.com.br"),
]
rows=[r for r in rows if r[1] or r[0]==AQM2 or r[0]==BS2]
rows=[r for r in rows if not (r[1]=="" and r[0]==BS)]
out="/workspace/analise_coleta/raw/cargill_nov.jsonl"
have=set()
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
print(sorted(c.items()))
