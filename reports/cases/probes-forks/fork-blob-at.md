# Fork blob at

`trace_call` · probes-forks · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. The blob fields run at block 56, at Cancun (block 56).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "blobVersionedHashes": [
        "0x015a4cab4911426699ed34483de6640cf55a568afc5c5edffdcbd8bcd4452f68"
      ],
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x186a0",
      "maxFeePerGas": "0x0",
      "maxPriorityFeePerGas": "0x0",
      "to": "0x00000000000000000000000000000000000000ee"
    },
    [
      "trace"
    ],
    "0x38"
  ]
}
```

</details>
