# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-09-30T13:03:47.160133+00:00**, [preflight](../evidence/2026-09-30/eval/preflight.json)) against the previous one (checked at **2026-09-29T21:59:40.336677+00:00**, [preflight](../evidence/2026-09-30/refresh/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.8.3 · cae51ad4 | 1.8.3 · cae51ad4 | Unchanged |
| Anvil dev | 1.8.4-nightly · 00989695 | 1.8.4-nightly · e3429853 | Updated |
| Besu stable | 26.9.0 · ee9c64c8 | 26.9.0 · ee9c64c8 | Unchanged |
| Besu dev | 26.9-develop · 3cbf077c | 26.9-develop · 67ce4ab1 | Updated |
| Erigon stable | 3.7.0 · bdc78cc4 | 3.7.0 · bdc78cc4 | Unchanged |
| Erigon dev | 3.8.0-dev · 85e1ca92 | 3.8.0-dev · 923b4d31 | Updated |
| Geth draft fork | 1.17.7-unstable · e26833e3 | 1.17.7-unstable · ec1cec0b | Updated |
| Nethermind stable | 2.0.0 · bec830cd | 2.0.0 · bec830cd | Unchanged |
| Nethermind dev | 2.2.0-preview · f69690c5 | 2.2.0-preview · 79173d14 | Updated |
| Reth stable | 2.7.0 · 3d592ece | 2.7.0 · 3d592ece | Unchanged |
| Reth dev | 2.7.0 · 60aeb532 | 2.7.0 · 43a93dbc | Updated |

## Verdict changes

1 verdict changed for 1 client.

### [Geth draft fork](clients/geth.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Geth draft fork | ⚠️ Differs | ✅ Checked cases agree |
