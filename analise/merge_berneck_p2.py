import json
IDB1="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
IDB2="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
M1="bma.road-southeast@cma-cgm.com"
JUL="Juliane.MARQUES@mercosul-line.com.br"
LIB="BMA.LIBERACAO@cma-cgm.com"
ZAP2="exportacao2@zappellini.com.br"; GTO="gtosta@berneck.com.br"; REP2="reporte2@berneck.com.br"
ZAP_BASE="exportacao.op@zappellini.com.br,op.sc@zappellini.com.br,exportacao@zappellini.com.br,exp-berneck@nelsonheusi.com,exportacao3@zappellini.com.br,exportacao1@zappellini.com.br,exportacao4@zappellini.com.br"
ZAP_CC="expo.docs@berneck.com.br,carregamentome@berneck.com.br,expedicaopaineislages@berneck.com.br"
ZAP_CCN="nfexpo_curitibanos@berneck.com.br"
MTZ_TO=JUL+",export.sc@zappellini.com.br,contabilidade1@zappellini.com.br,custos@zappellini.com.br"
MM="RES: [CMA CCGM] PROGRAMA\u00c7\u00c3O MULTIMODAL | BERNECK x ZAPPELLINI | WK 41"
S_LAC100="RE: SOLICITA\u00c7\u00c3O DE LACRE EXTRA SSZ1852100 - BERNECK - OV 313560 - ITAPO\u00c1 (LR) "
V="RE: [CMA CGM] BRIBB | Libera\u00e7\u00e3o de vazio - BERNECK | SSZ1852894 (LR)"
V2="RE: [CMA CGM] BRIBB | Libera\u00e7\u00e3o de vazio - BERNECK | SSZ1853927 (LS)"
V3="RE: [CMA CGM] BRIBB | Libera\u00e7\u00e3o de vazio - BERNECK | SSZ1853810 - SSZ1853973 (LS)"
JEN="jenifer.fraga@manufrio.com.br"; GATE="gate@manufrio.com.br"; CTN="controle.nvg@lechman.com.br"; DPVN="depot.nvg@lechman.com.br"; SUE="sueli.silva@lechman.com.br"; PAT="patrick.campos@santosbrasil.com.br"; CBAT="SSZ.CBATISTA@cma-cgm.com"
rows=[
 (IDB1,"RwIAAA=",MM,"exportacao5@zappellini.com.br","2026-10-07T01:05:49Z",MTZ_TO+","+M1,""),
 (IDB1,"RwMAAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 313290 A","dperico@berneck.com.br","2026-10-06T20:17:06Z",REP2+","+ZAP2+","+ZAP_BASE+","+M1+",atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br",ZAP_CC),
 (IDB1,"RwOAAA=",S_LAC100,LIB,"2026-10-06T19:00:16Z","gpinheiro@gport.com.br,alesandro.domingos@santosbrasil.com.br,jose@pontualagenciamentos.com.br,emmyle.silva@lechman.com.br,leticia.bianchini@lechman.com.br,depot.tci@santosbrasil.com.br,lechmanioa@lechman.com.br",M1+",expo.berneck@gport.com.br,gisiane_f_ramina@hotmail.com"),
 (IDB1,"RwSAAA=","Solicita\u00e7\u00e3o de carregamento - OV# 314721 A",REP2,"2026-10-06T17:45:45Z",ZAP_BASE+","+M1+",atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br",ZAP_CC),
 (IDB1,"RwbAAA=","SOLICITA\u00c7\u00c3O DE LACRE EXTRA SSZ1852100 - BERNECK - OV 313560 - ITAPO\u00c1","gpinheiro@gport.com.br","2026-10-06T14:42:10Z","alesandro.domingos@santosbrasil.com.br,"+LIB+",jose@pontualagenciamentos.com.br,emmyle.silva@lechman.com.br,leticia.bianchini@lechman.com.br,depot.tci@santosbrasil.com.br",M1+",expo.berneck@gport.com.br,gisiane_f_ramina@hotmail.com"),
 (IDB1,"RweAAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 313290 A",ZAP2,"2026-10-06T12:55:52Z",REP2+","+ZAP_BASE+","+M1+",atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br",ZAP_CC),
 (IDB1,"RwfAAA=","RE: [CMA CCGM] PROGRAMA\u00c7\u00c3O MULTIMODAL | BERNECK x ZAPPELLINI | WK 41",JUL,"2026-10-06T12:33:18Z","exportacao5@zappellini.com.br,export.sc@zappellini.com.br,contabilidade1@zappellini.com.br,custos@zappellini.com.br",M1),
 (IDB1,"RwhAAA=",MM,"exportacao5@zappellini.com.br","2026-10-05T22:29:55Z",MTZ_TO,M1),
 (IDB1,"RwmAAA=","RES: [CMA CGM] BRIBB | Libera\u00e7\u00e3o de vazio - BERNECK | SSZ1852142 (LS)",JEN,"2026-10-05T18:44:57Z",LIB+","+JUL+","+GATE,M1),
 (IDB1,"RwoAAA=","RE: [CMA CGM] BRIBB | Libera\u00e7\u00e3o de vazio - BERNECK | SSZ1852142 (LS)",LIB,"2026-10-05T18:40:11Z",JUL+","+JEN+","+GATE,M1),
 (IDB1,"RwxAAA=","[CMA CGM] BRIBB | Libera\u00e7\u00e3o de vazio - BERNECK | SSZ1852142",JUL,"2026-10-05T17:32:51Z",LIB,M1),
 (IDB1,"Rw1AAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 313491 A","exportacao4@zappellini.com.br","2026-10-05T17:08:43Z",REP2+",exportacao.op@zappellini.com.br,op.sc@zappellini.com.br,"+ZAP2+",exportacao@zappellini.com.br,exp-berneck@nelsonheusi.com,exportacao3@zappellini.com.br,exportacao1@zappellini.com.br,"+M1+",atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br",ZAP_CC+","+ZAP_CCN),
 (IDB1,"Rw2AAA=","Solicita\u00e7\u00e3o de carregamento - OV# 313491 A",REP2,"2026-10-05T16:45:49Z","exportacao.op@zappellini.com.br,op.sc@zappellini.com.br,"+ZAP2+",exportacao@zappellini.com.br,exp-berneck@nelsonheusi.com,exportacao3@zappellini.com.br,exportacao1@zappellini.com.br,exportacao4@zappellini.com.br,"+M1+",atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br",ZAP_CC+","+ZAP_CCN),
 (IDB1,"RxCAAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 305516 A",ZAP2,"2026-10-05T11:46:49Z",REP2+",exportacao.op@zappellini.com.br,op.sc@zappellini.com.br,exportacao@zappellini.com.br,exp-berneck@nelsonheusi.com,exportacao3@zappellini.com.br,exportacao1@zappellini.com.br,exportacao4@zappellini.com.br,atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br,"+M1,ZAP_CC),
 (IDB1,"RxGAAA=","RE: Solicita\u00e7\u00e3o de carregamento - OV# 305516 A",SUE,"2026-10-02T21:29:02Z",ZAP2+","+JUL+","+GTO+","+REP2+","+ZAP_BASE+",atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br,"+M1+","+CTN+","+DPVN,ZAP_CC),
 (IDB1,"RxHAAA=","RE: [CMA CCGM] PROGRAMA\u00c7\u00c3O MULTIMODAL | BERNECK x ZAPPELLINI | WK 41",JUL,"2026-10-02T20:55:54Z","export.sc@zappellini.com.br,contabilidade1@zappellini.com.br,custos@zappellini.com.br",M1),
 (IDB1,"RxIAAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 305516 A",ZAP2,"2026-10-02T20:15:59Z",JUL+","+GTO+","+REP2+",exportacao.op@zappellini.com.br,op.sc@zappellini.com.br,exportacao@zappellini.com.br,exp-berneck@nelsonheusi.com,exportacao3@zappellini.com.br,exportacao1@zappellini.com.br,exportacao4@zappellini.com.br,atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br,"+M1+","+SUE+","+CTN+","+DPVN,ZAP_CC),
 (IDB1,"RxRAAA=","RE: [CMA CGM] BRIBB | Libera\u00e7\u00e3o de vazio - BERNECK | SSZ1852894 (LR)",JUL,"2026-10-02T19:39:46Z",CTN+","+CBAT+","+DPVN,M1+","+LIB),
 (IDB1,"RxVAAA=","RES: "+V,CTN,"2026-10-02T17:57:57Z",CBAT+","+JUL+","+DPVN,M1+","+LIB),
 (IDB1,"RxWAAA=","RES: "+V,CBAT,"2026-10-02T17:53:13Z",JUL+","+DPVN,M1+","+LIB),
 (IDB1,"RxXAAA=","RES: "+V,JEN,"2026-10-02T17:42:15Z",LIB+","+JUL+","+GATE,M1),
 (IDB1,"RxYAAA=","RE: "+V,LIB,"2026-10-02T17:29:39Z",JUL+","+JEN+","+GATE,M1),
 (IDB1,"RxZAAA=","RE: "+V2,LIB,"2026-10-02T17:28:11Z",JUL+","+SUE+","+DPVN+",depot.tci@santosbrasil.com.br,"+PAT+","+JEN+","+GATE,M1),
 (IDB1,"RxbAAA=","RE: "+V,LIB,"2026-10-02T15:07:00Z",JUL+",depot.tci@santosbrasil.com.br,"+CTN,M1),
 (IDB1,"RxeAAA=","RES: "+V2,CTN,"2026-10-02T14:42:44Z",LIB+","+JUL+","+SUE+","+DPVN+",depot.tci@santosbrasil.com.br,"+PAT,M1),
 (IDB2,"O-5AAA=","RE: [CMA CGM] BRIBB | Libera\u00e7\u00e3o de vazio - BERNECK | SSZ1853810 - SSZ1853973 (LS)",LIB,"2026-10-02T14:34:39Z",JUL,M1),
 (IDB1,"RxgAAA=","RE: "+V2,LIB,"2026-10-02T14:31:17Z",JUL+","+SUE+","+DPVN+",depot.tci@santosbrasil.com.br,"+PAT,M1),
 (IDB1,"RxiAAA=","RE: [CMA CGM] BRIBB | Libera\u00e7\u00e3o de vazio - BERNECK | SSZ1852894",LIB,"2026-10-02T13:40:43Z",JUL+",depot.tci@santosbrasil.com.br",M1),
 (IDB1,"RxkAAA=",V3,JUL,"2026-10-02T12:59:06Z",LIB,M1),
 (IDB1,"RxlAAA=",V2,JUL,"2026-10-02T12:57:25Z",LIB,M1),
 (IDB1,"RxmAAA=","[CMA CGM] BRIBB | Libera\u00e7\u00e3o de vazio - BERNECK | SSZ1852894",JUL,"2026-10-02T12:06:16Z",LIB,M1),
 (IDB1,"RxnAAA=","RE: Solicita\u00e7\u00e3o de carregamento - OV# 305516 A",JUL,"2026-10-02T12:00:49Z",ZAP2+","+GTO+","+REP2+","+ZAP_BASE+",atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br,"+M1,ZAP_CC),
 (IDB1,"RxoAAA=","RES: Solicita\u00e7\u00e3o de carregamento - OV# 305516 A",ZAP2,"2026-10-02T11:52:48Z",GTO+","+REP2+",exportacao.op@zappellini.com.br,op.sc@zappellini.com.br,exportacao@zappellini.com.br,exp-berneck@nelsonheusi.com,exportacao3@zappellini.com.br,exportacao1@zappellini.com.br,exportacao4@zappellini.com.br,atendimento@zappellini.com.br,export.sc.zappellini@gmail.com,exportacao5@zappellini.com.br,"+M1,ZAP_CC),
]
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
