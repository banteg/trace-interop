# Combo blob type2 dynamic

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. The blob call runs with type 2, which does not change execution, at GASPRICE 3000000000, the word its CREATE2 child deploys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | 2 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-prague/manifest.json) |

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
      "maxFeePerBlobGas": "0x1",
      "maxFeePerGas": "0xb2d05e00",
      "maxPriorityFeePerGas": "0xb2d05e00",
      "to": "0x4e59b44847b379578588920ca78fbf26c0b4956c",
      "type": "0x2"
    },
    [
      "trace",
      "stateDiff"
    ],
    "latest"
  ]
}
```

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/1`: {'action': {'from': '0x4e59b44847b379578588920ca78fbf26c0b4956c', 'gas': '0x3b49f', 'init': '0x3a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0x03aabecabc004eeaae2f254e6d52da3d3980a45e', 'code': '0x00000000000000000000000000000000000000000000000000000000b2d05e00', 'gasUsed': '0x1911'},

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/1`: {'action': {'from': '0x4e59b44847b379578588920ca78fbf26c0b4956c', 'gas': '0x3b49f', 'init': '0x3a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0x03aabecabc004eeaae2f254e6d52da3d3980a45e', 'code': '0x00000000000000000000000000000000000000000000000000000000b2d05e00', 'gasUsed': '0x1911'},

</details>
