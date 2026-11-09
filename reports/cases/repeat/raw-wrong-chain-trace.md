# Raw wrong chain trace

`trace_rawTransaction` · repeat · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0xf86481858477359400825208940000000000000000000000000000000000001234018026a0680e20ade3f3bfbbb3d8e2246c26a13efb3a8e886c182c159cd240b4636342b8a027a25d70c994f869fa5abe6b841ddfff0ab32944d6e9719c830ace909c024a3b",
    [
      "trace"
    ]
  ]
}
```

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x0000000000000000000000000000000000001234', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

</details>
