# Changes since the previous matrix

[All reports](README.md) · [Test status key](technical.md#test-status-key)

Captured check verdicts per decision and build: the current matrix (builds checked at **2026-09-24T21:54:10.993904+00:00**, [preflight](../evidence/2026-09-25/fixture-wave/preflight.json)) against the previous one (checked at **2026-09-24T18:52:50.958598+00:00**, [preflight](../evidence/2026-09-24/adopted-stances/preflight.json)). The same code, ledger, corpus expectations and pinned draft assess both, so a change comes from the captured builds and evidence, not from a reassessment. Builds are paired by client and update channel. Submitted-fix markers (🛠️) are not compared; see [client fixes](../docs/client-fixes.md).

## Builds

| Client | Previous | Current | Change |
| --- | --- | --- | --- |
| Besu stable | 26.8.1 · d97cbd61 | 26.8.1 · d97cbd61 | Unchanged |
| Besu dev | 26.9-develop · 85b32978 | 26.9-develop · cf89071f | Updated |
| Erigon stable | 3.6.1 · 0c4d9c91 | 3.6.1 · 0c4d9c91 | Unchanged |
| Erigon dev | 3.8.0-dev · e26d9bd4 | 3.8.0-dev · 01c118ee | Updated |
| Geth draft fork | 1.17.7-unstable · bb5c4682 | 1.17.7-unstable · 0a663f3c | Updated |
| Nethermind stable | 2.0.0 · bec830cd | 2.0.0 · bec830cd | Unchanged |
| Nethermind dev | 2.1.0-preview · ce501a97 | 2.1.0-preview · 54b760cd | Updated |
| Reth stable | 2.6.0 · 73a3a008 | 2.6.0 · 73a3a008 | Unchanged |
| Reth dev | 2.5.2 · 58a51b3e | 2.5.2 · 58a51b3e | Unchanged |

## Verdict changes

23 verdicts changed for 5 clients.

### [Besu](clients/besu.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H26 · Account deletion across Cancun](decisions/H26.md) | Besu stable | ✅ Checked cases agree | ⚠️ Differs |
| [H28 · Historical state at system-operation boundaries](decisions/H28.md) | Besu stable | ✅ Checked cases agree | ⚠️ Differs |
| [H26 · Account deletion across Cancun](decisions/H26.md) | Besu dev | ✅ Checked cases agree | ⚠️ Differs |
| [H28 · Historical state at system-operation boundaries](decisions/H28.md) | Besu dev | ✅ Checked cases agree | ⚠️ Differs |

### [Erigon](clients/erigon.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H05 · Post-merge reward records](decisions/H05.md) | Erigon stable | ✅ Checked cases agree | ⚠️ Differs |
| [H23 · Special-action address matching](decisions/H23.md) | Erigon stable | ✅ Checked cases agree | ⚠️ Differs |
| [H26 · Account deletion across Cancun](decisions/H26.md) | Erigon stable | ✅ Checked cases agree | ⚠️ Differs |
| [H29 · Precompile call-frame inclusion](decisions/H29.md) | Erigon stable | ✅ Checked cases agree | ⚠️ Differs |
| [H05 · Post-merge reward records](decisions/H05.md) | Erigon dev | ✅ Checked cases agree | ⚠️ Differs |
| [H23 · Special-action address matching](decisions/H23.md) | Erigon dev | ✅ Checked cases agree | ⚠️ Differs |
| [H28 · Historical state at system-operation boundaries](decisions/H28.md) | Erigon dev | ✅ Checked cases agree | ⚠️ Differs |
| [H29 · Precompile call-frame inclusion](decisions/H29.md) | Erigon dev | ✅ Checked cases agree | ⚠️ Differs |

### [Geth draft fork](clients/geth.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H14 · Invalid-parameter error codes](decisions/H14.md) | Geth draft fork | ✅ Checked cases agree | ❔ Policy open |

### [Nethermind](clients/nethermind.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H23 · Special-action address matching](decisions/H23.md) | Nethermind stable | ✅ Checked cases agree | ⚠️ Differs |
| [H29 · Precompile call-frame inclusion](decisions/H29.md) | Nethermind stable | ✅ Checked cases agree | ⚠️ Differs |
| [H23 · Special-action address matching](decisions/H23.md) | Nethermind dev | ✅ Checked cases agree | ⚠️ Differs |
| [H29 · Precompile call-frame inclusion](decisions/H29.md) | Nethermind dev | ✅ Checked cases agree | ⚠️ Differs |

### [Reth](clients/reth.md)

| Decision | Build | Previous | Current |
| --- | --- | --- | --- |
| [H05 · Post-merge reward records](decisions/H05.md) | Reth stable | ✅ Checked cases agree | ⚠️ Differs |
| [H23 · Special-action address matching](decisions/H23.md) | Reth stable | ✅ Checked cases agree | ⚠️ Differs |
| [H29 · Precompile call-frame inclusion](decisions/H29.md) | Reth stable | ✅ Checked cases agree | ⚠️ Differs |
| [H05 · Post-merge reward records](decisions/H05.md) | Reth dev | ✅ Checked cases agree | ⚠️ Differs |
| [H23 · Special-action address matching](decisions/H23.md) | Reth dev | ✅ Checked cases agree | ⚠️ Differs |
| [H29 · Precompile call-frame inclusion](decisions/H29.md) | Reth dev | ✅ Checked cases agree | ⚠️ Differs |
