# Model environment free

`trace_call` · coverage · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Stack words and storage operands use minimal hex quantities at every depth. Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes. GASPRICE reflects the supplied fee; BASEFEE is zero for a zero-fee call, otherwise the selected base fee; other block fields are preserved. A new contract has creation markers for nonce one, returned runtime and balance, including empty values. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/coverage/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/coverage/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/coverage/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/coverage/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/coverage/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/coverage/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/coverage/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/coverage/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/coverage/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/coverage/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/coverage/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/coverage/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x3a6000524860205243604052426060524560805260a06000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x493e0",
      "gasPrice": "0x0"
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

**Anvil · 1.8.4-nightly · e15c2f1c** (`anvil Version: 1.8.4-nightly+e15c2f1c`)

- [H15](../../decisions/H15.md): GASPRICE reflects the supplied fee; BASEFEE is zero for a zero-fee call, otherwise the selected base fee; other block fields are preserved.

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c35e', 'init': '0x3a6000524860205243604052426060524560805260a06000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000000000000000000000000000000000

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H08](../../decisions/H08.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H17](../../decisions/H17.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H19](../../decisions/H19.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H20](../../decisions/H20.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H21](../../decisions/H21.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.
- [H08](../../decisions/H08.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H17](../../decisions/H17.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H19](../../decisions/H19.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H20](../../decisions/H20.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.
- [H21](../../decisions/H21.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H15](../../decisions/H15.md): GASPRICE reflects the supplied fee; BASEFEE is zero for a zero-fee call, otherwise the selected base fee; other block fields are preserved.

</details>
