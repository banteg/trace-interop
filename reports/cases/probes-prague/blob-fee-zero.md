# Blob fee zero

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** An explicit zero maxFeePerBlobGas is accepted, not rejected, and runs with BLOBBASEFEE 0. The factory's CREATE2 child deploys the word it read. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../clients/anvil_development.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |

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
      "maxFeePerBlobGas": "0x0",
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

**Anvil · 1.8.4-nightly · df92604b** (`anvil Version: 1.8.4-nightly+df92604b`)

- [H15](../../decisions/H15.md): An explicit zero maxFeePerBlobGas is accepted, not rejected, and runs with BLOBBASEFEE 0. The factory's CREATE2 child deploys the word it read. Expected a result; observed rpc_error -32003 Block `blob_gas_price` is greater than tx-specified `max_fee_per_blob_gas`

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H15](../../decisions/H15.md): An explicit zero maxFeePerBlobGas is accepted, not rejected, and runs with BLOBBASEFEE 0. The factory's CREATE2 child deploys the word it read. Expected a result; observed rpc_error -32003 Block `blob_gas_price` is greater than tx-specified `max_fee_per_blob_gas`

**Besu · 26.10-develop · 28edf391** (`besu/v26.10-develop-28edf39/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): An explicit zero maxFeePerBlobGas is accepted, not rejected, and runs with BLOBBASEFEE 0. The factory's CREATE2 child deploys the word it read. Expected a result; observed rpc_error -32603 Internal error

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): An explicit zero maxFeePerBlobGas is accepted, not rejected, and runs with BLOBBASEFEE 0. The factory's CREATE2 child deploys the word it read. Expected a result; observed rpc_error -32603 Internal error

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../decisions/H15.md): An explicit zero maxFeePerBlobGas is accepted, not rejected, and runs with BLOBBASEFEE 0. The factory's CREATE2 child deploys the word it read. Expected {'error': None, 'result': {'code': '0x0000000000000000000000000000000000000000000000000000000000000000'}}; got {'action': {'creationMethod': 'create2', 'from': '0x4e59b44847b379578588920ca78fbf26c0b4956c', 'gas': '0x3b49f', 'init': '0x4a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xab5f25204fcd3dd3bdd4739b52bdeb75e30ed223', 'code': '0x0000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0x1911'}, 'subtraces': 0, 'traceAddress': [0], 'type': 'create'}

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H15](../../decisions/H15.md): An explicit zero maxFeePerBlobGas is accepted, not rejected, and runs with BLOBBASEFEE 0. The factory's CREATE2 child deploys the word it read. Expected a result; observed rpc_error -32000 maxFeePerBlobGas, if specified, must be non-zero

**Reth · 2.7.0 · 5b686303** (`Reth Version: 2.7.0+5b686303`)

- [H15](../../decisions/H15.md): An explicit zero maxFeePerBlobGas is accepted, not rejected, and runs with BLOBBASEFEE 0. The factory's CREATE2 child deploys the word it read. Expected a result; observed rpc_error -32003 max fee per blob gas less than block blob gas fee

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../decisions/H15.md): An explicit zero maxFeePerBlobGas is accepted, not rejected, and runs with BLOBBASEFEE 0. The factory's CREATE2 child deploys the word it read. Expected a result; observed rpc_error -32003 max fee per blob gas less than block blob gas fee

</details>
