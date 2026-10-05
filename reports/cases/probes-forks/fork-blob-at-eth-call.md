# Fork blob at eth call

`eth_call` · probes-forks · [All reports](../../README.md)

**What this checks:** The blob fields run at block 56, at Cancun (block 56).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-05/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/probes-forks/manifest.json) |

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
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x186a0",
      "maxFeePerGas": "0x0",
      "maxPriorityFeePerGas": "0x0",
      "to": "0x00000000000000000000000000000000000000ee"
    },
    "0x38"
  ]
}
```

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The blob fields run at block 56, at Cancun (block 56). eth_call parity control for fork-blob-at. Observed: Expected ['0x']; got ['0x']

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): The blob fields run at block 56, at Cancun (block 56). eth_call parity control for fork-blob-at. Observed: Expected ['0x']; got ['0x']

**Erigon · 3.8.0-dev · 96188a47** (`3.8.0-dev-96188a47`)

- [H14](../../decisions/H14.md): The blob fields run at block 56, at Cancun (block 56). eth_call parity control for fork-blob-at. Observed: Expected ['0x']; got ['0x']

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): The blob fields run at block 56, at Cancun (block 56). eth_call parity control for fork-blob-at. Observed: Expected ['0x']; got ['0x']

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): The blob fields run at block 56, at Cancun (block 56). eth_call parity control for fork-blob-at. Observed: Expected ['0x']; got ['0x']

**Nethermind · 2.2.0-preview · e8955c4c** (`2.2.0-preview+e8955c4c`)

- [H14](../../decisions/H14.md): The blob fields run at block 56, at Cancun (block 56). eth_call parity control for fork-blob-at. Observed: Expected ['0x']; got ['0x']

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H14](../../decisions/H14.md): The blob fields run at block 56, at Cancun (block 56). eth_call parity control for fork-blob-at. Observed: Expected ['0x']; got ['0x']

**Reth · 2.7.0 · 42fa3c56** (`Reth Version: 2.7.0+42fa3c56`)

- [H14](../../decisions/H14.md): The blob fields run at block 56, at Cancun (block 56). eth_call parity control for fork-blob-at. Observed: Expected ['0x']; got ['0x']

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): The blob fields run at block 56, at Cancun (block 56). eth_call parity control for fork-blob-at. Observed: Expected ['0x']; got ['0x']

</details>
