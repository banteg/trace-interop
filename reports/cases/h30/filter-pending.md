# Filter pending

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Malformed input returns an error (-32602 recommended). trace_filter range bounds exclude pending, as eth_getLogs does (-32602 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/h30/manifest.json) |

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

**Anvil · 1.8.4-nightly · 60255eee** (`anvil Version: 1.8.4-nightly+60255eee`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas. Code -32603 (-32602 recommended).
- [H32](../../decisions/H32.md): trace_filter range bounds exclude pending, as eth_getLogs does (-32602 recommended). Code -32603 (-32602 recommended).

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas. Code -32603 (-32602 recommended).
- [H32](../../decisions/H32.md): trace_filter range bounds exclude pending, as eth_getLogs does (-32602 recommended). Code -32603 (-32602 recommended).

**Erigon · 3.8.0-dev · 5cb6c867** (`3.8.0-dev-5cb6c867`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas. Code -32000 (-32602 recommended).

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas

**Nethermind · 2.2.0-preview · 6dff813b** (`2.2.0-preview+6dff813b`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas
- [H32](../../decisions/H32.md): trace_filter range bounds exclude pending, as eth_getLogs does (-32602 recommended).

**Reth · 2.7.0 · 10bcf461** (`Reth Version: 2.7.0+10bcf461`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas

</details>
