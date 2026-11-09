# Raw validation intrinsic gas all

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | RPC error `800` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86a0a842da282a982520794000000000000000000000000000000000000100201808718e5bb3abd10a0a03e2bb48ffdc3a7718afc598d928b473e31cb4f1757a33a884d91d0e2bacc3eb7a00ff33e7901b8f83ce9451b3a94d395953062ce98020698dea332741bd49e596c",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. gas limit below 21000 intrinsic gas
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. gas limit below 21000 intrinsic gas
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

</details>
