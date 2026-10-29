# Beacon many 55

`trace_callMany` · probes-forks · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. The first trace_callMany item at block 55 runs on the same post-block state as trace_call. The one-item trace_callMany output equals trace_call at the same block.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/probes-forks/manifest.json) |

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

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d520', 'input': '0x0000000000000000000000000000000000000000000000000000000000000230', 'to': '0x000f3df6d732807ef1319fb7b8bb8522d0beac02', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x', 'subt

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0/trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x8d520', 'input': '0x0000000000000000000000000000000000000000000000000000000000000230', 'to': '0x000f3df6d732807ef1319fb7b8bb8522d0beac02', 'value': '0x0'}, 'error': 'Reverted', 'revertReason': '0x', 'subt

</details>
