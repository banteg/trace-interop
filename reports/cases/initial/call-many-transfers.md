# Call many transfers

`trace_callMany` · initial · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Each transfer has one successful root, with no fabricated failure. Unsigned execution accepts the supplied nonzero fee and returns one envelope per call; exact environment values are checked by coverage/model-environment. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |

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

**Anvil · 1.8.4-nightly · e3429853** (`anvil Version: 1.8.4-nightly+e3429853`)

- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. 0x0000000000000000000000000000000000001234: new account lacks creation markers for all fields

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. 0x0000000000000000000000000000000000001234: new account lacks creation markers for all fields

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. 0x0000000000000000000000000000000000001234: new account lacks creation markers for all fields
- Result shape at `0/stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x66863b', 'to': '0x262aafd8968b'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000001234': {'balance': {'+': '0x1'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x7435ed30a8b4aeb087

**Reth · 2.7.0 · 43a93dbc** (`Reth Version: 2.7.0+43a93dbc`)

- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

</details>
