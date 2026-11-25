# Call many transfers

`trace_callMany` · initial · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Each transfer has one successful root, with no fabricated failure. Unsigned execution accepts the supplied nonzero fee and returns one envelope per call; exact environment values are checked by coverage/model-environment. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |

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

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

</details>
