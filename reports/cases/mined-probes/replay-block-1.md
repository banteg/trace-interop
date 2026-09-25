# Replay block 1

`trace_replayBlockTransactions` · mined-probes · [All reports](../../README.md)

**What this checks:** The sender pays value, receipt gas at the effective price and any blob fee, and its nonce advances once. The fee recipient gains exactly the priority fee on the receipt gas. An absent account funded by the transaction is born with balance, zero nonce and empty code markers. Block replay has exactly one envelope per frozen transaction, with hashes in transaction order. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x1",
    [
      "trace",
      "stateDiff"
    ]
  ]
}
```

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H17](../../decisions/H17.md): An absent account funded by the transaction is born with balance, zero nonce and empty code markers. 0x000000000000000000000000000000000000b10b: expected {'balance': {'+': '0x7'}, 'code': {'+': '0x'}, 'nonce': {'+': '0x0'}, 'storage': {}}, got {'balance': {'+': '0x7'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}.
- [H17](../../decisions/H17.md): An absent account funded by the transaction is born with balance, zero nonce and empty code markers. 0x0000000000000000000000000000000000000000: expected {'balance': {'+': '0x2632e314a000'}, 'code': {'+': '0x'}, 'nonce': {'+': '0x0'}, 'storage': {}}, got {'balance': {'+': '0x2632e314a000'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}.
- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000000000: new account lacks creation markers for all fields; 0x000000000000000000000000000000000000b10b: new account lacks creation markers for all fields
- Result shape at `0/stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'+': '0x2632e314a000'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x000000000000000000000000000000000000b10b': {'balance': {'+': '0x7'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395

**Reth · 2.5.2 · 4630cc58** (`Reth Version: 2.5.2+4630cc58`)

- [H17](../../decisions/H17.md): An absent account funded by the transaction is born with balance, zero nonce and empty code markers. 0x000000000000000000000000000000000000b10b: expected {'balance': {'+': '0x7'}, 'code': {'+': '0x'}, 'nonce': {'+': '0x0'}, 'storage': {}}, got {'balance': {'*': {'from': '0x0', 'to': '0x7'}}, 'code': '=', 'nonce': '=', 'storage': {}}.
- [H17](../../decisions/H17.md): An absent account funded by the transaction is born with balance, zero nonce and empty code markers. 0x0000000000000000000000000000000000000000: expected {'balance': {'+': '0x2632e314a000'}, 'code': {'+': '0x'}, 'nonce': {'+': '0x0'}, 'storage': {}}, got {'balance': {'*': {'from': '0x0', 'to': '0x2632e314a000'}}, 'code': '=', 'nonce': '=', 'storage': {}}.
- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000000000: new account lacks creation markers for all fields; 0x000000000000000000000000000000000000b10b: new account lacks creation markers for all fields

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H17](../../decisions/H17.md): An absent account funded by the transaction is born with balance, zero nonce and empty code markers. 0x000000000000000000000000000000000000b10b: expected {'balance': {'+': '0x7'}, 'code': {'+': '0x'}, 'nonce': {'+': '0x0'}, 'storage': {}}, got {'balance': {'*': {'from': '0x0', 'to': '0x7'}}, 'code': '=', 'nonce': '=', 'storage': {}}.
- [H17](../../decisions/H17.md): An absent account funded by the transaction is born with balance, zero nonce and empty code markers. 0x0000000000000000000000000000000000000000: expected {'balance': {'+': '0x2632e314a000'}, 'code': {'+': '0x'}, 'nonce': {'+': '0x0'}, 'storage': {}}, got {'balance': {'*': {'from': '0x0', 'to': '0x2632e314a000'}}, 'code': '=', 'nonce': '=', 'storage': {}}.
- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000000000: new account lacks creation markers for all fields; 0x000000000000000000000000000000000000b10b: new account lacks creation markers for all fields

</details>
