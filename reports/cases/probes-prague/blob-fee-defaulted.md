# Blob fee defaulted

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. A blob call without maxFeePerBlobGas runs with BLOBBASEFEE 0. The factory's CREATE2 child deploys the word it read. Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | 2 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 328811cb](../../clients/anvil_development.md) | 2 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../clients/besu_development.md) | 2 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 2 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../clients/erigon_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../clients/nethermind_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../clients/reth_development.md) | 2 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "blobVersionedHashes": [
        "0x015a4cab4911426699ed34483de6640cf55a568afc5c5edffdcbd8bcd4452f68"
      ],
      "data": "0x00000000000000000000000000000000000000000000000000000000000000004a60005260206000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x493e0",
      "maxFeePerGas": "0x77359400",
      "maxPriorityFeePerGas": "0x77359400",
      "to": "0x4e59b44847b379578588920ca78fbf26c0b4956c"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · 328811cb** (`anvil Version: 1.8.4-nightly+328811cb`)

- [H15](../../decisions/H15.md): A blob call without maxFeePerBlobGas runs with BLOBBASEFEE 0. The factory's CREATE2 child deploys the word it read. Expected {'error': None, 'result': {'code': '0x0000000000000000000000000000000000000000000000000000000000000000'}}; got {'action': {'creationMethod': 'create2', 'from': '0x4e59b44847b379578588920ca78fbf26c0b4956c', 'gas': '0x3b49f', 'init': '0x4a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xab5f25204fcd3dd3bdd4739b52bdeb75e30ed223', 'code': '0x0000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0x1911'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H15](../../decisions/H15.md): A blob call without maxFeePerBlobGas runs with BLOBBASEFEE 0. The factory's CREATE2 child deploys the word it read. Expected {'error': None, 'result': {'code': '0x0000000000000000000000000000000000000000000000000000000000000000'}}; got {'action': {'creationMethod': 'create2', 'from': '0x4e59b44847b379578588920ca78fbf26c0b4956c', 'gas': '0x3b49f', 'init': '0x4a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xab5f25204fcd3dd3bdd4739b52bdeb75e30ed223', 'code': '0x0000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0x1911'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}

**Besu · 26.10-develop · 711f8142** (`besu/v26.10-develop-711f814/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): A blob call without maxFeePerBlobGas runs with BLOBBASEFEE 0. The factory's CREATE2 child deploys the word it read. Expected {'error': None, 'result': {'code': '0x0000000000000000000000000000000000000000000000000000000000000000'}}; got {'action': {'from': '0x4e59b44847b379578588920ca78fbf26c0b4956c', 'gas': '0x3b49f', 'init': '0x4a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xab5f25204fcd3dd3bdd4739b52bdeb75e30ed223', 'code': '0x0000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0x1911'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}
- Result shape at `trace/1`: {'action': {'from': '0x4e59b44847b379578588920ca78fbf26c0b4956c', 'gas': '0x3b49f', 'init': '0x4a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xab5f25204fcd3dd3bdd4739b52bdeb75e30ed223', 'code': '0x0000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0x1911'},

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): A blob call without maxFeePerBlobGas runs with BLOBBASEFEE 0. The factory's CREATE2 child deploys the word it read. Expected {'error': None, 'result': {'code': '0x0000000000000000000000000000000000000000000000000000000000000000'}}; got {'action': {'from': '0x4e59b44847b379578588920ca78fbf26c0b4956c', 'gas': '0x3b49f', 'init': '0x4a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xab5f25204fcd3dd3bdd4739b52bdeb75e30ed223', 'code': '0x0000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0x1911'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}
- Result shape at `trace/1`: {'action': {'from': '0x4e59b44847b379578588920ca78fbf26c0b4956c', 'gas': '0x3b49f', 'init': '0x4a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xab5f25204fcd3dd3bdd4739b52bdeb75e30ed223', 'code': '0x0000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0x1911'},

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H15](../../decisions/H15.md): A blob call without maxFeePerBlobGas runs with BLOBBASEFEE 0. The factory's CREATE2 child deploys the word it read. Expected {'error': None, 'result': {'code': '0x0000000000000000000000000000000000000000000000000000000000000000'}}; got {'action': {'creationMethod': 'create2', 'from': '0x4e59b44847b379578588920ca78fbf26c0b4956c', 'gas': '0x3b49f', 'init': '0x4a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xab5f25204fcd3dd3bdd4739b52bdeb75e30ed223', 'code': '0x0000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0x1911'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H15](../../decisions/H15.md): Assess the declared property. Cannot inspect this property: malformed_json.

**Reth · 2.7.0 · 078d0262** (`Reth Version: 2.7.0+078d0262`)

- [H15](../../decisions/H15.md): A blob call without maxFeePerBlobGas runs with BLOBBASEFEE 0. The factory's CREATE2 child deploys the word it read. Expected {'error': None, 'result': {'code': '0x0000000000000000000000000000000000000000000000000000000000000000'}}; got {'action': {'creationMethod': 'create2', 'from': '0x4e59b44847b379578588920ca78fbf26c0b4956c', 'gas': '0x3b49f', 'init': '0x4a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xab5f25204fcd3dd3bdd4739b52bdeb75e30ed223', 'code': '0x0000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0x1911'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../decisions/H15.md): A blob call without maxFeePerBlobGas runs with BLOBBASEFEE 0. The factory's CREATE2 child deploys the word it read. Expected {'error': None, 'result': {'code': '0x0000000000000000000000000000000000000000000000000000000000000000'}}; got {'action': {'creationMethod': 'create2', 'from': '0x4e59b44847b379578588920ca78fbf26c0b4956c', 'gas': '0x3b49f', 'init': '0x4a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xab5f25204fcd3dd3bdd4739b52bdeb75e30ed223', 'code': '0x0000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0x1911'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}

</details>
