# Filter null members

`trace_filter` · probes-forks · [All reports](../../README.md)

**What this checks:** Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 16 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 16 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 16 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 16 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 16 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "after": null,
      "count": null,
      "fromAddress": null,
      "fromBlock": "0x2",
      "mode": null,
      "toAddress": null,
      "toBlock": "0x5"
    }
  ]
}
```

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid filter params

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid filter params

**Erigon · 3.9.0-dev · 1ee57924** (`3.9.0-dev-1ee57924`)

- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: 'transactionHash' is a required property
- Result shape at `6`: 'transactionPosition' is a required property
- Result shape at `7`: 'transactionHash' is a required property
- Result shape at `7`: 'transactionPosition' is a required property

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress []: error None, result null.
- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- Result shape at `3`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0x395e712438dd92dc5d88276418e20a940d2ce71bd6a5c28cc62dab41acdd6436', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under any
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x49b9ca9a69434000'}, 'blockHash': '0x2cd37cf31e57ceb56e7d009ffda233a84acf52ae9a630ee91600b0f17099d092', 'blockNumber': 3, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under any
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'uncle', 'value': '0x3cb71f51fc558000'}, 'blockHash': '0x2cd37cf31e57ceb56e7d009ffda233a84acf52ae9a630ee91600b0f17099d092', 'blockNumber': 3, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under any
- Result shape at `6`: 'transactionHash' is a required property

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress []: error None, result null.
- [H05](../../decisions/H05.md): Reward records carry null transactionHash and transactionPosition. First at traceAddress []: error None, result null.
- Result shape at `3`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x4563918244f40000'}, 'blockHash': '0x395e712438dd92dc5d88276418e20a940d2ce71bd6a5c28cc62dab41acdd6436', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under any
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property
- Result shape at `5`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'block', 'value': '0x49b9ca9a69434000'}, 'blockHash': '0x2cd37cf31e57ceb56e7d009ffda233a84acf52ae9a630ee91600b0f17099d092', 'blockNumber': 3, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under any
- Result shape at `5`: 'transactionHash' is a required property
- Result shape at `5`: 'transactionPosition' is a required property
- Result shape at `6`: {'action': {'author': '0x0000000000000000000000000000000000000000', 'rewardType': 'uncle', 'value': '0x3cb71f51fc558000'}, 'blockHash': '0x2cd37cf31e57ceb56e7d009ffda233a84acf52ae9a630ee91600b0f17099d092', 'blockNumber': 3, 'subtraces': 0, 'traceAddress': [], 'type': 'reward'} is not valid under any
- Result shape at `6`: 'transactionHash' is a required property

**Reth · 2.7.0 · e6679687** (`Reth Version: 2.7.0+e6679687`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid params

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): Null mode, after, count and address lists are omitted, so blocks 2-5 return every record. Expected a result; observed rpc_error -32602 Invalid params

</details>
