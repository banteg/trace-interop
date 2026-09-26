# Legacy zero/trace/trace

`trace_call` · fee-compat · [All reports](../../../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../../../clients/anvil_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-compat/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../../../clients/anvil_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-compat/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-compat/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../../../clients/besu_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-compat/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-compat/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-compat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-26/anvil/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-compat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-compat/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../../../clients/nethermind_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../../../evidence/2026-09-26/anvil/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-compat/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-26/anvil/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-compat/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-26/anvil/fee-compat/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-26/anvil/fee-compat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x3a60005248602052436040524260605245608052333160a052413160c05260e06000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x30d40",
      "gasPrice": "0x0",
      "value": "0x7"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0b6b3a763fff90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0b6b3a763fff90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: execution output (224 bytes); trace_call: unclassified RPC error: internal error.
- [H15](../../../../decisions/H15.md): Execute each valid simulation and return one envelope per call.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: execution output (224 bytes); trace_call: unclassified RPC error: internal error.
- [H15](../../../../decisions/H15.md): Execute each valid simulation and return one envelope per call.

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: execution output (224 bytes); trace_call: base_fee rejection.
- [H15](../../../../decisions/H15.md): Execute each valid simulation and return one envelope per call.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: execution output (224 bytes); trace_call: base_fee rejection.
- [H15](../../../../decisions/H15.md): Execute each valid simulation and return one envelope per call.

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: execution output (224 bytes); trace_call: execution output (224 bytes). Differing words: BASEFEE: eth_call 0, trace_call 765625000.
- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0b6b3a763fff90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H15](../../../../decisions/H15.md): The identical eth_call and trace_call request has the same observable execution output or fee/funding rejection class. eth_call: execution output (224 bytes); trace_call: execution output (224 bytes). Differing words: BASEFEE: eth_call 0, trace_call 765625000.
- [H15](../../../../decisions/H15.md): Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Expected output 0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000200000000000000000000000000000000000000000000000000000000000000140000000000000000000000000000000000000000000000000000000005f5e1000000000000000000000000000000000000000000000000000de0b6b3a763fff90000000000000000000000000000000000000000000000000000000000000000; independently charged gas 98623.

</details>
