# Filter union

`trace_filter` · initial · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | 6 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/initial/manifest.json) |

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

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 4 ordinary records from this client's block trace.
- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. The H03 list semantics differ, so the special-action records cannot be judged separately.
- [H09](../../decisions/H09.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 4 ordinary records from this client's block trace.
- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. The H03 list semantics differ, so the special-action records cannot be judged separately.
- [H09](../../decisions/H09.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 4 ordinary records from this client's block trace.
- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. The H03 list semantics differ, so the special-action records cannot be judged separately.
- [H09](../../decisions/H09.md): Assess the declared property. Address selection differs from its reference; failure-bearing frame selection is not established.

</details>
