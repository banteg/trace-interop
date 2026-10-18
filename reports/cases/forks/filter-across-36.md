# Filter across 36

`trace_filter` · forks · [All reports](../../README.md)

**What this checks:** Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. A fork-crossing range equals the corresponding per-block traces. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 8 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | 8 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 16 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 16 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 16 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 16 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 16 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 16 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 16 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x23",
      "toBlock": "0x24"
    }
  ]
}
```

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H27](../../decisions/H27.md): A fork-crossing range equals the corresponding per-block traces.
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'result': {'gasUsed': '0x0
- Result shape at `5`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'result': {'gasUsed': '0x0',
- Result shape at `6`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x48b7c57589928d75656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'res

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H27](../../decisions/H27.md): A fork-crossing range equals the corresponding per-block traces.
- Result shape at `4`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'result': {'gasUsed': '0x0
- Result shape at `5`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'result': {'gasUsed': '0x0',
- Result shape at `6`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x48b7c57589928d75656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'res

**Erigon · 3.9.0-dev · 1ee57924** (`3.9.0-dev-1ee57924`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `15`: 'transactionHash' is a required property
- Result shape at `15`: 'transactionPosition' is a required property

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `15`: 'transactionHash' is a required property
- Result shape at `15`: 'transactionPosition' is a required property

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `15`: 'transactionHash' is a required property
- Result shape at `15`: 'transactionPosition' is a required property

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- Result shape at `2`: 'transactionHash' is a required property
- Result shape at `2`: 'transactionPosition' is a required property
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `15`: 'transactionHash' is a required property
- Result shape at `15`: 'transactionPosition' is a required property

</details>
