# Create reverted

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Every creation names its creationMethod; a successful one uses address, code and gasUsed. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. A reverted nested CREATE has error "Reverted" and result {gasUsed, output} with its revert bytes and execution gas, without address or code. The caller sees CREATE push 0 and four bytes of return data.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x6c63deadbeef6000526004601cfd600052600d60136000f06000523d60205260406000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x493e0",
      "gasPrice": "0x77359400"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress [0]: creationMethod null
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result null.
- [H09](../../decisions/H09.md): A reverted nested CREATE has error "Reverted" and result {gasUsed, output} with its revert bytes and execution gas, without address or code. record 1: expected {'absent': ['address', 'code'], 'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'gasUsed': '0x12', 'output': '0xdeadbeef'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}, got {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2d0', 'init': '0x6c63deadbeef6000526004601cfd600052600d60136000f06000523d60205260406000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000
- Result shape at `trace/1`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'} is not valid under any of the given schemas

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress [0]: creationMethod null
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result null.
- [H09](../../decisions/H09.md): A reverted nested CREATE has error "Reverted" and result {gasUsed, output} with its revert bytes and execution gas, without address or code. record 1: expected {'absent': ['address', 'code'], 'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'gasUsed': '0x12', 'output': '0xdeadbeef'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}, got {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2d0', 'init': '0x6c63deadbeef6000526004601cfd600052600d60136000f06000523d60205260406000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000
- Result shape at `trace/1`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'} is not valid under any of the given schemas

</details>
