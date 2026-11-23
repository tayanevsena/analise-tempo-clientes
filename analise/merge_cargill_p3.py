import json
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
AQM="AQMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAADSrFV1ygwrEK1d5Xhoqs19gcA-qQhS5nsYUyT70hlqAkATQAFlvmzuAAAAP6kIUuZ7GFMk_9IZagJAE0ABi2RHQAAAQ=="
ME="bma.road-southeast@cma-cgm.com"; BNS="bmn.tsena@cma-cgm.com"
S_DOC="Instrução Documentária - S51504.B01- BK SSZ1862967- CARGILL - SANTOS / HAIPHONG PORT, VIETNAM (CIP /EXW)"
S_CROSS="[CMA CGM] BRSSZ | CROSS DOCKING - COTTON | CARGILL x GUARUJÁ TERMINAIS | S51907.A01 - BKG SSZ1859739 - 15HCs"
PRE="S51907.A01 - BKG SSZ1859739 - 15HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
JUL="Juliane.MARQUES@mercosul-line.com.br"
ISK="isadora_alonso@cargill.com"; ADB="Adriano_Dasilvabomtempo@cargill.com"; VRA="Vitoria_Raiane@cargill.com"
HAR="Harielly_Dasilvabatista@cargill.com"; RNR="Renan_Ruani@cargill.com"; ITF="Itamar_Filho@cargill.com"
IAN="ian_marques@cargill.com"; CRI="Crisla_Leite@cargill.com"; NAT="Natalia_Queiroz@cargill.com"; LET="Leticia_Maximiano1@cargill.com"
CCTL="cotton_ctl@cargill.com"; NFE="Nfe@cargill.com"; COTFAT="cotton_faturamento@cargill.com"
CBD="-cbs-uberlandia-fss-itp-originacaocotton-cargillonly@exch.cargill.com"
CDD="cbs-uberlandia-ctl-cdm-all@exch.cargill.com"
CAS="-CASC-COTTON-ULA@cargill.com"
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
ULA=",".join([CAS,COTFAT,CBD,CCTL,CAS])
FBASE="FATURAMENTO – Exportação Indireta – ALGTRESC  – Instrução: S51907.A01 – PLACA: {p} – NF: {n}"
def FAT(p,n,pre="RES: "): return pre+FBASE.format(p=p,n=n)
CC_CAP=",".join(["-port-logistics-cotton@Cargill.com","cotton-br-docs@cargill.com","-port-allocation-cotton@exch.cargill.com","vinicius.calazans@agsurveyors.com","cotton@agsurveyors.com","giovanna.freitas@agsurveyors.com",ME])
TKRj=",".join(TKR)
CC_SFG=",".join(["administrativoalg2@trescoqueiros.com","financeiro3@trescoqueiros.com","administrativoalg3@trescoqueiros.com","administrativoalg@trescoqueiros.com","comercial2@trescoqueiros.com","comercial5@trescoqueiros.com","comercial@trescoqueiros.com","controladoria@trescoqueiros.com","comercial4@trescoqueiros.com","thomas@trescoqueiros.com",COTFAT,CBD,CCTL,CAS,LGG,LGG,JPR,AGFULL,BMA,RNR,ITF,CDD,"financeiro5@trescoqueiros.com","aprendizfinanceiro@trescoqueiros.com"])
rows=[
 (B4,"RzsAAA=","RES: "+S_CROSS,SO4,"2026-11-07T13:14:41Z",JUL+","+SO3+","+CO,ME),
 (B4,"Rx_AAA=",FAT("SPD0A75","228882"),ITF,"2026-11-06T20:08:02Z",IAN+","+CRI+","+COO+","+CCTL+","+NFE+","+VRA+","+ULA+","+LGG+","+JPR+","+AGFULL+","+BMA+",michael.freire@fribontransportes.com.br",TRESCO),
 (B4,"Rz_AAA=",FAT("SPD0A75","228882"),IAN,"2026-11-06T19:46:35Z",CRI+","+COO+","+CCTL+","+NFE+","+VRA+","+ITF+","+ULA+","+LGG+","+JPR+","+AGFULL+","+BMA+","+RNR+","+ITF+","+CDD,TRESCO),
 (AQM,"",FAT("SPD0A75","228882",pre=""),CRI,"2026-11-06T19:27:27Z",COO+","+CCTL+","+NFE+","+VRA+","+ITF+","+ULA+","+LGG+","+JPR+","+AGFULL+","+BMA+","+RNR+","+ITF+","+CDD,TRESCO),
 (B4,"RcdAAA=","RE: SDL-DOC - [CMA CGM] BRSSZ | INTERNO | ROAD | AJUSTE DE TAXAS | CARGILL - CHN3839530","bra.service@cma-cgm.com","2026-11-06T19:02:40Z",JUL,ME),
 (B4,"RcMAAA=","RE: SDL-DOC - [CMA CGM] BRSSZ | INTERNO | ROAD | AJUSTE DE TAXAS | CARGILL - CHN3839530",JUL,"2026-11-06T18:58:49Z","BRA.SERVICE@CMA-CGM.COM",ME),
 (B4,"RcNAAA=","RE: "+S_CROSS,JUL,"2026-11-06T18:58:37Z",OP3C,ME),
 (B4,"RcTAAA=","RES: BRSSZ | ACEITE | PRÉ-NOMEAÇÃO - "+PRE,ISK,"2026-11-06T17:50:04Z",JUL+","+ADB,CC_CAP),
 (B4,"RchAAA=",FAT("UAJ3I50","228803"),FATCO,"2026-11-06T15:17:24Z",CRI+",comercial3@trescoqueiros.com,"+JAI+","+COTCOO+","+COTCOO+","+CCTL+","+NFE+","+VRA+","+ITF+","+ULA+","+LGG+","+JPR+","+AGFULL+","+BMA+",rondonopolis.cotton@transportadoranavarini.com.br,cotton.mt@transportadoranavarini.com.br",TRESCO),
 (B4,"RciAAA=",FAT("SFG6E52","228827"),FATCO,"2026-11-06T15:15:11Z",NAT+","+HAR+",comercial3@trescoqueiros.com,"+JAI+","+COTCOO+","+COTCOO+","+CCTL+","+NFE+","+VRA+","+ITF+","+CAS,CC_SFG),
 (B4,"RxqAAA=",FAT("UAJ3I50","228803"),IAN,"2026-11-06T15:08:45Z",CRI+","+FATCO+",comercial3@trescoqueiros.com,"+JAI+","+COTCOO+","+COTCOO+","+CCTL+","+NFE+","+VRA+","+ITF+","+ULA+","+LGG+","+JPR+","+AGFULL+","+BMA+",rondonopolis.cotton@transportadoranavarini.com.br,cotton.mt@transportadoranavarini.com.br",TRESCO),
 (B4,"RcwAAA=",FAT("UAJ3I50","228803",pre=""),CRI,"2026-11-06T14:03:40Z",COO+","+CCTL+","+NFE+","+VRA+","+ITF+","+ULA+","+LGG+","+JPR+","+AGFULL+","+BMA+",rondonopolis.cotton@transportadoranavarini.com.br,cotton.mt@transportadoranavarini.com.br",TRESCO),
 (B4,"RcxAAA=",FAT("SFG6E52","228827"),ITF,"2026-11-06T13:38:38Z",IAN+","+NAT+","+FATCO+","+HAR+",comercial3@trescoqueiros.com,"+JAI+","+COTCOO+","+COTCOO+","+CCTL+","+NFE+","+VRA+","+CAS+",michael.freire@fribontransportes.com.br","administrativoalg2@trescoqueiros.com,michael.freire@fribontransportes.com.br,financeiro3@trescoqueiros.com,administrativoalg3@trescoqueiros.com,administrativoalg@trescoqueiros.com,comercial2@trescoqueiros.com,comercial5@trescoqueiros.com,comercial@trescoqueiros.com,controladoria@trescoqueiros.com,comercial4@trescoqueiros.com,thomas@trescoqueiros.com,"+COTFAT+","+CBD+","+CCTL+","+CAS+","+LGG+","+LGG+","+JPR+","+AGFULL+","+BMA+","+RNR+","+CDD+",financeiro5@trescoqueiros.com,aprendizfinanceiro@trescoqueiros.com,"+LET),
 (B4,"Rc1AAA=",FAT("SFG6E52","228827"),IAN,"2026-11-06T13:21:15Z",NAT+","+FATCO+","+HAR+",comercial3@trescoqueiros.com,"+JAI+","+COTCOO+","+COTCOO+","+CCTL+","+NFE+","+VRA+","+ITF+","+CAS,CC_SFG),
 (B4,"Rc5AAA=",FAT("SFG6E52","228827",pre=""),NAT,"2026-11-06T13:07:14Z",FATCO+","+HAR+",comercial3@trescoqueiros.com,"+JAI+","+COTCOO+","+COTCOO+","+CCTL+","+NFE+","+VRA+","+ITF+","+CAS,CC_SFG),
 (B4,"Rc7AAA=","RES: BRSSZ | ACEITE | PRÉ-NOMEAÇÃO - "+PRE,ISK,"2026-11-06T13:01:57Z",JUL+","+ADB,CC_CAP),
 (B4,"Rc-AAA=","ACEITE - "+S_DOC,"thiago.vergara@pibernat.com.br","2026-11-06T12:45:04Z",MJR,",".join(TKR+[ME,CCTL,EXPC,"-port-logistics-cotton@Cargill.com","cotton-br-docs@cargill.com","-port-allocation-cotton@exch.cargill.com"])),
 (B4,"RdIAAA=","RES: "+S_CROSS,SO4,"2026-11-06T12:24:29Z",JUL+","+BNS+","+SO3+","+CO,ME),
 (B4,"RdMAAA=","NFS DE EXPORTAÇÃO & DUE + Confirmação MAPA | "+S_DOC,JUL,"2026-11-06T12:13:06Z",",".join([MJR]+TKR+[CCTL,EXPC]),"-port-logistics-cotton@Cargill.com,cotton-br-docs@cargill.com,-port-allocation-cotton@exch.cargill.com,operacional4@guarujaterminais.com.br,operacional3@guarujaterminais.com.br,coordenador@guarujaterminais.com.br,transporte@guarujaterminais.com.br"),
 (B4,"RdSAAA=","RES: "+S_CROSS,SO4,"2026-11-06T11:56:13Z",BNS+","+JUL+","+SO3+","+CO,ME),
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
