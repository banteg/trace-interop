# Raw validation intrinsic gas trace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | RPC error `800` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86a0a842da282a982520794000000000000000000000000000000000000100201808718e5bb3abd10a0a03e2bb48ffdc3a7718afc598d928b473e31cb4f1757a33a884d91d0e2bacc3eb7a00ff33e7901b8f83ce9451b3a94d395953062ce98020698dea332741bd49e596c",
    [
      "trace"
    ]
  ]
}
```

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. gas limit below 21000 intrinsic gas
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. gas limit below 21000 intrinsic gas
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H13](../../decisions/H13.md): Assess the declared property. Cannot inspect this property: malformed_json.

</details>
