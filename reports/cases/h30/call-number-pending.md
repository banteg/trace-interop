# Call number pending

`trace_call` · h30 · [All reports](../../README.md)

**What this checks:** Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Every creation names its creationMethod; a successful one uses address, code and gasUsed.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x4360005260206000f3"
    },
    [
      "trace"
    ],
    "pending"
  ]
}
```

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): Accept pending only with a real pending environment, the block after the head; otherwise reject it (-32602 recommended), never evaluating latest instead. Executed at the head block, as latest.
- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- Result shape at `trace/0`: {'action': {'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8583e', 'init': '0x4360005260206000f3', 'value': '0x0'}, 'result': {'address': '0xe3a8b633a20d3bc82cfd6d6cb315dd9784b3ea41', 'code': '0x0000000000000000000000000000000000000000000000000000000000000030', 'gasUsed': '0x1911'},

</details>
