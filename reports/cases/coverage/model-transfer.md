# Model transfer

`trace_call` · coverage · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Every transfer to the independently empty-code recipient returns empty bytes. Return one execution envelope per modelled transfer. Transfer 0: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Transfer 0: new-account markers include zero nonce and empty code; the next call treats the account as existing.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/coverage/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/coverage/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/coverage/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/coverage/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/coverage/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/coverage/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/coverage/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/coverage/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/coverage/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-21/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/coverage/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-21/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/coverage/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
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
      "stateDiff",
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1234375000/gas, burn=765625000/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Transfer 0: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Price=2000000000, baseFee=765625000, gas=21000; expected debit=42000000000007, tip=25921875000000.

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H15](../../decisions/H15.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1234375000/gas, burn=765625000/gas, blob fee and destroyed wei=0.
- [H15](../../decisions/H15.md): Transfer 0: exact 21000-gas debit, value credit, miner tip, base-fee burn and per-call nonce progression. Price=2000000000, baseFee=765625000, gas=21000; expected debit=42000000000007, tip=25921875000000.

</details>
