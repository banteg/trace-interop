# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-09-28T23:39:02.591371+00:00**, [preflight](../evidence/2026-09-29/eval/preflight.json)) against the previous one (checked at **2026-09-28T17:01:47.435177+00:00**, [preflight](../evidence/2026-09-28/eval/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.8.3 · cae51ad4 | 1.8.3 · cae51ad4 | Unchanged |
| Anvil dev | 1.8.4-nightly · dd372126 | 1.8.4-nightly · dd372126 | Unchanged |
| Besu stable | 26.9.0 · ee9c64c8 | 26.9.0 · ee9c64c8 | Unchanged |
| Besu dev | 26.9-develop · c197ac57 | 26.9-develop · c197ac57 | Unchanged |
| Erigon stable | 3.7.0 · bdc78cc4 | 3.7.0 · bdc78cc4 | Unchanged |
| Erigon dev | 3.8.0-dev · a1ce80fb | 3.8.0-dev · 558586f0 | Updated |
| Geth draft fork | 1.17.7-unstable · e26833e3 | 1.17.7-unstable · e26833e3 | Unchanged |
| Nethermind stable | 2.0.0 · bec830cd | 2.0.0 · bec830cd | Unchanged |
| Nethermind dev | 2.1.0-preview · 45912ba3 | 2.1.0-preview · 82516987 | Updated |
| Reth stable | 2.7.0 · 3d592ece | 2.7.0 · 3d592ece | Unchanged |
| Reth dev | 2.5.2 · 5723a3fe | 2.5.2 · 5723a3fe | Unchanged |

## Verdict changes

9 verdicts changed for 2 clients.

### [Erigon](clients/erigon.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H09 · Failed frame results and error labels](decisions/H09.md) | Erigon dev | ⚠️ Differs | ✅ Checked cases agree |
| [H15 · Unsigned simulation fees and block environment](decisions/H15.md) | Erigon dev | ⚠️ Differs | 🟡 Partially assessed |
| [H23 · Special-action address matching](decisions/H23.md) | Erigon dev | ⚠️ Differs | ✅ Checked cases agree |

### [Nethermind](clients/nethermind.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H03 · Filter composition and mode](decisions/H03.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |
| [H04 · Empty address lists](decisions/H04.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |
| [H05 · Post-merge reward records](decisions/H05.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |
| [H20 · vmTrace step timing and deltas](decisions/H20.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |
| [H29 · Precompile call-frame inclusion](decisions/H29.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |
| [H30 · Omitted trace_filter range bounds](decisions/H30.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |
