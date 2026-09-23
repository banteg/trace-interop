# Model many transfers

`trace_callMany` · coverage · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Every transfer to the independently empty-code recipient returns empty bytes. Return one execution envelope per modelled transfer. Transfer 0: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Transfer 0: new-account markers include zero nonce and empty code; the next call treats the account as existing. Transfer 1: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Transfer 1: new-account markers include zero nonce and empty code; the next call treats the account as existing.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 📦 Release](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Besu · 🛠️ Development](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Erigon · 📦 Release](../../clients/erigon_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Erigon · 🛠️ Development](../../clients/erigon_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Geth draft fork · 🧪 Draft fork](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Nethermind · 📦 Release](../../clients/nethermind_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Nethermind · 🛠️ Development](../../clients/nethermind_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Reth · 📦 Release](../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |
| [Reth · 🛠️ Development](../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/coverage-matrix/coverage/observations.json) · [Build/run](../../../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) |

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
          "data": "0x",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x186a0",
          "gasPrice": "0x77359400",
          "to": "0x0000000000000000000000000000000000004444",
          "value": "0x7"
        },
        [
          "trace",
          "stateDiff"
        ]
      ],
      [
        {
          "data": "0x",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x186a0",
          "gasPrice": "0x77359400",
          "to": "0x0000000000000000000000000000000000004444",
          "value": "0x7"
        },
        [
          "trace",
          "stateDiff"
        ]
      ]
    ],
    "latest"
  ]
}
```

**Erigon · 🛠️ Development** (`3.8.0-dev-c25b8e47`)

- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=25921875000000, burn=16078125000000.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=25921875000000, burn=16078125000000.
- [H16](../../decisions/H16.md): Transfer 0: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Price=2000000000, baseFee=765625000, gas=21000; expected debit=42000000000007, tip=25921875000000.
- [H16](../../decisions/H16.md): Transfer 1: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Price=2000000000, baseFee=765625000, gas=21000; expected debit=42000000000007, tip=25921875000000.

**Erigon · 📦 Release** (`3.6.1-0c4d9c91`)

- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=25921875000000, burn=16078125000000.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=25921875000000, burn=16078125000000.
- [H16](../../decisions/H16.md): Transfer 0: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Price=2000000000, baseFee=765625000, gas=21000; expected debit=42000000000007, tip=25921875000000.
- [H16](../../decisions/H16.md): Transfer 1: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Price=2000000000, baseFee=765625000, gas=21000; expected debit=42000000000007, tip=25921875000000.

**Nethermind · 🛠️ Development** (`2.1.0-unstable+a404c4f0`)

- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000000000: new account lacks creation markers for all fields; 0x0000000000000000000000000000000000004444: new account lacks creation markers for all fields
- [H17](../../decisions/H17.md): Transfer 0: new-account markers include zero nonce and empty code; the next call treats the account as existing.

**Nethermind · 📦 Release** (`1.39.3+28cbe2a0`)

- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000000000: new account lacks creation markers for all fields; 0x0000000000000000000000000000000000004444: new account lacks creation markers for all fields
- [H17](../../decisions/H17.md): Transfer 0: new-account markers include zero nonce and empty code; the next call treats the account as existing.

**Reth · 🛠️ Development** (`Reth Version: 2.5.2+03cb186c`)

- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000004444: new account lacks creation markers for all fields
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=25921875000000, burn=16078125000000.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=25921875000000, burn=16078125000000.
- [H16](../../decisions/H16.md): Transfer 0: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Price=2000000000, baseFee=765625000, gas=21000; expected debit=42000000000007, tip=25921875000000.
- [H17](../../decisions/H17.md): Transfer 0: new-account markers include zero nonce and empty code; the next call treats the account as existing.
- [H16](../../decisions/H16.md): Transfer 1: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Price=2000000000, baseFee=765625000, gas=21000; expected debit=42000000000007, tip=25921875000000.

**Reth · 📦 Release** (`Reth Version: 2.6.0+73a3a008`)

- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000004444: new account lacks creation markers for all fields
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=25921875000000, burn=16078125000000.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=25921875000000, burn=16078125000000.
- [H16](../../decisions/H16.md): Transfer 0: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Price=2000000000, baseFee=765625000, gas=21000; expected debit=42000000000007, tip=25921875000000.
- [H17](../../decisions/H17.md): Transfer 0: new-account markers include zero nonce and empty code; the next call treats the account as existing.
- [H16](../../decisions/H16.md): Transfer 1: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Price=2000000000, baseFee=765625000, gas=21000; expected debit=42000000000007, tip=25921875000000.

</details>
