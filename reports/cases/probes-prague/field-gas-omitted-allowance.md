# Field gas omitted allowance

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed. Return one complete JSON-RPC response; never wrap an error envelope as a successful result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32003` | 🚧 Blocked | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../clients/anvil_development.md) | RPC error `-32003` | 🚧 Blocked | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | RPC error `-32603` | 🚧 Blocked | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | RPC error `-38014` | 🚧 Blocked | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | RPC error `-38014` | 🚧 Blocked | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | RPC error `-32000` | 🚧 Blocked | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gasPrice": "0x9184e72a000",
      "input": "0x5a60005260206000f3"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · df92604b** (`anvil Version: 1.8.4-nightly+df92604b`)

- [H15](../../decisions/H15.md): A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32003 Insufficient funds for gas * price + value.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32003 Insufficient funds for gas * price + value.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H15](../../decisions/H15.md): A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32003 Insufficient funds for gas * price + value.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32003 Insufficient funds for gas * price + value.

**Besu · 26.10-develop · 28edf391** (`besu/v26.10-develop-28edf39/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32603 Internal error.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32603 Internal error.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H15](../../decisions/H15.md): A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32603 Internal error.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32603 Internal error.

**Erigon · 3.8.0-dev · 50e2cc4f** (`3.8.0-dev-50e2cc4f`)

- [H15](../../decisions/H15.md): A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -38014 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -38014 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../decisions/H15.md): A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. The reference field-gas-omitted-allowance-eth-call returned no successful output.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Cap GAS word 0x0000000000000000000000000000000000000000000000000000000002fa20fc; got 0x

**Geth draft fork · 1.17.7-unstable · 67f41dea** (`Geth/v1.17.7-unstable-67f41dea-2026-09-30/linux-amd64/go1.26.1`)

- [H15](../../decisions/H15.md): A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -38014 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -38014 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000.

**Nethermind · 2.2.0-preview · 759efed7** (`2.2.0-preview+759efed7`)

- [H15](../../decisions/H15.md): A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32000 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32000 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.

</details>
