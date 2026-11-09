# Legacy revert/call/trace vmtrace

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Unrequested stateDiff is null. Output remains a byte string under every trace selection. Every creation names its creationMethod; a successful one uses address, code and gasUsed. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../../../clients/besu_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../../../clients/besu_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../../../evidence/2026-11-09/eval/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-11-09/eval/fee-policy/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x602a60005260206000fd",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x30d40",
      "gasPrice": "0x2da282a9",
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

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H10](../../../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (6 in total).
- [H09](../../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dae', 'init': '0x602a60005260206000fd', 'value': '0x7'}, 'error': 'Reverted', 'revertReason': '0x000000000000000000000000000000000000000000000000000000000000002a', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is n
- Result shape at `vmTrace`: {'code': '0x602a60005260206000fd', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 146859}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146856}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x0000000000

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H10](../../../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (6 in total).
- [H09](../../../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dae', 'init': '0x602a60005260206000fd', 'value': '0x7'}, 'error': 'Reverted', 'revertReason': '0x000000000000000000000000000000000000000000000000000000000000002a', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is n
- Result shape at `vmTrace`: {'code': '0x602a60005260206000fd', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 146859}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146856}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x0000000000

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'idx', 'op', 'pc', 'sub'] (6 in total).
- Result shape at `vmTrace`: {'code': '0x602a60005260206000fd', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 146859}, 'idx': '0', 'op': 'PUSH1', 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146856}, 'idx': '1', 'op': 'PUSH1', 'pc': 2, 'sub': N

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H21](../../../../decisions/H21.md): Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. First at root pc 0: members ['cost', 'ex', 'pc', 'sub'] (6 in total).
- Result shape at `vmTrace`: {'code': '0x602a60005260206000fd', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 146859}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x0'], 'store': None, 'used': 146856}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x0000000000

</details>
