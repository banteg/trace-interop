# Call transfer statediff

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; output `null` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Nethermind · 2.1.0-unstable · 2a3b2531](../../clients/nethermind_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 0 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x186a0",
      "gasPrice": "0x77359400",
      "to": "0x0000000000000000000000000000000000001234",
      "value": "0x1"
    },
    [
      "stateDiff"
    ],
    "0x30"
  ]
}
```

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=41964773970000, burn=35226030000.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H08](../../decisions/H08.md): Unrequested trace is an empty array.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=41964773970000, burn=35226030000.

**Nethermind · 2.1.0-unstable · 2a3b2531** (`2.1.0-unstable+2a3b2531`)

- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000001234: new account lacks creation markers for all fields

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H08](../../decisions/H08.md): Output remains a byte string under every trace selection.
- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000001234: new account lacks creation markers for all fields
- Result shape at `output`: None is not of type 'string'

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000001234: new account lacks creation markers for all fields
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=41964773970000, burn=35226030000.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000001234: new account lacks creation markers for all fields
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=41964773970000, burn=35226030000.

</details>
