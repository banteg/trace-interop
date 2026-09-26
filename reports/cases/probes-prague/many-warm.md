# Many warm

`trace_callMany` · probes-prague · [All reports](../../README.md)

**What this checks:** Return one execution envelope per input call, in order. Accounts and slots warmed by one item are cold again in the next: BALANCE then SLOAD cost cold, then warm.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 2 records | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/probes-prague/manifest.json) |

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
          "data": "0x61c0de31506000545060338060146000396000f35a61c0de31505a90036000525a61c0de31505a90036020525a600054505a90036040525a600054505a900360605260806000f3",
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

- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c0b6', 'init': '0x61c0de31506000545060338060146000396000f35a61c0de31505a90036000525a61c0de31505a90036020525a600054505a90036040525a600054505a900360605260806000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56a

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- Result shape at `0/trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c0b6', 'init': '0x61c0de31506000545060338060146000396000f35a61c0de31505a90036000525a61c0de31505a90036020525a600054505a90036040525a600054505a900360605260806000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56a

</details>
