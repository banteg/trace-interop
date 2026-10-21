# Combo blob type2 dynamic eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** The blob call runs with type 2, which does not change execution, at GASPRICE 3000000000, the word its CREATE2 child deploys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | `0x03aabecabc004eeaae2f254e6d52da3d3980a45e` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | `0x03aabecabc004eeaae2f254e6d52da3d3980a45e` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | `0x03aabecabc004eeaae2f254e6d52da3d3980a45e` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | `0x03aabecabc004eeaae2f254e6d52da3d3980a45e` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | `0x03aabecabc004eeaae2f254e6d52da3d3980a45e` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | `0x03aabecabc004eeaae2f254e6d52da3d3980a45e` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | `0x03aabecabc004eeaae2f254e6d52da3d3980a45e` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | `0x03aabecabc004eeaae2f254e6d52da3d3980a45e` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | `0x03aabecabc004eeaae2f254e6d52da3d3980a45e` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | `0x03aabecabc004eeaae2f254e6d52da3d3980a45e` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | `0x03aabecabc004eeaae2f254e6d52da3d3980a45e` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
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
    "latest"
  ]
}
```

**Anvil · 1.8.6-nightly · 9089a6bf** (`anvil Version: 1.8.6-nightly+9089a6bf`)

- [H14](../../decisions/H14.md): The blob call runs with type 2, which does not change execution, at GASPRICE 3000000000, the word its CREATE2 child deploys. eth_call parity control for combo-blob-type2-dynamic. Observed: Expected [None]; got ['0x03aabecabc004eeaae2f254e6d52da3d3980a45e']

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H14](../../decisions/H14.md): The blob call runs with type 2, which does not change execution, at GASPRICE 3000000000, the word its CREATE2 child deploys. eth_call parity control for combo-blob-type2-dynamic. Observed: Expected [None]; got ['0x03aabecabc004eeaae2f254e6d52da3d3980a45e']

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The blob call runs with type 2, which does not change execution, at GASPRICE 3000000000, the word its CREATE2 child deploys. eth_call parity control for combo-blob-type2-dynamic. Observed: Expected [None]; got ['0x03aabecabc004eeaae2f254e6d52da3d3980a45e']

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The blob call runs with type 2, which does not change execution, at GASPRICE 3000000000, the word its CREATE2 child deploys. eth_call parity control for combo-blob-type2-dynamic. Observed: Expected [None]; got ['0x03aabecabc004eeaae2f254e6d52da3d3980a45e']

**Erigon · 3.9.0-dev · d23467c5** (`3.9.0-dev-d23467c5`)

- [H14](../../decisions/H14.md): The blob call runs with type 2, which does not change execution, at GASPRICE 3000000000, the word its CREATE2 child deploys. eth_call parity control for combo-blob-type2-dynamic. Observed: Expected [None]; got ['0x03aabecabc004eeaae2f254e6d52da3d3980a45e']

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H14](../../decisions/H14.md): The blob call runs with type 2, which does not change execution, at GASPRICE 3000000000, the word its CREATE2 child deploys. eth_call parity control for combo-blob-type2-dynamic. Observed: Expected [None]; got ['0x03aabecabc004eeaae2f254e6d52da3d3980a45e']

**Geth draft fork · 1.17.9-unstable · a15b96ff** (`Geth/v1.17.9-unstable-a15b96ff-2026-10-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The blob call runs with type 2, which does not change execution, at GASPRICE 3000000000, the word its CREATE2 child deploys. eth_call parity control for combo-blob-type2-dynamic. Observed: Expected [None]; got ['0x03aabecabc004eeaae2f254e6d52da3d3980a45e']

**Nethermind · 2.3.0-preview · e2e011c8** (`2.3.0-preview+e2e011c8`)

- [H14](../../decisions/H14.md): The blob call runs with type 2, which does not change execution, at GASPRICE 3000000000, the word its CREATE2 child deploys. eth_call parity control for combo-blob-type2-dynamic. Observed: Expected [None]; got ['0x03aabecabc004eeaae2f254e6d52da3d3980a45e']

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H14](../../decisions/H14.md): The blob call runs with type 2, which does not change execution, at GASPRICE 3000000000, the word its CREATE2 child deploys. eth_call parity control for combo-blob-type2-dynamic. Observed: Expected [None]; got ['0x03aabecabc004eeaae2f254e6d52da3d3980a45e']

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H14](../../decisions/H14.md): The blob call runs with type 2, which does not change execution, at GASPRICE 3000000000, the word its CREATE2 child deploys. eth_call parity control for combo-blob-type2-dynamic. Observed: Expected [None]; got ['0x03aabecabc004eeaae2f254e6d52da3d3980a45e']

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H14](../../decisions/H14.md): The blob call runs with type 2, which does not change execution, at GASPRICE 3000000000, the word its CREATE2 child deploys. eth_call parity control for combo-blob-type2-dynamic. Observed: Expected [None]; got ['0x03aabecabc004eeaae2f254e6d52da3d3980a45e']

</details>
