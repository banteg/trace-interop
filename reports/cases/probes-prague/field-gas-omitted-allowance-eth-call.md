# Field gas omitted allowance eth call

`eth_call` · probes-prague · [All reports](../../README.md)

**What this checks:** A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | `0x000000000000000000000000000000000000000000000000000000000000b71c` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | `0x000000000000000000000000000000000000000000000000000000000000b71c` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32004` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | RPC error `-32004` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | RPC error `-32000` | 🔎 Control / not applicable | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | `0x000000000000000000000000000000000000000000000000000000000000b71c` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | `0x000000000000000000000000000000000000000000000000000000000000b71c` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/probes-prague/manifest.json) |

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

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -32004 Upfront gas cost exceeds account balance (transaction up-front gas cost 0x1b1ae4d6e2ef500000 exceeds transaction sender.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -32004 Upfront gas cost exceeds account balance (transaction up-front gas cost 0x1b1ae4d6e2ef500000 exceeds transaction sender.

**Erigon · 3.9.0-dev · d23467c5** (`3.9.0-dev-d23467c5`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -32000 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000.

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -32000 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000.

**Geth draft fork · 1.17.9-unstable · a15b96ff** (`Geth/v1.17.9-unstable-a15b96ff-2026-10-18/linux-amd64/go1.26.1`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -32000 err: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 100000000000000.

**Nethermind · 2.3.0-preview · e2e011c8** (`2.3.0-preview+e2e011c8`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -32000 err: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 100000000000000.

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -32000 err: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 100000000000000.

</details>
