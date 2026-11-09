# Field gas omitted allowance eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | `0x000000000000000000000000000000000000000000000000000000000000b71c` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | `0x000000000000000000000000000000000000000000000000000000000000b71c` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | RPC error `-32004` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | RPC error `-32004` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | `0x000000000000000000000000000000000000000000000000000000000000b71c` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | `0x000000000000000000000000000000000000000000000000000000000000b71c` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-prague/manifest.json) |

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

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -32004 Upfront gas cost exceeds account balance (transaction up-front gas cost 0x1b1ae4d6e2ef500000 exceeds transaction sender.

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -32004 Upfront gas cost exceeds account balance (transaction up-front gas cost 0x1b1ae4d6e2ef500000 exceeds transaction sender.

**Erigon · 3.9.0-dev · cf91acee** (`3.9.0-dev-cf91acee`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -32000 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000.

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -32000 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000.

**Geth draft fork · 1.17.11-unstable · e487da1e** (`Geth/v1.17.11-unstable-e487da1e-2026-11-01/linux-amd64/go1.26.1`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -32000 err: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 100000000000000.

**Nethermind · 2.3.0-preview · 4079edfa** (`2.3.0-preview+4079edfa`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -32000 err: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 100000000000000.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -32000 err: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 100000000000000.

</details>
