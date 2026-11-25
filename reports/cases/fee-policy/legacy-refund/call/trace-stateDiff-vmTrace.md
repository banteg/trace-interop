# Legacy refund/call/trace statediff vmtrace

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Every creation names its creationMethod; a successful one uses address, code and gasUsed. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure. Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../../../clients/reth_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../../../clients/reth_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../../../evidence/2026-11-25/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-25/eval/fee-policy/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x6001600055600060005560006000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x30d40",
      "gasPrice": "0x2da282a9",
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

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (9 in total).
- Result shape at `vmTrace`: {'code': '0x6001600055600060005560006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1'], 'store': None, 'used': 146815}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146812}, 'pc': 2, 'sub': None}, {'cost': 22100, 'ex': {'mem': None, 'pu

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (9 in total).
- Result shape at `vmTrace`: {'code': '0x6001600055600060005560006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1'], 'store': None, 'used': 146815}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146812}, 'pc': 2, 'sub': None}, {'cost': 22100, 'ex': {'mem': None, 'pu

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (9 in total).
- Result shape at `vmTrace`: {'code': '0x6001600055600060005560006000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x1'], 'store': None, 'used': 146815}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146812}, 'pc': 2, 'sub': None}, {'cost': 22100, 'ex': {'mem': None, 'pu

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999953817499939673; miner 0->60320; burn 46182500000000.

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H15](../../../../decisions/H15.md): Call 0: settle exact gas, unused-gas/refund credits, transferred value, nonce, beneficiary tip and base-fee burn. Sender 1000000000000000000->999953817499939673; miner 0->60320; burn 46182500000000.

</details>
