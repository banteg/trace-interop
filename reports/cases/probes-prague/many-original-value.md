# Many original value

`trace_callMany` · probes-prague · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Each item snapshots original storage: a slot committed by the previous item is clean and cold (5000 gas), not dirty.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Nethermind · 2.1.0-preview · b4211ad9](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/eval/probes-prague/manifest.json) |

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
          "data": "0x600160005560118060106000396000f35a60026000555a900360005260206000f3",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x493e0",
          "gasPrice": "0x77359400"
        },
        [
          "trace"
        ]
      ],
      [
        {
          "data": "0x",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x493e0",
          "gasPrice": "0x77359400",
          "to": "0x00de48310d77a4d56aa400248b0b1613508f5b73"
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

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H16](../../decisions/H16.md): Each item snapshots original storage: a slot committed by the previous item is clean and cold (5000 gas), not dirty. Expected ['0x5a60026000555a900360005260206000f3', '0x0000000000000000000000000000000000000000000000000000000000001390']; got ['0x5a60026000555a900360005260206000f3', '0x00000000000000000000000000000000000000000000000000000000000008a0']
- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c30c', 'init': '0x600160005560118060106000396000f35a60026000555a900360005260206000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x5a60026000555a900360005260206000f3', 'ga

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H16](../../decisions/H16.md): Each item snapshots original storage: a slot committed by the previous item is clean and cold (5000 gas), not dirty. Expected ['0x5a60026000555a900360005260206000f3', '0x0000000000000000000000000000000000000000000000000000000000001390']; got ['0x5a60026000555a900360005260206000f3', '0x00000000000000000000000000000000000000000000000000000000000008a0']
- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c30c', 'init': '0x600160005560118060106000396000f35a60026000555a900360005260206000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x5a60026000555a900360005260206000f3', 'ga

</details>
