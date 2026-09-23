# Call many transfers

`trace_callMany` · initial · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Each transfer has one successful root, with no fabricated failure. Unsigned execution accepts the supplied nonzero fee and returns one envelope per call; exact environment values are checked by coverage/model-environment. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/initial-clean/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) |

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
          "data": "0x",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x186a0",
          "gasPrice": "0x77359400",
          "to": "0x0000000000000000000000000000000000001234",
          "value": "0x1"
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
          "gas": "0x186a0",
          "gasPrice": "0x77359400",
          "to": "0x0000000000000000000000000000000000001234",
          "value": "0x1"
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

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=41964773970000, burn=35226030000.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=41964773970000, burn=35226030000.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=41964773970000, burn=35226030000.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=41964773970000, burn=35226030000.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000001234: new account lacks creation markers for all fields

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000001234: new account lacks creation markers for all fields

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000001234: new account lacks creation markers for all fields
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=41964773970000, burn=35226030000.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=41964773970000, burn=35226030000.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000001234: new account lacks creation markers for all fields
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=41964773970000, burn=35226030000.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=41964773970000, burn=35226030000.

</details>
