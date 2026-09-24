# Replay 7702 trace

`trace_replayTransaction` · initial · [All reports](../../README.md)

**What this checks:** trace_replayTransaction Assess the declared property. Individual replay includes its transactionHash. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. The method responds without Method not found (-32601).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |

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

**Besu · 26.9-develop · 85b32978** (`besu/v26.9-develop-85b3297/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash.
- Result shape at `/`: {'output': '0x', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x0', 'input': '0x', 'to': '0x0000000000000000000000000000000000000000', 'value': '0x0'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAd

</details>
