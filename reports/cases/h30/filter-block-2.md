# Filter block 2

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Filter the anchored canonical inventory before applying after/count, including count zero and past-end pages. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/h30/manifest.json) |

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
      "count": 3
    }
  ]
}
```

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H33](../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H33](../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H33](../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H33](../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Erigon · 3.8.0-dev · 85e1ca92** (`3.8.0-dev-85e1ca92`)

- [H33](../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H33](../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · e26833e3** (`Geth/v1.17.7-unstable-e26833e3-2026-09-26/linux-amd64/go1.26.1`)

- [H33](../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · f69690c5** (`2.2.0-preview+f69690c5`)

- [H33](../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H33](../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Reth · 2.7.0 · 60aeb532** (`Reth Version: 2.7.0+60aeb532`)

- [H33](../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H33](../../decisions/H33.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
