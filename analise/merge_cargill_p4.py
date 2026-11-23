import json
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
B3="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO3AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
BS="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAYtkRD6AAA="
BNSQ="AQMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAADSrFV1ygwrEK1d5Xhoqs19gcA-qQhS5nsYUyT70hlqAkATQAAAgEJAAAA-qQhS5nsYUyT70hlqAkATQAGLZEHNgAAAA=="
ME="bma.road-southeast@cma-cgm.com"; BNS="bmn.tsena@cma-cgm.com"
S_DOC="Instrução Documentária - S51504.B01- BK SSZ1862967- CARGILL - SANTOS / HAIPHONG PORT, VIETNAM (CIP /EXW)"
S_CROSS="[CMA CGM] BRSSZ | CROSS DOCKING - COTTON | CARGILL x GUARUJÁ TERMINAIS | S51907.A01 - BKG SSZ1859739 - 15HCs"
PRE="S51907.A01 - BKG SSZ1859739 - 15HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
IP="Instrução Documentária Provisória - S51907.A01 - BK SSZ1859739 - INDIRETA - SANTOS / KARACHI  | Safra 2026"
S_FAT="FATURAMENTO – Exportação Indireta – ALGTRESC  – Instrução: S51907.A01 – PLACA: RAT9G27 – NF: 228708"
JUL="Juliane.MARQUES@mercosul-line.com.br"
ISK="isadora_alonso@cargill.com"; ADB="Adriano_Dasilvabomtempo@cargill.com"; VRA="Vitoria_Raiane@cargill.com"
HAR="Harielly_Dasilvabatista@cargill.com"; RNR="Renan_Ruani@cargill.com"; ITF="Itamar_Filho@cargill.com"
IAN="ian_marques@cargill.com"; CRI="Crisla_Leite@cargill.com"; AND="andressa_nunes@cargill.com"
CCTL="cotton_ctl@cargill.com"; NFE="Nfe@cargill.com"; COTFAT="cotton_faturamento@cargill.com"
CBD="-cbs-uberlandia-fss-itp-originacaocotton-cargillonly@exch.cargill.com"
SO3="operacional3@guarujaterminais.com.br"; SO4="operacional4@guarujaterminais.com.br"; CO="coordenador@guarujaterminais.com.br"
OP3C="operacional4@guarujaterminais.com.br,operacional3@guarujaterminais.com.br,coordenador@guarujaterminais.com.br"
FATCO="faturamento@cooami.com.br"; JAI="jaison@cooami.com.br"; COTCOO="cotton@cooami.com.br"
COO=",".join([FATCO,"comercial3@trescoqueiros.com",JAI,COTCOO,COTCOO])
TRESCO=",".join(["administrativoalg2@trescoqueiros.com","financeiro3@trescoqueiros.com","administrativoalg3@trescoqueiros.com","administrativoalg@trescoqueiros.com","comercial2@trescoqueiros.com","comercial5@trescoqueiros.com","comercial@trescoqueiros.com","controladoria@trescoqueiros.com","comercial4@trescoqueiros.com","thomas@trescoqueiros.com","financeiro4@trescoqueiros.com","financeiro5@trescoqueiros.com","aprendizfinanceiro@trescoqueiros.com"])
LGG="LAURIANE_GONCALVES@CRGL-THIRDPARTY.COM"; JPR="JENNIFER_PERIS@CRGL-THIRDPARTY.COM"
AGFULL=",".join(["cotton@agsurveyors.com","certificate@agsurveyors.com","marcela.correia@agsurveyors.com","micael.santiago@agsurveyors.com"])
BMA=",".join([ME,JUL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com","thaina.santos@mercosul-line.com.br","bma.mcastro@cma-cgm.com"])
MJR="Mariajulia_Ramos@cargill.com"; EXPC="expo.cargill.cotton@pibernat.com.br"
TKR=["joana.santos@tkrinspection.com","Skarlatty.Boden@tkrinspection.com","renato.costa@tkrinspection.com","kelly.lopes@tkrinspection.com","carlos.osman@tkrinspection.com","cotton@tkrinspection.com"]
TKRj=",".join(TKR)
CC_CAP=",".join(["-port-logistics-cotton@Cargill.com","cotton-br-docs@cargill.com","-port-allocation-cotton@exch.cargill.com","vinicius.calazans@agsurveyors.com","cotton@agsurveyors.com","giovanna.freitas@agsurveyors.com",ME])
AGS3="vinicius.calazans@agsurveyors.com,cotton@agsurveyors.com,giovanna.freitas@agsurveyors.com"
CC_IP=",".join(["-port-logistics-cotton@Cargill.com","cotton-br-docs@cargill.com","cotton_gtocbr@cargill.com"])
MED=",".join(["mediterranean@mediterraneanlogistica.com.br","contato@expurgaguacu.com.br","santos@expurgaguacu.com.br"])
FATEZ="FATURAMENTO – Exportação Indireta – ALGTRESC  – Instrução: S51907.A01 – PLACA: EZU3I46 – NF: 228743"
FATEZs="FATURAMENTO – Exportação Indireta – ALGTRESC – Instrução: S51907.A01 – PLACA: EZU3I46 – NF: 228743"
FULA=",".join(["-CASC-COTTON-ULA@cargill.com",COTFAT,CBD,CCTL,"-CASC-COTTON-ULA@cargill.com"])
TONAV=FATCO+",comercial3@trescoqueiros.com,"+JAI+","+COTCOO+","+COTCOO+","+CCTL+","+NFE+","+VRA+","+ITF+","+CAS(CAS=None) if False else FATCO+",comercial3@trescoqueiros.com,"+JAI+","+COTCOO+","+COTCOO+","+CCTL+","+NFE+","+VRA+","+ITF+",-CASC-COTTON-ULA@cargill.com,cotton_faturamento@cargill.com,-cbs-uberlandia-fss-itp-originacaocotton-cargillonly@exch.cargill.com,"+CCTL+",-CASC-COTTON-ULA@cargill.com,"+LGG+","+JPR+","+AGFULL+","+BMA+",rondonopolis.cotton@transportadoranavarini.com.br,cotton.mt@transportadoranavarini.com.br"
LB="BMA.LIBERACAO@cma-cgm.com,cma.lechman@lechman.com.br,lucas.silva@lechman.com.br"
rows=[
 (B4,"RdUAAA=","RE: "+S_CROSS,JUL,"2026-11-06T11:46:50Z",BNS+","+OP3C,ME),
 (B4,"RdaAAA=","RES: "+IP+" // M-3762/26","laiza@mediterraneanlogistica.com.br","2026-11-06T01:14:07Z",AND+","+JUL+","+AGS3+","+ME+","+MED,CC_IP),
 (B4,"RdgAAA=","RE: "+S_CROSS,BNS,"2026-11-05T21:35:42Z",JUL+","+OP3C,ME),
 (BNSQ,"","RE: "+S_CROSS,BNS,"2026-11-05T21:34:00Z",JUL+","+OP3C,ME),
 (B4,"RdiAAA=",S_DOC,MJR,"2026-11-05T21:14:54Z",",".join([TKR[0],JUL,TKR[1],ME,TKR[2],TKR[3],TKR[4],TKR[5],"cotton_ctl@Cargill.com",EXPC]),"-port-logistics-cotton@Cargill.com,cotton-br-docs@cargill.com,-port-allocation-cotton@exch.cargill.com"),
 (B4,"RdlAAA=","Re: "+FATEZs,"filial.sapezal@transportadoranavarini.com.br","2026-11-05T20:49:35Z",IAN,"Crisla_Leite@cargill.com,"+TONAV),
 (B4,"RdsAAA=","RES: BRSSZ | ACEITE | PRÉ-NOMEAÇÃO - "+PRE,ISK,"2026-11-05T20:01:13Z",JUL+","+ADB,CC_CAP),
 (B4,"ReBAAA=","RES: [CMA CGM] BRSSZ | Liberação de vazio - CARGILL | COTTON | SSZ1859739 (LR)","lucas.silva@lechman.com.br","2026-11-05T16:49:01Z","BMA.LIBERACAO@cma-cgm.com,"+JUL+",cma.lechman@lechman.com.br",ME),
 (B4,"ReCAAA=","RE: "+S_CROSS,JUL,"2026-11-05T16:41:07Z",OP3C,ME),
 (BS,"","PROGRAMAÇÃO DE ENTREGAS – MERCOSUL – 06/11/2026","RAYNARA.SANTOS@MERCOSUL-LINE.COM.BR","2026-11-05T15:17:31Z","roselma@rrtransporte.com,operacional@rrtransporte.com,intermodalmanaus@mercosul-line.com.br,jhonnespinheiro@rrtransporte.com,Thiago.Negreiros@mercosul-line.com.br",""),
 (B4,"ReRAAA=","RE: [CMA CGM] BRSSZ | Liberação de vazio - CARGILL | COTTON | SSZ1859739 (LR)","BMA.LIBERACAO@cma-cgm.com","2026-11-05T14:05:18Z",JUL+",cma.lechman@lechman.com.br,lucas.silva@lechman.com.br",ME),
 (B4,"ReTAAA=","RES: "+IP,"contato@expurgaguacu.com.br","2026-11-05T13:57:17Z",AND+","+JUL+","+AGS3+","+ME+",mediterranean@mediterraneanlogistica.com.br,santos@expurgaguacu.com.br",CC_IP),
 (B4,"ReYAAA=","RES: "+FATEZ,IAN,"2026-11-05T12:49:42Z",CRI+","+FATCO+",comercial3@trescoqueiros.com,"+JAI+","+COTCOO+","+COTCOO+","+CCTL+","+NFE+","+VRA+","+ITF+",-CASC-COTTON-ULA@cargill.com,filial.sapezal@transportadoranavarini.com.br,"+COTFAT+","+CBD+","+CCTL+",-CASC-COTTON-ULA@cargill.com,"+LGG+","+JPR+","+AGFULL+","+BMA+",rondonopolis.cotton@transportadoranavarini.com.br,cotton.mt@transportadoranavarini.com.br",TRESCO),
 (B3,"RMMAAA=","[CMA CGM] BRSSZ | Liberação de vazio - CARGILL | COTTON | SSZ1859739",JUL,"2026-11-05T12:45:40Z","BMA.LIBERACAO@cma-cgm.com",ME),
 (B4,"ReaAAA=","RES: BRSSZ | ACEITE | PRÉ-NOMEAÇÃO - "+PRE,ISK,"2026-11-05T12:29:29Z",JUL+","+ADB,CC_CAP),
 (B4,"RebAAA=",IP,AND,"2026-11-05T12:18:29Z",JUL+","+AGS3+","+ME+",mediterranean@mediterraneanlogistica.com.br,contato@expurgaguacu.com.br,santos@expurgaguacu.com.br",CC_IP),
 (B4,"RehAAA=","RES: "+FATEZ,FATCO,"2026-11-05T12:08:51Z",CRI+",comercial3@trescoqueiros.com,"+JAI+","+COTCOO+","+COTCOO+","+CCTL+","+NFE+","+VRA+","+ITF+",-CASC-COTTON-ULA@cargill.com,filial.sapezal@transportadoranavarini.com.br,"+COTFAT+","+CBD+","+CCTL+",-CASC-COTTON-ULA@cargill.com,"+LGG+","+JPR+","+AGFULL+","+BMA+",rondonopolis.cotton@transportadoranavarini.com.br,cotton.mt@transportadoranavarini.com.br",TRESCO+","+FATCO),
 (B4,"RejAAA=",FATEZ,CRI,"2026-11-05T11:52:36Z",TONAV,TRESCO),
 (B4,"RelAAA=","RES: "+S_FAT,ITF,"2026-11-05T11:51:25Z",IAN+","+HAR+",michael.freire@fribontransportes.com.br,"+FATCO+",comercial3@trescoqueiros.com,"+JAI+","+COTCOO+","+COTCOO+","+CCTL+","+NFE+","+VRA+",-CASC-COTTON-ULA@cargill.com,"+COTFAT+","+CBD+","+CCTL+",-CASC-COTTON-ULA@cargill.com,"+LGG+","+JPR+","+AGFULL+","+BMA+","+RNR+",cbs-uberlandia-ctl-cdm-all@exch.cargill.com",TRESCO),
 (B4,"RenAAA=","RES: "+S_FAT,IAN,"2026-11-05T11:30:15Z",HAR+","+FATCO+",comercial3@trescoqueiros.com,"+JAI+","+COTCOO+","+COTCOO+","+CCTL+","+NFE+","+VRA+","+ITF+",-CASC-COTTON-ULA@cargill.com,"+COTFAT+","+CBD+","+CCTL+",-CASC-COTTON-ULA@cargill.com,"+LGG+","+JPR+","+AGFULL+","+BMA+","+RNR+","+ITF+",cbs-uberlandia-ctl-cdm-all@exch.cargill.com",TRESCO),
]
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
