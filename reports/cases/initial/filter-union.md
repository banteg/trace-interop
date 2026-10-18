# Filter union

`trace_filter` · initial · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Reward and SELFDESTRUCT records carry result null. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 6 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 6 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2",
      "toBlock": "0x2",
      "fromAddress": [
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f"
      ],
      "toAddress": [
        "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      ],
      "mode": "union"
    }
  ]
}
```

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 4 ordinary records from this client's block trace.
- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. The H03 list semantics differ, so the special-action records cannot be judged separately.
- [H09](../../decisions/H09.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 4 ordinary records from this client's block trace.
- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. The H03 list semantics differ, so the special-action records cannot be judged separately.
- [H09](../../decisions/H09.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [6, 0]: error None, result null.
- Result shape at `2`: {'action': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'balance': '0x0', 'refundAddress': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [6, 0], 'transac

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [6, 0]: error None, result null.
- Result shape at `2`: {'action': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'balance': '0x0', 'refundAddress': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [6, 0], 'transac

</details>
