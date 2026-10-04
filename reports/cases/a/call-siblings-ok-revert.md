# Call siblings ok revert

`trace_call` · a · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 3 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | 3 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000001004",
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

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [1]: error 'Reverted', result null.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x, gasUsed 0x6; derived from frozen bytecode.
- Result shape at `trace/2`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001004', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [1], 'type': 'call'} is not valid under any of the given sch

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [1]: error 'Reverted', result null.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x, gasUsed 0x6; derived from frozen bytecode.
- Result shape at `trace/2`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001004', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [1], 'type': 'call'} is not valid under any of the given sch

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [1]: error 'Reverted', result null.
- [H09](../../decisions/H09.md): The fixture REVERT frame preserves its exact return bytes and opcode gas, regardless of error wording. Expected output 0x, gasUsed 0x6; derived from frozen bytecode.
- Result shape at `trace/2`: {'action': {'callType': 'call', 'from': '0x0000000000000000000000000000000000001004', 'gas': '0xea60', 'input': '0x', 'to': '0x0000000000000000000000000000000000001003', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [1], 'type': 'call'} is not valid under any of the given sch

</details>
