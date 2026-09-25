# Beacon many 55

`trace_callMany` · probes-forks · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. The first trace_callMany item at block 55 runs on the same post-block state as trace_call. The one-item trace_callMany output equals trace_call at the same block.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/probes-forks/manifest.json) |

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
          "data": "0x0000000000000000000000000000000000000000000000000000000000000230",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x77359400",
          "to": "0x000F3df6D732807Ef1319fB7B8bB8522d0Beac02"
        },
        [
          "trace"
        ]
      ]
    ],
    "0x37"
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d520', 'input': '0x0000000000000000000000000000000000000000000000000000000000000230', 'to': '0x000f3df6d732807ef1319fb7b8bb8522d0beac02', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x', 'subt

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d520', 'input': '0x0000000000000000000000000000000000000000000000000000000000000230', 'to': '0x000f3df6d732807ef1319fb7b8bb8522d0beac02', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x', 'subt

**Erigon · 3.8.0-dev · f8cfe5a7** (`3.8.0-dev-f8cfe5a7`)

- [H28](../../decisions/H28.md): The first trace_callMany item at block 55 runs on the same post-block state as trace_call. Expected ['0x']; got ['0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd']
- [H28](../../decisions/H28.md): The one-item trace_callMany output equals trace_call at the same block. Reference 0x; got 0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H28](../../decisions/H28.md): The first trace_callMany item at block 55 runs on the same post-block state as trace_call. Expected ['0x']; got ['0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd']
- [H28](../../decisions/H28.md): The one-item trace_callMany output equals trace_call at the same block. Reference 0x; got 0x83472eda6eb475906aeeb7f09e757ba9f6663b9f6a5bf8611d6306f677f67ebd

**Nethermind · 2.1.0-preview · ee1f57da** (`2.1.0-preview+ee1f57da`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d520', 'input': '0x0000000000000000000000000000000000000000000000000000000000000230', 'to': '0x000f3df6d732807ef1319fb7b8bb8522d0beac02', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddre

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d520', 'input': '0x0000000000000000000000000000000000000000000000000000000000000230', 'to': '0x000f3df6d732807ef1319fb7b8bb8522d0beac02', 'value': '0x0'}, 'error': 'Reverted', 'subtraces': 0, 'traceAddre

</details>
