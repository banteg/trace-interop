# Filter union

`trace_filter` · initial · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Reward and SELFDESTRUCT records carry result null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 6 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |

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

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Expected 2 such records from this client's block trace; got 1.
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'error':

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Expected 2 such records from this client's block trace; got 1.
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'error':

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [6, 0]: error None, result null.
- Result shape at `2`: {'action': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'balance': '0x0', 'refundAddress': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [6, 0], 'transac

</details>
