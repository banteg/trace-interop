# Field gas omitted allowance many

`trace_callMany` · probes-prague · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. A priced omitted-gas call follows eth_call defaulting, including any smaller sender allowance or block limit. A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | RPC error `-32004` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | RPC error `-32004` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | RPC error `-38014` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-prague/manifest.json) |

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

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order. H15 owns this error, a funds validation rejection: Upfront gas cost exceeds account balance (transaction up-front gas cost 0x1b1ae4d6e2ef500000 exceeds transaction sender . There is no executed result to inspect.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -32004 Upfront gas cost exceeds account balance (transaction up-front gas cost 0x1b1ae4d6e2ef500000 exceeds transaction sender.

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order. H15 owns this error, a funds validation rejection: Upfront gas cost exceeds account balance (transaction up-front gas cost 0x1b1ae4d6e2ef500000 exceeds transaction sender . There is no executed result to inspect.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -32004 Upfront gas cost exceeds account balance (transaction up-front gas cost 0x1b1ae4d6e2ef500000 exceeds transaction sender.

**Erigon · 3.9.0-dev · 6955d198** (`3.9.0-dev-6955d198`)

- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order. H15 owns this error, a funds validation rejection: first run for txIndex 0 error: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C26590293. There is no executed result to inspect.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -38014 first run for txIndex 0 error: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C26590293.

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order. H15 owns this error, a funds validation rejection: first run for txIndex 0 error: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C26590293. There is no executed result to inspect.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -38014 first run for txIndex 0 error: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C26590293.

**Geth draft fork · 1.17.11-unstable · 0f1fb2ae** (`Geth/v1.17.11-unstable-0f1fb2ae-2026-10-28/linux-amd64/go1.26.1`)

- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order. H15 owns this error, a funds validation rejection: call 0: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 100000000000. There is no executed result to inspect.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -38014 call 0: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 100000000000.

**Nethermind · 2.3.0-preview · fc9abf09** (`2.3.0-preview+fc9abf09`)

- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order. H15 owns this error, a funds validation rejection: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000 . There is no executed result to inspect.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -38014 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H16](../../decisions/H16.md): Return one execution envelope per input call, in order. H15 owns this error, a funds validation rejection: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000 . There is no executed result to inspect.
- [H15](../../decisions/H15.md): A priced omitted-gas budget must not exceed the RPC cap, even when eth_call and trace_call agree. Rejected for funds, so there is no executed result to judge: rpc_error -38014 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000.

</details>
