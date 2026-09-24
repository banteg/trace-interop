# Call siblings revert ok

`trace_call` · repeat · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. The successful second sibling retains its output and has no error. Stack words use minimal hex quantities at every depth. Failed frames have an error string and an explicit object or null result. The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. Root VM bytecode equals the independently frozen execution source.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |
| [Nethermind · 2.1.0-unstable · 9d6e8b8d](../../clients/nethermind_development.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 3 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 3 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |

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
      "to": "0x0000000000000000000000000000000000001005"
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

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H24](../../decisions/H24.md): The successful second sibling retains its output and has no error.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x, gasUsed 0x6; derived from frozen bytecode.
- Result shape at `trace/1`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'call'} is not valid under any of the given sch
- Result shape at `trace/2`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [1], 'type': 'call'} is not valid under any of the given sch

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H24](../../decisions/H24.md): The successful second sibling retains its output and has no error.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x, gasUsed 0x6; derived from frozen bytecode.
- Result shape at `trace/1`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'call'} is not valid under any of the given sch
- Result shape at `trace/2`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [1], 'type': 'call'} is not valid under any of the given sch

**Nethermind · 2.1.0-unstable · 9d6e8b8d** (`2.1.0-unstable+9d6e8b8d`)

- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x, gasUsed 0x6; derived from frozen bytecode.
- Result shape at `trace/1`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'call'} is not valid under any of the given sch

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- [H09](../../decisions/H09.md): Failed frames have an error string and an explicit object or null result.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x, gasUsed 0x6; derived from frozen bytecode.
- Result shape at `trace/1`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001005', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'call'} is not valid under any of the given sch
- Result shape at `vmTrace`: {'code': '0x6020600060006000600061100361ea60f1506020600060006000600061100261ea60f15000', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x20'], 'store': None, 'used': 578997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 578994}, 'pc': 2, 'sub':

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H20](../../decisions/H20.md): At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. subtrace 7: operation 2 post-step gas does not deduct this operation cost; subtrace 7: operation 2 reports a memory write for a read/return; operation 8 post-step gas does not deduct this operation cost; operation 9 post-step gas does not deduct this operation cost

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H20](../../decisions/H20.md): At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. subtrace 7: operation 2 post-step gas does not deduct this operation cost; subtrace 7: operation 2 reports a memory write for a read/return; operation 8 post-step gas does not deduct this operation cost; operation 9 post-step gas does not deduct this operation cost

</details>
