# Análise Tempo dedicado por cliente – Sul/Sudeste

Análise do tempo dedicado por cliente a partir da caixa de e-mail
(`bmn.tsena@cma-cgm.com`), período 15/08/2026 – 19/11/2026 (datas UTC,
dias locais UTC−3). Critério de pertencimento (gate): e-mails em que a própria
conta, `bma.road-southeast@cma-cgm.com` ou `bma.road-south@cma-cgm.com`
estão em Para/CC (ou se a remetente for a própria conta); `bma.road-northeast` fora do escopo.

## Resultado final

**Total: 11.448 minutos = 190h48** sobre **55 dias com atividade**
(208,1 min/dia) ou **62 dias úteis** (184,6 min/dia).

Por mês: ago 135 min (2h15, 8 dias) · set 75 min (1h15, 5 dias) ·
out 6.130 min (102h10, 26 dias) · nov 5.108 min (85h08, 16 dias).

| Cliente | Minutos | Horas | Min/dia (55 dias ativos) | Min/dia (62 dias úteis) |
|---|---:|---:|---:|---:|
| ED&F MAN | 4.203 | 70h00 | 107,8 (39 dias ativos) | 67,8 |
| CAN PACK | 1.790 | 29h50 | 63,9 (28) | 28,9 |
| CARGILL | 1.420 | 23h40 | 50,7 (28) | 22,9 |
| PERNOD RICARD | 840 | 14h00 | 56,0 (15) | 13,5 |
| DSV | 745 | 12h25 | 74,5 (10) | 12,0 |
| BERNECK | 655 | 10h55 | 72,8 (9) | 10,6 |
| CEVA | 630 | 10h30 | 57,3 (11) | 10,2 |
| UNILEVER | 560 | 9h20 | 28,0 (20) | 9,0 |
| NISSAN | 280 | 4h40 | 35,0 (8) | 4,5 |
| ARGOFRUTA | 160 | 2h40 | 32,0 (5) | 2,6 |
| NATURAL ONE | 100 | 1h40 | 25,0 (4) | 1,6 |
| APL | 60 | 1h00 | 30,0 (2) | 1,0 |
| BRX | 5 | 0h05 | 5,0 (1) | 0,1 |
| GROSFILLEX | 0 | 0h00 | 0,0 — nenhum e-mail no mailbox | 0,0 |

## Entregáveis (`entrega/`)

- `tempo_clientes_sul_sudeste_dias_com_atividade.xlsx` — base dias com atividade
- `tempo_clientes_sul_sudeste_dias_uteis.xlsx` — base dias úteis (62)
- `CANVAS_dias_com_atividade.md` / `CANVAS_dias_uteis.md` — documentação por versão

Cada workbook: RESUMO (ordenado por minutos, TOTAL, Indicador mensal),
MENSAL (SUMIFS por mês, linhas de dias editáveis em amarelo),
10 abas DET (clientes de palavra-chave, item a item), BASE (todas as 1.098
linhas classificadas, fonte dos clientes por domínio e do TOTAL) e
METODOLOGIA. Tudo com fórmulas vivas (SUMIFS/COUNTIFS).

## Pipeline (`analise/`)

1. **Coleta** (`raw/*.jsonl`, `merge_*.py`): busca Outlook por cliente em janelas
   de data ([15/08–01/09], [01/09–01/10], [01/10–16/10], [16/10–01/11],
   [01/11–11/11], [11/11–19/11]) com paginação; janelas ≥250 itens divididas ao
   meio (teto silencioso de ~275 resultados por consulta). Cada janela repetida
   com `folder_id: "deleteditems"` (2 itens DSV de 19/11, marcados "Apagado").
   Linhas brutas de remetente/destinatários/CC em `to`/`cc` podem ser string CSV
   ou lista — normalizadas na consolidação.
2. **Consolidação** (`consolidate.py`): gate final (me/RS/RST em Para/CC ou
   remetente = eu) → 142 candidatos fora; exclusões (bounce/undeliverable,
   postmaster, RSVPs de calendário, Teams @thread.v2, "Indicadores SUL/SD");
   multi-cliente atribuído ao primeiro citado no assunto; tipo Enviado (10 min)
   vs Recebido classificado pelo assunto normalizado (ordem Outros → Doc →
   Demanda; 3/5/20 min) com word-boundaries para nf/xml/due/ord/ddl; dedupe
   45 min por assunto normalizado sem prefixos RE/RES/FW/ENC (203 réplicas
   marcadas "Duplicado (fora da contagem)"). Saída: `data/final_rows.json`
   com 1.098 linhas: contadas, duplicadas e apagadas (item a item nas DET).
3. **Geração** (`generate_workbooks.py`): as duas pastas em `entrega/` +
   `data/resumo_diag.json`.
4. **Verificação** (`checker.py`): reavalia cada fórmula gerada com um
   mini-avaliador próprio (COUNTIFS/SUMIFS/IF/SUM, alinhamento por linha lida do
   workbook real) e confere com valores recalculados de `data/final_rows.json`;
   valida abas, contagem de linhas DET/BASE, ordenação do RESUMO e documentação
   da base na METODOLOGIA. Saída: **STATUS: CLEAN** nas duas pastas.

```bash
cd analise
python3 consolidate.py          # reconsolida raw/*.jsonl -> data/final_rows.json
python3 generate_workbooks.py   # regenera entrega/*.xlsx
python3 checker.py              # deve imprimir: STATUS: CLEAN
```
