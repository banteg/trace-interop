# Replay transfer vmtrace

`trace_replayTransaction` · initial · [All reports](../../README.md)

**What this checks:** Individual replay includes its transactionHash. Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. The method responds without Method not found (-32601). trace_replayTransaction Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 0 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../clients/anvil_development.md) | 0 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | 0 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_replayTransaction",
  "params": [
    "0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe",
    [
      "vmTrace"
    ]
  ]
}
```

**Anvil · 1.8.4-nightly · df92604b** (`anvil Version: 1.8.4-nightly+df92604b`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash. transactionHash 'absent', expected 0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe.
- Result shape at `/`: {'output': '0x', 'stateDiff': None, 'trace': [], 'vmTrace': {'code': '0x', 'ops': []}} is not valid under any of the given schemas

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash. transactionHash 'absent', expected 0x99a8eb5c9ab03c42137bcb263c525487dac03192bebd5c6762c8511e3b867afe.
- Result shape at `/`: {'output': '0x', 'stateDiff': None, 'trace': [], 'vmTrace': {'code': '0x', 'ops': []}} is not valid under any of the given schemas

**Besu · 26.10-develop · 28edf391** (`besu/v26.10-develop-28edf39/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess the declared property. Cannot inspect this property: unsupported.

</details>
