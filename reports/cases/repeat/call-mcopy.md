# Call mcopy

`trace_call` · repeat · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. MCOPY reports its same-step write of word 42 at offset 32. Stack words and storage operands use minimal hex quantities at every depth. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. At every VM depth, every pc lies inside the code, PUSH matches bytecode, each step deducts its cost and a call or creation also receives its child leftover or, entering no frame, includes the gas it forwarded, subtraces appear only on calls and creations, MLOAD mem is its loaded word, call mem is the output window or the copied return data, and RETURN/REVERT report no mem. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x000000000000000000000000000000000000100a",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x"
    },
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "0x30"
  ]
}
```

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H20](../../decisions/H20.md): MCOPY reports its same-step write of word 42 at offset 32.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 6 (MCOPY) mem: expected {'off': 32, 'data': '0x000000000000000000000000000000000000000000000000000000000000002a'}, got None
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 6 (MCOPY) mem: expected {'off': 32, 'data': '0x000000000000000000000000000000000000000000000000000000000000002a'}, got None

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H20](../../decisions/H20.md): MCOPY reports its same-step write of word 42 at offset 32.
- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 6 (MCOPY) mem: expected {'off': 32, 'data': '0x000000000000000000000000000000000000000000000000000000000000002a'}, got None
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 6 (MCOPY) mem: expected {'off': 32, 'data': '0x000000000000000000000000000000000000000000000000000000000000002a'}, got None

</details>
