# Blob fee priced

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. A maxFeePerBlobGas that covers the blob base fee keeps the selected block's BLOBBASEFEE. The factory's CREATE2 child deploys the word it read.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/gas-zero/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/gas-zero/probes-prague/manifest.json) |

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
      "maxFeePerBlobGas": "0x1",
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

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/1`: {'action': {'from': '0x4e59b44847b379578588920ca78fbf26c0b4956c', 'gas': '0x3b49f', 'init': '0x4a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xab5f25204fcd3dd3bdd4739b52bdeb75e30ed223', 'code': '0x0000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0x1911'},

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/1`: {'action': {'from': '0x4e59b44847b379578588920ca78fbf26c0b4956c', 'gas': '0x3b49f', 'init': '0x4a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0xab5f25204fcd3dd3bdd4739b52bdeb75e30ed223', 'code': '0x0000000000000000000000000000000000000000000000000000000000000001', 'gasUsed': '0x1911'},

</details>
