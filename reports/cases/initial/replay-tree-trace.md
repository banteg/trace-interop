# Replay tree trace

`trace_replayTransaction` · initial · [All reports](../../README.md)

**What this checks:** Individual replay includes its transactionHash. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Failed frames have an error string and an explicit object or null result. Assess this declared topic case. trace_replayTransaction

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | Method unavailable `-32601` | ⛔ Method unavailable | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 9 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 9 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 9 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/geth-contract-sync/geth-contract-initial/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 9 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 9 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 9 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 9 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-23/harness-audit-native-initial/observations.json) · [Build/run](../../../evidence/2026-09-23/harness-audit-native-initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayTransaction",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738",
    [
      "trace"
    ]
  ]
}
```

**Geth draft fork · 🧪 Draft fork** (`Geth/v1.17.6-unstable-c36ee43e-2026-09-23/linux-amd64/go1.26.1`)

- [H01](../../decisions/H01.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H09](../../decisions/H09.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.
- [H07](../../decisions/H07.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H09](../../decisions/H09.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H01](../../decisions/H01.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H01](../../decisions/H01.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H01](../../decisions/H01.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `/`: {'output': '0xffee', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'result': {'gasUsed': '0x2343f', 'output': '0xffee'}, 'subtrac

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H01](../../decisions/H01.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `/`: {'output': '0xffee', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'result': {'gasUsed': '0x2343f', 'output': '0xffee'}, 'subtrac

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash.
- [H01](../../decisions/H01.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `/`: {'output': '0xffee', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'result': {'gasUsed': '0x2343f', 'output': '0xffee'}, 'subtrac

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash.
- [H01](../../decisions/H01.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `/`: {'output': '0xffee', 'stateDiff': None, 'trace': [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'result': {'gasUsed': '0x2343f', 'output': '0xffee'}, 'subtrac

</details>
