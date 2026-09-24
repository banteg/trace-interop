# Replay revert trace

`trace_replayTransaction` · initial · [All reports](../../README.md)

**What this checks:** trace_replayTransaction Assess the declared property. Individual replay includes its transactionHash. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Failed frames have an error string and an explicit object or null result. The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. The method responds without Method not found (-32601).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-24/h17-retest/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/initial/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-24/h17-retest/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/initial/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h17-retest/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/initial/manifest.json) |
| [Nethermind · 2.1.0-unstable · 9d6e8b8d](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h17-retest/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h17-retest/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayTransaction",
  "params": [
    "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
    [
      "trace"
    ]
  ]
}
```

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.
- [H09](../../decisions/H09.md): Assess the declared property. Cannot inspect this property: unsupported.

**Nethermind · 2.1.0-unstable · 9d6e8b8d** (`2.1.0-unstable+9d6e8b8d`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72, gasUsed 0x889; derived from frozen bytecode.
- Result shape at `/`: {'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72, gasUsed 0x889; derived from frozen bytecode.
- Result shape at `/`: {'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash.
- Result shape at `/`: {'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13

</details>
