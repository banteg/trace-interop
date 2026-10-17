# Transaction tree

`trace_transaction` · initial · [All reports](../../README.md)

**What this checks:** Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. The creation fixture contains its CREATE frame; every creation names its creationMethod and successful creations include address, code and gasUsed. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Anvil · 1.8.6-nightly · de005f70](../../clients/anvil_development.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../clients/besu_development.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../clients/erigon_development.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../clients/go-ethereum_trace.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../clients/nethermind_development.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../clients/reth_development.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/initial/manifest.json) |

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

**Besu · 26.10-develop · 0776d82f** (`besu/v26.10-develop-0776d82/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [1]: error 'Reverted', result null.
- [H10](../../decisions/H10.md): The creation fixture contains its CREATE frame; every creation names its creationMethod and successful creations include address, code and gasUsed. traceAddress [6]: result.code null
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'result':

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [1]: error 'Reverted', result null.
- [H10](../../decisions/H10.md): The creation fixture contains its CREATE frame; every creation names its creationMethod and successful creations include address, code and gasUsed. traceAddress [6]: result.code null
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'result':

</details>
