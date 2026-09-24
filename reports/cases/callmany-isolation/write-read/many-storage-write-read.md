# Write read/many storage write read

`trace_callMany` · callmany-isolation · [All reports](../../../README.md)

**What this checks:** Return one execution envelope per input call, in order. The second call reads the first call’s simulated write. Each call reports its own sender nonce transition, including a reverted call. Only the first call writes slot zero; reverted writes and later reads add no storage transition. Check accounting against independent gas. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../clients/besu_release.md) | 2 records | 🟡 Partially assessed | [Response](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../../clients/besu_development.md) | 2 records | 🟡 Partially assessed | [Response](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../../clients/erigon_release.md) | 2 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../../clients/erigon_development.md) | 2 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../../clients/go-ethereum_trace.md) | 2 records | 🟡 Partially assessed | [Response](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../clients/nethermind_release.md) | 2 records | 🟡 Partially assessed | [Response](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../../clients/nethermind_development.md) | 2 records | 🟡 Partially assessed | [Response](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/observations.json.gz) · [Build/run](../../../../evidence/2026-09-24/adopted-stances/callmany-isolation/manifest.json) |

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

**Besu · 26.9-develop · 85b32978** (`besu/v26.9-develop-85b3297/linux-x86_64/openjdk-java-25`)

- [H16](../../../decisions/H16.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H16](../../../decisions/H16.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H16](../../../decisions/H16.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H16](../../../decisions/H16.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Geth draft fork · 1.17.7-unstable · bb5c4682** (`Geth/v1.17.7-unstable-bb5c4682-2026-09-24/linux-amd64/go1.26.1`)

- [H16](../../../decisions/H16.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H16](../../../decisions/H16.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Nethermind · 2.1.0-preview · ce501a97** (`2.1.0-preview+ce501a97`)

- [H16](../../../decisions/H16.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H16](../../../decisions/H16.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H16](../../../decisions/H16.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H16](../../../decisions/H16.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H16](../../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

</details>
