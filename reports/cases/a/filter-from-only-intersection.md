# Filter from only intersection

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | 5 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | 5 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/a/manifest.json) |

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
      "mode": "intersection"
    }
  ]
}
```

**Anvil · 1.8.6-nightly · 9089a6bf** (`anvil Version: 1.8.6-nightly+9089a6bf`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 4 ordinary records from this client's block trace.
- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. The H03 list semantics differ, so the special-action records cannot be judged separately.
- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.9.0-dev · d23467c5** (`3.9.0-dev-d23467c5`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.9-unstable · a15b96ff** (`Geth/v1.17.9-unstable-a15b96ff-2026-10-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.3.0-preview · e2e011c8** (`2.3.0-preview+e2e011c8`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
