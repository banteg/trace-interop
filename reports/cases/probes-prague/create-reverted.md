# Create reverted

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. A reverted nested CREATE has error "Reverted" and result {gasUsed, output} with its revert bytes and execution gas, without address or code. The caller sees CREATE push 0 and four bytes of return data.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |

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

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result {"address": "0xa121e69656643935d9773b079316e0bf2bcfead3", "code": "0xdeadbeef", "gasUsed": "0x12"}.
- [H09](../../decisions/H09.md): A reverted nested CREATE has error "Reverted" and result {gasUsed, output} with its revert bytes and execution gas, without address or code. record 1: expected {'absent': ['address', 'code'], 'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'gasUsed': '0x12', 'output': '0xdeadbeef'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0xdeadbeef', 'gasUsed': '0x12'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}
- Result shape at `trace/1`: {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0xdeadbeef', 'gasUsed': '0x12'},

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result {"address": "0xa121e69656643935d9773b079316e0bf2bcfead3", "code": "0xdeadbeef", "gasUsed": "0x12"}.
- [H09](../../decisions/H09.md): A reverted nested CREATE has error "Reverted" and result {gasUsed, output} with its revert bytes and execution gas, without address or code. record 1: expected {'absent': ['address', 'code'], 'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'gasUsed': '0x12', 'output': '0xdeadbeef'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0xdeadbeef', 'gasUsed': '0x12'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}
- Result shape at `trace/1`: {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0xdeadbeef', 'gasUsed': '0x12'},

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result null.
- [H09](../../decisions/H09.md): A reverted nested CREATE has error "Reverted" and result {gasUsed, output} with its revert bytes and execution gas, without address or code. record 1: expected {'absent': ['address', 'code'], 'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'gasUsed': '0x12', 'output': '0xdeadbeef'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}, got {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2d0', 'init': '0x6c63deadbeef6000526004601cfd600052600d60136000f06000523d60205260406000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000
- Result shape at `trace/1`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'} is not valid under any of the given schemas

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result null.
- [H09](../../decisions/H09.md): A reverted nested CREATE has error "Reverted" and result {gasUsed, output} with its revert bytes and execution gas, without address or code. record 1: expected {'absent': ['address', 'code'], 'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'gasUsed': '0x12', 'output': '0xdeadbeef'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}, got {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2d0', 'init': '0x6c63deadbeef6000526004601cfd600052600d60136000f06000523d60205260406000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x0000000000000000000000000000000000
- Result shape at `trace/1`: {'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'} is not valid under any of the given schemas

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result {"address": "0xa121e69656643935d9773b079316e0bf2bcfead3", "code": "0xdeadbeef", "gasUsed": "0x12"}.
- [H09](../../decisions/H09.md): A reverted nested CREATE has error "Reverted" and result {gasUsed, output} with its revert bytes and execution gas, without address or code. record 1: expected {'absent': ['address', 'code'], 'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'gasUsed': '0x12', 'output': '0xdeadbeef'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0xdeadbeef', 'gasUsed': '0x12'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}
- Result shape at `trace/1`: {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0xdeadbeef', 'gasUsed': '0x12'},

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result {"address": "0xa121e69656643935d9773b079316e0bf2bcfead3", "code": "0xdeadbeef", "gasUsed": "0x12"}.
- [H09](../../decisions/H09.md): A reverted nested CREATE has error "Reverted" and result {gasUsed, output} with its revert bytes and execution gas, without address or code. record 1: expected {'absent': ['address', 'code'], 'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'gasUsed': '0x12', 'output': '0xdeadbeef'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0xdeadbeef', 'gasUsed': '0x12'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}
- Result shape at `trace/1`: {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0xdeadbeef', 'gasUsed': '0x12'},

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result null.
- [H09](../../decisions/H09.md): A reverted nested CREATE has error "Reverted" and result {gasUsed, output} with its revert bytes and execution gas, without address or code. record 1: expected {'absent': ['address', 'code'], 'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'gasUsed': '0x12', 'output': '0xdeadbeef'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}
- Result shape at `trace/1`: {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'} is not valid under any of the given schemas

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result null.
- [H09](../../decisions/H09.md): A reverted nested CREATE has error "Reverted" and result {gasUsed, output} with its revert bytes and execution gas, without address or code. record 1: expected {'absent': ['address', 'code'], 'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'gasUsed': '0x12', 'output': '0xdeadbeef'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}
- Result shape at `trace/1`: {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddress': [0], 'type': 'create'} is not valid under any of the given schemas

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result {"address": "0xa121e69656643935d9773b079316e0bf2bcfead3", "code": "0xdeadbeef", "gasUsed": "0x12"}.
- [H09](../../decisions/H09.md): A reverted nested CREATE has error "Reverted" and result {gasUsed, output} with its revert bytes and execution gas, without address or code. record 1: expected {'absent': ['address', 'code'], 'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'gasUsed': '0x12', 'output': '0xdeadbeef'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0xdeadbeef', 'gasUsed': '0x12'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}
- Result shape at `trace/1`: {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0xdeadbeef', 'gasUsed': '0x12'},

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result {"address": "0xa121e69656643935d9773b079316e0bf2bcfead3", "code": "0xdeadbeef", "gasUsed": "0x12"}.
- [H09](../../decisions/H09.md): A reverted nested CREATE has error "Reverted" and result {gasUsed, output} with its revert bytes and execution gas, without address or code. record 1: expected {'absent': ['address', 'code'], 'action': {'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'gasUsed': '0x12', 'output': '0xdeadbeef'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}, got {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0xdeadbeef', 'gasUsed': '0x12'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}
- Result shape at `trace/1`: {'action': {'creationMethod': 'create', 'from': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'gas': '0x338a3', 'init': '0x63deadbeef6000526004601cfd', 'value': '0x0'}, 'error': 'Reverted', 'result': {'address': '0xa121e69656643935d9773b079316e0bf2bcfead3', 'code': '0xdeadbeef', 'gasUsed': '0x12'},

</details>
