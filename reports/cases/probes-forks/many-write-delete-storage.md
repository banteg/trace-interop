# Many write delete storage

`trace_callMany` · probes-forks · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. A deleted account reports storage {} or optional old-slot - entries; account deletion implies every slot is wiped. Before Cancun the final item deletes the account created by an earlier item. Account deletion wipes all storage; optional - entries report the item's pre-values, including slot zero written to 42 by the preceding item.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-03/fork-features/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-03/fork-features/probes-forks/manifest.json) |

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

**Besu · 26.10-develop · 711f8142** (`besu/v26.10-develop-711f814/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x0c2c51a0990aee1d73c1228de158688341557508', 'gas': '0x3c372', 'init': '0x600f80600b6000396000f336156008576000ff5b602a60005500', 'value': '0x0'}, 'result': {'address': '0x8a700907005c5c3b442322abfb6bec88772ebd11', 'code': '0x36156008576000ff5b602a60005500', 'gasUsed': '0xbd0'},

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x0c2c51a0990aee1d73c1228de158688341557508', 'gas': '0x3c372', 'init': '0x600f80600b6000396000f336156008576000ff5b602a60005500', 'value': '0x0'}, 'result': {'address': '0x8a700907005c5c3b442322abfb6bec88772ebd11', 'code': '0x36156008576000ff5b602a60005500', 'gasUsed': '0xbd0'},

</details>
