# Replay revert trace

`trace_replayTransaction` · initial · [All reports](../../README.md)

**What this checks:** Individual replay includes its transactionHash. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. The method responds without Method not found (-32601). trace_replayTransaction Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayTransaction",
  "params": [
    "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
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

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.

</details>
