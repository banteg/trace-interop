# Filter to only intersection

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/a/manifest.json) |

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
      ],
      "mode": "intersection"
    }
  ]
}
```

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 2 records from this client's block trace.
- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 2 records from this client's block trace.
- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 2 records from this client's block trace.
- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · c8449896** (`Geth/v1.17.7-unstable-c8449896-2026-09-26/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
