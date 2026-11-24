import json
IDB1="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
IDB2="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
M1="bma.road-southeast@cma-cgm.com"; M2="bma.road-south@cma-cgm.com"
JUL="Juliane.MARQUES@mercosul-line.com.br"; THA="thaina.santos@mercosul-line.com.br"
LIB="BMA.LIBERACAO@cma-cgm.com"
ZAP_TO="reporte2@berneck.com.br,exportacao.op@zappellini.com.br,op.sc@zappellini.com.br,exportacao2@zappellini.com.br,exportacao@zappellini.com.br,exp-berneck@nelsonheusi.com,exportacao3@zappellini.com.br,exportacao1@zappellini.com.br,exportacao4@zappellini.com.br,"+M1+",atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br"
ZAP_CC="expo.docs@berneck.com.br,carregamentome@berneck.com.br,expedicaopaineislages@berneck.com.br"
ZAP_CCN="nfexpo_curitibanos@berneck.com.br"
MTZ_TO=JUL+",export.sc@zappellini.com.br,contabilidade1@zappellini.com.br,custos@zappellini.com.br"
LAC_TO=LIB+",gpinheiro@gport.com.br,alesandro.domingos@santosbrasil.com.br,jose@pontualagenciamentos.com.br,emmyle.silva@lechman.com.br,leticia.bianchini@lechman.com.br,depot.tci@santosbrasil.com.br"
LAC_CC=M1+",expo.berneck@gport.com.br"
TCI="relacionamento.tci@santosbrasil.com.br"; GTO="gtosta@berneck.com.br"
AAC_LIST="reporte2@berneck.com.br,exportacao.op@zappellini.com.br,op.sc@zappellini.com.br,exportacao2@zappellini.com.br,exportacao@zappellini.com.br,exportacao3@zappellini.com.br,marcos@macomissaria.com.br,m.a.servicos@uol.com.br,atendimento@macomissaria.com.br,exportacao1@zappellini.com.br,exportacao4@zappellini.com.br,"+M1+",atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br,aaraujo@berneck.com.br,carregamentome@berneck.com.br,gtosta@berneck.com.br,fdaldegan@berneck.com.br,mhrocha@berneck.com.br,jfontoura@berneck.com.br,rsantos@berneck.com.br"
S_MM="[CMA CCGM] PROGRAMA\u00c7\u00c3O MULTIMODAL | BERNECK x ZAPPELLINI | WK 41"
S_LAC2202="SOLICITA\u00c7\u00c3O DE LACRE EXTRA SSZ1852202 - BERNECK - 313171 - ITAPO\u00c1"
S_LAC2856="SOLICITA\u00c7\u00c3O DE LACRE EXTRA SSZ1852856 - BERNECK - 309908 A- IMBITUBA"
S_VAZ="RE: [CMA CGM] BRIBB | Libera\u00e7\u00e3o de vazio - BERNECK | SSZ1854646 (LR)"
S_VAZ0="[CMA CGM] BRIBB | Libera\u00e7\u00e3o de vazio - BERNECK | SSZ1854646"
rows=[
 (IDB1,"P67AAA=","AJUSTE TRANSPORT ORDER TEMU6344668 - BERNECK","SSZ.TMARQUES@cma-cgm.com","2026-10-20T13:43:16Z",M2,THA),
 (IDB1,"RsUAAA=","RES: "+S_MM,"exportacao5@zappellini.com.br","2026-10-15T15:55:06Z",MTZ_TO,M1),
 (IDB1,"RsXAAA=","[Santos Brasil] - Ticket: 1254029 - Re: Solicita\u00e7\u00e3o de carregamento - OV# 314721 A",TCI,"2026-10-15T14:52:35Z",GTO+","+ZAP_TO,ZAP_CC),
 (IDB1,"RsYAAA=","RES: [Santos Brasil] - Ticket: 1254029 - Re: Solicita\u00e7\u00e3o de carregamento - OV# 314721 A","exportacao2@zappellini.com.br","2026-10-15T14:32:32Z",TCI+","+GTO,ZAP_CC),
 (IDB1,"RsZAAA=","[Santos Brasil] - Ticket: 1254029 - Re: Solicita\u00e7\u00e3o de carregamento - OV# 314721 A",TCI,"2026-10-15T14:07:39Z",GTO+",exportacao.op@zappellini.com.br,exportacao@zappellini.com.br,exportacao2@zappellini.com.br,exp-berneck@nelsonheusi.com,expedicaopaineislages@berneck.com.br,expo.docs@berneck.com.br,op.sc@zappellini.com.br,carregamentome@berneck.com.br,"+M1+",exportacao1@zappellini.com.br,exportacao3@zappellini.com.br,reporte2@berneck.com.br,exportacao4@zappellini.com.br,atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br",ZAP_CC),
 (IDB1,"RsaAAA=","Solicita\u00e7\u00e3o de carregamento - OV# 314721 A",GTO,"2026-10-15T13:52:26Z","exportacao2@zappellini.com.br,reporte2@berneck.com.br,exportacao.op@zappellini.com.br,op.sc@zappellini.com.br,exportacao@zappellini.com.br,exp-berneck@nelsonheusi.com,exportacao3@zappellini.com.br,exportacao1@zappellini.com.br,exportacao4@zappellini.com.br,"+M1+",atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br,"+TCI,ZAP_CC),
 (IDB1,"Rs3AAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 314721 A","dperico@berneck.com.br","2026-10-14T12:48:33Z",ZAP_TO,ZAP_CC),
 (IDB1,"Rs5AAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 313402 A","dperico@berneck.com.br","2026-10-14T12:03:07Z",ZAP_TO,ZAP_CC+","+ZAP_CCN),
 (IDB1,"Rs9AAA=","RES: "+S_MM,"exportacao5@zappellini.com.br","2026-10-14T00:55:20Z",MTZ_TO,M1),
 (IDB1,"RtfAAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 313402 A","exportacao2@zappellini.com.br","2026-10-13T13:59:54Z",ZAP_TO,ZAP_CC+","+ZAP_CCN),
 (IDB1,"RtgAAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 314721 A","exportacao2@zappellini.com.br","2026-10-13T13:57:42Z",ZAP_TO,ZAP_CC),
 (IDB1,"RthAAA=","Ord. Frete 0300131422 - Retirar em Curitibanos","reporte2@berneck.com.br","2026-10-13T13:30:42Z","logistica@berneck.com.br",M1+",HER.ESANCHEZ@cma-cgm.com"),
 (IDB1,"RtiAAA=","[BERNECK - Portal das transportadoras] Novo Cadastro","nao_responda@berneck.com.br","2026-10-13T13:21:47Z",M1,""),
 (IDB1,"Rt0AAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 313068 A","dperico@berneck.com.br","2026-10-13T11:33:33Z",ZAP_TO,ZAP_CC),
 (IDB1,"Rt1AAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 310632","dperico@berneck.com.br","2026-10-13T11:30:44Z",ZAP_TO,ZAP_CC),
 (IDB1,"RuBAAA=","RES: "+S_MM,"exportacao5@zappellini.com.br","2026-10-10T01:01:28Z",MTZ_TO,M1),
 (IDB1,"RuCAAA=","RES: "+S_MM,"exportacao5@zappellini.com.br","2026-10-09T22:27:21Z",MTZ_TO,M1),
 (IDB1,"RuHAAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 310594","dperico@berneck.com.br","2026-10-09T21:02:17Z",ZAP_TO,ZAP_CC),
 (IDB1,"RueAAA=","RE: SOLICITA\u00c7\u00c3O DE LACRE EXTRA SSZ1852202 - BERNECK - 313171 - ITAPO\u00c1 (LR)","emmyle.silva@lechman.com.br","2026-10-09T17:19:31Z",LAC_TO+",lechmanioa@lechman.com.br",LAC_CC+",gisiane_f_ramina@hotmail.com"),
 (IDB1,"RufAAA=","RE: SOLICITA\u00c7\u00c3O DE LACRE EXTRA SSZ1852100 - BERNECK - OV 313560 - ITAPO\u00c1 (LR)","emmyle.silva@lechman.com.br","2026-10-09T17:15:28Z",LAC_TO+",lechmanioa@lechman.com.br",LAC_CC+",gisiane_f_ramina@hotmail.com"),
 (IDB1,"RuiAAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 309294 A","dperico@berneck.com.br","2026-10-09T16:45:53Z",ZAP_TO.replace("exportacao@zappellini.com.br,","exportacao@zappellini.com.br,exportacao3@zappellini.com.br,marcos@macomissaria.com.br,m.a.servicos@uol.com.br,atendimento@macomissaria.com.br,",1),ZAP_CC),
 (IDB1,"RutAAA=","Cancelar: Solicita\u00e7\u00e3o de carregamento - OV# 309294 A","aacarvalho@berneck.com.br","2026-10-09T14:36:51Z",AAC_LIST,ZAP_CC),
 (IDB1,"RuuAAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 309294 A","aacarvalho@berneck.com.br","2026-10-09T14:33:30Z",AAC_LIST,ZAP_CC),
 (IDB1,"RuvAAA=","Cancelar: Solicita\u00e7\u00e3o de carregamento - OV# 309294 A","aacarvalho@berneck.com.br","2026-10-09T14:30:52Z",AAC_LIST,ZAP_CC),
 (IDB1,"RuwAAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 309294 A","aacarvalho@berneck.com.br","2026-10-09T14:30:06Z",AAC_LIST,ZAP_CC),
 (IDB1,"RuxAAA=","Cancelar: Solicita\u00e7\u00e3o de carregamento - OV# 309294 A","aacarvalho@berneck.com.br","2026-10-09T14:26:56Z",AAC_LIST,ZAP_CC),
 (IDB1,"RuyAAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 309294 A","aacarvalho@berneck.com.br","2026-10-09T14:25:51Z",AAC_LIST,ZAP_CC),
 (IDB1,"RuzAAA=","RE: "+S_MM,JUL,"2026-10-09T13:49:54Z",MTZ_TO,M1),
 (IDB1,"Ru0AAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 313068 A","exportacao@zappellini.com.br","2026-10-09T12:38:15Z","reporte2@berneck.com.br,exportacao.op@zappellini.com.br,op.sc@zappellini.com.br,exportacao2@zappellini.com.br,exp-berneck@nelsonheusi.com,exportacao3@zappellini.com.br,exportacao1@zappellini.com.br,exportacao4@zappellini.com.br,"+M1+",atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br",ZAP_CC),
 (IDB1,"Ru1AAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 310594","exportacao4@zappellini.com.br","2026-10-09T12:33:32Z",ZAP_TO.replace(",exportacao4@zappellini.com.br,",",",1),ZAP_CC),
 (IDB1,"Ru3AAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 313296","dperico@berneck.com.br","2026-10-09T11:32:55Z",ZAP_TO,ZAP_CC+","+ZAP_CCN),
 (IDB1,"Ru4AAA=","RES: "+S_MM,"exportacao5@zappellini.com.br","2026-10-09T00:49:56Z",MTZ_TO+","+M1,M1),
 (IDB1,"Ru5AAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 309294 A","exportacao5@zappellini.com.br","2026-10-08T20:54:05Z",ZAP_TO,ZAP_CC),
 (IDB1,"RvAAAA=","RE: SOLICITA\u00c7\u00c3O DE LACRE EXTRA SSZ1852202 - BERNECK - 313171 - ITAPO\u00c1 (LR)","emmyle.silva@lechman.com.br","2026-10-08T20:00:46Z",LAC_TO+",lechmanioa@lechman.com.br",LAC_CC+",gisiane_f_ramina@hotmail.com"),
 (IDB1,"RvBAAA=","RE: SOLICITA\u00c7\u00c3O DE LACRE EXTRA SSZ1852202 - BERNECK - 313171 - ITAPO\u00c1 (LR)",LIB,"2026-10-08T19:44:41Z",LAC_TO+",emmyle.silva@lechman.com.br,lechmanioa@lechman.com.br",LAC_CC+",gisiane_f_ramina@hotmail.com"),
 (IDB1,"RvEAAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 313491 A","dperico@berneck.com.br","2026-10-08T19:00:12Z",ZAP_TO,ZAP_CC+","+ZAP_CCN),
 (IDB1,"RvGAAA=",S_LAC2202,"gpinheiro@gport.com.br","2026-10-08T18:40:27Z",LAC_TO,LAC_CC+",gisiane_f_ramina@hotmail.com"),
 (IDB1,"RvLAAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 313296","exportacao@zappellini.com.br","2026-10-08T16:54:03Z","reporte2@berneck.com.br,exportacao.op@zappellini.com.br,op.sc@zappellini.com.br,exportacao2@zappellini.com.br,exp-berneck@nelsonheusi.com,exportacao3@zappellini.com.br,exportacao1@zappellini.com.br,exportacao4@zappellini.com.br,"+M1+",atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br",ZAP_CC+","+ZAP_CCN),
 (IDB1,"RvWAAA=","RES: "+S_MM,"exportacao5@zappellini.com.br","2026-10-08T01:13:16Z",MTZ_TO+","+M1,M1),
 (IDB1,"RvZAAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 310685 A","dperico@berneck.com.br","2026-10-07T21:04:30Z",ZAP_TO,ZAP_CC+","+ZAP_CCN),
 (IDB2,"RvdAAA=","RE: SOLICITA\u00c7\u00c3O DE LACRE EXTRA SSZ1852856 - BERNECK - 309908 A- IMBITUBA(LS)","Patrick.Campos@santosbrasil.com.br","2026-10-07T19:58:50Z",LAC_TO,LAC_CC),
 (IDB1,"RvlAAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 313491 A","exportacao2@zappellini.com.br","2026-10-07T19:11:54Z",GTO+",exportacao4@zappellini.com.br,reporte2@berneck.com.br,exportacao.op@zappellini.com.br,op.sc@zappellini.com.br,exportacao@zappellini.com.br,exp-berneck@nelsonheusi.com,exportacao3@zappellini.com.br,exportacao1@zappellini.com.br,"+M1+",atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br,bra.cgr@cma-cgm.com",ZAP_CC+","+ZAP_CCN+","+M1),
 (IDB1,"RvqAAA=","RE: SOLICITA\u00c7\u00c3O DE LACRE EXTRA SSZ1852856 - BERNECK - 309908 A- IMBITUBA(LS)",LIB,"2026-10-07T18:16:47Z",LAC_TO,LAC_CC+",jose@pontualagenciamentos.com.br"),
 (IDB1,"RvvAAA=","SOLICITA\u00c7\u00c3O DE LACRE EXTRA SSZ1852856 - BERNECK - 309908 A- IMBITUBA","gpinheiro@gport.com.br","2026-10-07T17:42:24Z","alesandro.domingos@santosbrasil.com.br,"+LIB+",jose@pontualagenciamentos.com.br,emmyle.silva@lechman.com.br,leticia.bianchini@lechman.com.br,depot.tci@santosbrasil.com.br",LAC_CC+",jose@pontualagenciamentos.com.br"),
 (IDB1,"Rv6AAA=","RE: "+S_MM,JUL,"2026-10-07T14:55:12Z",MTZ_TO,M1),
 (IDB2,"POWAAA=","RES: "+S_VAZ,"jenifer.fraga@manufrio.com.br","2026-10-07T14:50:52Z",LIB+","+JUL+",gate@manufrio.com.br",M2),
 (IDB2,"POZAAA=","RE: "+S_VAZ.replace("(LR)","",1) if False else "RE: "+S_VAZ,LIB,"2026-10-07T14:44:51Z",JUL+",gate@manufrio.com.br",M2),
 (IDB2,"PMPAAA=",S_VAZ0,JUL,"2026-10-07T13:42:40Z",LIB,M2),
 (IDB1,"RwBAAA=","RE: RES: Solicita\u00e7\u00e3o de carregamento - OV# 313491 A","bra.cgr@cma-cgm.com","2026-10-07T13:18:48Z",GTO,"exportacao3@zappellini.com.br,"+ZAP_CCN+",exportacao4@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao@zappellini.com.br,exp-berneck@nelsonheusi.com,"+ZAP_CC+",exportacao1@zappellini.com.br,reporte2@berneck.com.br,atendimento@zappellini.com.br,exportacao.op@zappellini.com.br,exportacao2@zappellini.com.br,"+M1+",exportacao5@zappellini.com.br,ssz.fsantana@cma-cgm.com"),
 (IDB1,"RwCAAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 313491 A",GTO,"2026-10-07T13:16:14Z","exportacao4@zappellini.com.br,reporte2@berneck.com.br,exportacao.op@zappellini.com.br,op.sc@zappellini.com.br,exportacao2@zappellini.com.br,exportacao@zappellini.com.br,exp-berneck@nelsonheusi.com,exportacao3@zappellini.com.br,exportacao1@zappellini.com.br,"+M1+",atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br,bra.cgr@cma-cgm.com",ZAP_CC+","+ZAP_CCN+","+M1),
 (IDB1,"RwHAAA=","RES: "+S_MM,"exportacao5@zappellini.com.br","2026-10-07T01:06:43Z",MTZ_TO,M1),
]
rows=[(a,b,c,d,e,f,g) for a,b,c,d,e,f,g in rows]
out="/workspace/analise_coleta/raw/berneck_all.jsonl"
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
import collections as C
c=C.Counter(json.loads(l)["date"][:10] for l in open(out))
print("by day:",sorted(c.items()))
