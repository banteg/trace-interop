# Replay tree trace

`trace_replayTransaction` · initial · [All reports](../../README.md)

**What this checks:** Individual replay includes its transactionHash. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Reward and SELFDESTRUCT records carry result null. The method responds without Method not found (-32601). trace_replayTransaction Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 9 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | 9 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |

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

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H29](../../decisions/H29.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H29](../../decisions/H29.md): Assess the declared property. Cannot inspect this property: unsupported.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H09](../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [3]: error 'Mutable Call In Static Context', result null.
- Result shape at `/`: {'output': '0xffee', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'result': {'gasUsed': '0x2343f', 'output': '0xffee'}, 'subtrac

</details>
