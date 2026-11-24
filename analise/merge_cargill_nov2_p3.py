import json, os, collections
B4="AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ME="bma.road-southeast@cma-cgm.com"
PRE="S51907.A01 - BKG SSZ1859739 - 15HCs - SANTOS / PORT QASIM (CMA-CGM/ZIRANLOG) - CASA | Safra 2026"
S_CROSS="[CMA CGM] BRSSZ | CROSS DOCKING - COTTON | CARGILL x GUARUJ\u00c1 TERMINAIS | S51907.A01 - BKG SSZ1859739 - 15HCs"
S_DOC="Instru\u00e7\u00e3o Document\u00e1ria - S51504.B01- BK SSZ1862967- CARGILL - SANTOS / HAIPHONG PORT, VIETNAM (CIP /EXW)"
S_DRAFT="BRSSZ | DRAFT PARCIAL & ATUALIZA\u00c7\u00c3O DE DESCARGA | "+PRE
JUL="Juliane.MARQUES@mercosul-line.com.br"
ISK="isadora_alonso@cargill.com"; ADB="Adriano_Dasilvabomtempo@cargill.com"; VRA="Vitoria_Raiane@cargill.com"; SMA="Sandielle_Maia@cargill.com"
SO3="operacional3@guarujaterminais.com.br"; SO4="operacional4@guarujaterminais.com.br"; CO="coordenador@guarujaterminais.com.br"
TRN="transporte@guarujaterminais.com.br"
CCTL="cotton_ctl@cargill.com"; PLGC="-port-logistics-cotton@cargill.com"; CDocs="cotton-br-docs@cargill.com"; PAC="-port-allocation-cotton@exch.cargill.com"
MJR="Mariajulia_Ramos@cargill.com"
YAS="yasmin.mello@pibernat.com.br"; THR="thierre.mendonca@pibernat.com.br"; EXPC="expo.cargill.cotton@pibernat.com.br"
TKR=["joana.santos@tkrinspection.com","Skarlatty.Boden@tkrinspection.com","renato.costa@tkrinspection.com","kelly.lopes@tkrinspection.com","carlos.osman@tkrinspection.com","cotton@tkrinspection.com"]
TJUL3=JUL+","+SO3+","+CO
OP3C=",".join([SO4,SO3,CO])
CC_BIG=",".join([YAS,MJR,TKR[0],TKR[1],ME,TKR[2],TKR[3],TKR[4],TKR[5],CCTL,EXPC,PLGC,CDocs,PAC])
rows=[
 (B4,"SFdAAA=","***PLANILHA DE PESO*** Instru\u00e7\u00f5es Document\u00e1ria - "+S_DOC,YAS,"2026-11-11T18:58:14Z",ISK,",".join([JUL,MJR,TKR[0],TKR[1],ME,TKR[2],TKR[3],TKR[4],TKR[5],CCTL,EXPC,PLGC,CDocs,PAC])),
 (B4,"SFfAAA=","PLANILHA ATUALIZADA  ///S51907.A01 - BKG SSZ1859739 - 15HCs",SO4,"2026-11-11T18:43:12Z",TJUL3,ME),
 (B4,"SErAAA=","RES: "+S_CROSS,SO4,"2026-11-11T16:48:37Z",TJUL3,ME),
 (B4,"SE0AAA=","RE: NFS DE EXPORTA\u00c7\u00c3O & DUE + Confirma\u00e7\u00e3o MAPA | "+S_DOC,JUL,"2026-11-11T13:57:39Z",",".join([MJR,TKR[0],TKR[1],ME,TKR[2],TKR[3],TKR[4],TKR[5],CCTL,EXPC,SO4]),",".join([PLGC,CDocs,PAC,SO3,CO,TRN,"BRA.SERVICE@CMA-CGM.COM"])),
 (B4,"SE3AAA=","Re: GUARUJA TERMINAIS - POSICIONAMENTO MAPA // S51504.B01- BK SSZ1862967 - DATA: 11/11 - RGDE2620251 - CARGILL",THR,"2026-11-11T13:50:38Z",JUL,CC_BIG),
 (B4,"SE8AAA=","RE: GUARUJA TERMINAIS - POSICIONAMENTO MAPA // S51504.B01- BK SSZ1862967 - DATA: 11/11 - RGDE2620251 - CARGILL",JUL,"2026-11-11T13:14:26Z",THR,CC_BIG),
 (B4,"SE9AAA=","RE: NFS DE EXPORTA\u00c7\u00c3O & DUE + Confirma\u00e7\u00e3o MAPA | "+S_DOC,JUL,"2026-11-11T13:12:40Z",",".join([MJR,TKR[0],TKR[1],ME,TKR[2],TKR[3],TKR[4],TKR[5],CCTL,EXPC]),",".join([PLGC,CDocs,PAC,SO4,SO3,CO,TRN,"BRA.SERVICE@CMA-CGM.COM"])),
 (B4,"SE-AAA=","Re: GUARUJA TERMINAIS - POSICIONAMENTO MAPA // S51504.B01- BK SSZ1862967 - DATA: 11/11 - RGDE2620251 - CARGILL",THR,"2026-11-11T13:04:26Z",JUL,CC_BIG),
 (B4,"SFAAAA=","RE: "+S_CROSS,JUL,"2026-11-11T13:00:42Z",OP3C,ME),
 (B4,"SFFAAA=","RE: GUARUJA TERMINAIS - POSICIONAMENTO MAPA // S51504.B01- BK SSZ1862967 - DATA: 11/11 - RGDE2620251 - CARGILL",JUL,"2026-11-11T12:34:46Z",THR,CC_BIG),
 (B4,"SFxAAA=","RES: "+S_DRAFT,ISK,"2026-11-11T11:21:26Z",",".join([JUL,ADB,VRA,SMA]),",".join([PLGC,CDocs,PAC,"vinicius.calazans@agsurveyors.com","cotton@agsurveyors.com","giovanna.freitas@agsurveyors.com",ME,SO3,CO,SO4])),
]
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
c=collections.Counter(json.loads(l)["date"][:10] for l in open(out))
print("by day:",sorted(c.items()))
