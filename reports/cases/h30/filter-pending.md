# Filter pending

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Malformed input returns an error (-32602 recommended). trace_filter range bounds exclude pending, as eth_getLogs does (-32602 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/h30/manifest.json) |
| [Anvil · 1.8.6-nightly · de005f70](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/h30/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-17/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/h30/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../clients/besu_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-17/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/h30/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/h30/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/h30/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "pending",
      "toBlock": "pending",
      "count": 3
    }
  ]
}
```

**Anvil · 1.8.6-nightly · de005f70** (`anvil Version: 1.8.6-nightly+de005f70`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas

**Besu · 26.10-develop · 0776d82f** (`besu/v26.10-develop-0776d82/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas. Code -32603 (-32602 recommended).
- [H32](../../decisions/H32.md): trace_filter range bounds exclude pending, as eth_getLogs does (-32602 recommended). Code -32603 (-32602 recommended).

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas. Code -32603 (-32602 recommended).
- [H32](../../decisions/H32.md): trace_filter range bounds exclude pending, as eth_getLogs does (-32602 recommended). Code -32603 (-32602 recommended).

**Erigon · 3.8.0-dev · 5b452f41** (`3.8.0-dev-5b452f41`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas. Code -32000 (-32602 recommended).

**Geth draft fork · 1.17.7-unstable · 71db3b03** (`Geth/v1.17.7-unstable-71db3b03-2026-10-14/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas

**Nethermind · 2.2.0-preview · cd336c4c** (`2.2.0-preview+cd336c4c`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas

**Reth · 2.7.0 · ec3e7e42** (`Reth Version: 2.7.0+ec3e7e42`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas

</details>
