# Transaction tree

`trace_transaction` · initial · [All reports](../../README.md)

**What this checks:** Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. The creation fixture contains its CREATE frame and successful creations include address, code and gasUsed. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 10 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | 10 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_transaction",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738"
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [1]: error 'Reverted', result null.
- [H10](../../decisions/H10.md): The creation fixture contains its CREATE frame and successful creations include address, code and gasUsed.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'result':

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [1]: error 'Reverted', result null.
- [H10](../../decisions/H10.md): The creation fixture contains its CREATE frame and successful creations include address, code and gasUsed.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'result':

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [1]: error 'Reverted', result null.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'result':

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [1]: error 'Reverted', result null.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'result':

</details>
