# Many write delete storage

`trace_callMany` · probes-forks · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. A deleted account reports storage {} or optional old-slot - entries; account deletion implies every slot is wiped. Before Cancun the final item deletes the account created by an earlier item. Account deletion wipes all storage; optional - entries report the item's pre-values, including slot zero written to 42 by the preceding item.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/probes-forks/manifest.json) |

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

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x0c2c51a0990aee1d73c1228de158688341557508', 'gas': '0x3c372', 'init': '0x600f80600b6000396000f336156008576000ff5b602a60005500', 'value': '0x0'}, 'result': {'address': '0x8a700907005c5c3b442322abfb6bec88772ebd11', 'code': '0x36156008576000ff5b602a60005500', 'gasUsed': '0xbd0'},

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x0c2c51a0990aee1d73c1228de158688341557508', 'gas': '0x3c372', 'init': '0x600f80600b6000396000f336156008576000ff5b602a60005500', 'value': '0x0'}, 'result': {'address': '0x8a700907005c5c3b442322abfb6bec88772ebd11', 'code': '0x36156008576000ff5b602a60005500', 'gasUsed': '0xbd0'},

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H26](../../decisions/H26.md): Before Cancun the final item deletes the account created by an earlier item. Expected {'balance': {'-': '0x0'}, 'code': {'-': '0x36156008576000ff5b602a60005500'}, 'nonce': {'-': '0x1'}}; got {'balance': {'*': {'from': '0x0', 'to': None}}, 'code': {'*': {'from': '0x36156008576000ff5b602a60005500', 'to': None}}, 'nonce': {'*': {'from': '0x1', 'to': None}}, 'storage': {}}
- Result shape at `2/stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0xc4f20ba89d2beda72', 'to': '0xc4f20e804f3642855'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0c2c51a0990aee1d73c1228de158688341557508': {'balance': {'*': {'from': '0xc097ce7bc90715b34aea0f71398400', 'to': '0xc097ce7bc90

</details>
