# Many number default

`trace_callMany` · h30 · [All reports](../../README.md)

**What this checks:** trace_callMany accepts an omitted block and uses latest (NUMBER 48).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_callMany",
  "params": [
    [
      [
        {
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x77359400",
          "data": "0x4360005260206000f3"
        },
        [
          "trace"
        ]
      ]
    ]
  ]
}
```

</details>
