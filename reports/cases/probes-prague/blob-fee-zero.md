# Blob fee zero

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Blob defaults, validation and BLOBBASEFEE for omitted or zero pricing remain separately unresolved. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32003` | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | RPC error `-32003` | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | 2 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 2 call frames; nonempty output | 🟡 Partially assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | RPC error `-32000` | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32003` | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | RPC error `-32003` | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/probes-prague/manifest.json) |

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

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H15](../../decisions/H15.md): Blob defaults, validation and BLOBBASEFEE for omitted or zero pricing remain separately unresolved. Observed rpc_error -32003: Block `blob_gas_price` is greater than tx-specified `max_fee_per_blob_gas`. The retained universal-zero expectation no longer defines conformance.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H15](../../decisions/H15.md): Blob defaults, validation and BLOBBASEFEE for omitted or zero pricing remain separately unresolved. Observed rpc_error -32003: Block `blob_gas_price` is greater than tx-specified `max_fee_per_blob_gas`. The retained universal-zero expectation no longer defines conformance.

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Blob defaults, validation and BLOBBASEFEE for omitted or zero pricing remain separately unresolved. Observed rpc_error -32603: Internal error. The retained universal-zero expectation no longer defines conformance.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): Blob defaults, validation and BLOBBASEFEE for omitted or zero pricing remain separately unresolved. Observed rpc_error -32603: Internal error. The retained universal-zero expectation no longer defines conformance.

**Erigon · 3.8.0-dev · 85e1ca92** (`3.8.0-dev-85e1ca92`)

- [H15](../../decisions/H15.md): Blob defaults, validation and BLOBBASEFEE for omitted or zero pricing remain separately unresolved. Observed deployed BLOBBASEFEE word 0x0000000000000000000000000000000000000000000000000000000000000000. The retained universal-zero expectation no longer defines conformance.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../decisions/H15.md): Blob defaults, validation and BLOBBASEFEE for omitted or zero pricing remain separately unresolved. Observed deployed BLOBBASEFEE word 0x0000000000000000000000000000000000000000000000000000000000000001. The retained universal-zero expectation no longer defines conformance.

**Geth draft fork · 1.17.7-unstable · e26833e3** (`Geth/v1.17.7-unstable-e26833e3-2026-09-26/linux-amd64/go1.26.1`)

- [H15](../../decisions/H15.md): Blob defaults, validation and BLOBBASEFEE for omitted or zero pricing remain separately unresolved. Observed deployed BLOBBASEFEE word 0x0000000000000000000000000000000000000000000000000000000000000000. The retained universal-zero expectation no longer defines conformance.

**Nethermind · 2.2.0-preview · f69690c5** (`2.2.0-preview+f69690c5`)

- [H15](../../decisions/H15.md): Blob defaults, validation and BLOBBASEFEE for omitted or zero pricing remain separately unresolved. Observed rpc_error -32000: maxFeePerBlobGas, if specified, must be non-zero. The retained universal-zero expectation no longer defines conformance.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H15](../../decisions/H15.md): Blob defaults, validation and BLOBBASEFEE for omitted or zero pricing remain separately unresolved. Observed rpc_error -32000: maxFeePerBlobGas, if specified, must be non-zero. The retained universal-zero expectation no longer defines conformance.

**Reth · 2.7.0 · 60aeb532** (`Reth Version: 2.7.0+60aeb532`)

- [H15](../../decisions/H15.md): Blob defaults, validation and BLOBBASEFEE for omitted or zero pricing remain separately unresolved. Observed rpc_error -32003: max fee per blob gas less than block blob gas fee. The retained universal-zero expectation no longer defines conformance.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../decisions/H15.md): Blob defaults, validation and BLOBBASEFEE for omitted or zero pricing remain separately unresolved. Observed rpc_error -32003: max fee per blob gas less than block blob gas fee. The retained universal-zero expectation no longer defines conformance.

</details>
