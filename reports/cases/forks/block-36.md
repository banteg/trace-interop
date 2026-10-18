# Block 36

`trace_block` · forks · [All reports](../../README.md)

**What this checks:** Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 12 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | 12 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 12 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 12 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 12 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 12 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 12 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 12 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 12 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/forks/manifest.json) |

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

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'error':
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31
- Result shape at `5`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'erro
- Result shape at `8`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a011', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'result': {'address': '0x2d

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'error':
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31
- Result shape at `5`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'erro
- Result shape at `8`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a011', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'result': {'address': '0x2d

**Erigon · 3.9.0-dev · 1ee57924** (`3.9.0-dev-1ee57924`)

- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `11`: 'transactionHash' is a required property
- Result shape at `11`: 'transactionPosition' is a required property

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `11`: 'transactionHash' is a required property
- Result shape at `11`: 'transactionPosition' is a required property

**Geth draft fork · 1.17.9-unstable · fdbb46a5** (`Geth/v1.17.9-unstable-fdbb46a5-2026-10-18/linux-amd64/go1.26.1`)

- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H09](../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [3]: error 'Mutable Call In Static Context', result null.
- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [6, 0]: error None, result null.
- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `5`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'erro
- Result shape at `9`: {'action': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'balance': '0x0', 'refundAddress': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'subtraces': 0, 'traceAddress': [6, 0], 'transa
- Result shape at `11`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x1bc16d674ec80000'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under an
- Result shape at `11`: 'transactionHash' is a required property
- Result shape at `11`: 'transactionPosition' is a required property

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H09](../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [3]: error 'Mutable Call In Static Context', result null.
- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [6, 0]: error None, result null.
- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `5`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'erro
- Result shape at `9`: {'action': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'balance': '0x0', 'refundAddress': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'subtraces': 0, 'traceAddress': [6, 0], 'transa
- Result shape at `11`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x1bc16d674ec80000'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under an
- Result shape at `11`: 'transactionHash' is a required property
- Result shape at `11`: 'transactionPosition' is a required property

**Reth · 2.7.0 · e6679687** (`Reth Version: 2.7.0+e6679687`)

- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H27](../../decisions/H27.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
