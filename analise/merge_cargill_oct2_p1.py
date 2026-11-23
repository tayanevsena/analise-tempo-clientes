import json, collections
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ME="bma.road-southeast@cma-cgm.com"
JUL="Juliane.MARQUES@mercosul-line.com.br"; THA="thaina.santos@mercosul-line.com.br"
GRAZ="graziela.braga@pibernat.com.br"; PPAL="Paula_Palazzo@cargill.com"; GETH="gethelp@cargill.com"
GIO="Giovana_Santos1@cargill.com"; WES="Wesley_Delisolasantos@cargill.com"; TFA="Tiago_Faria@cargill.com"
CASC="Casc_Impo@cargill.com"; CSIMP="-CASC-GTOC-IMP@exch.cargill.com"; ITRG="impo.cargill.rgd@pibernat.com.br"; BSVC="bra.service@cma-cgm.com"
AGRO2="-AGROQUIMICOS-CROPINPUT@cargill.com"; NBAR="Natalia_Barreto@cargill.com"; CLF="Clara_Fernanda@cargill.com"; JAC="Jaciara_Marquesdesouza@cargill.com"
FINCUST="-finance-customs-cargillonly@cargill.com"; DEV="bma.log-devolucao@cma-cgm.com"
UNI=",".join(["atendimentoaocliente.sts@uni.com.br","operacional.sts@uni.com.br"])
CC_UNI2=",".join(["tatiana.ranieri@uni.com.br","laiza.may@uni.com.br","katny.barros@uni.com.br","helio@uni.com.br","cac@unitradinglog.com.br","faturamento.sts@uni.com.br",ME,"valerio.carvalho@uni.com.br","giovanna.reis@unitradinglog.com.br"])
S_IMP_374="[CMA CCGM] BRSSZ | PROGRAMA\u00c7\u00c3O IMPORTA\u00e7\u00c3O | CARGILL x UNITRADING | CHN3831374".replace("IMPORTA\u00e7\u00c3O","IMPORTA\u00c7\u00c3O")
S_IMP_374="[CMA CCGM] BRSSZ | PROGRAMA\u00c7\u00c3O IMPORTA\u00c7\u00c3O | CARGILL x UNITRADING | CHN3831374"
S_YM="LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001903376-2 | CHLORFENAPYR - RIO VERDE | CASC0141/26, PO 521715Z366 | YN2026WM152-2 (CHN3839530)"
S_G275="RE: LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001889833-6 | DSA| CASC0137/26, PO 521715Z359 | GLIFOSATO NGC - RIO VERDE | GHYD260275 (CHN3831378) *CARGA DSA*"
S_G276="RE: LIBERA\u00c7\u00c3o PARA TRANSPORTE | 26BR0001879016-0 | DSA | CASC0139/26, PO 521715Z361 | GLIFOSATO NGC - RIO VERDE | GHYD260276 (CHN3831443)".replace("TRANSPORTE | 26","TRANSPORTE | 26").replace("\u00e7\u00e3o PARA","\u00c7\u00c3O PARA")
S_G276="RE: LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001879016-0 | DSA | CASC0139/26, PO 521715Z361 | GLIFOSATO NGC - RIO VERDE | GHYD260276 (CHN3831443)"
RPA1="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAYtkauwPWFAAA="
RPA2="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAYtkauwPV1AAA="
S_RPA="ENVIO DOCS DE ENTREGA - COOPERATIVA DE TRANSPORTE DE CARGAS DO ESTADO DE SANTA CATAR"
S_DEV="BRSSZ | DEVOLU\u00c7\u00c3O IMPORTA\u00c7\u00c3O | CARGILL | CHN3831374"
S_DEV0=" "+S_DEV
S_G277="RE: LIBERA\u00c7\u00c3O PARA TRANSPORTE | 26BR0001896221-2 | DSA | CASC0138/26, PO 521715Z360 | GLIFOSATO NGC - DANFE SOLICITADA| GHYD260277 (CHN3831374)"
rows=[
 (B4,"RsOAAA=","SOLICITA\u00c7\u00c3O // ESTADIA // CMA CGM //  CARGIL - BOOKING: 26BR00018962212 - CHN3831374","fellipe.xavier@unitradinglog.com.br","2026-10-15T19:10:59Z",JUL,CC_UNI2),
 (None,RPA1,S_RPA,"rpa_no_reply@mercosul-line.com.br","2026-10-15T06:25:47Z","almakio@coopercarga.com.br,portomanaus@coopercarga.com.br","doc.norte@mercosul-line.com.br"),
 (B4,"RspAAA=",S_YM,GRAZ,"2026-10-14T18:31:12Z",",".join([PPAL,ME,BSVC,JUL]),",".join([GIO,AGRO2,CASC,ITRG,CSIMP,WES,TFA,FINCUST,NBAR,CLF,JAC])),
 (None,RPA2,S_RPA,"rpa_no_reply@mercosul-line.com.br","2026-10-14T16:07:46Z","almakio@coopercarga.com.br,portomanaus@coopercarga.com.br","doc.norte@mercosul-line.com.br"),
 (B4,"Rs6AAA=",S_IMP_374,"giovanna.reis@unitradinglog.com.br","2026-10-14T11:51:12Z",",".join([JUL,"atendimentoaocliente.sts@uni.com.br"]),",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RtEAAA=",S_G275,JUL,"2026-10-13T20:53:34Z",",".join([GRAZ,"GetHelp@cargill.com",PPAL,ME,BSVC,GIO]),",".join([CASC,AGRO2,ITRG,CSIMP,WES,TFA])),
 (B4,"RtFAAA=","RE: "+S_IMP_374,JUL,"2026-10-13T20:52:08Z",",".join(["giovanna.reis@unitradinglog.com.br","atendimentoaocliente.sts@uni.com.br"]),",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RtVAAA=",S_G276,THA,"2026-10-13T18:31:45Z",",".join([JUL,GRAZ,"GetHelp@cargill.com",ME,BSVC,"AGROQUIMICOS-CROPINPUT@cargill.com",PPAL,WES]),",".join([GIO,CASC,AGRO2,ITRG,CSIMP,TFA])),
 (B4,"RtaAAA=",S_DEV0,THA,"2026-10-13T15:01:20Z",",".join([DEV,JUL]),ME),
 (B4,"RtbAAA="," "+S_IMP_374,THA,"2026-10-13T14:53:05Z",",".join(["giovanna.reis@unitradinglog.com.br",JUL,"atendimentoaocliente.sts@uni.com.br"]),",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RtdAAA=","RES: "+S_DEV,DEV,"2026-10-13T14:07:17Z",JUL,ME),
 (B4,"RteAAA=",S_IMP_374,"giovanna.reis@unitradinglog.com.br","2026-10-13T14:02:27Z",",".join([JUL,"atendimentoaocliente.sts@uni.com.br"]),",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RtmAAA=",S_DEV,JUL,"2026-10-13T12:45:05Z",DEV,ME),
 (B4,"RtzAAA=",S_IMP_374,"giovanna.reis@unitradinglog.com.br","2026-10-13T11:42:06Z",",".join([JUL,"atendimentoaocliente.sts@uni.com.br"]),",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RuLAAA=",S_G277,JUL,"2026-10-09T19:36:05Z",",".join([GRAZ,PPAL,ME,BSVC]),",".join([GIO,AGRO2,CASC,NBAR,ITRG,CSIMP,WES,TFA])),
 (B4,"RuMAAA=","RE: "+S_IMP_374,JUL,"2026-10-09T19:31:50Z",",".join(["giovanna.reis@unitradinglog.com.br","atendimentoaocliente.sts@uni.com.br"]),",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RuVAAA=",S_IMP_374,"giovanna.reis@unitradinglog.com.br","2026-10-09T19:10:50Z",",".join([JUL,"atendimentoaocliente.sts@uni.com.br"]),",".join([ME,"operacional.sts@uni.com.br"])),
 (B4,"RujAAA=",S_G276,JUL,"2026-10-09T16:04:50Z",",".join([GRAZ,"GetHelp@cargill.com",ME,BSVC,"AGROQUIMICOS-CROPINPUT@cargill.com",PPAL,WES]),",".join([GIO,CASC,AGRO2,ITRG,CSIMP,TFA])),
 (B4,"RulAAA=",S_G275,JUL,"2026-10-09T16:02:30Z",",".join([GRAZ,"GetHelp@cargill.com",PPAL,ME,BSVC]),",".join([GIO,CASC,AGRO2,ITRG,CSIMP,WES,TFA])),
 (B4,"RvIAAA=",S_IMP_374,JUL,"2026-10-08T17:46:41Z","atendimentoaocliente.sts@uni.com.br",",".join([ME,"operacional.sts@uni.com.br"])),
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
