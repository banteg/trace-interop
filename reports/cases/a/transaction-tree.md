# Transaction tree

`trace_transaction` · a · [All reports](../../README.md)

**What this checks:** Failed frames have an error string and an explicit object or null result. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 9 records | Differs; result shape differs | [Response](../../../evidence/2026-09-23/h03-modes-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-a/manifest.json) |
| [Besu · Release](../../clients/besu_release.md) | Setup incomplete; not assessed | Not assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Besu · Release](../../clients/besu_release.md) | 9 records | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-a-besu-retry/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a-besu-retry/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 9 records | Differs; result shape differs | [Response](../../../evidence/2026-09-23/h03-modes-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-a/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 9 records | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 9 records | Partially assessed | [Response](../../../evidence/2026-09-23/h03-modes-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-a/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 9 records | Partially assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 9 records | Partially assessed | [Response](../../../evidence/2026-09-23/h03-modes-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-a/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 9 records | Partially assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 9 records | Partially assessed | [Response](../../../evidence/2026-09-21/geth-e29edff-a/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-a/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 9 records | Partially assessed | [Response](../../../evidence/2026-09-23/h03-modes-geth-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-geth-a/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 9 records | Differs; result shape differs | [Response](../../../evidence/2026-09-23/h03-modes-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-a/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 9 records | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 9 records | Differs; result shape differs | [Response](../../../evidence/2026-09-23/h03-modes-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-a/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 9 records | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 9 records | Partially assessed | [Response](../../../evidence/2026-09-23/h03-modes-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-a/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 9 records | Partially assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 9 records | Partially assessed | [Response](../../../evidence/2026-09-23/h03-modes-a/observations.json) · [Build/run](../../../evidence/2026-09-23/h03-modes-a/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 9 records | Partially assessed | [Response](../../../evidence/2026-09-21/verified-a/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_transaction",
  "params": [
    "0x55d219e322321525fb6d15c388d730e0f6d0ae119e68163ffcea6d3ee50fa738"
  ]
}
```

**Geth draft fork · Draft fork** (`Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1`)

- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result':

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result':

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result':

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result':

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result':

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result':

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result':

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result':

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Geth draft fork · Draft fork** (`Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1`)

- [H23](../../decisions/H23.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

</details>
