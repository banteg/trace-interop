# Missing block call

`trace_call` · a · [All reports](../../README.md)

**What this checks:** An unknown single selected block returns Resource not found (-32001).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../clients/besu_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../clients/go-ethereum_trace.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../clients/nethermind_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/a/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000001002",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "data": "0x"
    },
    [
      "trace"
    ],
    "0xffff"
  ]
}
```

**Besu · 26.9-develop · 85b32978** (`besu/v26.9-develop-85b3297/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): An unknown single selected block returns Resource not found (-32001).

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): An unknown single selected block returns Resource not found (-32001).

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H06](../../decisions/H06.md): An unknown single selected block returns Resource not found (-32001).

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H06](../../decisions/H06.md): An unknown single selected block returns Resource not found (-32001).

**Nethermind · 2.1.0-preview · ce501a97** (`2.1.0-preview+ce501a97`)

- [H06](../../decisions/H06.md): An unknown single selected block returns Resource not found (-32001).

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H06](../../decisions/H06.md): An unknown single selected block returns Resource not found (-32001).

</details>
