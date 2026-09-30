# Field gas omitted allowance many

`trace_callMany` · probes-prague · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Return one complete JSON-RPC response; never wrap an error envelope as a successful result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32003` | 🚧 Blocked | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | RPC error `-32003` | 🚧 Blocked | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | Error envelope nested inside result | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | Error envelope nested inside result | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | RPC error `-38014` | 🚧 Blocked | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | RPC error `-38014` | 🚧 Blocked | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | RPC error `-32000` | 🚧 Blocked | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_callMany",
  "params": [
    [
      [
        {
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gasPrice": "0x9184e72a000",
          "input": "0x5a60005260206000f3"
        },
        [
          "trace"
        ]
      ]
    ],
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · e3429853** (`anvil Version: 1.8.4-nightly+e3429853`)

- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order. H15 owns this error, a funds validation rejection: Insufficient funds for gas * price + value. There is no executed result to inspect.
- [H15](../../decisions/H15.md): A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32003 Insufficient funds for gas * price + value.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32003 Insufficient funds for gas * price + value.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order. H15 owns this error, a funds validation rejection: Insufficient funds for gas * price + value. There is no executed result to inspect.
- [H15](../../decisions/H15.md): A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32003 Insufficient funds for gas * price + value.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32003 Insufficient funds for gas * price + value.

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order. H25 owns this error, an error envelope returned as a successful result. There is no executed result to inspect.
- [H15](../../decisions/H15.md): A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed result -32603 Internal error.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed result -32603 Internal error.
- Result shape at `/`: {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'} is not of type 'array'

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order. H25 owns this error, an error envelope returned as a successful result. There is no executed result to inspect.
- [H15](../../decisions/H15.md): A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed result -32603 Internal error.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed result -32603 Internal error.
- Result shape at `/`: {'error': {'code': -32603, 'message': 'Internal error'}, 'id': 1, 'jsonrpc': '2.0'} is not of type 'array'

**Erigon · 3.8.0-dev · 923b4d31** (`3.8.0-dev-923b4d31`)

- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order. H15 owns this error, a funds validation rejection: first run for txIndex 0 error: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C26590293. There is no executed result to inspect.
- [H15](../../decisions/H15.md): A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -38014 first run for txIndex 0 error: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C26590293.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -38014 first run for txIndex 0 error: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C26590293.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H15](../../decisions/H15.md): A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. The reference field-gas-omitted-allowance-eth-call returned no successful output.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Cap GAS word 0x0000000000000000000000000000000000000000000000000000000002fa20fc; got 0x

**Geth draft fork · 1.17.7-unstable · ec1cec0b** (`Geth/v1.17.7-unstable-ec1cec0b-2026-09-30/linux-amd64/go1.26.1`)

- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order. H15 owns this error, a funds validation rejection: call 0: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 100000000000. There is no executed result to inspect.
- [H15](../../decisions/H15.md): A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -38014 call 0: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 100000000000.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -38014 call 0: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 100000000000.

**Nethermind · 2.2.0-preview · 79173d14** (`2.2.0-preview+79173d14`)

- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order. H15 owns this error, a funds validation rejection: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000 . There is no executed result to inspect.
- [H15](../../decisions/H15.md): A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32000 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Depends on H15: The client may reject its default gas budget for insufficient funds; gas defaulting requires a successful eth_call control. Observed rpc_error -32000 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.

</details>
