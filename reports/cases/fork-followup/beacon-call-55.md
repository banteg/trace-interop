# Beacon call 55

`trace_call` · fork-followup · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Failed frames have an error string and an explicit object or null result. Historical trace_call uses only system changes through the selected block.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/fork-followup/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x0000000000000000000000000000000000000000000000000000000000000230",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "to": "0x000F3df6D732807Ef1319fB7B8bB8522d0Beac02"
    },
    [
      "trace"
    ],
    "0x37"
  ]
}
```

**Besu · 🛠️ Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d520', 'input': '0x0000000000000000000000000000000000000000000000000000000000000230', 'to': '0x000f3df6d732807ef1319fb7b8bb8522d0beac02', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x', 'subt

**Besu · 📦 Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d520', 'input': '0x0000000000000000000000000000000000000000000000000000000000000230', 'to': '0x000f3df6d732807ef1319fb7b8bb8522d0beac02', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x', 'subt

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H28](../../decisions/H28.md): Historical trace_call uses only system changes through the selected block.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d520', 'input': '0x0000000000000000000000000000000000000000000000000000000000000230', 'to': '0x000f3df6d732807ef1319fb7b8bb8522d0beac02', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddre

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d520', 'input': '0x0000000000000000000000000000000000000000000000000000000000000230', 'to': '0x000f3df6d732807ef1319fb7b8bb8522d0beac02', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddre

</details>
