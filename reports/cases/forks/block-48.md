# Block 48

`trace_block` · forks · [All reports](../../README.md)

**What this checks:** A PoS block has no synthetic PoW reward records. Failed frames have an error string and an explicit object or null result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 4 records | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 4 records | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 3 records | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 3 records | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 3 records | Checked cases agree | [Response](../../../evidence/2026-09-21/geth-e29edff-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-forks/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 4 records | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 4 records | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 3 records | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 3 records | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-forks/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_block",
  "params": [
    "0x30"
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `2`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf2eb34f49098983181d2d0f124d5a310bcd9687c80dbbb8652f3aa4975fe48fe', 'blockNumber': 48, 'error':

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `2`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf2eb34f49098983181d2d0f124d5a310bcd9687c80dbbb8652f3aa4975fe48fe', 'blockNumber': 48, 'error':

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `2`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf2eb34f49098983181d2d0f124d5a310bcd9687c80dbbb8652f3aa4975fe48fe', 'blockNumber': 48, 'error':
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- Result shape at `2`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf2eb34f49098983181d2d0f124d5a310bcd9687c80dbbb8652f3aa4975fe48fe', 'blockNumber': 48, 'error':
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

</details>
