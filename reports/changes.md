# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-09-29T08:19:31.590286+00:00**, [preflight](../evidence/2026-09-29/refresh/preflight.json)) against the previous one (checked at **2026-09-28T23:39:02.591371+00:00**, [preflight](../evidence/2026-09-29/eval/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.8.3 · cae51ad4 | 1.8.3 · cae51ad4 | Unchanged |
| Anvil dev | 1.8.4-nightly · dd372126 | 1.8.4-nightly · 00989695 | Updated |
| Besu stable | 26.9.0 · ee9c64c8 | 26.9.0 · ee9c64c8 | Unchanged |
| Besu dev | 26.9-develop · c197ac57 | 26.9-develop · c197ac57 | Unchanged |
| Erigon stable | 3.7.0 · bdc78cc4 | 3.7.0 · bdc78cc4 | Unchanged |
| Erigon dev | 3.8.0-dev · 558586f0 | 3.8.0-dev · a2a19253 | Updated |
| Geth draft fork | 1.17.7-unstable · e26833e3 | 1.17.7-unstable · e26833e3 | Unchanged |
| Nethermind stable | 2.0.0 · bec830cd | 2.0.0 · bec830cd | Unchanged |
| Nethermind dev | 2.1.0-preview · 82516987 | 2.2.0-preview · 287f54f0 | Updated |
| Reth stable | 2.7.0 · 3d592ece | 2.7.0 · 3d592ece | Unchanged |
| Reth dev | 2.5.2 · 5723a3fe | 2.7.0 · 60aeb532 | Updated |

## Verdict changes

1 verdict changed for 1 client.

### [Nethermind](clients/nethermind.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H09 · Failed frame results and error labels](decisions/H09.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |
