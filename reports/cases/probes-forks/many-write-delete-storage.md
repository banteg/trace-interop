# Many write delete storage

`trace_callMany` · probes-forks · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Reward and SELFDESTRUCT records carry result null. A deleted account reports storage {} or optional old-slot - entries; account deletion implies every slot is wiped. Before Cancun the final item deletes the account created by an earlier item. Account deletion wipes all storage; optional - entries report the item's pre-values, including slot zero written to 42 by the preceding item.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.1 · e83703cd](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/probes-forks/manifest.json) |

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

**Besu · 26.10-develop · 781a7e1d** (`besu/v26.10-develop-781a7e1/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x0c2c51a0990aee1d73c1228de158688341557508', 'gas': '0x3c372', 'init': '0x600f80600b6000396000f336156008576000ff5b602a60005500', 'value': '0x0'}, 'result': {'address': '0x8a700907005c5c3b442322abfb6bec88772ebd11', 'code': '0x36156008576000ff5b602a60005500', 'gasUsed': '0xbd0'},

**Besu · 26.10.1 · e83703cd** (`besu/v26.10.1/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x0c2c51a0990aee1d73c1228de158688341557508', 'gas': '0x3c372', 'init': '0x600f80600b6000396000f336156008576000ff5b602a60005500', 'value': '0x0'}, 'result': {'address': '0x8a700907005c5c3b442322abfb6bec88772ebd11', 'code': '0x36156008576000ff5b602a60005500', 'gasUsed': '0xbd0'},

</details>
