# Blob fee zero statediff

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Output remains a byte string under every trace selection. A blob call whose maxFeePerBlobGas is omitted or 0 pays no blob fee, so the sender pays 0 wei more than the same call without blob fields.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-prague/manifest.json) |

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

**Reth · 2.7.0 · e6679687** (`Reth Version: 2.7.0+e6679687`)

- [H15](../../decisions/H15.md): A blob call whose maxFeePerBlobGas is omitted or 0 pays no blob fee, so the sender pays 0 wei more than the same call without blob fields. Expected a result; observed rpc_error -32003 max fee per blob gas less than block blob gas fee

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H15](../../decisions/H15.md): A blob call whose maxFeePerBlobGas is omitted or 0 pays no blob fee, so the sender pays 0 wei more than the same call without blob fields. Expected a result; observed rpc_error -32003 max fee per blob gas less than block blob gas fee

</details>
