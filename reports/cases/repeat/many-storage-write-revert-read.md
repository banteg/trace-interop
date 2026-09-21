# Many storage write revert read

`trace_callMany` · repeat · [All reports](../../README.md)

**What this checks:** Sequential calls retain prior writes and roll back reverted writes.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 3 records | Checked cases agree; result shape differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 3 records | Checked cases agree; result shape differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 3 records | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 3 records | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 3 records | Checked cases agree | [Response](../../../evidence/2026-09-21/geth-e29edff-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-repeat/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 3 records | Checked cases agree; result shape differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 3 records | Checked cases agree; result shape differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 3 records | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 3 records | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_callMany",
  "params": [
    [
      [
        {
          "data": "0x000000000000000000000000000000000000000000000000000000000000002a0000000000000000000000000000000000000000000000000000000000000000",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x77359400",
          "to": "0x0000000000000000000000000000000000001001"
        },
        [
          "trace",
          "stateDiff"
        ]
      ],
      [
        {
          "data": "0x000000000000000000000000000000000000000000000000000000000000002b0000000000000000000000000000000000000000000000000000000000000001",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x77359400",
          "to": "0x0000000000000000000000000000000000001001"
        },
        [
          "trace",
          "stateDiff"
        ]
      ],
      [
        {
          "data": "0x",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x77359400",
          "to": "0x0000000000000000000000000000000000001001"
        },
        [
          "trace",
          "stateDiff"
        ]
      ]
    ],
    "0x30"
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- Result shape at `1/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d4a0', 'input': '0x000000000000000000000000000000000000000000000000000000000000002b0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x0000000000000000000000000000000000001001', '

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- Result shape at `1/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d4a0', 'input': '0x000000000000000000000000000000000000000000000000000000000000002b0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x0000000000000000000000000000000000001001', '

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- Result shape at `1/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d4a0', 'input': '0x000000000000000000000000000000000000000000000000000000000000002b0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x0000000000000000000000000000000000001001', '

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- Result shape at `1/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d4a0', 'input': '0x000000000000000000000000000000000000000000000000000000000000002b0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x0000000000000000000000000000000000001001', '

</details>
