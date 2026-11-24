import json
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
FTX="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ME="bma.road-southeast@cma-cgm.com"
JUL="Juliane.MARQUES@mercosul-line.com.br"
GRAZ="graziela.braga@pibernat.com.br"; PPAL="Paula_Palazzo@cargill.com"; GETH="gethelp@cargill.com"
GIO="Giovana_Santos1@cargill.com"; WES="Wesley_Delisolasantos@cargill.com"; TFA="Tiago_Faria@cargill.com"
CASC="Casc_Impo@cargill.com"; CSIMP="-CASC-GTOC-IMP@exch.cargill.com"; ITRG="impo.cargill.rgd@pibernat.com.br"; BSVC="bra.service@cma-cgm.com"
AGRO="AGROQUIMICOS-CROPINPUT@cargill.com"; AGRO2="-AGROQUIMICOS-CROPINPUT@cargill.com"; NBAR="Natalia_Barreto@cargill.com"
TEALL="-CASC-IMPORTS-TE-ALL@Cargill.com"; JAC="Jaciara_Marquesdesouza@cargill.com"; RPAN="rpa_no_reply@mercosul-line.com.br"; DOCT="doc.norte@mercosul-line.com.br"
RAY="RAYNARA.SANTOS@MERCOSUL-LINE.COM.BR"; EMAT="SSZ.EMATOS@cma-cgm.com"
CHGLIST=[CASC,BSVC,"Rafael_Felicissimo@cargill.com","Danilo_Rezende@cargill.com","Isabela_Limadeoliveira@cargill.com","CELSO_VELOSO@cargill.com",PPAL,"priscila_liziero@cargill.com",GIO,JAC,CSIMP,"Marcella_Chompresilva@cargill.com",TFA,WES,"Analu_Kuhn@cargill.com","Moacir_Valim@cargill.com","Nataniele_Paula@cargill.com","Fabio_Caruso@cargill.com","Luciana_Gugelmin@cargill.com"]
S_G275="LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001889833-6 | DSA| CASC0137/26, PO 521715Z359 | GLIFOSATO NGC - RIO VERDE | GHYD260275 (CHN3831378) *CARGA DSA*"
S_G276="LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001879016-0 | DSA | CASC0139/26, PO 521715Z361 | GLIFOSATO NGC - RIO VERDE | GHYD260276 (CHN3831443)"
S_G277="LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001896221-2 | DSA | CASC0138/26, PO 521715Z360 | GLIFOSATO NGC - DANFE SOLICITADA| GHYD260277 (CHN3831374)"
S_IMP_378="RE: [CMA CCGM] BRSSZ | PROGRAMA\u00c7\u00c3O IMPORTA\u00c7\u00c3O | CARGILL x UNITRADING | CHN3831378"
S_IMP_443="RE: [CMA CCGM] BRSSZ | PROGRAMA\u00c7\u00c3O IMPORTA\u00c7\u00c3O | CARGILL x UNITRADING | CHN3831443"
S_CHG="RE: **PROGRAMA\u00c7\u00c3O DE CHEGADAS - PROCESSOS COM A CMA**"
S_PR08="PROGRAMA\u00c7\u00c3O DE ENTREGAS \u2013 MERCOSUL \u2013 08/10/2026"
S_PR07="PROGRAMA\u00c7\u00c3O DE ENTREGAS \u2013 MERCOSUL \u2013 07/10/2026"
S_LD="LISTA DE DESCARGA - MERCOSUL FORTALEZA/0BCOMN1RC"
S_RWL="ENVIO DOCS DE ENTREGA - W L TRANSPORTE DE CARGAS E SERVICOS ADMINISTRATIVO LTDA"
S_RRR="ENVIO DOCS DE ENTREGA - R R DE ANDRADE LIMA SERVICOS DE TRANSPORTES EIRELI"
rows=[
 (B4,"RvJAAA=",S_IMP_378,JUL,"2026-10-08T17:46:07Z","atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RvKAAA=",S_IMP_443,JUL,"2026-10-08T17:45:27Z","atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RvMAAA=","RE: "+S_G275,JUL,"2026-10-08T16:51:49Z",",".join([GRAZ,GETH,PPAL,ME,BSVC]),",".join([GIO,CASC,AGRO2,ITRG,CSIMP,WES,TFA])),
 (B4,"RvNAAA=","RE: "+S_G277,JUL,"2026-10-08T16:51:26Z",",".join([GRAZ,PPAL,ME,BSVC]),",".join([GIO,AGRO2,CASC,NBAR,ITRG,CSIMP,WES,TFA])),
 (None,FTX+"anpJGSAAA=",S_RWL,RPAN,"2026-10-08T09:25:01Z","willians@wltransportes-am.com.br,kellen.silva@wltransportes-am.com.br",DOCT),
 (None,FTX+"anpJFkAAA=",S_RWL,RPAN,"2026-10-08T06:35:14Z","willians@wltransportes-am.com.br,kellen.silva@wltransportes-am.com.br",DOCT),
 (B4,"RvaAAA=","RE: "+S_G276,JUL,"2026-10-07T20:33:56Z",",".join([GRAZ,GETH,ME,BSVC,AGRO,PPAL,WES]),",".join([GIO,CASC,AGRO2,ITRG,CSIMP,TFA])),
 (B4,"RvoAAA=",S_G275,GRAZ,"2026-10-07T18:29:56Z",",".join([GETH,PPAL,JUL,ME,BSVC]),",".join([GIO,CASC,AGRO2,ITRG,CSIMP,WES,TFA])),
 (B4,"RvrAAA=",S_G277,GRAZ,"2026-10-07T18:14:36Z",",".join([PPAL,JUL,ME,BSVC]),",".join([GIO,AGRO2,CASC,NBAR,ITRG,CSIMP,WES,TFA])),
 (B4,"RvwAAA=","Re: "+S_G276,GRAZ,"2026-10-07T17:40:22Z",",".join([GETH,JUL,ME,BSVC,AGRO,PPAL,WES]),",".join([GIO,CASC,AGRO2,ITRG,CSIMP,TFA])),
 (B4,"RvxAAA=",S_G276,GRAZ,"2026-10-07T17:40:16Z",",".join([GETH,JUL,ME,BSVC]),",".join([GIO,CASC,AGRO2,PPAL,ITRG,CSIMP,WES,TFA])),
 (None,FTX+"PNoAAA=",S_PR08,RAY,"2026-10-07T11:55:55Z","operacional@wltransportes-am.com.br,willians@wltransportes-am.com.br,kellen.silva@wltransportes-am.com.br,intermodalmanaus@mercosul-line.com.br,Thiago.Negreiros@mercosul-line.com.br,transporteswl@hotmail.com",""),
 (None,FTX+"anpJD8AAA=",S_RRR,RPAN,"2026-10-07T05:43:22Z","roselma@rrtransporte.com",DOCT),
 (None,FTX+"PGkAAA=",S_PR07,RAY,"2026-10-06T17:32:06Z","roselma@rrtransporte.com,operacional@rrtransporte.com,intermodalmanaus@mercosul-line.com.br,jhonnespinheiro@rrtransporte.com,Thiago.Negreiros@mercosul-line.com.br",""),
 (B4,"Rw6AAA=",S_CHG,JUL,"2026-10-05T14:15:26Z",",".join([EMAT]+CHGLIST),",".join([TEALL,ME,BSVC])),
 (None,FTX+"OyZAAA=","RES: "+S_LD,"MAO.AARAUJO@ccis-network.com","2026-10-05T13:15:38Z",",".join([RAY,"Thiago.Negreiros@mercosul-line.com.br","bma.pwelferinger@cma-cgm.com","ssz.rcamacho@cma-cgm.com","cristhian.silva@mercosul-line.com.br","anacarolina.esteves@mercosul-line.com.br"]),",".join(["multimodal.norte@mercosul-line.com.br","mao.lgaia@ccis-network.com","EXT.TBARBOZA@ccis-network.com"])),
 (None,FTX+"OzOAAA=",S_LD,RAY,"2026-10-05T11:36:05Z",",".join(["MAO.AARAUJO@ccis-network.com","Thiago.Negreiros@mercosul-line.com.br","bma.pwelferinger@cma-cgm.com","ssz.rcamacho@cma-cgm.com","cristhian.silva@mercosul-line.com.br","anacarolina.esteves@mercosul-line.com.br"]),"multimodal.norte@mercosul-line.com.br"),
 (B4,"RxFAAA=",S_CHG,EMAT,"2026-10-02T23:40:37Z",",".join([JUL]+CHGLIST),",".join([TEALL,ME,BSVC])),
 (B4,"RxLAAA=",S_CHG,JUL,"2026-10-02T20:05:35Z",",".join(CHGLIST[:13]+[EMAT]+CHGLIST[13:]),",".join([TEALL,ME])),
]
out="/workspace/analise_coleta/raw/cargill_oct.jsonl"
have=set()
for l in open(out): have.add(json.loads(l)["id"])
new=0
with open(out,"a") as f:
    for r in rows:
        idb,suf,s,fr,d,to,cc=r
        id_=suf if idb is None else idb+suf
        if id_ in have: continue
        f.write(json.dumps({"id":id_,"folder":"main","date":d,"subject":s,"from":fr,"to":to,"cc":cc},ensure_ascii=False)+"\n")
        have.add(id_); new+=1
print("new:",new,"total:",len(have))
import collections as C
c=C.Counter(json.loads(l)["date"][:10] for l in open(out))
print("by day:",sorted(c.items()))
