# Replay tree trace

`trace_replayTransaction` · initial · [All reports](../../README.md)

**What this checks:** Individual replay includes its transactionHash. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. The method responds without Method not found (-32601). trace_replayTransaction Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 9 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · dd372126](../../clients/anvil_development.md) | 9 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · a1ce80fb](../../clients/erigon_development.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 9 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · 45912ba3](../../clients/nethermind_development.md) | 9 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |
| [Reth · 2.5.2 · 5723a3fe](../../clients/reth_development.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-28/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-28/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayTransaction",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      "trace"
    ]
  ]
}
```

**Anvil · 1.8.4-nightly · dd372126** (`anvil Version: 1.8.4-nightly+dd372126`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash. transactionHash 'absent', expected 0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738.
- Result shape at `/`: {'output': '0xffee', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'result': {'gasUsed': '0x2343f', 'output': '0xffee'}, 'subtrac

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash. transactionHash 'absent', expected 0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738.
- Result shape at `/`: {'output': '0xffee', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'result': {'gasUsed': '0x2343f', 'output': '0xffee'}, 'subtrac

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H29](../../decisions/H29.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H29](../../decisions/H29.md): Assess the declared property. Cannot inspect this property: unsupported.

**Nethermind · 2.1.0-preview · 45912ba3** (`2.1.0-preview+45912ba3`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [1]: error 'Reverted', result null.
- Result shape at `/`: {'output': '0xffee', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'result': {'gasUsed': '0x2343f', 'output': '0xffee'}, 'subtrac

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [1]: error 'Reverted', result null.
- Result shape at `/`: {'output': '0xffee', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'result': {'gasUsed': '0x2343f', 'output': '0xffee'}, 'subtrac

</details>
