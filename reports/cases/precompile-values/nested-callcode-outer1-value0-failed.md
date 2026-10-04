# Nested callcode outer1 value0 failed

`trace_call` · precompile-values · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Omit nested zero-value precompiles; retain nonzero transferred/inherited value and number the emitted tree. A handled precompile failure must not mark the successful parent as failed. The constructor returns the precompile call success bit; a funded successful call must return one. Successful creation uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth. Failed frames have an error string; an exceptional halt omits result or sets it to null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/precompile-values/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/precompile-values/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/precompile-values/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/precompile-values/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/precompile-values/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/precompile-values/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/precompile-values/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/precompile-values/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/precompile-values/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/precompile-values/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/precompile-values/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/precompile-values/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x100000",
      "gasPrice": "0x3b9aca00",
      "value": "0x1",
      "data": "0x602a600052604060006080600060006006620186a0f260005260206000f3"
    },
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H24](../../decisions/H24.md): A handled precompile failure must not mark the successful parent as failed.
- Result shape at `trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xf2f5e', 'init': '0x602a600052604060006080600060006006620186a0f260005260206000f3', 'value': '0x1'}, 'error': 'Precompile error', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schema

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H24](../../decisions/H24.md): A handled precompile failure must not mark the successful parent as failed.
- Result shape at `trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xf2f5e', 'init': '0x602a600052604060006080600060006006620186a0f260005260206000f3', 'value': '0x1'}, 'error': 'Precompile error', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schema

</details>
