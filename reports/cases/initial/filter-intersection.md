# Filter intersection

`trace_filter` · initial · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../clients/besu_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/initial/manifest.json) |

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
      "mode": "intersection"
    }
  ]
}
```

**Besu · 26.9-develop · 85b32978** (`besu/v26.9-develop-85b3297/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 records from this client's block trace.

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 records from this client's block trace.

</details>
