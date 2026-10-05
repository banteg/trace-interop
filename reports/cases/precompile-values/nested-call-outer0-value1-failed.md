# Nested call outer0 value1 failed

`trace_callMany` · precompile-values · [All reports](../../README.md)

**What this checks:** Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree. The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome. A handled precompile failure must not mark the successful parent as failed. The constructor returns the precompile call success bit; a funded successful call must return one. The preceding simulated transfer funds the actual zero-value creation address with one wei. Return one execution envelope per input call, in order. Failed frames have an error string; an exceptional halt omits result or sets it to null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/precompile-values/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/precompile-values/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/precompile-values/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/precompile-values/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/precompile-values/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/precompile-values/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/precompile-values/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/precompile-values/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/precompile-values/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/precompile-values/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/precompile-values/manifest.json) |

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
          "data": "0x602a600052604060006080600060016006620186a0f160005260206000f3",
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

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- [H29](../../decisions/H29.md): The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome.
- [H24](../../decisions/H24.md): A handled precompile failure must not mark the successful parent as failed.
- Result shape at `1/trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xf2f52', 'init': '0x602a600052604060006080600060016006620186a0f160005260206000f3', 'value': '0x0'}, 'error': 'Precompile error', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schema

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H29](../../decisions/H29.md): Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree.
- [H29](../../decisions/H29.md): The retained child identifies the fixture precompile call-site, opcode, input, value and execution outcome.
- [H24](../../decisions/H24.md): A handled precompile failure must not mark the successful parent as failed.
- Result shape at `1/trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xf2f52', 'init': '0x602a600052604060006080600060016006620186a0f160005260206000f3', 'value': '0x0'}, 'error': 'Precompile error', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schema

</details>
