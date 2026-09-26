# Create2 collision

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Failed frames have an error string; an exceptional halt omits result or sets it to null. A CREATE2 address collision emits a failed create frame with no result; the caller continues with a later sibling at [2]. A CREATE2 address collision frame has error "Contract address collision". The collision pushes 0 and the caller continues to a successful CALL.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 4 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 4 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 4 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 4 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 4 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Nethermind · 2.1.0-preview · b4211ad9](../../clients/nethermind_development.md) | 3 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 4 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 4 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x6460006000f3600052602a6005601b6000f5602052602a6005601b6000f5604052600060006000600060006110025af160605260606020f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x4c4b40",
      "gasPrice": "0x77359400"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A CREATE2 address collision frame has error "Contract address collision". Expected {'error': 'Contract address collision'}; got {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x4954ee', 'init': '0x60006000f3', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [1], 'type': 'create'}
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x4b792c', 'init': '0x6460006000f3600052602a6005601b6000f5602052602a6005601b6000f5604052600060006000600060006110025af160605260606020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'cod
- Result shape at `trace/1`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x49d01c', 'init': '0x60006000f3', 'value': '0x0'}, 'result': {'address': '0x2ff5d0da975b92c71e01d1eb0cde4e0126e9d75a', 'code': '0x', 'gasUsed': '0x6'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'} is not valid under
- Result shape at `trace/2`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x4954ee', 'init': '0x60006000f3', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [1], 'type': 'create'} is not valid under any of the given schemas

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A CREATE2 address collision frame has error "Contract address collision". Expected {'error': 'Contract address collision'}; got {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x4954ee', 'init': '0x60006000f3', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [1], 'type': 'create'}
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x4b792c', 'init': '0x6460006000f3600052602a6005601b6000f5602052602a6005601b6000f5604052600060006000600060006110025af160605260606020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'cod
- Result shape at `trace/1`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x49d01c', 'init': '0x60006000f3', 'value': '0x0'}, 'result': {'address': '0x2ff5d0da975b92c71e01d1eb0cde4e0126e9d75a', 'code': '0x', 'gasUsed': '0x6'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'} is not valid under
- Result shape at `trace/2`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x4954ee', 'init': '0x60006000f3', 'value': '0x0'}, 'error': 'Illegal state change', 'subtraces': 0, 'traceAddress': [1], 'type': 'create'} is not valid under any of the given schemas

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H09](../../decisions/H09.md): A CREATE2 address collision frame has error "Contract address collision". Expected {'error': 'Contract address collision'}; got {'action': {'creationMethod': 'create2', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x4954ee', 'init': '0x60006000f3', 'value': '0x0'}, 'error': 'contract address collision', 'result': None, 'subtraces': 0, 'traceAddress': [1], 'type': 'create'}

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H09](../../decisions/H09.md): A CREATE2 address collision frame has error "Contract address collision". Expected {'error': 'Contract address collision'}; got {'action': {'creationMethod': 'create2', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x4954ee', 'init': '0x60006000f3', 'value': '0x0'}, 'error': 'contract address collision', 'result': None, 'subtraces': 0, 'traceAddress': [1], 'type': 'create'}

**Nethermind · 2.1.0-preview · b4211ad9** (`2.1.0-preview+b4211ad9`)

- [H29](../../decisions/H29.md): A CREATE2 address collision emits a failed create frame with no result; the caller continues with a later sibling at [2]. record 0: expected {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'value': '0x0'}, 'error': None, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73'}, 'subtraces': 3, 'traceAddress': [], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x4b792c', 'init': '0x6460006000f3600052602a6005601b6000f5602052602a6005601b6000f5604052600060006000600060006110025af160605260606020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000002ff5d0da975b92c71e01d1eb0cde4e0126e9d75a00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0x4afaf1'}, 'subtraces': 2, 'traceAddress': [], 'type': 'create'}
- [H09](../../decisions/H09.md): A CREATE2 address collision frame has error "Contract address collision". No frame matches {'traceAddress': [1], 'type': 'create'}.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H29](../../decisions/H29.md): A CREATE2 address collision emits a failed create frame with no result; the caller continues with a later sibling at [2]. record 0: expected {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'value': '0x0'}, 'error': None, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73'}, 'subtraces': 3, 'traceAddress': [], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x4b792c', 'init': '0x6460006000f3600052602a6005601b6000f5602052602a6005601b6000f5604052600060006000600060006110025af160605260606020f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000002ff5d0da975b92c71e01d1eb0cde4e0126e9d75a00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0x4afaf1'}, 'subtraces': 2, 'traceAddress': [], 'type': 'create'}
- [H09](../../decisions/H09.md): A CREATE2 address collision frame has error "Contract address collision". No frame matches {'traceAddress': [1], 'type': 'create'}.

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H09](../../decisions/H09.md): A CREATE2 address collision frame has error "Contract address collision". Expected {'error': 'Contract address collision'}; got {'action': {'creationMethod': 'create2', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x4954ee', 'init': '0x60006000f3', 'value': '0x0'}, 'error': 'CreateCollision', 'result': None, 'subtraces': 0, 'traceAddress': [1], 'type': 'create'}

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H09](../../decisions/H09.md): A CREATE2 address collision frame has error "Contract address collision". Expected {'error': 'Contract address collision'}; got {'action': {'creationMethod': 'create2', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x4954ee', 'init': '0x60006000f3', 'value': '0x0'}, 'error': 'CreateCollision', 'result': None, 'subtraces': 0, 'traceAddress': [1], 'type': 'create'}

</details>
