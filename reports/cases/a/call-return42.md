# Call return42

`trace_call` · a · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth. The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. Root VM bytecode equals the independently frozen execution source. Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. Modelled execution returns exactly the independently computed bytes.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Nethermind · 2.1.0-unstable · 2a3b2531](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "to": "0x0000000000000000000000000000000000001002"
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

**Nethermind · 2.1.0-unstable · 2a3b2531** (`2.1.0-unstable+2a3b2531`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 578994}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x000000000

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 578994}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x000000000

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 578997, got 579000; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 578994, got 578997; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. operation 2 post-step gas does not deduct this operation cost; operation 3 post-step gas does not deduct this operation cost; operation 5 post-step gas does not deduct this operation cost; operation 5 reports a memory write for a read/return
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (PUSH1) used: expected 578997, got 579000; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 578994, got 578997; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H20](../../decisions/H20.md): The independently executable replay/raw root has exact costs, post-step gas, stack and memory effects. step 0 (PUSH1) used: expected 578997, got 579000; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 578994, got 578997; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}
- [H20](../../decisions/H20.md): At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. operation 2 post-step gas does not deduct this operation cost; operation 3 post-step gas does not deduct this operation cost; operation 5 post-step gas does not deduct this operation cost; operation 5 reports a memory write for a read/return
- [H20](../../decisions/H20.md): Every modelled step has exact opcode cost, post-step gas, stack effects, memory writes and storage effects. step 0 (PUSH1) used: expected 578997, got 579000; step 0 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}; step 1 (PUSH1) used: expected 578994, got 578997; step 1 (PUSH1) mem: expected None, got {'data': '0x', 'off': 0}

</details>
