# Missing block call

`trace_call` · a · [All reports](../../README.md)

**What this checks:** An unknown selected block returns an error with code -32001, never null or a result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/a/manifest.json) |

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

**Anvil · 1.8.7-nightly · 716e795c** (`anvil Version: 1.8.7-nightly+716e795c`)

- [H06](../../decisions/H06.md): An unknown selected block returns an error with code -32001, never null or a result. Code -32602.

**Anvil · 1.8.6 · 6bad0a66** (`anvil Version: 1.8.6+6bad0a66`)

- [H06](../../decisions/H06.md): An unknown selected block returns an error with code -32001, never null or a result. Code -32602.

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): An unknown selected block returns an error with code -32001, never null or a result. Code -32000.

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H06](../../decisions/H06.md): An unknown selected block returns an error with code -32001, never null or a result. Code -32000.

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H06](../../decisions/H06.md): An unknown selected block returns an error with code -32001, never null or a result. Code -32000.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H06](../../decisions/H06.md): An unknown selected block returns an error with code -32001, never null or a result. Code -32000.

</details>
