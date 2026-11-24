# CANVAS — Tempo dedicado por cliente – Sul/Sudeste · Versão "dias úteis"

**Arquivo:** `tempo_clientes_sul_sudeste_dias_uteis.xlsx`
**Caixa:** Tayane Sena (bmn.tsena@cma-cgm.com) · coleta no Outlook com conector autenticado
**Período:** 15/08/2026 – 19/11/2026 (coleta) · análise mensal ago/set/out/nov · datas em UTC, dias locais em UTC−3
**Base de dias desta versão:** dias úteis de 15/08 a 15/11/2026, excl. fins de semana e feriados nacionais 07/09, 12/10 e 02/11 = **62 dias** (ago 11 · set 21 · out 21 · nov 9).

## Abas

Mesma estrutura, dados e fórmulas vivas da versão "dias com atividade" (`CANVAS_dias_com_atividade.md`); a única diferença é a base de dias (RESUMO col. K e linhas "Dias" da MENSAL = 11/21/21/9, células de entrada editáveis amarelas).

**Fórmulas vivas:** COUNTIFS/SUMIFS sobre DET/BASE; verificado por `analise/checker.py` com reavaliação independente de cada fórmula a partir de `data/final_rows.json` — **STATUS: CLEAN**.

## Resumo (base dias úteis — divisor 62)

| Cliente | Minutos | Horas | Min/dia |
|---|---:|---:|---:|
| ED&F MAN | 4.203 | 70h00 | 67,8 |
| CAN PACK | 1.790 | 29h50 | 28,9 |
| CARGILL | 1.420 | 23h40 | 22,9 |
| PERNOD RICARD | 840 | 14h00 | 13,5 |
| DSV | 745 | 12h25 | 12,0 |
| BERNECK | 655 | 10h55 | 10,6 |
| CEVA | 630 | 10h30 | 10,2 |
| UNILEVER | 560 | 9h20 | 9,0 |
| NISSAN | 280 | 4h40 | 4,5 |
| ARGOFRUTA | 160 | 2h40 | 2,6 |
| NATURAL ONE | 100 | 1h40 | 1,6 |
| APL | 60 | 1h00 | 1,0 |
| BRX | 5 | 0h05 | 0,1 |
| GROSFILLEX | 0 | 0h00 | 0,0 (nenhum e-mail no mailbox) |
| **TOTAL** | **11.448** | **190h48** | **184,6** |

Min/dia por mês (dias úteis do mês como divisor): ago 135/11 = 12,3 · set 75/21 = 3,6 · out 6.130/21 = 291,9 · nov 5.108/9 = 567,6.
