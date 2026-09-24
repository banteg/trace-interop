# Many selfdestruct diff

`trace_callMany` · probes-prague · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. SELFDESTRUCT of a contract created by an earlier item keeps the account: balance changes, code and nonce are unchanged, no deletion markers.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-prague/manifest.json) |

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
          "data": "0x600480600b6000396000f361beefff",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x493e0",
          "gasPrice": "0x77359400",
          "value": "0x5"
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
          "trace",
          "stateDiff"
        ]
      ],
      [
        {
          "data": "0x72de48310d77a4d56aa400248b0b1613508f5b733b60005261beef3160205260406000f3",
          "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
          "gas": "0x493e0",
          "gasPrice": "0x77359400"
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

**Besu · 26.9-develop · cf89071f** (`besu/v26.9-develop-cf89071/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c3fe', 'init': '0x600480600b6000396000f361beefff', 'value': '0x5'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x61beefff', 'gasUsed': '0x338'}, 'subtraces': 0, 'traceAddress': [], 'type':
- Result shape at `2/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2b8', 'init': '0x72de48310d77a4d56aa400248b0b1613508f5b733b60005261beef3160205260406000f3', 'value': '0x0'}, 'result': {'address': '0xd30c8839c1145609e564b986f667b273ddcb8496', 'code': '0x0000000000000000000000000000000000

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c3fe', 'init': '0x600480600b6000396000f361beefff', 'value': '0x5'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x61beefff', 'gasUsed': '0x338'}, 'subtraces': 0, 'traceAddress': [], 'type':
- Result shape at `2/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c2b8', 'init': '0x72de48310d77a4d56aa400248b0b1613508f5b733b60005261beef3160205260406000f3', 'value': '0x0'}, 'result': {'address': '0xd30c8839c1145609e564b986f667b273ddcb8496', 'code': '0x0000000000000000000000000000000000

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H26](../../decisions/H26.md): SELFDESTRUCT of a contract created by an earlier item keeps the account: balance changes, code and nonce are unchanged, no deletion markers. Expected {'balance': {'*': {'from': '0x5', 'to': '0x0'}}, 'code': '=', 'nonce': '='}; got {'0x0000000000000000000000000000000000000000': {'balance': {'+': '0x17936826bac0'}, 'code': {'+': '0x'}, 'nonce': {'+': '0x0'}, 'storage': {}}, '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf': {'balance': '=', 'code': '=', 'nonce': {'*': {'from': '0xa', 'to': '0xb'}}, 'storage': {}}}

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- Result shape at `1/stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x3cabb03b4af0', 'to': '0x78d93543d7f8'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x000000000000000000000000000000000000beef': {'balance': {'+': '0x5'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x00de48310d77

</details>
