# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-09-29T21:59:40.336677+00:00**, [preflight](../evidence/2026-09-30/refresh/preflight.json)) against the previous one (checked at **2026-09-29T08:19:31.590286+00:00**, [preflight](../evidence/2026-09-29/refresh/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.8.3 · cae51ad4 | 1.8.3 · cae51ad4 | Unchanged |
| Anvil dev | 1.8.4-nightly · 00989695 | 1.8.4-nightly · 00989695 | Unchanged |
| Besu stable | 26.9.0 · ee9c64c8 | 26.9.0 · ee9c64c8 | Unchanged |
| Besu dev | 26.9-develop · c197ac57 | 26.9-develop · 3cbf077c | Updated |
| Erigon stable | 3.7.0 · bdc78cc4 | 3.7.0 · bdc78cc4 | Unchanged |
| Erigon dev | 3.8.0-dev · a2a19253 | 3.8.0-dev · 85e1ca92 | Updated |
| Geth draft fork | 1.17.7-unstable · e26833e3 | 1.17.7-unstable · e26833e3 | Unchanged |
| Nethermind stable | 2.0.0 · bec830cd | 2.0.0 · bec830cd | Unchanged |
| Nethermind dev | 2.2.0-preview · 287f54f0 | 2.2.0-preview · f69690c5 | Updated |
| Reth stable | 2.7.0 · 3d592ece | 2.7.0 · 3d592ece | Unchanged |
| Reth dev | 2.7.0 · 60aeb532 | 2.7.0 · 60aeb532 | Unchanged |

## Verdict changes

18 verdicts changed for 6 clients.

### [Anvil](clients/anvil.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Anvil stable | ⚪ Not assessed | ⚠️ Differs |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Anvil dev | ⚪ Not assessed | ⚠️ Differs |

### [Besu](clients/besu.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Besu stable | 🔎 Control / not applicable | ⚠️ Differs |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Besu dev | 🔎 Control / not applicable | ⚠️ Differs |

### [Erigon](clients/erigon.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Erigon stable | 🚧 Blocked | ⚠️ Differs |
| [H06 · Missing transactions and paths](decisions/H06.md) | Erigon dev | ⚠️ Differs | ✅ Checked cases agree |
| [H16 · Fee accounting and sequential state diffs](decisions/H16.md) | Erigon dev | ✅ Checked cases agree | 🟡 Partially assessed |
| [H20 · vmTrace step timing and deltas](decisions/H20.md) | Erigon dev | ⚠️ Differs | ✅ Checked cases agree |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Erigon dev | 🚧 Blocked | ⚠️ Differs |

### [Geth draft fork](clients/geth.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H16 · Fee accounting and sequential state diffs](decisions/H16.md) | Geth draft fork | ✅ Checked cases agree | 🟡 Partially assessed |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Geth draft fork | 🔎 Control / not applicable | ✅ Checked cases agree |

### [Nethermind](clients/nethermind.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Nethermind stable | 🔎 Control / not applicable | ⚠️ Differs |
| [H06 · Missing transactions and paths](decisions/H06.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |
| [H16 · Fee accounting and sequential state diffs](decisions/H16.md) | Nethermind dev | ✅ Checked cases agree | 🟡 Partially assessed |
| [H23 · Special-action address matching](decisions/H23.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Nethermind dev | 🔎 Control / not applicable | ⚠️ Differs |

### [Reth](clients/reth.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Reth stable | 🔎 Control / not applicable | ⚠️ Differs |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Reth dev | 🔎 Control / not applicable | ⚠️ Differs |
