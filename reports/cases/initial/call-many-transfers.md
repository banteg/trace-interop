# Call many transfers

`trace_callMany` · initial · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Each transfer has one successful root, with no fabricated failure. Unsigned execution accepts the supplied nonzero fee and returns one envelope per call; exact environment values are checked by coverage/model-environment. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee and blob fee.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |

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
          "to": "0x0000000000000000000000000000000000001234",
          "gas": "0x186a0",
          "gasPrice": "0x77359400",
          "value": "0x1",
          "data": "0x"
        },
        [
          "trace",
          "stateDiff"
        ]
      ],
      [
        {
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "to": "0x0000000000000000000000000000000000001234",
          "gas": "0x186a0",
          "gasPrice": "0x77359400",
          "value": "0x1",
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

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee and blob fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee=0.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee and blob fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee=0.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee and blob fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee=0.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee and blob fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee=0.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000001234: new account lacks creation markers for all fields
- Result shape at `0/stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x66863b', 'to': '0x262aafd8968b'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000001234': {'balance': {'+': '0x1'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x7435ed30a8b4aeb087

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000001234: new account lacks creation markers for all fields
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee and blob fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee=0.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee and blob fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee=0.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000001234: new account lacks creation markers for all fields
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee and blob fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee=0.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee and blob fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee=0.

</details>
