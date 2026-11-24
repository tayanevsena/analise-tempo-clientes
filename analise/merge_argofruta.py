# merge ARGOFRUTA rows into raw/argofruta_all.jsonl
import json, os

OUT = "/workspace/analise_coleta/raw/argofruta_all.jsonl"
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "a").close()  # ensure exists

ID1 = "AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bO4AAD_pCFLmexhTJPvSGWoCQBNAAYtk"
IDPC = "AAMkADEyNjUxZDk2LTlkZTEtNGFkYy1hMTJmLTVlMTVmODYyMTNlYwBGAAAAAABKsVXXKDCsQrV3leGiqzX2BwD_pCFLmexhTJPvSGWoCQBNAAWW_bPCAAD_pCFLmexhTJPvSGWoCQBNAAb"

ME = "bmn.tsena@cma-cgm.com"
M1 = "bma.road-southeast@cma-cgm.com"
NE = "bma.road-northeast@cma-cgm.com"
JUL = "Juliane.MARQUES@mercosul-line.com.br"
JEFF = "jefferson.silva@mercosul-line.com.br"
ANA = "anacarolina.esteves@mercosul-line.com.br"
RCE = "RCE.JLIMA@cma-cgm.com"
HER = "her.pbarrantes@cma-cgm.com"
APH = "ssc.BRAaphelpdesk@cma-cgm.com"
SOA = "ssc.brsoa@cma-cgm.com"
FIN = "financeiro@lotusstransportes.com.br"
FLA = "faturamento_logistica@argofruta.com"
JME = "ssz.jmeireles@cma-cgm.com"
ANI = "SSC.ANISHAD@cma-cgm.com"
PTA = "SSC.PTAWADE@cma-cgm.com"
KKA = "SSC.KKADDI@cma-cgm.com"
PBA = "SSC.PBANGAR@cma-cgm.com"
PAG = "bma.pagamentos@cma-cgm.com"
GBS = "gbs.BRintermodal@cma-cgm.com"
PED = "pedro@lotusstransportes.com.br"
FATL = "faturamento@lotusstransportes.com.br"
SJ = "sergio.junior@lotusstransportes.com.br"
FGA = "francielle.goncalves@lotusstransportes.com.br"
OPE6 = "operacional6@lotusstransportes.com.br"
OH2 = "operacional2@lotusstransportes.com.br"
OPL = "operacional@lotusstransportes.com.br"
OPE3 = "operacional3@lotusstransportes.com.br"
OPL4 = "operacional4@lotusstransportes.com.br"
EXPD = "expedicao@lotusstransportes.com.br"
RNO = "rnovoa@lotusstransportes.com.br"
FBOT = "fabricioboturao@lotusstransportes.com.br"
TCH = "toninhocopenhagen@uol.com.br"
JOAO = "joao@lotusstransportes.com.br"
PRIS = "priscillapaiva@lotusstransportes.com.br"
LOGIST = "logistica@lotusstransportes.com.br"
EDU = "eduarda@lotusstransportes.com.br"
RIC = "ricardo@copenhagenaduaneira.com.br"
TON = "toninho@copenhagenaduaneira.com.br"
SELMA = "selma@copenhagenaduaneira.com.br"
OPCA = "operacional@copenhagenaduaneira.com.br"
VANDA = "vandacopenhagen@uol.com.br"
BMF = "bma.faturamento@cma-cgm.com"
THIAGO = "thiago@argofruta.com"
LOGX = "logistics@argofruta.com"
LOG2 = "logistics2@argofruta.com"
DOC2 = "documentation2@argofruta.com"
EXPA = "exportacao@argofruta.com"
MARCIO = "marcio.miranda@argofruta.com"
SS1 = "support.sales@argofruta.com"
SS2 = "support2.sales@argofruta.com"
MUR = "murilo.junior@argofruta.com"
LIMS = "limes.sales@argofruta.com"
LIME = "lime.sales@argofruta.com"
APCA = "aprendiz.controladoria@argofruta.com"
SSUP = "commercial.support@argofruta.com"
VALD = "valdemir.santos@argofruta.com"
FER = "fernando@argofruta.com"
FERS = "fernando.souza@argofruta.com"
THA = "thaiana.viana@argofruta.com"
CERT = "certificacao@argofruta.com"
MANGO = "mango.sales@argofruta.com"
NAT = "natalia.silva@argofruta.com"
OPA2 = "operacional@argologistica.com.br"
OPA2B = "operacional2@argologistica.com.br"
ORL = "orlando.sarmento@argologistica.com.br"
CPH = "copenhagen@uol.com.br"
SERGIO = "sergiocopenhagen@uol.com.br"
FAB = "fabricioboturao@lotusstransportes.com.br"
LUCOS = "BMA.LUCOSTA@cma-cgm.com"
SSIL = "bma.ssilva@cma-cgm.com"
NTH = "bma.nth-multimodal@cma-cgm.com"
FRUIT = "bra.fruit.service@cma-cgm.com"
BRASVC = "BRA.SERVICE@CMA-CGM.COM"
LUC = "lucas.silva@lechman.com.br"
CMALE = "cma.lechman@lechman.com.br"
LIB2 = "BMA.LIBERACAO@cma-cgm.com"
RAIL = "bma.railmultimodal@cma-cgm.com"
AUD = "audriney.nascimento@mercosul-line.com.br"
BII = "ssz.inland.insurance@cma-cgm.com"
BRC = "BRA.Collection@cma-cgm.com"
BRF_E = "brf.earaujo@cma-cgm.com"
BRF_P = "BRF.POLIVEIRA@cma-cgm.com"
CPA = "contas.pagar@argofruta.com"
ROS = "rosangela.ferreira@argofruta.com"
INV = "bma.invoices@cma-cgm.com"

TO_NFXML_A = [THIAGO, EDU, OPE6, MARCIO, RIC, TON, TCH, OPCA, LOGIST, SERGIO, FAB, OPE3, PED, SELMA, CPH, JEFF, RCE, DOC2, LOG2, SS1, SS2, EXPA, MUR, LIMS, LOGX, APCA, LUCOS, SSIL, NTH, LUCOS, M1, VALD, FER, FERS]
TO_NFXML_B = [EDU, OPE6, MARCIO, RIC, TON, TCH, OPCA, LOGIST, SERGIO, FAB, OPE3, PED, SELMA, CPH, JEFF, RCE, DOC2, LOG2, SS1, SS2, EXPA, MUR, LIMS, LOGX, APCA, LUCOS, SSIL, NTH, LUCOS, M1, VALD, FER, FERS]
TO_NFXML_C = [THIAGO, OPE6, MARCIO, RIC, TON, TCH, OPCA, LOGIST, SERGIO, FAB, OPE3, PED, SELMA, CPH, JEFF, RCE, DOC2, LOG2, SS1, SS2, EXPA, MUR, LIMS, LOGX, APCA, LUCOS, SSIL, NTH, LUCOS, M1, VALD, FER, FERS]
TO_AL0482_A = [MARCIO, RIC, TON, TCH, OPCA, M1, LOGIST, SERGIO, OPE6, OPE3, PED, SELMA, BMF, EDU]
TO_AL0482_B = [RIC, TON, TCH, OPCA, M1, LOGIST, SERGIO, OPE6, OPE3, PED, SELMA, BMF, EDU]
CC_AL0482 = [LOGX, SS1, THIAGO, SSUP, EXPA, LOG2, MUR, DOC2, "daniel.sanchez@argofruta.com", LIME, APCA]
CC_LIMAO = [OH2, OPL, EXPD, RNO, FBOT, TCH, JOAO, PRIS, PED, OPL4, LOGIST, EDU, RIC, TON, OPE3, DOC2, LOG2, EXPA, BRASVC, M1]
CC14 = [FIN, FLA, JUL, M1, JME, SOA, ANI, PTA, KKA, PBA, PAG, GBS, PED, FATL]
CC16 = [FIN, FLA, JUL, M1, JME, SOA, ANI, PTA, KKA, PBA, PAG, GBS, PED, FATL]
CC14B = [FIN, FLA, JUL, M1, JME, SOA, ANI, PTA, KKA, PBA, PAG, GBS, PED]
CC13 = [FIN, SJ, FLA, JUL, M1, JME, SOA, ANI, PTA, KKA, PBA, PAG, GBS]

S_FATU = "URGENTEE: Fatura Nº 1/1/027220 Cliente: CMA CGM FRANCE "
S_FATRE = "RE: Fatura Nº 1/1/027220 Cliente: CMA CGM FRANCE "
S_FATRES = "RES: Fatura Nº 1/1/027220 Cliente: CMA CGM FRANCE "
S_BRFOR = "RE: BRFOR | FATURAS DIVERGENTES - ARGOFRUTA | 11029 / 11016 / 11028 / 10676 / 10716 / 10775 / 10794 / 10825 / 10844 / 11018"
S_CIRA1 = "RE: CIRA RFI 10155 BRA459386136 ARGO LOGISTICA LTDA"
S_CIRA0 = "RE: CIRA RFI 10061 BRA458789849 ARGO LOGISTICA LTDA"
S_SIN = "RES: SINISTRO // UNIDADE CGMU5249339 // CMA CGM // NAVIO CMA CGM KOUROU"
S_NF0499RES = "RES: Nota Fiscal e XML - AL0499/2026 -IDEAL CITRUS- PORT OF LOADING: SANTOS - PORT OF DESTINATION:SOUTHAMPTON - CTE - 27880 "
S_NF0499 = "Nota Fiscal e XML - AL0499/2026 -IDEAL CITRUS- PORT OF LOADING: SANTOS - PORT OF DESTINATION:SOUTHAMPTON"
S_NF0500RES = "RES: Nota Fiscal e XML - AL0500/2026 -IDEAL CITRUS- PORT OF LOADING: SANTOS - PORT OF DESTINATION:SOUTHAMPTON - CTE 27879"
S_NF0500 = "Nota Fiscal e XML - AL0500/2026 -IDEAL CITRUS- PORT OF LOADING: SANTOS - PORT OF DESTINATION:SOUTHAMPTON"
S_NF0489RES = "RES: Nota Fiscal e XML - AL0489/2026 -IDEAL CITRUS- PORT OF LOADING: SANTOS - PORT OF DESTINATION:ROTTERDAM - CTE - 27838"
S_NF0489 = "Nota Fiscal e XML - AL0489/2026 -IDEAL CITRUS- PORT OF LOADING: SANTOS - PORT OF DESTINATION:ROTTERDAM"
S_NF0482RES = "RES: Nota Fiscal e XML - AL0482/2026 - PORT OF LOADING: SANTOS - PORT OF DESTINATION: ROTTERDAM - CTE - 27772"
S_NF0482 = "Nota Fiscal e XML - AL0482/2026 - PORT OF LOADING: SANTOS - PORT OF DESTINATION: ROTTERDAM"
S_IRC = "Re: FW: [iRECOVERY OCEAN INVOICE REQUEST] - RC26-0017786 Invoicing Notification - Damage Recovery - Brazil"
S_CPH19 = "COPENHAGEN ASSESSORIA E COMERCIO EXTERIOR LTDA - NF-e 13719- VENCIMENTO 16/12/2026"
S_CPH03 = "COPENHAGEN ASSESSORIA E COMERCIO EXTERIOR LTDA - NF-e 13703- VENCIMENTO 06/11/2026"
S_VAL1 = "RE: VALORES  EMBARQUES  ARGOFRUTA COMERCIALEXPORTADORA LTDA - NAVIO  MAERSK  LAGUNA"
S_VAL0 = "VALORES  EMBARQUES  ARGOFRUTA COMERCIALEXPORTADORA LTDA - NAVIO  MAERSK  LAGUNA"
S_VAL2 = "RE: VALORES  EMBARQUES  ARGOFRUTA COMERCIALEXPORTADORA LTDA - NAVIO  MAERSK LINS"
S_VAL20 = "VALORES  EMBARQUES  ARGOFRUTA COMERCIALEXPORTADORA LTDA - NAVIO  MAERSK LINS"
S_PL1 = "RES: PROGRAMAÇÃO LIMÃO // SEMANA 45 // CMA CGM )(LS)"
S_PL2 = "RE: PROGRAMAÇÃO LIMÃO // SEMANA 45 // CMA CGM"
S_PL3 = "RE: RES: PROGRAMAÇÃO LIMÃO // SEMANA 45 // CMA CGM )(LS)"
S_PL4 = "Re: PROGRAMAÇÃO LIMÃO // SEMANA 45 // CMA CGM )(LS)"
S_PL5 = "RE: PROGRAMAÇÃO LIMÃO // SEMANA 45 // CMA CGM )(LS)"
S_LVA1 = "[CMA CGM] BRSSZ | Liberação de vazio - ARGOFRUTA | LIMÃO | WK 45"
S_LVA1RE = "RE: [CMA CGM] BRSSZ | Liberação de vazio - ARGOFRUTA | LIMÃO | WK 45(LS)"
S_LVA1RES = "RES: [CMA CGM] BRSSZ | Liberação de vazio - ARGOFRUTA | LIMÃO | WK 45(LS)"


def R(idb, sfx, date, subject, frm, to, cc):
    return {
        "id": (idb + sfx) if idb is not None else sfx,
        "folder": "main",
        "date": date,
        "subject": subject,
        "from": frm,
        "to": ",".join(to),
        "cc": ",".join(cc),
    }


rows = [
    R(IDPC, "Gqk6gAAA=", "2026-11-19T15:13:44Z", S_CIRA1, APH, [LOGX, OPA2, THA, OPA2B, ORL], [PBA, INV, NE]),
    R(IDPC, "Gqk6\bfAAA=", "2026-11-19T15:12:05Z", S_CIRA0, APH, [THA, MARCIO, LOGX, CERT, DOC2, MANGO, NAT, "viviane@ftrade.com.br"], [PBA, INV, NE]),
    R(IDPC, "Gqk6\bgAAA=", "2026-11-19T13:11:31Z", S_SIN, BII, [LOGX], ["joao.lima@argofruta.com", "finance.argo@argofruta.com", "daniel.sanchez@argofruta.com", "arshiley.neves@argofruta.com", "jhonatan.holanda@argofruta.com", THA, "Jonathan.santos@abagroup.com.br", "flavia@argofruta.com", ROS, EXPA, OPA2, RCE, JUL, BRF_E, BRF_P, NE, OPA2B, ORL]),
    R(ID1, "S0nAAA=", "2026-11-18T19:11:07Z", S_NF0499RES, FGA, TO_NFXML_A, []),
    R(ID1, "SMFAAA=", "2026-11-18T18:28:45Z", S_NF0499, THIAGO, TO_NFXML_B, []),
    R(IDPC, "ETdj8AAA=", "2026-11-18T17:32:42Z", S_BRFOR, FRUIT, [JEFF], [LOGX, NE, ANA, RCE]),
    R(ID1, "S0PAAA=", "2026-11-18T15:33:52Z", S_NF0500RES, FGA, TO_NFXML_A, []),
    R(ID1, "S0UAAA=", "2026-11-18T14:36:58Z", S_NF0500, THIAGO, TO_NFXML_B, []),
    R(IDPC, "ETdjjAAA=", "2026-11-18T14:17:57Z", S_BRFOR, JEFF, [FRUIT], [LOGX, NE, ANA, RCE]),
    R(ID1, "Sc7AAA=", "2026-11-16T20:38:27Z", S_BRFOR, FRUIT, [JEFF], [LOGX, NE, ANA, RCE]),
    R(ID1, "SIrAAA=", "2026-11-16T19:12:54Z", S_CPH19, VANDA, [BMF], [M1, EXPA, TON]),
    R(ID1, "SdrAAA=", "2026-11-16T17:07:15Z", S_BRFOR, JEFF, [FRUIT], [LOGX, NE, ANA, RCE]),
    R(ID1, "SKEAAA=", "2026-11-16T13:09:36Z", S_FATU, SJ, [HER, APH, SOA], CC14),
    R(ID1, "SGNAAA=", "2026-11-12T17:29:51Z", S_VAL1, JUL, [VANDA], [M1, EXPA, TON]),
    R(ID1, "SGlAAA=", "2026-11-12T14:34:22Z", S_FATU, SJ, [HER, APH, SOA], CC14),
    R(ID1, "SG5AAA=", "2026-11-12T12:14:38Z", S_NF0489RES, FGA, TO_NFXML_C, []),
    R(ID1, "SF0AAA=", "2026-11-11T21:07:26Z", S_NF0489, THIAGO, TO_NFXML_B, []),
    R(ID1, "SFgAAA=", "2026-11-11T18:32:13Z", S_VAL0, VANDA, [JUL], [M1, EXPA, TON]),
    R(ID1, "SENAAA=", "2026-11-09T20:47:07Z", S_FATRE, HER, [SJ, APH, SOA], CC14),
    R(ID1, "RyjAAA=", "2026-11-09T19:30:31Z", S_FATU, SJ, [HER, APH, SOA], CC14),
    R(ID1, "RcUAAA=", "2026-11-06T17:49:23Z", S_FATRES, SJ, [HER, APH, SOA], CC14B),
    R(ID1, "Rd4AAA=", "2026-11-05T17:54:00Z", S_NF0482RES, FGA, TO_AL0482_A, CC_AL0482),
    R(ID1, "Rd6AAA=", "2026-11-05T17:40:49Z", S_IRC, LOGX, [BRC, BRF_E, JUL, JEFF, M1], [LOG2, THA, OPA2, CPA, ROS]),
    R(ID1, "ReDAAA=", "2026-11-05T16:36:13Z", S_NF0482, MARCIO, TO_AL0482_B, CC_AL0482),
    R(ID1, "Re1AAA=", "2026-11-04T20:09:22Z", S_PL1, OPE6, [LOGX, JUL], CC_LIMAO),
    R(ID1, "Re7AAA=", "2026-11-04T19:34:55Z", S_FATRE, HER, [SJ, APH, SOA], CC14B),
    R(ID1, "RfFAAA=", "2026-11-04T16:25:57Z", S_LVA1RES, LUC, [LIB2, JUL, BRASVC, FRUIT, CMALE], [M1]),
    R(ID1, "RfHAAA=", "2026-11-04T15:26:04Z", S_PL2, JUL, [OPE6, LOGX], CC_LIMAO),
    R(ID1, "RfKAAA=", "2026-11-04T15:07:42Z", S_LVA1RE, LIB2, [JUL, BRASVC, FRUIT, LUC, CMALE], [M1]),
    R(ID1, "RfMAAA=", "2026-11-04T14:58:01Z", S_LVA1RE, FRUIT, [JUL], [LIB2, M1]),
    R(ID1, "RfUAAA=", "2026-11-04T14:20:59Z", S_PL3, FRUIT, [OPE6, M1, JUL], [JUL, PRIS, OPL, DOC2, TCH, TON, OPE3, JOAO, OH2, RIC, EDU, LOGX, EXPD, RNO, LOGIST, PED, EXPA, OPL4, FBOT]),
    R(ID1, "RfZAAA=", "2026-11-04T13:53:07Z", S_LVA1RE, JUL, [LIB2, BRASVC, FRUIT], [M1]),
    R(ID1, "RfpAAA=", "2026-11-04T13:16:46Z", S_LVA1RE, LIB2, [JUL, BRASVC], [M1]),
    R(ID1, "RfrAAA=", "2026-11-04T13:13:24Z", S_PL1, OPE6, [JUL, LOGX], CC_LIMAO),
    R(ID1, "RftAAA=", "2026-11-04T12:36:38Z", S_PL4, LOGX, [JUL], CC_LIMAO),
    R(ID1, "Rf3AAA=", "2026-11-03T20:37:19Z", S_LVA1, JUL, [LIB2], [M1]),
    R(ID1, "Rf4AAA=", "2026-11-03T20:35:07Z", S_PL5, JUL, [LOGX, OPE6], CC_LIMAO),
    R(ID1, "Rf5AAA=", "2026-11-03T20:24:39Z", S_PL4, LOGX, [JUL], [OPE6, RAIL, LIB2, OH2, OPL, EXPD, RNO, FBOT, TCH, JOAO, PRIS, PED, OPL4, LOGIST, EDU, RIC, TON, OPE3, DOC2, LOG2, EXPA, BRASVC, M1, AUD]),
    R(ID1, "Rf6AAA=", "2026-11-03T20:23:35Z", S_PL5, JUL, [OPE6, RAIL, LIB2, LOGX, OH2, OPL, EXPD, RNO, FBOT, TCH, JOAO, PRIS, PED, OPL4, LOGIST, EDU, RIC, TON, OPE3, DOC2, LOG2, EXPA, BRASVC, M1], [AUD]),
    R(ID1, "Rf7AAA=", "2026-11-03T20:21:20Z", S_PL1, OPE6, [RAIL, LIB2, LOGX, OH2, OPL, EXPD, RNO, FBOT, TCH, JOAO, PRIS, PED, OPL4, LOGIST, EDU, RIC, TON, OPE3, DOC2, LOG2, EXPA, BRASVC, M1, JUL], [AUD]),
    R(ID1, "RgbAAA=", "2026-11-03T13:18:12Z", S_PL5, RAIL, [LIB2, OPE6, LOGX, OH2, OPL, EXPD, RNO, FBOT, TCH, JOAO, PRIS, PED, OPL4, LOGIST, EDU, RIC, TON, OPE3, DOC2, LOG2, EXPA, BRASVC, M1, JUL], [AUD]),
    R(ID1, "RjKAAA=", "2026-10-27T18:00:38Z", S_FATRES, SJ, [HER, APH, SOA], CC14B),
    R(ID1, "RlJAAA=", "2026-10-23T17:56:10Z", S_FATRE, HER, [SJ, APH, SOA], [FIN, FLA, JUL, M1, JME, ANI, PTA, KKA, PBA, PAG, GBS, PED]),
    R(ID1, "RlXAAA=", "2026-10-23T14:04:30Z", S_FATRES, SJ, [HER, APH, SOA], CC14B),
    R(ID1, "RmOAAA=", "2026-10-22T19:02:26Z", S_FATRES, SJ, [HER, APH, SOA], CC14B),
    R(ID1, "Ru-AAA=", "2026-10-08T20:01:16Z", S_FATRES, FATL, [HER, APH, SOA], CC13),
    R(ID1, "RwVAAA=", "2026-10-06T17:21:38Z", S_CPH03, VANDA, [BMF], [M1, EXPA, TON]),
    R(ID1, "RwWAAA=", "2026-10-06T15:58:46Z", S_FATRE, HER, [APH, SOA], CC13),
    R(ID1, "Rw5AAA=", "2026-10-05T14:19:41Z", S_VAL2, JUL, [VANDA], [M1, EXPA, TON]),
    R(ID1, "Rw7AAA=", "2026-10-05T13:42:22Z", S_VAL20, VANDA, [JUL], [M1, EXPA, TON]),
    R(ID1, "RxpAAA=", "2026-10-01T19:17:59Z", S_FATRE, HER, [FATL, FLA, JUL, M1, JME, SOA, ANI, PTA, KKA, PBA, PAG, GBS], [FIN, SJ]),
]

existing = set()
if os.path.exists(OUT):
    with open(OUT, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                existing.add(json.loads(line)["id"])

new = 0
with open(OUT, "a", encoding="utf-8") as f:
    for r in rows:
        if r["id"] in existing:
            continue
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
        existing.add(r["id"])
        new += 1

print(f"new: {new} total: {len(existing)}")

from collections import Counter
by_day = Counter()
with open(OUT, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            by_day[json.loads(line)["date"][:10]] += 1
for d in sorted(by_day):
    print(d, by_day[d])
