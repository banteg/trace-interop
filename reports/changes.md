# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-09-28T17:01:47.435177+00:00**, [preflight](../evidence/2026-09-28/eval/preflight.json)) against the previous one (checked at **2026-09-27T18:12:29.400867+00:00**, [preflight](../evidence/2026-09-27/eval/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.8.3 · cae51ad4 | 1.8.3 · cae51ad4 | Unchanged |
| Anvil dev | 1.8.4-nightly · 07915e32 | 1.8.4-nightly · dd372126 | Updated |
| Besu stable | 26.9.0 · ee9c64c8 | 26.9.0 · ee9c64c8 | Unchanged |
| Besu dev | 26.9-develop · accdae00 | 26.9-develop · c197ac57 | Updated |
| Erigon stable | 3.7.0 · bdc78cc4 | 3.7.0 · bdc78cc4 | Unchanged |
| Erigon dev | 3.8.0-dev · 3904de43 | 3.8.0-dev · a1ce80fb | Updated |
| Geth draft fork | 1.17.7-unstable · e26833e3 | 1.17.7-unstable · e26833e3 | Unchanged |
| Nethermind stable | 2.0.0 · bec830cd | 2.0.0 · bec830cd | Unchanged |
| Nethermind dev | 2.1.0-preview · 5ece5fba | 2.1.0-preview · 45912ba3 | Updated |
| Reth stable | 2.6.0 · 73a3a008 | 2.7.0 · 3d592ece | Updated |
| Reth dev | 2.5.2 · 863f7055 | 2.5.2 · 5723a3fe | Updated |

## Verdict changes

17 verdicts changed for 2 clients.

### [Erigon](clients/erigon.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H08 · Empty output and unrequested components](decisions/H08.md) | Erigon dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H11 · Empty trace-type selection](decisions/H11.md) | Erigon dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H16 · Fee accounting and sequential state diffs](decisions/H16.md) | Erigon dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H17 · New-account stateDiff encoding](decisions/H17.md) | Erigon dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H19 · vmTrace executing bytecode](decisions/H19.md) | Erigon dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H21 · vmTrace numeric and optional metadata encoding](decisions/H21.md) | Erigon dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H30 · Omitted trace_filter range bounds](decisions/H30.md) | Erigon dev | ⚠️ Differs | ✅ Checked cases agree |

### [Reth](clients/reth.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H02 · trace_get selector and return shape](decisions/H02.md) | Reth stable | ⚠️ Differs | ✅ Checked cases agree |
| [H03 · Filter composition and mode](decisions/H03.md) | Reth stable | ⚠️ Differs | ✅ Checked cases agree |
| [H05 · Post-merge reward records](decisions/H05.md) | Reth stable | ⚠️ Differs | ✅ Checked cases agree |
| [H07 · Replay transactionHash field](decisions/H07.md) | Reth stable | ⚠️ Differs | ✅ Checked cases agree |
| [H16 · Fee accounting and sequential state diffs](decisions/H16.md) | Reth stable | ⚠️ Differs | ✅ Checked cases agree |
| [H17 · New-account stateDiff encoding](decisions/H17.md) | Reth stable | ⚠️ Differs | ✅ Checked cases agree |
| [H18 · EIP-7702 code changes in stateDiff](decisions/H18.md) | Reth stable | ⚠️ Differs | ✅ Checked cases agree |
| [H19 · vmTrace executing bytecode](decisions/H19.md) | Reth stable | ⚠️ Differs | ✅ Checked cases agree |
| [H30 · Omitted trace_filter range bounds](decisions/H30.md) | Reth stable | ⚠️ Differs | ✅ Checked cases agree |
| [H31 · Omitted trace_callMany block](decisions/H31.md) | Reth stable | ⚠️ Differs | ✅ Checked cases agree |
