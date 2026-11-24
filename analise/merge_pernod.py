# merge PERNOD RICARD rows into raw/pernod_all.jsonl
import json, os
from collections import Counter

OUT = "/workspace/analise_coleta/raw/pernod_all.jsonl"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "a").close()

ID1 = "AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
ID2 = "AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAACOz3_7AAD_pCFLmexhTJPvSGWoCQBNAAYtk"

ME = "bmn.tsena@cma-cgm.com"
RS = "bma.road-southeast@cma-cgm.com"
RST = "bma.road-south@cma-cgm.com"

ADR = "adriana.souza@coopercarga.com.br"
KAY = "kayron@coopercarga.com.br"
FAB = "fabiola.santos@coopercarga.com.br"
MAY = "mayara.santos@coopercarga.com.br"
BRU = "bruna.carvalho@coopercarga.com.br"
YOL = "yolanda@coopercarga.com.br"
CAI = "caique.santos@coopercarga.com.br"
CAB = "cabotagem@coopercarga.com.br"
DAN = "daniela@coopercarga.com.br"
RAF = "rafaelli.lima@coopercarga.com.br"
ANAC = "ana.carolina@coopercarga.com.br"
RAFE = "rafael.teixeira@coopercarga.com.br"
ADM = "admguaruja@coopercarga.com.br"
CAS = "cassiano@coopercarga.com.br"
VIT = "vitoria.ferreira@coopercarga.com.br"

JUL = "Juliane.MARQUES@mercosul-line.com.br"
THA = "thaina.santos@mercosul-line.com.br"
ANAR = "ana.santos@rasioterminais.com.br"
MIK = "mikaelle.martins@rasio.com.br"

NLEY = "BMA.NLEY@cma-cgm.com"
JBAT = "BMA.JBATISTA@cma-cgm.com"
DARO = "BMA.DARODRIGUES@cma-cgm.com"
ILN = "bma.ils_newbusiness@cma-cgm.com"
MCAS = "bma.mcastro@cma-cgm.com"
LUCO = "BMA.LUCOSTA@cma-cgm.com"
RORT = "BMA.RORTEGA@cma-cgm.com"
NAA = "ssz.naalves@cma-cgm.com"
MMES = "SSZ.MMESSIANO@cma-cgm.com"
RCA = "ssz.rcamacho@cma-cgm.com"
VIF = "SSZ.VIFERRAZ@cma-cgm.com"
CFR = "SSZ.CFRAZAO@cma-cgm.com"
AGO = "bma.agomes@cma-cgm.com"
LIB = "BMA.LIBERACAO@cma-cgm.com"
BRA = "BRA.SERVICE@CMA-CGM.COM"
bral = "bra.service@cma-cgm.com"
RCE = "RCE.JLIMA@cma-cgm.com"
FAT = "bma.faturamento@cma-cgm.com"
SSZCS = "ssz.customerservice@ccis-network.com"

EDU = "Eduardo.FIGUEIRA@mercosul-line.com.br"
MIRL = "mirella.lucena@mercosul-line.com.br"
JEF = "jefferson.silva@mercosul-line.com.br"

LEA = "leandro.silva@pernod-ricard.com"
IGO_C = "Igor.Fernandes.ext@pernod-ricard.com"
IGOL = "igor.fernandes.ext@pernod-ricard.com"
LUCP = "lucas.moraes@pernod-ricard.com"
NATP = "natalia.vanechapaiva@pernod-ricard.com"
MILP = "milena.martins@pernod-ricard.com"
CAION = "caio.negreiros@pernod-ricard.com"
ROS = "rosita.castro@supplog.com"

ANDS = "anderson.siqueira@santosbrasil.com.br"
GIO = "giovanna.jesus@santosbrasil.com.br"
COB = "cobranca@santosbrasil.com.br"
LUA = "luanda.pitombo@santosbrasil.com.br"
VAN = "vanessa.amaral@santosbrasil.com.br"

FATG = "faturamento.gja@uni.com.br"
ATN = "atendimentoaocliente.gja@uni.com.br"
TRN = "transporte.gja@uni.com.br"
UNT = "uniterminal.gja@uni.com.br"
RN = "rodrigo.noe@uni.com.br"
ATNR = "atendimento@rasio.com.br"
TRNR = "transporte@rasio.com.br"
TERR = "terminal@rasio.com.br"

MIRI = "mirian.sanches@sanfra.com.br"
SANE = "sanfra.exportacao@sanfra.com.br"
CIB = "cibele@sanfra.com.br"
FAB_S = "fabio@sanfra.com.br"
MAL = "malcon@sanfra.com.br"
WEL = "welington@sanfra.com.br"

SAL1 = "Re:  Alinhamento na Operação Multimodal - CMA CGM - Pernod Ricard"
SAL2 = "RE:  Alinhamento na Operação Multimodal - CMA CGM - Pernod Ricard"
SAL0 = " Alinhamento na Operação Multimodal - CMA CGM - Pernod Ricard"
SALR = "RE: Alinhamento na Operação Multimodal - CMA CGM - Pernod Ricard"
SHO1 = "Re:  Homologação fornecedores - Mercosul"
SHO2 = "RE:  Homologação fornecedores - Mercosul"
SG2 = "RE:  [CMA CGM] BRSSZ | Programação PERNOD RICARD | COOPERCARGA - SSZ1854820"
SG3 = "RE:   [CMA CGM] BRSSZ | Programação PERNOD RICARD | COOPERCARGA - SSZ1854820"
SG0 = " [CMA CGM] BRSSZ | Programação PERNOD RICARD | COOPERCARGA - SSZ1854820"
SPR = "RE: [CMA CGM] BRSSZ | Programação PERNORD RICARD | PRE STACKING"
SPS = "RES: [CMA CGM] BRSSZ | Programação PERNORD RICARD | PRE STACKING"
SP0 = " [CMA CGM] BRSSZ | Programação PERNORD RICARD | PRE STACKING"
SPTO = " *Solicitação T/O* [CMA CGM] BRSSZ | Programação PERNORD RICARD | PRE STACKING - SSZ1854820"
SPTOR = "RE: *Solicitação T/O* [CMA CGM] BRSSZ | Programação PERNORD RICARD | PRE STACKING - SSZ1854820"
SCU_RE = "RE: SDL-DOC - [CMA CGM] BRSSZ | CUSTOS ADICIONAIS | PERNOD RICARD | SSZ1854820"
SCU = "SDL-DOC - [CMA CGM] BRSSZ | CUSTOS ADICIONAIS | PERNOD RICARD | SSZ1854820"
SLV_RE = "RE:  [CMA CGM] BRSSZ | Liberação de vazio - PERNOD RICARD | SSZ1854820 (LS)"
SLV0 = " [CMA CGM] BRSSZ | Liberação de vazio - PERNOD RICARD | SSZ1854820"
SPS2 = "RE: Pre-stacking // PERNOD RICARD"
SKI = "RE: [Kick off Operacional] - CMA CGM x PRB"
SKI_P1 = "RES: PERNOD | RE: [INTERNO] [Kick off Operacional] - CMA CGM x PRB"
SKI_P2 = "PERNOD | RE: [INTERNO] [Kick off Operacional] - CMA CGM x PRB"

CC_LS = [RS, ADM, CAS, VIT]
CC_LSR = [RS, ADM, CAS, VIT, RAFE]
CC_PRE1 = [LUCO, RORT, ILN, RS, THA, RCE, NLEY]
CC_PRE2 = [LUCO, RORT, ILN, RS]
CC_KICK_A = [JBAT, RS, NLEY, DARO, ILN, JUL, LUA, VAN, BRA]

rows = []


def R(idb, sfx, date, subject, frm, to, cc):
    rows.append({
        "id": (idb + sfx) if idb else sfx,
        "folder": "main",
        "date": date,
        "subject": subject,
        "from": frm,
        "to": to,
        "cc": cc,
    })


R(ID1, "SMDAAA=", "2026-11-17T18:16:05Z", SAL1, NLEY, [NAA, JUL, THA, RORT, LUCO], [AGO, MMES, RCA, DARO, VIF, CFR, JBAT, EDU, MCAS, ILN, RS])
R(ID1, "SIzAAA=", "2026-11-17T13:48:21Z", SAL2, JBAT, [NAA, JUL, THA, RORT, LUCO, NLEY], [AGO, MMES, RCA, DARO, VIF, CFR, EDU, MCAS, ILN, RS])
R(ID1, "SJIAAA=", "2026-11-17T11:47:15Z", SAL0, NAA, [JUL, THA, RORT, LUCO, NLEY], [AGO, MMES, RCA, DARO, VIF, CFR, JBAT, EDU, MCAS, ILN, RS])
R(ID1, "SJ_AAA=", "2026-11-16T14:14:15Z", SALR, JUL, [DARO, NAA, THA, RORT, LUCO, NLEY], [AGO, MMES, RCA, VIF, CFR, JBAT, EDU, MCAS, ILN, RS])
R(ID1, "SGgAAA=", "2026-11-12T14:54:26Z", SHO1, NLEY, [JUL, LEA, DARO], [LUCP, MIRL, RS, ILN])
R(ID1, "SGtAAA=", "2026-11-12T14:18:16Z", SHO2, JUL, [LEA, NLEY, DARO], [LUCP, MIRL, RS, ILN])
R(ID1, "Re_AAA=", "2026-11-04T17:51:08Z", SG2, JUL, [RAFE, FAB, BRU, YOL, MAY, KAY, ADR, CAI, CAB, DAN], CC_LS)
R(ID1, "Re-AAA=", "2026-11-04T17:48:58Z", SG2, RAFE, [JUL, FAB, BRU, YOL, MAY, KAY, ADR, CAI, CAB, DAN], CC_LS)
R(ID1, "RfLAAA=", "2026-11-04T14:59:10Z", SG2, JUL, [FAB, BRU, YOL, MAY, KAY, ADR, CAI, CAB, DAN], CC_LSR)
R(ID1, "RfeAAA=", "2026-11-04T13:39:00Z", SG2, FAB, [JUL, BRU, YOL, MAY, KAY, ADR, CAI, CAB, DAN], CC_LSR)
R(ID1, "Rg2AAA=", "2026-10-30T19:01:26Z", SG2, FAB, [JUL, BRU, YOL, MAY, KAY, ADR, CAI, CAB, DAN], CC_LSR)
R(ID1, "RixAAA=", "2026-10-28T14:36:36Z", SCU_RE, bral, [JUL], [RS])
R(ID1, "Ri_AAA=", "2026-10-27T20:38:00Z", SCU, JUL, [BRA], [RS])
R(ID1, "RjEAAA=", "2026-10-27T20:08:20Z", SPTOR, JUL, [MIK, RS], [FATG])
R(ID1, "RjLAAA=", "2026-10-27T17:49:26Z", SPS, ANAR, [JUL, RN, RAF, ANAC, YOL, ATN, TRN, UNT, UNT, ATN], [RS, ADR, CAI, BRU, CAB])
R(ID1, "RjMAAA=", "2026-10-27T17:28:27Z", SPR, JUL, [RN, ANAR, RAF, ANAC, YOL, ATN, TRN, UNT, UNT, ATN], [RS, ADR, CAI, BRU, CAB])
R(ID1, "RjYAAA=", "2026-10-27T13:57:12Z", SPTO, MIK, [THA, JUL, RS], [FATG, FAT])
R(ID1, "RjpAAA=", "2026-10-26T20:51:23Z", SPR, RN, [THA, ANAR, RAF, ANAC, YOL, ATN, TRN, UNT, UNT, ATN], [RS, ADR, CAI, BRU, JUL, CAB])
R(ID1, "RjsAAA=", "2026-10-26T20:13:43Z", SP0, THA, [ANAR, RAF, ANAC, YOL, ATN, TRN, UNT, UNT, ATN], [RS, ADR, CAI, BRU, JUL, CAB])
R(ID1, "RjtAAA=", "2026-10-26T20:01:40Z", SKI_P1, ANDS, [GIO, COB, THA], CC_KICK_A)
R(ID1, "RjuAAA=", "2026-10-26T19:59:41Z", SKI_P2, GIO, [ANDS, COB], [JBAT, RS, NLEY, DARO, ILN, JUL, LUA, VAN, THA, BRA])
R(ID1, "RjxAAA=", "2026-10-26T19:22:21Z", SG2, ADR, [THA, JUL, BRU, YOL, MAY, KAY, CAI, CAB, DAN], [RS])
R(ID1, "RkDAAA=", "2026-10-26T15:25:06Z", SG2, THA, [ADR, JUL, BRU, YOL, MAY, KAY, CAI, CAB, DAN], [RS])
R(ID1, "RkEAAA=", "2026-10-26T15:20:07Z", SG2, ADR, [JUL, BRU, YOL, MAY, KAY, CAI, CAB, DAN], [RS])
R(ID1, "RkIAAA=", "2026-10-26T14:45:10Z", SPS, ANAR, [THA, RAF, ANAC, YOL, ATN, TRN, UNT, UNT, ATN], [RS, ADR, CAI, BRU, JUL, CAB])
R(ID1, "RkKAAA=", "2026-10-26T14:01:52Z", SPR, THA, [ANAR, RAF, ANAC, YOL, ATN, TRN, UNT, UNT, ATN], [RS, ADR, CAI, BRU, JUL, CAB])
R(ID1, "RkMAAA=", "2026-10-26T12:32:39Z", SPS, ANAR, [RAF, ANAC, THA, YOL, ATN, TRN, UNT, UNT, ATN], [RS, ADR, CAI, BRU, JUL, CAB])
R(ID1, "RkVAAA=", "2026-10-24T20:48:14Z", SG2, JUL, [BRU, YOL, MAY, KAY, ADR, CAI, CAB, DAN], [RS])
R(ID1, "RkuAAA=", "2026-10-23T22:04:21Z", SG2, BRU, [THA, YOL, MAY, KAY, ADR, CAI, CAB, DAN], [RS, JUL])
R(ID1, "RkwAAA=", "2026-10-23T21:26:35Z", SPS, ANAR, [RAF, ANAC, THA, YOL, ATN, TRN, UNT, UNT, ATN], [RS, ADR, CAI, BRU, JUL, CAB])
R(ID1, "RkzAAA=", "2026-10-23T21:04:44Z", SPR, RAF, [ANAR, ANAC, THA, YOL, ATN, TRN, UNT, TERR, ATNR], [RS, ADR, CAI, BRU, JUL, CAB])
R(ID1, "Rk9AAA=", "2026-10-23T19:23:10Z", SG0, THA, [BRU, YOL, MAY, KAY, ADR, CAI, CAB, DAN], [RS, JUL])
R(ID1, "Rk_AAA=", "2026-10-23T19:17:45Z", SPS, ANAR, [ANAC, THA, YOL, ATN, TRN, UNT], [RS, ADR, CAI, BRU, JUL, CAB])
R(ID1, "RlDAAA=", "2026-10-23T18:34:19Z", SPR, ANAC, [THA, YOL, ATNR, TRNR, TERR], [RS, ADR, CAI, BRU, JUL, CAB])
R(ID1, "RlFAAA=", "2026-10-23T18:17:14Z", SP0, THA, [YOL, ATNR, TRNR, TERR], [RS, ADR, CAI, BRU, JUL, CAB])
R(ID1, "RlQAAA=", "2026-10-23T16:01:22Z", SG3, BRU, [THA, YOL, MAY, KAY, ADR, CAI, JUL, CAB, DAN, RS], [])
R(ID1, "RlVAAA=", "2026-10-23T14:09:22Z", SG3, THA, [YOL, MAY, KAY, ADR, CAI, BRU, JUL, CAB, DAN, RS], [CAB])
R(ID1, "RlYAAA=", "2026-10-23T13:57:28Z", SG3, YOL, [MAY, KAY, ADR, THA, CAI, BRU, JUL, CAB, DAN, RS], [CAB])
R(ID1, "RljAAA=", "2026-10-23T12:11:03Z", SG3, MAY, [KAY, ADR, THA, CAI, BRU, JUL, CAB, DAN], [RS])
R(ID1, "RluAAA=", "2026-10-23T10:30:59Z", SG3, KAY, [ADR, THA, CAI, MAY, BRU, JUL, CAB, DAN], [RS])
R(ID1, "RlwAAA=", "2026-10-23T09:13:17Z", SG3, KAY, [ADR, THA, CAI, MAY, BRU, JUL, CAB, DAN], [RS])
R(ID1, "RlxAAA=", "2026-10-23T09:06:52Z", SG3, KAY, [ADR, THA, CAI, MAY, BRU, JUL, CAB, DAN], [RS])
R(ID1, "RmEAAA=", "2026-10-22T22:00:50Z", SG3, ADR, [THA, CAI, MAY, BRU, KAY, JUL, CAB, DAN], [RS])
R(ID1, "RmRAAA=", "2026-10-22T18:52:24Z", SG3, ADR, [THA, CAI, MAY, BRU, KAY, JUL, CAB, DAN], [RS])
R(ID1, "RmWAAA=", "2026-10-22T18:23:25Z", SG3, THA, [CAI, ADR, MAY, BRU, KAY, JUL, CAB, DAN], [RS])
R(ID1, "RmkAAA=", "2026-10-22T13:58:41Z", SG0, THA, [CAI, ADR, MAY, BRU, KAY, JUL, CAB, DAN], [RS])
R(ID2, "Rm0AAA=", "2026-10-22T01:10:13Z", SG3, CAI, [ADR, THA, MAY, BRU, KAY, JUL, CAB, DAN], [RS])
R(ID1, "Rn6AAA=", "2026-10-20T13:49:58Z", SG3, ADR, [THA, MAY, BRU, KAY, JUL, CAB, DAN], [RS])
R(ID1, "Rn7AAA=", "2026-10-20T13:39:21Z", SG0, THA, [MAY, BRU, KAY, JUL, ADR, CAB, DAN], [RS])
R(ID1, "RoqAAA=", "2026-10-19T19:42:57Z", SLV_RE, LIB, [THA, JUL, SSZCS], [RS])
R(ID1, "Ro4AAA=", "2026-10-19T18:38:38Z", SLV0, THA, [JUL, LIB], [RS])
R(ID1, "RpUAAA=", "2026-10-19T13:01:30Z", SPS2, MCAS, [JUL, IGO_C, LEA, ROS, DARO], CC_PRE1)
R(ID1, "Rp8AAA=", "2026-10-18T17:53:38Z", SLV0, JUL, [LIB], [RS])
R(ID1, "Rp9AAA=", "2026-10-18T17:51:15Z", SPS2, JUL, [MCAS, IGO_C, LEA, ROS, DARO], CC_PRE1)
R(ID1, "Rr_AAA=", "2026-10-16T12:51:27Z", SPS2, MCAS, [IGO_C, LEA, NLEY, ROS, DARO, JUL, THA, JEF, RCE], CC_PRE2)
R(ID2, "O-nAAA=", "2026-10-02T15:03:07Z", SKI, BRA, [IGOL], [MIRI, LEA, SANE, NATP, MILP, CIB, FAB_S, MAL, JBAT, WEL, CAION, DARO])
R(ID2, "O-7AAA=", "2026-10-02T14:31:26Z", SKI, BRA, [IGOL, RST], [MIRI, MILP, CIB, MAL, JBAT, WEL, CAION, DARO, LEA, SANE, NATP, FAB_S])

with open(OUT, "r", encoding="utf-8") as f:
    seen = {json.loads(l)["id"] for l in f if l.strip()}

new = 0
with open(OUT, "a", encoding="utf-8") as f:
    for r_ in rows:
        if r_["id"] in seen:
            continue
        f.write(json.dumps(r_, ensure_ascii=False) + "\n")
        seen.add(r_["id"])
        new += 1

with open(OUT, "r", encoding="utf-8") as f:
    all_lines = [json.loads(l) for l in f if l.strip()]
print(f"new: {new} total: {len(all_lines)}")
print("by day:", Counter(x["date"][:10] for x in all_lines))
