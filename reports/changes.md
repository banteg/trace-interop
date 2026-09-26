# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-09-26T06:31:54.559335+00:00**, [preflight](../evidence/2026-09-26/eval/preflight.json)) against the previous one (checked at **2026-09-25T08:32:17.467627+00:00**, [preflight](../evidence/2026-09-25/refresh/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Besu stable | 26.8.1 · d97cbd61 | 26.9.0 · ee9c64c8 | Updated |
| Besu dev | 26.9-develop · accdae00 | 26.9-develop · accdae00 | Unchanged |
| Erigon stable | 3.7.0 · bdc78cc4 | 3.7.0 · bdc78cc4 | Unchanged |
| Erigon dev | 3.8.0-dev · f8cfe5a7 | 3.8.0-dev · 7853b922 | Updated |
| Geth draft fork | 1.17.7-unstable · 0a663f3c | 1.17.7-unstable · c8449896 | Updated |
| Nethermind stable | 2.0.0 · bec830cd | 2.0.0 · bec830cd | Unchanged |
| Nethermind dev | 2.1.0-preview · ee1f57da | 2.1.0-preview · b4211ad9 | Updated |
| Reth stable | 2.6.0 · 73a3a008 | 2.6.0 · 73a3a008 | Unchanged |
| Reth dev | 2.5.2 · 4630cc58 | 2.5.2 · df7b7fdf | Updated |

## Verdict changes

7 verdicts changed for 3 clients.

### [Erigon](clients/erigon.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H05 · Post-merge reward records](decisions/H05.md) | Erigon dev | ⚠️ Differs | ✅ Checked cases agree |
| [H28 · Historical state at system-operation boundaries](decisions/H28.md) | Erigon dev | ⚠️ Differs | ✅ Checked cases agree |

### [Geth draft fork](clients/geth.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H09 · Failed frame results and error labels](decisions/H09.md) | Geth draft fork | 🟡 Partially assessed | ✅ Checked cases agree |
| [H29 · Precompile call-frame inclusion](decisions/H29.md) | Geth draft fork | ⚠️ Differs | ✅ Checked cases agree |

### [Reth](clients/reth.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H17 · New-account stateDiff encoding](decisions/H17.md) | Reth dev | ⚠️ Differs | ✅ Checked cases agree |
| [H18 · EIP-7702 code changes in stateDiff](decisions/H18.md) | Reth dev | ⚠️ Differs | ✅ Checked cases agree |
| [H19 · vmTrace executing bytecode](decisions/H19.md) | Reth dev | ⚠️ Differs | ✅ Checked cases agree |
