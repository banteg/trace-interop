# Fork type1 before eth call

`eth_call` · probes-forks · [All reports](../../README.md)

**What this checks:** An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.1 · e83703cd](../../clients/besu_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../clients/besu_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../clients/erigon_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../clients/nethermind_release.md) | RPC error `-32603` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../clients/nethermind_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../clients/reth_release.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../clients/reth_development.md) | `0x` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |

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

**Besu · 26.10-develop · 781a7e1d** (`besu/v26.10-develop-781a7e1/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected ['0x']; got ['0x']

**Besu · 26.10.1 · e83703cd** (`besu/v26.10.1/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected ['0x']; got ['0x']

**Erigon · 3.9.0-dev · 598ba625** (`3.9.0-dev-598ba625`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected ['0x']; got ['0x']

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected ['0x']; got ['0x']

**Geth draft fork · 1.17.9-unstable · a15b96ff** (`Geth/v1.17.9-unstable-a15b96ff-2026-10-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected ['0x']; got ['0x']

**Nethermind · 2.3.0-preview · 7192e7f3** (`2.3.0-preview+7192e7f3`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected ['0x']; got ['0x']

**Nethermind · 2.2.1 · c4f1015b** (`2.2.1+c4f1015b`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected a result; observed rpc_error -32603 Internal error

**Reth · 2.8.0 · 53bf066f** (`Reth Version: 2.8.0+53bf066f`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected ['0x']; got ['0x']

**Reth · 2.8.1 · d763342f** (`Reth Version: 2.8.1+d763342f`)

- [H14](../../decisions/H14.md): An explicit type 1 with no access-list fields runs at block 31, before Berlin (block 32): type is not a feature. eth_call parity control for fork-type1-before. Observed: Expected ['0x']; got ['0x']

</details>
