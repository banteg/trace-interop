# Replay revert trace

`trace_replayTransaction` · initial · [All reports](../../README.md)

**What this checks:** Individual replay includes its transactionHash. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. The method responds without Method not found (-32601). trace_replayTransaction Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/initial/manifest.json) |

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

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash. transactionHash 'absent', expected 0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae.
- Result shape at `/`: {'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash. transactionHash 'absent', expected 0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae.
- Result shape at `/`: {'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72, gasUsed 0x889; derived from frozen bytecode.
- Result shape at `/`: {'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13

</details>
