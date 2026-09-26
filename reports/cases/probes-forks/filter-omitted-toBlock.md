# Filter omitted toblock

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** Retain supporting reference evidence. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 279 records | 🔎 Control / not applicable; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 279 records | 🔎 Control / not applicable; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 350 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 350 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 350 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 375 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |
| [Nethermind · 2.1.0-preview · b4211ad9](../../clients/nethermind_development.md) | 375 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 350 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 350 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2"
    }
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `24`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x92c0a3cd8b571ac5656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0xc80abc7c7ff55e123dd2a22190a845894ebb363b3a0355c1cb5dfc57cbeb613e', 'blockNumber': 8, 'resu
- Result shape at `25`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x4dde844b71bcdf95512fb4dc94e84fb67b512ed8', 'value': '0x1'}, 'blockHash': '0xc80abc7c7ff55e123dd2a22190a845894ebb363b3a0355c1cb5dfc57cbeb613e', 'blockNumber': 8, 'result': {'gasUsed': '0x0',
- Result shape at `28`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xa66c701845710c6c656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0x9b33350a0ba145d68e650268822204c0b76798a7724e7c1ebc60268f8ee0f968', 'blockNumber': 9, 'resu
- Result shape at `29`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x1f5bde34b4afc686f136c7a3cb6ec376f7357759', 'value': '0x1'}, 'blockHash': '0x9b33350a0ba145d68e650268822204c0b76798a7724e7c1ebc60268f8ee0f968', 'blockNumber': 9, 'result': {'gasUsed': '0x0',
- Result shape at `32`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x06072144caa6635a656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0x46b9527975bd5b8a68582a18e68eaac0618048e6386f9e1fa0a6e18de6e8c96f', 'blockNumber': 10, 'res
- Result shape at `33`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x3ae75c08b4c907eb63a8960c45b86e1e9ab6123c', 'value': '0x1'}, 'blockHash': '0x46b9527975bd5b8a68582a18e68eaac0618048e6386f9e1fa0a6e18de6e8c96f', 'blockNumber': 10, 'result': {'gasUsed': '0x0',
- Result shape at `36`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xb2cbef3dfb5e69d8656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0xaa6cc431712ea8ebe17e14682184305add9f375af0cd6187d6b2b136eac85d1d', 'blockNumber': 11, 'res
- Result shape at `37`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x5f552da00dfb4d3749d9e62dcee3c918855a86a0', 'value': '0x1'}, 'blockHash': '0xaa6cc431712ea8ebe17e14682184305add9f375af0cd6187d6b2b136eac85d1d', 'blockNumber': 11, 'result': {'gasUsed': '0x0',

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `24`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x92c0a3cd8b571ac5656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0xc80abc7c7ff55e123dd2a22190a845894ebb363b3a0355c1cb5dfc57cbeb613e', 'blockNumber': 8, 'resu
- Result shape at `25`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x4dde844b71bcdf95512fb4dc94e84fb67b512ed8', 'value': '0x1'}, 'blockHash': '0xc80abc7c7ff55e123dd2a22190a845894ebb363b3a0355c1cb5dfc57cbeb613e', 'blockNumber': 8, 'result': {'gasUsed': '0x0',
- Result shape at `28`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xa66c701845710c6c656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0x9b33350a0ba145d68e650268822204c0b76798a7724e7c1ebc60268f8ee0f968', 'blockNumber': 9, 'resu
- Result shape at `29`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x1f5bde34b4afc686f136c7a3cb6ec376f7357759', 'value': '0x1'}, 'blockHash': '0x9b33350a0ba145d68e650268822204c0b76798a7724e7c1ebc60268f8ee0f968', 'blockNumber': 9, 'result': {'gasUsed': '0x0',
- Result shape at `32`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x06072144caa6635a656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0x46b9527975bd5b8a68582a18e68eaac0618048e6386f9e1fa0a6e18de6e8c96f', 'blockNumber': 10, 'res
- Result shape at `33`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x3ae75c08b4c907eb63a8960c45b86e1e9ab6123c', 'value': '0x1'}, 'blockHash': '0x46b9527975bd5b8a68582a18e68eaac0618048e6386f9e1fa0a6e18de6e8c96f', 'blockNumber': 10, 'result': {'gasUsed': '0x0',
- Result shape at `36`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0xb2cbef3dfb5e69d8656d6974', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x2'}, 'blockHash': '0xaa6cc431712ea8ebe17e14682184305add9f375af0cd6187d6b2b136eac85d1d', 'blockNumber': 11, 'res
- Result shape at `37`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x5f552da00dfb4d3749d9e62dcee3c918855a86a0', 'value': '0x1'}, 'blockHash': '0xaa6cc431712ea8ebe17e14682184305add9f375af0cd6187d6b2b136eac85d1d', 'blockNumber': 11, 'result': {'gasUsed': '0x0',

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

**Geth draft fork · 1.17.7-unstable · c8449896** (`Geth/v1.17.7-unstable-c8449896-2026-09-26/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0-preview · b4211ad9** (`2.1.0-preview+b4211ad9`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

</details>
