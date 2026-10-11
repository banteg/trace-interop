# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-10-11T12:46:46.611161+00:00**, [preflight](../evidence/2026-10-11/eval/preflight.json)) against the previous one (checked at **2026-10-05T19:51:21.922482+00:00**, [preflight](../evidence/2026-10-05/eval/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.8.5 · 51a52c59 | 1.8.5 · 51a52c59 | Unchanged |
| Anvil dev | 1.8.4-nightly · e15c2f1c | 1.8.6-nightly · 32624734 | Updated |
| Besu stable | 26.9.0 · ee9c64c8 | 26.9.0 · ee9c64c8 | Unchanged |
| Besu dev | 26.10-develop · 1d62d893 | 26.10-develop · d05d8e74 | Updated |
| Erigon stable | 3.7.1 · 8c1e3893 | 3.7.1 · 8c1e3893 | Unchanged |
| Erigon dev | 3.8.0-dev · 96188a47 | 3.8.0-dev · 1d3ebbf2 | Updated |
| Geth draft fork | 1.17.7-unstable · e67cfd25 | 1.17.7-unstable · e67cfd25 | Unchanged |
| Nethermind stable | 2.1.0 · b3e7e84c | 2.1.0 · b3e7e84c | Unchanged |
| Nethermind dev | 2.2.0-preview · e8955c4c | 2.2.0-preview · 204457ad | Updated |
| Reth stable | 2.7.0 · 3d592ece | 2.7.0 · 3d592ece | Unchanged |
| Reth dev | 2.7.0 · 42fa3c56 | 2.7.0 · 1a4dbbe1 | Updated |

## Verdict changes

15 verdicts changed for 2 clients.

### [Anvil](clients/anvil.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H06 · Missing transactions and paths](decisions/H06.md) | Anvil dev | ⚠️ Differs | ✅ Checked cases agree |
| [H09 · Failed frame results and error labels](decisions/H09.md) | Anvil dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H14 · Invalid parameters and rejected calls](decisions/H14.md) | Anvil dev | ⚠️ Differs | ✅ Checked cases agree |
| [H15 · Unsigned simulation fees and block environment](decisions/H15.md) | Anvil dev | ⚠️ Differs | ✅ Checked cases agree |
| [H16 · Fee accounting and sequential state diffs](decisions/H16.md) | Anvil dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H17 · New-account stateDiff encoding](decisions/H17.md) | Anvil dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H18 · EIP-7702 code changes in stateDiff](decisions/H18.md) | Anvil dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H19 · vmTrace executing bytecode](decisions/H19.md) | Anvil dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H20 · vmTrace step timing and deltas](decisions/H20.md) | Anvil dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H23 · Special-action address matching](decisions/H23.md) | Anvil dev | 🟡 Partially assessed | ⚠️ Differs |
| [H26 · Account deletion across Cancun](decisions/H26.md) | Anvil dev | 🟡 Partially assessed | ⚠️ Differs |
| [H28 · Historical state at system-operation boundaries](decisions/H28.md) | Anvil dev | 🚧 Blocked | ✅ Checked cases agree |
| [H29 · Precompile call-frame inclusion](decisions/H29.md) | Anvil dev | ⚠️ Differs | ✅ Checked cases agree |

### [Besu](clients/besu.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H15 · Unsigned simulation fees and block environment](decisions/H15.md) | Besu dev | ⚠️ Differs | 🟡 Partially assessed |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Besu dev | ⚠️ Differs | 🟡 Partially assessed |
