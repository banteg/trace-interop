# Many storage write read

`trace_callMany` · a · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. The second call reads the first call’s simulated write. Each call reports its own sender nonce transition, including a reverted call. Only the first call writes slot zero; reverted writes and later reads add no storage transition. Check accounting against independent gas. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 2 records | 🟡 Partially assessed | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Anvil · 1.8.4-nightly · dd372126](../../clients/anvil_development.md) | 2 records | 🟡 Partially assessed | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 records | 🟡 Partially assessed | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 2 records | 🟡 Partially assessed | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Erigon · 3.8.0-dev · 558586f0](../../clients/erigon_development.md) | 2 records | 🟡 Partially assessed | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 2 records | 🟡 Partially assessed | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | 🟡 Partially assessed | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Nethermind · 2.1.0-preview · 82516987](../../clients/nethermind_development.md) | 2 records | 🟡 Partially assessed | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_callMany",
  "params": [
    [
      [
        {
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "to": "0x0000000000000000000000000000000000001001",
          "gas": "0x927c0",
          "gasPrice": "0x77359400",
          "data": "0x000000000000000000000000000000000000000000000000000000000000002a0000000000000000000000000000000000000000000000000000000000000000"
        },
        [
          "trace",
          "stateDiff"
        ]
      ],
      [
        {
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "to": "0x0000000000000000000000000000000000001001",
          "gas": "0x927c0",
          "gasPrice": "0x77359400",
          "data": "0x"
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

**Anvil · 1.8.4-nightly · dd372126** (`anvil Version: 1.8.4-nightly+dd372126`)

- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Erigon · 3.8.0-dev · 558586f0** (`3.8.0-dev-558586f0`)

- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Geth draft fork · 1.17.7-unstable · e26833e3** (`Geth/v1.17.7-unstable-e26833e3-2026-09-26/linux-amd64/go1.26.1`)

- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Nethermind · 2.1.0-preview · 82516987** (`2.1.0-preview+82516987`)

- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Check accounting against independent gas. The refund is not independently derived; balances settle within the refund bound. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Reth · 2.5.2 · 5723a3fe** (`Reth Version: 2.5.2+5723a3fe`)

- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=34829..43536 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000..23137 (root execution gas plus independently calculated Prague intrinsic/floor cost, less any refund), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

</details>
