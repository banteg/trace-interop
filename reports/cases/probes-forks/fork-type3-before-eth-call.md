# Fork type3 before eth call

`eth_call` · probes-forks · [All reports](../../README.md)

**What this checks:** An explicit type 3 with no blob fields runs at block 55, before Cancun (block 56): type is not a feature.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../clients/besu_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../clients/erigon_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../clients/go-ethereum_trace.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../clients/nethermind_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../clients/reth_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-17/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x186a0",
      "to": "0x00000000000000000000000000000000000000ee",
      "type": "0x3"
    },
    "0x37"
  ]
}
```

**Besu · 26.10-develop · 0776d82f** (`besu/v26.10-develop-0776d82/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): An explicit type 3 with no blob fields runs at block 55, before Cancun (block 56): type is not a feature. eth_call parity control for fork-type3-before. Observed: Expected ['0x']; got ['0x']

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): An explicit type 3 with no blob fields runs at block 55, before Cancun (block 56): type is not a feature. eth_call parity control for fork-type3-before. Observed: Expected ['0x']; got ['0x']

**Erigon · 3.8.0-dev · 5b452f41** (`3.8.0-dev-5b452f41`)

- [H14](../../decisions/H14.md): An explicit type 3 with no blob fields runs at block 55, before Cancun (block 56): type is not a feature. eth_call parity control for fork-type3-before. Observed: Expected ['0x']; got ['0x']

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): An explicit type 3 with no blob fields runs at block 55, before Cancun (block 56): type is not a feature. eth_call parity control for fork-type3-before. Observed: Expected ['0x']; got ['0x']

**Geth draft fork · 1.17.7-unstable · 71db3b03** (`Geth/v1.17.7-unstable-71db3b03-2026-10-14/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): An explicit type 3 with no blob fields runs at block 55, before Cancun (block 56): type is not a feature. eth_call parity control for fork-type3-before. Observed: Expected ['0x']; got ['0x']

**Nethermind · 2.2.0-preview · cd336c4c** (`2.2.0-preview+cd336c4c`)

- [H14](../../decisions/H14.md): An explicit type 3 with no blob fields runs at block 55, before Cancun (block 56): type is not a feature. eth_call parity control for fork-type3-before. Observed: Expected ['0x']; got ['0x']

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H14](../../decisions/H14.md): An explicit type 3 with no blob fields runs at block 55, before Cancun (block 56): type is not a feature. eth_call parity control for fork-type3-before. Observed: Expected a result; observed rpc_error -32000 need at least 1 blob for a blob transaction

**Reth · 2.7.0 · ec3e7e42** (`Reth Version: 2.7.0+ec3e7e42`)

- [H14](../../decisions/H14.md): An explicit type 3 with no blob fields runs at block 55, before Cancun (block 56): type is not a feature. eth_call parity control for fork-type3-before. Observed: Expected ['0x']; got ['0x']

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): An explicit type 3 with no blob fields runs at block 55, before Cancun (block 56): type is not a feature. eth_call parity control for fork-type3-before. Observed: Expected ['0x']; got ['0x']

</details>
