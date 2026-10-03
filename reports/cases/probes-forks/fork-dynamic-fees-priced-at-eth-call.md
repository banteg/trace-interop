# Fork dynamic fees priced at eth call

`eth_call` · probes-forks · [All reports](../../README.md)

**What this checks:** At London (block 36) the dynamic fees run at GASPRICE 2000000000, min(tip + base fee, cap).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../clients/besu_development.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../clients/erigon_development.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../clients/nethermind_development.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../clients/reth_development.md) | `0x0000000000000000000000000000000000000000000000000000000077359400` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "data": "0x3a60005260206000f3",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x186a0",
      "maxFeePerGas": "0x77359400",
      "maxPriorityFeePerGas": "0x3b9aca00"
    },
    "0x24"
  ]
}
```

**Besu · 26.10-develop · 711f8142** (`besu/v26.10-develop-711f814/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): At London (block 36) the dynamic fees run at GASPRICE 2000000000, min(tip + base fee, cap). eth_call parity control for fork-dynamic-fees-priced-at. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): At London (block 36) the dynamic fees run at GASPRICE 2000000000, min(tip + base fee, cap). eth_call parity control for fork-dynamic-fees-priced-at. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Erigon · 3.8.0-dev · 6da806cb** (`3.8.0-dev-6da806cb`)

- [H14](../../decisions/H14.md): At London (block 36) the dynamic fees run at GASPRICE 2000000000, min(tip + base fee, cap). eth_call parity control for fork-dynamic-fees-priced-at. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): At London (block 36) the dynamic fees run at GASPRICE 2000000000, min(tip + base fee, cap). eth_call parity control for fork-dynamic-fees-priced-at. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Geth draft fork · 1.17.7-unstable · 67f41dea** (`Geth/v1.17.7-unstable-67f41dea-2026-09-30/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): At London (block 36) the dynamic fees run at GASPRICE 2000000000, min(tip + base fee, cap). eth_call parity control for fork-dynamic-fees-priced-at. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Nethermind · 2.2.0-preview · 3370d566** (`2.2.0-preview+3370d566`)

- [H14](../../decisions/H14.md): At London (block 36) the dynamic fees run at GASPRICE 2000000000, min(tip + base fee, cap). eth_call parity control for fork-dynamic-fees-priced-at. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H14](../../decisions/H14.md): At London (block 36) the dynamic fees run at GASPRICE 2000000000, min(tip + base fee, cap). eth_call parity control for fork-dynamic-fees-priced-at. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Reth · 2.7.0 · 078d0262** (`Reth Version: 2.7.0+078d0262`)

- [H14](../../decisions/H14.md): At London (block 36) the dynamic fees run at GASPRICE 2000000000, min(tip + base fee, cap). eth_call parity control for fork-dynamic-fees-priced-at. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): At London (block 36) the dynamic fees run at GASPRICE 2000000000, min(tip + base fee, cap). eth_call parity control for fork-dynamic-fees-priced-at. Observed: Expected ['0x0000000000000000000000000000000000000000000000000000000077359400']; got ['0x0000000000000000000000000000000000000000000000000000000077359400']

</details>
