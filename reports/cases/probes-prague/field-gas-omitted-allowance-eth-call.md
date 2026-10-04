# Field gas omitted allowance eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | RPC error `-32003` | 🚧 Blocked | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | RPC error `-32003` | 🚧 Blocked | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32004` | 🚧 Blocked | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | RPC error `-32004` | 🚧 Blocked | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | RPC error `-32000` | 🚧 Blocked | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | RPC error `-32000` | 🚧 Blocked | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | RPC error `-32000` | 🚧 Blocked | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | RPC error `-32000` | 🚧 Blocked | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | RPC error `-32000` | 🚧 Blocked | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `0x000000000000000000000000000000000000000000000000000000000000b71c` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | `0x000000000000000000000000000000000000000000000000000000000000b71c` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "eth_call",
  "params": [
    {
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gasPrice": "0x9184e72a000",
      "input": "0x5a60005260206000f3"
    },
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · 60255eee** (`anvil Version: 1.8.4-nightly+60255eee`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32003 Insufficient funds for gas * price + value.

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32003 Insufficient funds for gas * price + value.

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32004 Upfront gas cost exceeds account balance (transaction up-front gas cost 0x1b1ae4d6e2ef500000 exceeds transaction sender.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32004 Upfront gas cost exceeds account balance (transaction up-front gas cost 0x1b1ae4d6e2ef500000 exceeds transaction sender.

**Erigon · 3.8.0-dev · 5cb6c867** (`3.8.0-dev-5cb6c867`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32000 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32000 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000.

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32000 err: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 100000000000000.

**Nethermind · 2.2.0-preview · 6dff813b** (`2.2.0-preview+6dff813b`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32000 err: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 100000000000000.

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32000 err: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 100000000000000.

</details>
