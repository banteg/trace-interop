# Block 36

`trace_block` · forks · [All reports](../../README.md)

**What this checks:** Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 12 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../clients/besu_development.md) | 12 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 12 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 12 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../clients/go-ethereum_trace.md) | 12 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 12 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../clients/nethermind_development.md) | 12 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 12 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 12 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-24/adopted-stances/forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_block",
  "params": [
    "0x24"
  ]
}
```

**Besu · 26.9-develop · 85b32978** (`besu/v26.9-develop-85b3297/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'error':
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31
- Result shape at `8`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a011', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'result': {'address': '0x2d

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'error':
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31
- Result shape at `8`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a011', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'result': {'address': '0x2d

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `11`: 'transactionHash' is a required property
- Result shape at `11`: 'transactionPosition' is a required property

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `11`: 'transactionHash' is a required property
- Result shape at `11`: 'transactionPosition' is a required property

**Geth draft fork · 1.17.7-unstable · bb5c4682** (`Geth/v1.17.7-unstable-bb5c4682-2026-09-24/linux-amd64/go1.26.1`)

- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0-preview · ce501a97** (`2.1.0-preview+ce501a97`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'error':
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31
- Result shape at `11`: 'transactionHash' is a required property
- Result shape at `11`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.
- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'error':
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31
- Result shape at `11`: 'transactionHash' is a required property
- Result shape at `11`: 'transactionPosition' is a required property

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `11`: 'transactionHash' is a required property
- Result shape at `11`: 'transactionPosition' is a required property

</details>
