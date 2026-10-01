# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-10-01T11:19:31.990714+00:00**, [preflight](../evidence/2026-10-01/eval/preflight.json)) against the previous one (checked at **2026-09-30T13:03:47.160133+00:00**, [preflight](../evidence/2026-09-30/eval/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.8.3 · cae51ad4 | 1.8.3 · cae51ad4 | Unchanged |
| Anvil dev | 1.8.4-nightly · e3429853 | 1.8.4-nightly · df92604b | Updated |
| Besu stable | 26.9.0 · ee9c64c8 | 26.9.0 · ee9c64c8 | Unchanged |
| Besu dev | 26.9-develop · 67ce4ab1 | 26.10-develop · 28edf391 | Updated |
| Erigon stable | 3.7.0 · bdc78cc4 | 3.7.0 · bdc78cc4 | Unchanged |
| Erigon dev | 3.8.0-dev · 923b4d31 | 3.8.0-dev · 50e2cc4f | Updated |
| Geth draft fork | 1.17.7-unstable · ec1cec0b | 1.17.7-unstable · 67f41dea | Updated |
| Nethermind stable | 2.0.0 · bec830cd | 2.0.0 · bec830cd | Unchanged |
| Nethermind dev | 2.2.0-preview · 79173d14 | 2.2.0-preview · 759efed7 | Updated |
| Reth stable | 2.7.0 · 3d592ece | 2.7.0 · 3d592ece | Unchanged |
| Reth dev | 2.7.0 · 43a93dbc | 2.7.0 · 5b686303 | Updated |

## Verdict changes

7 verdicts changed for 2 clients.

### [Anvil](clients/anvil.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H09 · Failed frame results and error labels](decisions/H09.md) | Anvil dev | ⚠️ Differs | 🟡 Partially assessed |
| [H20 · vmTrace step timing and deltas](decisions/H20.md) | Anvil dev | ⚠️ Differs | 🟡 Partially assessed |

### [Nethermind](clients/nethermind.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H13 · Signed transaction execution validity](decisions/H13.md) | Nethermind dev | ⚠️ Differs | 🟡 Partially assessed |
| [H14 · Invalid parameters and rejected calls](decisions/H14.md) | Nethermind dev | ⚠️ Differs | ❔ Policy open |
| [H15 · Unsigned simulation fees and block environment](decisions/H15.md) | Nethermind dev | ⚠️ Differs | 🟡 Partially assessed |
| [H32 · Trace block tags and pending state](decisions/H32.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |
