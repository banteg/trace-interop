# Typed out of gas/call/trace vmtrace

`trace_call` · fee-policy · [All reports](../../../../README.md)

**What this checks:** Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. Failed frames have an error string; an exceptional halt omits result or sets it to null. Execute each valid simulation and return one envelope per call. Call 0: use BASEFEE zero for zero fees and the selected base fee for priced calls; preserve other block fields and expose upfront payment and prior settlement through BALANCE. Call 0: distinguish admission from the known execution success/failure.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/observations.json.gz) · [Build/run](../../../../../evidence/2026-09-25/fixture-wave/fee-policy/manifest.json) |

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

**Besu · 26.9-develop · cf89071f** (`besu/v26.9-develop-cf89071/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas
- Result shape at `vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 9223372036854775807, 'ex': {'mem': None, 'push': [], 'store': None, 'used': -9223372036854628908}, 'pc': 5, 'sub': None}]} is not valid under any

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23dd6', 'init': '0x63ffffffff51', 'value': '0x7'}, 'error': 'Out of gas', 'subtraces': 0, 'traceAddress': [], 'type': 'create'} is not valid under any of the given schemas
- Result shape at `vmTrace`: {'code': '0x63ffffffff51', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0xffffffff'], 'store': None, 'used': 146899}, 'pc': 0, 'sub': None}, {'cost': 9223372036854775807, 'ex': {'mem': None, 'push': [], 'store': None, 'used': -9223372036854628908}, 'pc': 5, 'sub': None}]} is not valid under any

</details>
