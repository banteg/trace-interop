# Fork type1 before eth call

`eth_call` · probes-forks · [All reports](../../README.md)

**What this checks:** An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | RPC error `-32603` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | RPC error `-32603` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-04/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-forks/manifest.json) |

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
      "type": "0x1"
    },
    "0x1f"
  ]
}
```

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected ['0x']; got ['0x']

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected ['0x']; got ['0x']

**Erigon · 3.8.0-dev · 5cb6c867** (`3.8.0-dev-5cb6c867`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected ['0x']; got ['0x']

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected ['0x']; got ['0x']

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected ['0x']; got ['0x']

**Nethermind · 2.2.0-preview · 6dff813b** (`2.2.0-preview+6dff813b`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected a result; observed rpc_error -32603 Internal error

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected a result; observed rpc_error -32603 Internal error

**Reth · 2.7.0 · 10bcf461** (`Reth Version: 2.7.0+10bcf461`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected ['0x']; got ['0x']

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected ['0x']; got ['0x']

</details>
