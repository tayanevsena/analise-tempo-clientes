# CANVAS — Tempo dedicado por cliente – Sul/Sudeste · Versão "dias com atividade"

**Arquivo:** `tempo_clientes_sul_sudeste_dias_com_atividade.xlsx`
**Caixa:** Tayane Sena (bmn.tsena@cma-cgm.com) · coleta no Outlook com conector autenticado
**Período:** 15/08/2026 – 19/11/2026 (coleta) · análise mensal ago/set/out/nov · datas em UTC, dias locais em UTC−3
**Base de dias desta versão:** dias corridos com ≥1 e-mail contabilizado (incl. sáb., dom. e feriados), calculados do próprio resultado — **55 dias no total** (união entre clientes; ago 8 · set 5 · out 26 · nov 16).

## Abas

| Aba | Conteúdo |
|---|---|
| RESUMO | Cliente · Doc · Demanda · Outros · Recebidos · Enviados · Minutos · Horas · Min/dia · % expediente (540 min), ordenado por minutos; linha TOTAL; bloco "Indicador mensal" (dias/minutos/horas/min-dia/% do dia). Coluna K "Dias (referência)" = células de entrada editáveis amarelas pré-preenchidas com os dias com atividade calculados |
| MENSAL | Minutos por cliente/mês via fórmulas SUMIFS; linha "Dias" editável (amarelo); linha Min/dia |
| DET_CARGILL … DET_GROSFILLEX (10) | Itens item a item dos clientes de palavra-chave: Data (UTC), Mês, Tipo, De, Para, CC, Assunto, Classificação, Minutos, Situação ("Contado", "Duplicado (fora da contagem)", "Apagado (fora da contagem)") |
| BASE | Todas as 1.098 linhas classificadas (14 clientes), incluindo duplicados/apagados — fonte das fórmulas dos 4 clientes por domínio e do TOTAL |
| METODOLOGIA | Escopo, gate, teto da busca, regras 3/5/10/20, dedupe 45 min, exclusões, fusos e base de dias |

**Fórmulas vivas:** RESUMO/MENSAL usam COUNTIFS/SUMIFS sobre DET (clientes de palavra-chave) e BASE (domínio + TOTAL). Nenhum número colado onde há fonte auditável. Verificado por `analise/checker.py`, que reavaliou cada fórmula de forma independente a partir de `data/final_rows.json` — **STATUS: CLEAN**.

## Resumo (base dias com atividade)

| Cliente | Minutos | Horas | Min/dia | Dias |
|---|---:|---:|---:|---:|
| ED&F MAN | 4.203 | 70h00 | 107,8 | 39 |
| CAN PACK | 1.790 | 29h50 | 63,9 | 28 |
| CARGILL | 1.420 | 23h40 | 50,7 | 28 |
| PERNOD RICARD | 840 | 14h00 | 56,0 | 15 |
| DSV | 745 | 12h25 | 74,5 | 10 |
| BERNECK | 655 | 10h55 | 72,8 | 9 |
| CEVA | 630 | 10h30 | 57,3 | 11 |
| UNILEVER | 560 | 9h20 | 28,0 | 20 |
| NISSAN | 280 | 4h40 | 35,0 | 8 |
| ARGOFRUTA | 160 | 2h40 | 32,0 | 5 |
| NATURAL ONE | 100 | 1h40 | 25,0 | 4 |
| APL | 60 | 1h00 | 30,0 | 2 |
| BRX | 5 | 0h05 | 5,0 | 1 |
| GROSFILLEX | 0 | 0h00 | 0,0 | 0 (nenhum e-mail no mailbox) |
| **TOTAL** | **11.448** | **190h48** | **208,1** | **55 dias** |

Por mês: ago 135 min (2h15) · set 75 min (1h15) · out 6.130 min (102h10) · nov 5.108 min (85h08).
