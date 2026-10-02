# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-10-02T14:41:05.957366+00:00**, [preflight](../evidence/2026-10-02/eval/preflight.json)) against the previous one (checked at **2026-10-01T11:19:31.990714+00:00**, [preflight](../evidence/2026-10-01/eval/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Anvil stable | 1.8.3 · cae51ad4 | 1.8.4 · 50af4efe | Updated |
| Anvil dev | 1.8.4-nightly · df92604b | 1.8.4-nightly · 328811cb | Updated |
| Besu stable | 26.9.0 · ee9c64c8 | 26.9.0 · ee9c64c8 | Unchanged |
| Besu dev | 26.10-develop · 28edf391 | 26.10-develop · 711f8142 | Updated |
| Erigon stable | 3.7.0 · bdc78cc4 | 3.7.1 · 8c1e3893 | Updated |
| Erigon dev | 3.8.0-dev · 50e2cc4f | 3.8.0-dev · 6da806cb | Updated |
| Geth draft fork | 1.17.7-unstable · 67f41dea | 1.17.7-unstable · 67f41dea | Unchanged |
| Nethermind stable | 2.0.0 · bec830cd | 2.1.0 · b3e7e84c | Updated |
| Nethermind dev | 2.2.0-preview · 759efed7 | 2.2.0-preview · 3370d566 | Updated |
| Reth stable | 2.7.0 · 3d592ece | 2.7.0 · 3d592ece | Unchanged |
| Reth dev | 2.7.0 · 5b686303 | 2.7.0 · 078d0262 | Updated |

## Verdict changes

18 verdicts changed for 3 clients.

### [Anvil](clients/anvil.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H03 · Filter composition and mode](decisions/H03.md) | Anvil stable | ⚠️ Differs | ✅ Checked cases agree |
| [H08 · Empty output and unrequested components](decisions/H08.md) | Anvil stable | ⚠️ Differs | ✅ Checked cases agree |
| [H09 · Failed frame results and error labels](decisions/H09.md) | Anvil stable | ⚠️ Differs | 🟡 Partially assessed |
| [H17 · New-account stateDiff encoding](decisions/H17.md) | Anvil stable | ⚠️ Differs | 🟡 Partially assessed |
| [H18 · EIP-7702 code changes in stateDiff](decisions/H18.md) | Anvil stable | ⚠️ Differs | 🟡 Partially assessed |
| [H19 · vmTrace executing bytecode](decisions/H19.md) | Anvil stable | ⚠️ Differs | 🟡 Partially assessed |
| [H20 · vmTrace step timing and deltas](decisions/H20.md) | Anvil stable | ⚠️ Differs | 🟡 Partially assessed |
| [H30 · Omitted trace_filter range bounds](decisions/H30.md) | Anvil stable | ⚠️ Differs | ✅ Checked cases agree |
| [H31 · Omitted trace_callMany block](decisions/H31.md) | Anvil stable | ⚠️ Differs | ✅ Checked cases agree |
| [H17 · New-account stateDiff encoding](decisions/H17.md) | Anvil dev | ⚠️ Differs | 🟡 Partially assessed |
| [H26 · Account deletion across Cancun](decisions/H26.md) | Anvil dev | ⚠️ Differs | 🟡 Partially assessed |

### [Besu](clients/besu.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H11 · Empty trace-type selection](decisions/H11.md) | Besu dev | ⚠️ Differs | ✅ Checked cases agree |
| [H25 · Well-formed errors for rejected raw transactions](decisions/H25.md) | Besu dev | ⚠️ Differs | ✅ Checked cases agree |

### [Nethermind](clients/nethermind.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H08 · Empty output and unrequested components](decisions/H08.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H11 · Empty trace-type selection](decisions/H11.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H16 · Fee accounting and sequential state diffs](decisions/H16.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H17 · New-account stateDiff encoding](decisions/H17.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
| [H26 · Account deletion across Cancun](decisions/H26.md) | Nethermind stable | ⚠️ Differs | ✅ Checked cases agree |
