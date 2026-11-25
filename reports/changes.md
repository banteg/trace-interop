# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-11-25T15:07:31.009461+00:00**, [preflight](../evidence/2026-11-25/eval/preflight.json)) against the previous one (checked at **2026-11-09T13:27:57.706035+00:00**, [preflight](../evidence/2026-11-09/eval/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.9.0 · 6056c584 | 1.10.0 · 083e2299 | Updated |
| Anvil dev | 1.9.1-nightly · 6165f031 | 1.10.1-nightly · 50d75f19 | Updated |
| Besu stable | 26.11.0 · 0e595f9e | 26.11.2 · 09b9e94d | Updated |
| Besu dev | 26.11-develop · 3f41096a | 26.11-develop · f58f40e2 | Updated |
| Erigon stable | 3.8.1 · cf6f1413 | 3.8.2 · 8a3f3b2c | Updated |
| Erigon dev | 3.9.0-dev · cf91acee | 3.9.0-dev · e91aca7f | Updated |
| Geth draft fork | 1.17.11-unstable · e487da1e | 1.17.11-unstable · edbd5f17 | Updated |
| Nethermind stable | 2.2.2 · be201120 | 2.2.2 · be201120 | Unchanged |
| Nethermind dev | 2.3.0-preview · 4079edfa | 2.4.0-preview · e2f069a6 | Updated |
| Reth stable | 2.10.1 · 58ebce14 | 2.11.0 · b9abbcc1 | Updated |
| Reth dev | 2.10.1 · 5efe80f5 | 2.11.0 · 7f5e740c | Updated |

## Verdict changes

36 verdicts changed for 5 clients.

### [Anvil](clients/anvil.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H04 · Empty address lists](decisions/H04.md) | Anvil stable | ⚠️ Differs | ✅ Checked cases agree |
| [H20 · vmTrace step timing and deltas](decisions/H20.md) | Anvil stable | ✅ Checked cases agree | ⚠️ Differs |
| [H23 · Special-action address matching](decisions/H23.md) | Anvil stable | ⚠️ Differs | ✅ Checked cases agree |
| [H26 · Account deletion across Cancun](decisions/H26.md) | Anvil stable | ⚠️ Differs | ✅ Checked cases agree |
| [H04 · Empty address lists](decisions/H04.md) | Anvil dev | ⚠️ Differs | ✅ Checked cases agree |
| [H20 · vmTrace step timing and deltas](decisions/H20.md) | Anvil dev | ✅ Checked cases agree | ⚠️ Differs |
| [H23 · Special-action address matching](decisions/H23.md) | Anvil dev | ⚠️ Differs | ✅ Checked cases agree |
| [H26 · Account deletion across Cancun](decisions/H26.md) | Anvil dev | ⚠️ Differs | ✅ Checked cases agree |

### [Besu](clients/besu.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H01 · Method coverage](decisions/H01.md) | Besu stable | ⛔ Method unavailable | ✅ Checked cases agree |
| [H07 · Replay transactionHash field](decisions/H07.md) | Besu stable | 🟡 Partially assessed | ✅ Checked cases agree |
| [H08 · Empty output and unrequested components](decisions/H08.md) | Besu stable | 🟡 Partially assessed | ✅ Checked cases agree |
| [H10 · Creation result field names](decisions/H10.md) | Besu stable | ⚠️ Differs | ✅ Checked cases agree |
| [H13 · Signed transaction execution validity](decisions/H13.md) | Besu stable | ⚠️ Differs | 🟡 Partially assessed |
| [H15 · Unsigned simulation fees and block environment](decisions/H15.md) | Besu stable | 🟡 Partially assessed | ⚠️ Differs |
| [H17 · New-account stateDiff encoding](decisions/H17.md) | Besu stable | 🟡 Partially assessed | ✅ Checked cases agree |
| [H18 · EIP-7702 code changes in stateDiff](decisions/H18.md) | Besu stable | 🟡 Partially assessed | ✅ Checked cases agree |
| [H19 · vmTrace executing bytecode](decisions/H19.md) | Besu stable | 🟡 Partially assessed | ✅ Checked cases agree |
| [H22 · Precompile return bytes](decisions/H22.md) | Besu stable | ⚠️ Differs | ✅ Checked cases agree |
| [H24 · Sibling failure isolation](decisions/H24.md) | Besu stable | ⚠️ Differs | ✅ Checked cases agree |
| [H26 · Account deletion across Cancun](decisions/H26.md) | Besu stable | ⚠️ Differs | ✅ Checked cases agree |
| [H32 · Trace block tags and pending state](decisions/H32.md) | Besu stable | ⚠️ Differs | ✅ Checked cases agree |
| [H10 · Creation result field names](decisions/H10.md) | Besu dev | ⚠️ Differs | ✅ Checked cases agree |
| [H13 · Signed transaction execution validity](decisions/H13.md) | Besu dev | ⚠️ Differs | 🟡 Partially assessed |
| [H17 · New-account stateDiff encoding](decisions/H17.md) | Besu dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H22 · Precompile return bytes](decisions/H22.md) | Besu dev | ⚠️ Differs | ✅ Checked cases agree |
| [H24 · Sibling failure isolation](decisions/H24.md) | Besu dev | ⚠️ Differs | ✅ Checked cases agree |
| [H26 · Account deletion across Cancun](decisions/H26.md) | Besu dev | ⚠️ Differs | ✅ Checked cases agree |

### [Erigon](clients/erigon.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H05 · Post-merge reward records](decisions/H05.md) | Erigon stable | ⚠️ Differs | ✅ Checked cases agree |
| [H06 · Missing transactions and paths](decisions/H06.md) | Erigon stable | ⚠️ Differs | ✅ Checked cases agree |
| [H15 · Unsigned simulation fees and block environment](decisions/H15.md) | Erigon stable | ✅ Checked cases agree | ⚠️ Differs |
| [H21 · vmTrace numeric and optional metadata encoding](decisions/H21.md) | Erigon stable | ⚠️ Differs | ✅ Checked cases agree |
| [H15 · Unsigned simulation fees and block environment](decisions/H15.md) | Erigon dev | ✅ Checked cases agree | ⚠️ Differs |

### [Nethermind](clients/nethermind.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H14 · Invalid parameters and rejected calls](decisions/H14.md) | Nethermind dev | ✅ Checked cases agree | ⚠️ Differs |

### [Reth](clients/reth.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H04 · Empty address lists](decisions/H04.md) | Reth dev | ⚠️ Differs | ✅ Checked cases agree |
| [H23 · Special-action address matching](decisions/H23.md) | Reth dev | 🟡 Partially assessed | ✅ Checked cases agree |
| [H33 · Single-block hash selection in trace_filter](decisions/H33.md) | Reth dev | ⚠️ Differs | ✅ Checked cases agree |
