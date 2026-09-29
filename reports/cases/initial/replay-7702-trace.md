# Replay 7702 trace

`trace_replayTransaction` · initial · [All reports](../../README.md)

**What this checks:** Individual replay includes its transactionHash. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. The method responds without Method not found (-32601). trace_replayTransaction Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · dd372126](../../clients/anvil_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 558586f0](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · 82516987](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayTransaction",
  "params": [
    "0xb54bc1221b206db9ee0449a716ddde73c1e2d0f72d2e789fcb51230fe851cc8a",
    [
      "trace"
    ]
  ]
}
```

**Anvil · 1.8.4-nightly · dd372126** (`anvil Version: 1.8.4-nightly+dd372126`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash. transactionHash 'absent', expected 0xb54bc1221b206db9ee0449a716ddde73c1e2d0f72d2e789fcb51230fe851cc8a.
- Result shape at `/`: {'output': '0x', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x0', 'input': '0x', 'to': '0x0000000000000000000000000000000000000000', 'value': '0x0'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAd

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash. transactionHash 'absent', expected 0xb54bc1221b206db9ee0449a716ddde73c1e2d0f72d2e789fcb51230fe851cc8a.
- Result shape at `/`: {'output': '0x', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x0', 'input': '0x', 'to': '0x0000000000000000000000000000000000000000', 'value': '0x0'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAd

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.

</details>
