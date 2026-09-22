# Nested callcode outer0 value1 success

`trace_callMany` · precompile-values · [All reports](../../README.md)

**What this checks:** Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree. A handled precompile failure must not mark the successful parent as failed. The constructor returns the precompile call success bit; a funded successful call must return one. The preceding simulated transfer funds the actual zero-value creation address with one wei. Return one execution envelope per input call, in order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 2 records | Differs | [Response](../../../evidence/2026-09-23/precompile-values-native/observations.json) · [Build/run](../../../evidence/2026-09-23/precompile-values-native/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 2 records | Differs | [Response](../../../evidence/2026-09-23/precompile-values-native/observations.json) · [Build/run](../../../evidence/2026-09-23/precompile-values-native/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 2 records | Checked cases agree | [Response](../../../evidence/2026-09-23/precompile-values-native/observations.json) · [Build/run](../../../evidence/2026-09-23/precompile-values-native/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 2 records | Checked cases agree | [Response](../../../evidence/2026-09-23/precompile-values-native/observations.json) · [Build/run](../../../evidence/2026-09-23/precompile-values-native/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 2 records | Checked cases agree | [Response](../../../evidence/2026-09-23/geth-40eecf3-precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-40eecf3-precompile-values/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 2 records | Checked cases agree; result shape differs | [Response](../../../evidence/2026-09-23/precompile-values-native/observations.json) · [Build/run](../../../evidence/2026-09-23/precompile-values-native/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 2 records | Checked cases agree; result shape differs | [Response](../../../evidence/2026-09-23/precompile-values-native/observations.json) · [Build/run](../../../evidence/2026-09-23/precompile-values-native/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 2 records | Checked cases agree | [Response](../../../evidence/2026-09-23/precompile-values-native/observations.json) · [Build/run](../../../evidence/2026-09-23/precompile-values-native/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 2 records | Checked cases agree | [Response](../../../evidence/2026-09-23/precompile-values-native/observations.json) · [Build/run](../../../evidence/2026-09-23/precompile-values-native/manifest.json) |

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
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x5208",
          "gasPrice": "0x3b9aca00",
          "nonce": "0x85",
          "to": "0x93216e4a663e3a680a0fe006285935f47caa5738",
          "value": "0x1"
        },
        [
          "trace",
          "stateDiff"
        ]
      ],
      [
        {
          "data": "0x6000600052604060006080600060016006620186a0f260005260206000f3",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x100000",
          "gasPrice": "0x3b9aca00",
          "nonce": "0x86",
          "value": "0x0"
        },
        [
          "trace",
          "stateDiff",
          "vmTrace"
        ]
      ]
    ],
    "latest"
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- Result shape at `1/vmTrace`: {'code': '0x6000600052604060006080600060016006620186a0f260005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995163}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995160}, 'pc': 2, 'sub': None}, {'cost'

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- Result shape at `1/vmTrace`: {'code': '0x6000600052604060006080600060016006620186a0f260005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995163}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995160}, 'pc': 2, 'sub': None}, {'cost'

</details>
