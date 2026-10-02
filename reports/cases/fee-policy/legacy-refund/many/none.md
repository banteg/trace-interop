# Legacy refund/many/none

`trace_callMany` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../../../clients/anvil_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.4-nightly · 328811cb](../../../../clients/anvil_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-02/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-02/eval/fee-policy/manifest.json) |

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
          "data": "0x6001600055600060005560006000f3",
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
