# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-11-09T13:27:57.706035+00:00**, [preflight](../evidence/2026-11-09/eval/preflight.json)) against the previous one (checked at **2026-10-29T12:46:43.495599+00:00**, [preflight](../evidence/2026-10-29/eval/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.8.6 · 6bad0a66 | 1.9.0 · 6056c584 | Updated |
| Anvil dev | 1.8.7-nightly · 716e795c | 1.9.1-nightly · 6165f031 | Updated |
| Besu stable | 26.10.2 · d3e1aea7 | 26.11.0 · 0e595f9e | Updated |
| Besu dev | 26.10-develop · 7f08e68a | 26.11-develop · 3f41096a | Updated |
| Erigon stable | 3.8.1 · cf6f1413 | 3.8.1 · cf6f1413 | Unchanged |
| Erigon dev | 3.9.0-dev · 6955d198 | 3.9.0-dev · cf91acee | Updated |
| Geth draft fork | 1.17.11-unstable · 0f1fb2ae | 1.17.11-unstable · e487da1e | Updated |
| Nethermind stable | 2.2.2 · be201120 | 2.2.2 · be201120 | Unchanged |
| Nethermind dev | 2.3.0-preview · fc9abf09 | 2.3.0-preview · 4079edfa | Updated |
| Reth stable | 2.9.0 · c9a780f4 | 2.10.1 · 58ebce14 | Updated |
| Reth dev | 2.8.1 · 966010c9 | 2.10.1 · 5efe80f5 | Updated |

## Verdict changes

20 verdicts changed for 2 clients.

### [Anvil](clients/anvil.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H06 · Missing transactions and paths](decisions/H06.md) | Anvil stable | ⚠️ Differs | ✅ Checked cases agree |
| [H09 · Failed frame results and error labels](decisions/H09.md) | Anvil stable | 🟡 Partially assessed | ✅ Checked cases agree |
| [H14 · Invalid parameters and rejected calls](decisions/H14.md) | Anvil stable | ⚠️ Differs | ✅ Checked cases agree |
| [H15 · Unsigned simulation fees and block environment](decisions/H15.md) | Anvil stable | ⚠️ Differs | ✅ Checked cases agree |
| [H16 · Fee accounting and sequential state diffs](decisions/H16.md) | Anvil stable | 🟡 Partially assessed | ✅ Checked cases agree |
| [H17 · New-account stateDiff encoding](decisions/H17.md) | Anvil stable | 🟡 Partially assessed | ✅ Checked cases agree |
| [H18 · EIP-7702 code changes in stateDiff](decisions/H18.md) | Anvil stable | 🟡 Partially assessed | ✅ Checked cases agree |
| [H19 · vmTrace executing bytecode](decisions/H19.md) | Anvil stable | 🟡 Partially assessed | ✅ Checked cases agree |
| [H20 · vmTrace step timing and deltas](decisions/H20.md) | Anvil stable | 🟡 Partially assessed | ✅ Checked cases agree |
| [H23 · Special-action address matching](decisions/H23.md) | Anvil stable | 🟡 Partially assessed | ⚠️ Differs |
| [H26 · Account deletion across Cancun](decisions/H26.md) | Anvil stable | 🟡 Partially assessed | ⚠️ Differs |
| [H28 · Historical state at system-operation boundaries](decisions/H28.md) | Anvil stable | 🚧 Blocked | ✅ Checked cases agree |
| [H06 · Missing transactions and paths](decisions/H06.md) | Anvil dev | ⚠️ Differs | ✅ Checked cases agree |

### [Besu](clients/besu.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H01 · Method coverage](decisions/H01.md) | Besu dev | ⛔ Method unavailable | ✅ Checked cases agree |
| [H07 · Replay transactionHash field](decisions/H07.md) | Besu dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H08 · Empty output and unrequested components](decisions/H08.md) | Besu dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H14 · Invalid parameters and rejected calls](decisions/H14.md) | Besu dev | ⚠️ Differs | ✅ Checked cases agree |
| [H18 · EIP-7702 code changes in stateDiff](decisions/H18.md) | Besu dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H19 · vmTrace executing bytecode](decisions/H19.md) | Besu dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H32 · Trace block tags and pending state](decisions/H32.md) | Besu dev | ⚠️ Differs | ✅ Checked cases agree |
