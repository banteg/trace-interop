# Typed out of gas/call/trace vmtrace

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Unrequested stateDiff is null. Output remains a byte string under every trace selection. Every creation names its creationMethod; a successful one uses address, code and gasUsed. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Failed frames have an error string; an exceptional halt carries result null. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../../../clients/erigon_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../../../clients/nethermind_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-10-18/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-10-18/eval/fee-policy/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x63ffffffff51",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x30d40",
      "maxFeePerGas": "0x5b450550",
      "maxPriorityFeePerGas": "0x1",
      "value": "0x7"
    },
    [
      "trace",
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H10](../../../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (2 in total).
- [H09](../../../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress []: error 'Out of gas', result null.
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas
- Result shape at `vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 9223372036854775807, 'ex': {'mem': None, 'push': [], 'store': None, 'used': -9223372036854628908}, 'pc': 5, 'sub': None}]} is not valid under any

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H10](../../../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (2 in total).
- [H09](../../../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress []: error 'Out of gas', result null.
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas
- Result shape at `vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 9223372036854775807, 'ex': {'mem': None, 'push': [], 'store': None, 'used': -9223372036854628908}, 'pc': 5, 'sub': None}]} is not valid under any

**Erigon · 3.9.0-dev · 1ee57924** (`3.9.0-dev-1ee57924`)

- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (2 in total).
- Result shape at `vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'idx': '0', 'op': 'PUSH4', 'pc': 0, 'sub': None}, {'cost': 35184775266310, 'ex': None, 'idx': '1', 'op': 'MLOAD', 'pc': 5, 'sub': None}]} is not valid under any of the given sch

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (2 in total).
- Result shape at `vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'idx': '0', 'op': 'PUSH4', 'pc': 0, 'sub': None}, {'cost': 35184775266310, 'ex': None, 'idx': '1', 'op': 'MLOAD', 'pc': 5, 'sub': None}]} is not valid under any of the given sch

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (2 in total).
- [H09](../../../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress []: error 'Out of gas', result null.
- Result shape at `trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas
- Result shape at `vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 146899, 'ex': None, 'pc': 5, 'sub': None}]} is not valid under any of the given schemas

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (2 in total).
- [H09](../../../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress []: error 'Out of gas', result null.
- Result shape at `trace/0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas
- Result shape at `vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 146899, 'ex': None, 'pc': 5, 'sub': None}]} is not valid under any of the given schemas

</details>
