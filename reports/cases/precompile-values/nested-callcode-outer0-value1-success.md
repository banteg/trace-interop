# Nested callcode outer0 value1 success

`trace_callMany` · precompile-values · [All reports](../../README.md)

**What this checks:** Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree. The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome. A handled precompile failure must not mark the successful parent as failed. The constructor returns the precompile call success bit; a funded successful call must return one. The preceding simulated transfer funds the actual zero-value creation address with one wei. Return one execution envelope per input call, in order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/precompile-values/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/precompile-values/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/precompile-values/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/precompile-values/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/precompile-values/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/precompile-values/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/precompile-values/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/precompile-values/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/precompile-values/manifest.json) |

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
          "to": "0x93216e4a663e3a680a0fe006285935f47caa5738",
          "value": "0x1",
          "gas": "0x5208",
          "gasPrice": "0x3b9aca00",
          "nonce": "0x85"
        },
        [
          "trace",
          "stateDiff"
        ]
      ],
      [
        {
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x100000",
          "gasPrice": "0x3b9aca00",
          "value": "0x0",
          "data": "0x6000600052604060006080600060016006620186a0f260005260206000f3",
          "nonce": "0x86"
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

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- [H29](../../decisions/H29.md): The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome.
- Result shape at `1/trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xf2f5e', 'init': '0x6000600052604060006080600060016006620186a0f260005260206000f3', 'value': '0x0'}, 'result': {'address': '0x93216e4a663e3a680a0fe006285935f47caa5738', 'code': '0x0000000000000000000000000000000000000000000000

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- [H29](../../decisions/H29.md): The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome.
- Result shape at `1/trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xf2f5e', 'init': '0x6000600052604060006080600060016006620186a0f260005260206000f3', 'value': '0x0'}, 'result': {'address': '0x93216e4a663e3a680a0fe006285935f47caa5738', 'code': '0x0000000000000000000000000000000000000000000000

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `0/stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x66863b', 'to': '0x13113e4e468b'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f': {'balance': {'*': {'from': '0xc097ce7bc90715b34755ccb0391096', 'to': '0xc097ce7bc90715b34742b33eaec
- Result shape at `1/vmTrace`: {'code': '0x6000600052604060006080600060016006620186a0f260005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995163}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995160}, 'pc': 2, 'sub': None}, {'cost'

</details>
