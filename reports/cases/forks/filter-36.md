# Filter 36

`trace_filter` · forks · [All reports](../../README.md)

**What this checks:** Failed frames have an error string and an explicit object or null result. A single-block filter agrees with trace_block at the same fork.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 12 records | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 12 records | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 12 records | Checked cases agree; result shape differs | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 12 records | Checked cases agree; result shape differs | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 12 records | Checked cases agree | [Response](../../../evidence/2026-09-21/geth-e29edff-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-forks/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 12 records | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 12 records | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 12 records | Checked cases agree; result shape differs | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 12 records | Checked cases agree; result shape differs | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x24",
      "toBlock": "0x24"
    }
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'error':
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31
- Result shape at `5`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'erro
- Result shape at `8`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a011', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'result': {'address': '0x2d

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'error':
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31
- Result shape at `5`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'erro
- Result shape at `8`: {'action': {'creationMethod': 'create', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0x6a011', 'init': '0x5b646368696c6460006000a133ff', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'result': {'address': '0x2d

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- Result shape at `11`: 'transactionHash' is a required property
- Result shape at `11`: 'transactionPosition' is a required property

**Erigon · Release** (`3.6.1-0c4d9c91`)

- Result shape at `11`: 'transactionHash' is a required property
- Result shape at `11`: 'transactionPosition' is a required property

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'error':
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31
- Result shape at `5`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'erro
- Result shape at `11`: 'transactionHash' is a required property
- Result shape at `11`: 'transactionPosition' is a required property

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'error':
- Result shape at `3`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31
- Result shape at `5`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0x6e5b6369d615c8e0c46837766f513bb31e33ce819e637cd70f66871abed86eed', 'blockNumber': 36, 'erro
- Result shape at `11`: 'transactionHash' is a required property
- Result shape at `11`: 'transactionPosition' is a required property

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- Result shape at `11`: 'transactionHash' is a required property
- Result shape at `11`: 'transactionPosition' is a required property

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- Result shape at `11`: 'transactionHash' is a required property
- Result shape at `11`: 'transactionPosition' is a required property

</details>
