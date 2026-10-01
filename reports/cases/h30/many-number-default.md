# Many number default

`trace_callMany` · h30 · [All reports](../../README.md)

**What this checks:** trace_callMany accepts an omitted block and uses latest (NUMBER 48).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../clients/anvil_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/h30/manifest.json) |

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

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H31](../../decisions/H31.md): trace_callMany accepts an omitted block and uses latest (NUMBER 48).

**Besu · 26.10-develop · 28edf391** (`besu/v26.10-develop-28edf39/linux-x86_64/openjdk-java-25`)

- [H31](../../decisions/H31.md): trace_callMany accepts an omitted block and uses latest (NUMBER 48).

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H31](../../decisions/H31.md): trace_callMany accepts an omitted block and uses latest (NUMBER 48).

</details>
