# Transaction tree

`trace_transaction` · a · [All reports](../../README.md)

**What this checks:** Failed frames have an error string and an explicit object or null result. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Nethermind · 2.1.0-unstable · 2a3b2531](../../clients/nethermind_development.md) | 9 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 9 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |

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

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H23](../../decisions/H23.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result':

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H23](../../decisions/H23.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result':

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H23](../../decisions/H23.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H23](../../decisions/H23.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.7-unstable · fa8ecb92** (`Geth/v1.17.7-unstable-fa8ecb92-2026-09-24/linux-amd64/go1.26.1`)

- [H23](../../decisions/H23.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.1.0-unstable · 2a3b2531** (`2.1.0-unstable+2a3b2531`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H23](../../decisions/H23.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result':

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H23](../../decisions/H23.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d5b8', 'input': '0x', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'result':

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H23](../../decisions/H23.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H23](../../decisions/H23.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
