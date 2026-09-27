# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-09-27T18:12:29.400867+00:00**, [preflight](../evidence/2026-09-27/eval/preflight.json)) against the previous one (checked at **2026-09-26T08:35:29.730208+00:00**, [preflight](../evidence/2026-09-26/anvil/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.8.3 · cae51ad4 | 1.8.3 · cae51ad4 | Unchanged |
| Anvil dev | 1.8.4-nightly · 5a99f1a8 | 1.8.4-nightly · 07915e32 | Updated |
| Besu stable | 26.9.0 · ee9c64c8 | 26.9.0 · ee9c64c8 | Unchanged |
| Besu dev | 26.9-develop · accdae00 | 26.9-develop · accdae00 | Unchanged |
| Erigon stable | 3.7.0 · bdc78cc4 | 3.7.0 · bdc78cc4 | Unchanged |
| Erigon dev | 3.8.0-dev · 7853b922 | 3.8.0-dev · 3904de43 | Updated |
| Geth draft fork | 1.17.7-unstable · c8449896 | 1.17.7-unstable · e26833e3 | Updated |
| Nethermind stable | 2.0.0 · bec830cd | 2.0.0 · bec830cd | Unchanged |
| Nethermind dev | 2.1.0-preview · fca93966 | 2.1.0-preview · 5ece5fba | Updated |
| Reth stable | 2.6.0 · 73a3a008 | 2.6.0 · 73a3a008 | Unchanged |
| Reth dev | 2.5.2 · df7b7fdf | 2.5.2 · 863f7055 | Updated |

## Verdict changes

9 verdicts changed for 3 clients.

### [Anvil](clients/anvil.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H03 · Filter composition and mode](decisions/H03.md) | Anvil dev | ⚠️ Differs | ✅ Checked cases agree |
| [H08 · Empty output and unrequested components](decisions/H08.md) | Anvil dev | ⚠️ Differs | ✅ Checked cases agree |
| [H18 · EIP-7702 code changes in stateDiff](decisions/H18.md) | Anvil dev | ⚠️ Differs | 🟡 Partially assessed |
| [H19 · vmTrace executing bytecode](decisions/H19.md) | Anvil dev | ⚠️ Differs | 🟡 Partially assessed |
| [H26 · Account deletion across Cancun](decisions/H26.md) | Anvil dev | 🟡 Partially assessed | ⚠️ Differs |
| [H30 · Omitted trace_filter range bounds](decisions/H30.md) | Anvil dev | ⚠️ Differs | ✅ Checked cases agree |
| [H31 · Omitted trace_callMany block](decisions/H31.md) | Anvil dev | ⚠️ Differs | ✅ Checked cases agree |

### [Geth draft fork](clients/geth.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H32 · Trace block tags and pending state](decisions/H32.md) | Geth draft fork | ✅ Checked cases agree | 🟡 Partially assessed |

### [Nethermind](clients/nethermind.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H25 · Well-formed errors for rejected raw transactions](decisions/H25.md) | Nethermind dev | ⚠️ Differs | ✅ Checked cases agree |
