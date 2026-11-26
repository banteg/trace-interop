# Combo blob gasprice capped

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Output remains a byte string under every trace selection. Every creation names its creationMethod; a successful one uses address, code and gasUsed. The blob call runs at GASPRICE 2000000000, the word its CREATE2 child deploys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-11-26/return-ex/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-26/return-ex/probes-prague/manifest.json) |

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
      "data": "0x00000000000000000000000000000000000000000000000000000000000000003a60005260206000f3",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x493e0",
      "gasPrice": "0x77359400",
      "maxFeePerBlobGas": "0x1",
      "to": "0x4e59b44847b379578588920ca78fbf26c0b4956c"
    },
    [
      "trace",
      "stateDiff"
    ],
    "latest"
  ]
}
```

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H14](../../decisions/H14.md): The blob call runs at GASPRICE 2000000000, the word its CREATE2 child deploys. Expected a result; observed rpc_error -32602 both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H14](../../decisions/H14.md): The blob call runs at GASPRICE 2000000000, the word its CREATE2 child deploys. Expected a result; observed rpc_error -32602 both gasPrice and (maxFeePerGas or maxPriorityFeePerGas) specified

</details>
