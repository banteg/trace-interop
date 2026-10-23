# Filter to

`trace_filter` · initial · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Reward and SELFDESTRUCT records carry result null. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Anvil · 1.8.7-nightly · 4e8874b2](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Besu · 26.10.1 · e83703cd](../../clients/besu_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../clients/besu_development.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../clients/nethermind_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/initial/manifest.json) |

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
      "toAddress": [
        "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      ]
    }
  ]
}
```

**Besu · 26.10-develop · 781a7e1d** (`besu/v26.10-develop-781a7e1/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Expected 1 such records from this client's block trace; got 0.
- [H09](../../decisions/H09.md): Assess the declared property. Address selection differs from its reference; failure-bearing frame selection is not established.

**Besu · 26.10.1 · e83703cd** (`besu/v26.10.1/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Expected 1 such records from this client's block trace; got 0.
- [H09](../../decisions/H09.md): Assess the declared property. Address selection differs from its reference; failure-bearing frame selection is not established.

**Nethermind · 2.2.1 · c4f1015b** (`2.2.1+c4f1015b`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [6, 0]: error None, result null.
- Result shape at `1`: {'action': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'balance': '0x0', 'refundAddress': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'}, 'blockHash': '0xad340c8620df478fa43b66e0ff842b64b6956d589a0aef951fc3fb9b7ddab4e2', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [6, 0], 'transac

</details>
