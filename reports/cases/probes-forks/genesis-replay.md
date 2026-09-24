# Genesis replay

`trace_replayBlockTransactions` · probes-forks · [All reports](../../README.md)

**What this checks:** The genesis block has no transaction or reward records. Block replay returns [].

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/probes-forks/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/probes-forks/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayBlockTransactions",
  "params": [
    "0x0",
    [
      "trace"
    ]
  ]
}
```

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H05](../../decisions/H05.md): The genesis block has no transaction or reward records. Block replay returns []. Expected a result; observed rpc_error -32000 block not found: earliest

**Nethermind · 2.1.0-preview · 54b760cd** (`2.1.0-preview+54b760cd`)

- [H05](../../decisions/H05.md): The genesis block has no transaction or reward records. Block replay returns []. Expected a result; observed rpc_error -32000 header not found

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H05](../../decisions/H05.md): The genesis block has no transaction or reward records. Block replay returns []. Expected a result; observed rpc_error -32000 header not found

</details>
