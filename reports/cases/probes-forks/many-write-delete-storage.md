# Many write delete storage

`trace_callMany` · probes-forks · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Reward and SELFDESTRUCT records carry result null. A deleted account reports storage {} or optional old-slot - entries; account deletion implies every slot is wiped. Before Cancun the final item deletes the account created by an earlier item. Account deletion wipes all storage; optional - entries report the item's pre-values, including slot zero written to 42 by the preceding item.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/probes-forks/manifest.json) |

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
          "data": "0x600f80600b6000396000f336156008576000ff5b602a60005500",
          "from": "0x0c2c51a0990aee1d73c1228de158688341557508",
          "gas": "0x493e0",
          "gasPrice": "0x77359400"
        },
        [
          "trace",
          "stateDiff"
        ]
      ],
      [
        {
          "data": "0x",
          "from": "0x0c2c51a0990aee1d73c1228de158688341557508",
          "gas": "0x493e0",
          "gasPrice": "0x77359400",
          "to": "0x8a700907005c5c3b442322abfb6bec88772ebd11"
        },
        [
          "trace",
          "stateDiff"
        ]
      ],
      [
        {
          "data": "0x01",
          "from": "0x0c2c51a0990aee1d73c1228de158688341557508",
          "gas": "0x493e0",
          "gasPrice": "0x77359400",
          "to": "0x8a700907005c5c3b442322abfb6bec88772ebd11"
        },
        [
          "trace",
          "stateDiff"
        ]
      ]
    ],
    "0x37"
  ]
}
```

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x0c2c51a0990aee1d73c1228de158688341557508', 'gas': '0x3c372', 'init': '0x600f80600b6000396000f336156008576000ff5b602a60005500', 'value': '0x0'}, 'result': {'address': '0x8a700907005c5c3b442322abfb6bec88772ebd11', 'code': '0x36156008576000ff5b602a60005500', 'gasUsed': '0xbd0'},

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x0c2c51a0990aee1d73c1228de158688341557508', 'gas': '0x3c372', 'init': '0x600f80600b6000396000f336156008576000ff5b602a60005500', 'value': '0x0'}, 'result': {'address': '0x8a700907005c5c3b442322abfb6bec88772ebd11', 'code': '0x36156008576000ff5b602a60005500', 'gasUsed': '0xbd0'},

</details>
