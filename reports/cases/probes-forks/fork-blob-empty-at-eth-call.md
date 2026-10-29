# Fork blob empty at eth call

`eth_call` · probes-forks · [All reports](../../README.md)

**What this checks:** An empty blobVersionedHashes list at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | RPC error `-32602` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | RPC error `-32003` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "blobVersionedHashes": [],
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

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-empty-at. Observed: Observed rpc_error -32602: Invalid blob count (blob transactions must have at least one blob) (-32003 recommended)

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-empty-at. Observed: Observed rpc_error -32602: Invalid blob count (blob transactions must have at least one blob) (-32003 recommended)

**Erigon · 3.9.0-dev · 6955d198** (`3.9.0-dev-6955d198`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-empty-at. Observed: Observed rpc_error -32000: blob txn must contain at least one blob versioned hash (-32003 recommended)

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-empty-at. Observed: Observed rpc_error -32000: blob txn must contain at least one blob versioned hash (-32003 recommended)

**Geth draft fork · 1.17.11-unstable · 0f1fb2ae** (`Geth/v1.17.11-unstable-0f1fb2ae-2026-10-28/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-empty-at. Observed: Observed rpc_error -32000: err: blob transaction missing blob hashes (supplied gas 100000) (-32003 recommended)

**Nethermind · 2.3.0-preview · fc9abf09** (`2.3.0-preview+fc9abf09`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-empty-at. Observed: Observed rpc_error -32000: need at least 1 blob for a blob transaction (-32003 recommended)

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-empty-at. Observed: Observed rpc_error -32000: need at least 1 blob for a blob transaction (-32003 recommended)

**Reth · 2.8.1 · 966010c9** (`Reth Version: 2.8.1+966010c9`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-empty-at. Observed: Observed rpc_error -32003: blob transaction missing blob hashes

**Reth · 2.9.0 · c9a780f4** (`Reth Version: 2.9.0+c9a780f4`)

- [H14](../../decisions/H14.md): An empty blobVersionedHashes list at block 56, at Cancun (block 56) describes no transaction, so the call is rejected (-32003 recommended), never run with the field ignored. eth_call parity control for fork-blob-empty-at. Observed: Observed rpc_error -32003: blob transaction missing blob hashes

</details>
