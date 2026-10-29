# Write read/many storage write read

`trace_callMany` · callmany-isolation · [All reports](../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. The second call reads the first call’s simulated write. Each call reports its own sender nonce transition, including a reverted call. Only the first call writes slot zero; reverted writes and later reads add no storage transition. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/callmany-isolation/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/callmany-isolation/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/callmany-isolation/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/callmany-isolation/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/callmany-isolation/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/callmany-isolation/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/callmany-isolation/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/callmany-isolation/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/callmany-isolation/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../../evidence/2026-10-29/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/callmany-isolation/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../../evidence/2026-10-29/eval/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/callmany-isolation/manifest.json) |

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
          "data": "0x000000000000000000000000000000000000000000000000000000000000002a0000000000000000000000000000000000000000000000000000000000000000",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x77359400",
          "to": "0x0000000000000000000000000000000000001001"
        },
        [
          "trace",
          "stateDiff"
        ]
      ],
      [
        {
          "data": "0x",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x77359400",
          "to": "0x0000000000000000000000000000000000001001"
        },
        [
          "trace",
          "stateDiff"
        ]
      ]
    ],
    "0x30"
  ]
}
```

**Reth · 2.8.1 · 966010c9** (`Reth Version: 2.8.1+966010c9`)

- [H15](../../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less the modelled refund 0), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less the modelled refund 0), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Reth · 2.9.0 · c9a780f4** (`Reth Version: 2.9.0+c9a780f4`)

- [H15](../../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less the modelled refund 0), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less the modelled refund 0), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

</details>
