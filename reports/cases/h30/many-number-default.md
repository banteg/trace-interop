# Many number default

`trace_callMany` · h30 · [All reports](../../README.md)

**What this checks:** trace_callMany accepts an omitted block and uses latest (NUMBER 48).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h17-retest/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/h30/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h17-retest/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/h30/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/h30/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/h30/manifest.json) |
| [Nethermind · 2.1.0-unstable · 9d6e8b8d](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/h30/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h17-retest/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/h30/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h17-retest/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/h30/manifest.json) |

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
          "data": "0x4360005260206000f3",
          "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
          "gas": "0x927c0",
          "gasPrice": "0x77359400"
        },
        [
          "trace"
        ]
      ]
    ]
  ]
}
```

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H31](../../decisions/H31.md): trace_callMany accepts an omitted block and uses latest (NUMBER 48).

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H31](../../decisions/H31.md): trace_callMany accepts an omitted block and uses latest (NUMBER 48).

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H31](../../decisions/H31.md): trace_callMany accepts an omitted block and uses latest (NUMBER 48).

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H31](../../decisions/H31.md): trace_callMany accepts an omitted block and uses latest (NUMBER 48).

</details>
