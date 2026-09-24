# Nested callcode outer0 value1 failed

`trace_callMany` · precompile-values · [All reports](../../README.md)

**What this checks:** Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree. The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome. A handled precompile failure must not mark the successful parent as failed. The constructor returns the precompile call success bit; a funded successful call must return one. The preceding simulated transfer funds the actual zero-value creation address with one wei. Return one execution envelope per input call, in order. Failed frames have an error string and an explicit object or null result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h17-retest/precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompile-values/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h17-retest/precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompile-values/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompile-values/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompile-values/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompile-values/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h17-retest/precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompile-values/manifest.json) |
| [Nethermind · 2.1.0-unstable · 9d6e8b8d](../../clients/nethermind_development.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h17-retest/precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompile-values/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompile-values/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/precompile-values/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/precompile-values/manifest.json) |

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
          "data": "0x602a600052604060006080600060016006620186a0f260005260206000f3",
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

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- [H29](../../decisions/H29.md): The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome.
- [H24](../../decisions/H24.md): A handled precompile failure must not mark the successful parent as failed.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `1/trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xf2f52', 'init': '0x602a600052604060006080600060016006620186a0f260005260206000f3', 'value': '0x0'}, 'error': 'Precompile error', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schema

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- [H29](../../decisions/H29.md): The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome.
- [H24](../../decisions/H24.md): A handled precompile failure must not mark the successful parent as failed.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `1/trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xf2f52', 'init': '0x602a600052604060006080600060016006620186a0f260005260206000f3', 'value': '0x0'}, 'error': 'Precompile error', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schema

**Nethermind · 2.1.0-unstable · 9d6e8b8d** (`2.1.0-unstable+9d6e8b8d`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `1/trace/1`: {'action': {'callType': 'callcode', 'from': '0x93216e4a663e3a680a0fe006285935f47caa5738', 'gas': '0x18f9c', 'input': '0x000000000000000000000000000000000000000000000000000000000000002a00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `1/trace/1`: {'action': {'callType': 'callcode', 'from': '0x93216e4a663e3a680a0fe006285935f47caa5738', 'gas': '0x18f9c', 'input': '0x000000000000000000000000000000000000000000000000000000000000002a00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
- Result shape at `1/vmTrace`: {'code': '0x602a600052604060006080600060016006620186a0f260005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 995151}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 995148}, 'pc': 2, 'sub': None}, {'cost'

</details>
