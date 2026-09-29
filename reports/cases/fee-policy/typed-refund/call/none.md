# Typed refund/call/none

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Successful creation uses address, code and gasUsed.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../../../clients/anvil_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.4-nightly · dd372126](../../../../clients/anvil_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/eval/fee-policy/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/eval/fee-policy/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../../../clients/besu_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/eval/fee-policy/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../../clients/erigon_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 558586f0](../../../../clients/erigon_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../../../clients/go-ethereum_trace.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/eval/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/eval/fee-policy/manifest.json) |
| [Nethermind · 2.1.0-preview · 82516987](../../../../clients/nethermind_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/eval/fee-policy/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../../../clients/reth_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-29/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-29/eval/fee-policy/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x6001600055600060005560006000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x30d40",
      "maxFeePerGas": "0x5b450550",
      "maxPriorityFeePerGas": "0x1",
      "value": "0x7"
    },
    [],
    "latest"
  ]
}
```

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H08](../../../../decisions/H08.md): Unrequested trace is an empty array.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H15](../../../../decisions/H15.md): Execute each valid simulation and return one envelope per call.

</details>
