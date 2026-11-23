import json, os
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ME="bma.road-southeast@cma-cgm.com"
JUL="Juliane.MARQUES@mercosul-line.com.br"; THA="thaina.santos@mercosul-line.com.br"
ISK="isadora_alonso@cargill.com"; ADB="Adriano_Dasilvabomtempo@cargill.com"; PED="Pedrohenrique_Defreitas@cargill.com"
VRA="Vitoria_Raiane@cargill.com"; SMA="Sandielle_Maia@cargill.com"; GT="cotton_gtocbr@cargill.com"
SO3="operacional3@guarujaterminais.com.br"; SO4="operacional4@guarujaterminais.com.br"; CO="coordenador@guarujaterminais.com.br"
CAM="camila.alonso@agsurveyors.com"; MIC="micael.santiago@agsurveyors.com"; COTAG="cotton@agsurveyors.com"; VCA="vinicius.calazans@agsurveyors.com"; GFR="giovanna.freitas@agsurveyors.com"; MART="marcela.correia@agsurveyors.com"; CERT="certificate@agsurveyors.com"
PLGC="-port-logistics-cotton@Cargill.com"; CDocs="cotton-br-docs@cargill.com"; PAC="-port-allocation-cotton@exch.cargill.com"; CCTL="cotton_ctl@Cargill.com"; CAS="-CASC-COTTON-ULA@cargill.com"; COTFAT="cotton_faturamento@cargill.com"; CBD="-cbs-uberlandia-fss-itp-originacaocotton-cargillonly@exch.cargill.com"; NFE="Nfe@cargill.com"
LGG="LAURIANE_GONCALVES@CRGL-THIRDPARTY.COM"; JPR="JENNIFER_PERIS@CRGL-THIRDPARTY.COM"
REN="Renata_Lima@cargill.com"; CRI="Crisla_Leite@cargill.com"
SO4T=",".join([JUL,SO3,CO]); T_CRO2=",".join([SO4,SO3,CO])
CC_ACE=",".join([PLGC,CDocs,PAC,VCA,COTAG,GFR,ME])
CC_ACE2=",".join([PLGC,CDocs,PAC,VCA,GFR])
COO=["faturamento@cooami.com.br","jessica.tristao@algceleste.com","cotton@cooami.com.br","jaison@cooami.com.br","fiscal@gpcagro.com"]
T_LCE=",".join(COO+[COTFAT,CBD,CCTL,CAS,LGG,COTAG,CERT,MART,MIC,ME,JUL,"BMA.LUCOSTA@cma-cgm.com","BMA.RORTEGA@cma-cgm.com",THA,"bma.mcastro@cma-cgm.com","geronimo@bomfrete.com.br","cotton_cargill@bomfrete.com.br"])
CC_LCE=",".join(["ctecotton@bomfrete.com.br","willyan.souza@algceleste.com","thiago.feitosa@algceleste.com","durvacil.assis@algceleste.com",NFE,CCTL,CAS,"gerenciamentoderisco@bomfrete.com.br","cotton_cargill@bomfrete.com.br","geronimo@bomfrete.com.br","g.ricardo@bomfrete.com.br","wellington.lima@bomfrete.com.br","jaison@cooami.com.br"])
CC_LCE2=CC_LCE+",jeniffer@bomfrete.com.br,jackeline@bomfrete.com.br"
S_ALG="FATURAMENTO \u2013 Exporta\u00e7\u00e3o Indireta \u2013 ALGCELES  \u2013 Instru\u00e7\u00e3o: S51504.B01 \u2013 PLACA: SPU4H46 \u2013 NF: 228425 / 228423"
S_PLU10="PLANILHA ATUALIZADA //| S51504.B01 - BKG SSZ1862967 10HCs"
S_CRO15="[CMA CGM] BRSSZ | CROSS DOCKING - COTTON | CARGILL x GUARUJ\u00c1 TERMINAIS | S51907.A01 - BKG SSZ1859739 - 15HCs"
S_ACES="BRSSZ | ACEITE | PR\u00c9-NOMEA\u00c7\u00c3O - S51907.A01 - BKG SSZ1859739 - 15HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
S_DCD="BRSSZ | DADOS DE CONTAINERS | PR\u00c9-NOMEA\u00c7\u00c3O - S51504.B01 - BKG SSZ1862967 - SANTOS / HAIPHONG (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
T_TIQ=",".join([JUL,"Danilo_Mendes@cargill.com","raynara@mercosul-line.com.br"])  # placeholder overwritten below
T_TIQ=",".join([JUL,"Danilo_Mendes@cargill.com","raynara@mercosul-line.com.br"])
rows=[
 (B4,"RgeAAA=","PROGRAMA\u00c7\u00c3O SAFRA 26-27 - CMA-CGM/ZIRANLOG",ADB,"2026-10-31T14:03:39Z",",".join([ME,JUL,THA]),",".join([PAC,PLGC])),
 (None,"AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAa6NfELAAA=","ENVIO DOCS DE ENTREGA - R R DE ANDRADE LIMA SERVICOS DE TRANSPORTES EIRELI","rpa_no_reply@mercosul-line.com.br","2026-10-31T06:00:02Z","roselma@rrtransporte.com","doc.norte@mercosul-line.com.br"),
 (B4,"RgrAAA=","RES: "+S_ALG,"ctecotton@bomfrete.com.br","2026-10-30T20:31:32Z",",".join([REN,CRI])+","+T_LCE,CC_LCE2),
 (B4,"RgsAAA=","Re: ATA Guaruj\u00e1 Terminais e CMA CGM - Cotton Season","BMA.NLEY@cma-cgm.com","2026-10-30T20:17:58Z",JUL,",".join(["bma.mcastro@cma-cgm.com","anacarolina.esteves@mercosul-line.com.br",ME])),
 (B4,"RgvAAA=","RE: ATA Guaruj\u00e1 Terminais e CMA CGM - Cotton Season",JUL,"2026-10-30T20:07:07Z","BMA.NLEY@cma-cgm.com",",".join(["bma.mcastro@cma-cgm.com","anacarolina.esteves@mercosul-line.com.br",ME])),
 (B4,"RgyAAA=","RES: "+S_ALG,REN,"2026-10-30T19:24:44Z",",".join([CRI])+","+T_LCE,CC_LCE),
 (B4,"RgzAAA=",S_ALG,CRI,"2026-10-30T19:12:09Z",T_LCE,CC_LCE),
 (B4,"Rg9AAA=","RES: "+S_PLU10,SO4,"2026-10-30T16:17:01Z",SO4T,ME),
 (B4,"Rg_AAA=","RES: "+S_CRO15,SO4,"2026-10-30T16:12:31Z",SO4T,ME),
 (B4,"RhBAAA=",S_PLU10,SO4,"2026-10-30T15:57:02Z",SO4T,ME),
 (B4,"RhKAAA=","Draft e Status Estufagem | S51504.B01 - BKG SSZ1862967 - SANTOS / HAIPHONG (CMA-CGM/ZIRANLOG) - CASA | Safra 2026",JUL,"2026-10-30T15:21:07Z",",".join([ISK,PED,MART,ADB,ME,COTAG]),",".join([PLGC,CDocs,PAC,VCA,GFR])),
 (B4,"RhLAAA=","RE: "+S_PLU10,JUL,"2026-10-30T15:16:14Z",T_CRO2,ME),
 (B4,"RhMAAA=",S_CRO15,JUL,"2026-10-30T15:14:53Z",T_CRO2,ME),
 (B4,"RhNAAA=","RE: BRSSZ | ACEITE | "+S_ACES[0:0]+"BRSSZ | ACEITE | PR\u00c9-NOMEA\u00c7\u00c3O - S51907.A01 - BKG SSZ1859739 - 15HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026",JUL,"2026-10-30T15:09:52Z",ADB,CC_ACE),
 (B4,"RhQAAA=","RES: BRSSZ | DADOS DE CONTAINERS | PR\u00c9-NOMEA\u00c7\u00e3O - S51504.B01 - BKG SSZ1862967 - SANTOS / HAIPHONG (CMA-CGM/ZIRANLOG) - CASA | Safra 2026",ISK,"2026-10-30T14:38:32Z",",".join([JUL,PED,MART,ADB,ME,COTAG]),CC_ACE2),
 (None,"AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAYtkQx9AAA=","PROGRAMA\u00c7\u00c3O DE ENTREGAS \u2013 MERCOSUL \u2013 03/11/2026","RAYNARA.SANTOS@MERCOSUL-LINE.COM.BR","2026-10-30T14:33:14Z",",".join(["roselma@rrtransporte.com","operacional@rrtransporte.com","intermodalmanaus@mercosul-line.com.br","jhonnespinheiro@rrtransporte.com","Thiago.Negreiros@mercosul-line.com.br"]),""),
 (B4,"RhWAAA=","RES: BRSSZ | DADOS DE CONTAINERS | PR\u00c9-NOMEA\u00c7\u00e3O - S51504.B01 - BKG SSZ1862967 - SANTOS / HAIPHONG (CMA-CGM/ZIRANLOG) - CASA | Safra 2026",ISK,"2026-10-30T12:44:24Z",",".join([JUL,PED,MART,ADB,ME,COTAG]),CC_ACE2),
 (B4,"RhlAAA=",S_PLU10,SO4,"2026-10-30T11:45:04Z",SO4T,ME),
 (None,"AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAa5hrOcAAA=","ENVIO DOCS DE ENTREGA - R R DE ANDRADE LIMA SERVICOS DE TRANSPORTES EIRELI","rpa_no_reply@mercosul-line.com.br","2026-10-30T05:52:12Z","roselma@rrtransporte.com","doc.norte@mercosul-line.com.br"),
 (B4,"Rh8AAA=","RES: BRSSZ | ACEITE | PR\u00c9-NOMEA\u00c7\u00c3O - S51907.A01 - BKG SSZ1859739 - 15HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026",ADB,"2026-10-29T18:55:48Z",JUL,CC_ACE),
]
out="/workspace/analise_coleta/raw/cargill_oct.jsonl"
have=set()
if os.path.exists(out):
    for l in open(out): have.add(json.loads(l)["id"])
new=0
with open(out,"a") as f:
    for r in rows:
        idb,suf,s,fr,d,to,cc=r
        id_=(idb+suf) if idb else suf
        if id_ in have: continue
        f.write(json.dumps({"id":id_,"folder":"main","date":d,"subject":s,"from":fr,"to":to,"cc":cc},ensure_ascii=False)+"\n")
        have.add(id_); new+=1
print("new:",new,"total:",len(have))
import collections
c=collections.Counter(json.loads(l)["date"][:10] for l in open(out))
print("by day:",sorted(c.items()))
