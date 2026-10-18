# Filter from empty to set

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |

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
      "fromAddress": [],
      "toAddress": [
        "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      ]
    }
  ]
}
```

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Expected 1 such records from this client's block trace; got 0.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Expected 1 such records from this client's block trace; got 0.

</details>
