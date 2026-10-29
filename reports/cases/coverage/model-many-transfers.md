# Model many transfers

`trace_callMany` · coverage · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Every transfer to the independently empty-code recipient returns empty bytes. Return one execution envelope per modelled transfer. Transfer 0: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Transfer 0: new-account markers include zero nonce and empty code; the next call treats the account as existing. Transfer 1: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Transfer 1: new-account markers include zero nonce and empty code; the next call treats the account as existing.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/coverage/manifest.json) |

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

**Reth · 2.8.1 · 966010c9** (`Reth Version: 2.8.1+966010c9`)

- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1234375000/gas, burn=765625000/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1234375000/gas, burn=765625000/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Transfer 0: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Price=2000000000, baseFee=765625000, gas=21000; expected debit=42000000000007, tip=25921875000000.
- [H15](../../decisions/H15.md): Transfer 1: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Price=2000000000, baseFee=765625000, gas=21000; expected debit=42000000000007, tip=25921875000000.

**Reth · 2.9.0 · c9a780f4** (`Reth Version: 2.9.0+c9a780f4`)

- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1234375000/gas, burn=765625000/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1234375000/gas, burn=765625000/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Transfer 0: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Price=2000000000, baseFee=765625000, gas=21000; expected debit=42000000000007, tip=25921875000000.
- [H15](../../decisions/H15.md): Transfer 1: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Price=2000000000, baseFee=765625000, gas=21000; expected debit=42000000000007, tip=25921875000000.

</details>
