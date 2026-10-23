# Legacy out of gas/many/none

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../../../clients/anvil_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.7-nightly · 4e8874b2](../../../../clients/anvil_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Besu · 26.10.1 · e83703cd](../../../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-23/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-23/eval/fee-policy/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_callMany",
  "params": [
    [
      [
        {
          "data": "0x63ffffffff51",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x30d40",
          "gasPrice": "0x2da282a9",
          "value": "0x7"
        },
        []
      ]
    ],
    "latest"
  ]
}
```

</details>
