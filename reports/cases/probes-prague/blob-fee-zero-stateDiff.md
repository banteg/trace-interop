# Blob fee zero statediff

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** A blob call whose maxFeePerBlobGas is omitted or 0 pays no blob fee, so the sender pays 0 wei more than the same call without blob fields. Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 328811cb](../../clients/anvil_development.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../clients/besu_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../clients/reth_development.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../evidence/2026-10-03/blob-charge/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/blob-charge/probes-prague/manifest.json) |

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
      "stateDiff"
    ],
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · 328811cb** (`anvil Version: 1.8.4-nightly+328811cb`)

- [H15](../../decisions/H15.md): A blob call whose maxFeePerBlobGas is omitted or 0 pays no blob fee, so the sender pays 0 wei more than the same call without blob fields. Expected a result; observed rpc_error -32003 Block `blob_gas_price` is greater than tx-specified `max_fee_per_blob_gas`

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H15](../../decisions/H15.md): A blob call whose maxFeePerBlobGas is omitted or 0 pays no blob fee, so the sender pays 0 wei more than the same call without blob fields. Expected a result; observed rpc_error -32003 Block `blob_gas_price` is greater than tx-specified `max_fee_per_blob_gas`

**Besu · 26.10-develop · 711f8142** (`besu/v26.10-develop-711f814/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): A blob call whose maxFeePerBlobGas is omitted or 0 pays no blob fee, so the sender pays 0 wei more than the same call without blob fields. Expected 0 wei beyond the reference charge 119520000000000; charged 131072, -119519999868928 against the reference.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): A blob call whose maxFeePerBlobGas is omitted or 0 pays no blob fee, so the sender pays 0 wei more than the same call without blob fields. Expected a result; observed rpc_error -32603 Internal error

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H15](../../decisions/H15.md): A blob call whose maxFeePerBlobGas is omitted or 0 pays no blob fee, so the sender pays 0 wei more than the same call without blob fields. Expected a result; observed rpc_error -32000 maxFeePerBlobGas, if specified, must be non-zero

**Reth · 2.7.0 · 078d0262** (`Reth Version: 2.7.0+078d0262`)

- [H15](../../decisions/H15.md): A blob call whose maxFeePerBlobGas is omitted or 0 pays no blob fee, so the sender pays 0 wei more than the same call without blob fields. Expected a result; observed rpc_error -32003 max fee per blob gas less than block blob gas fee

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../decisions/H15.md): A blob call whose maxFeePerBlobGas is omitted or 0 pays no blob fee, so the sender pays 0 wei more than the same call without blob fields. Expected a result; observed rpc_error -32003 max fee per blob gas less than block blob gas fee

</details>
