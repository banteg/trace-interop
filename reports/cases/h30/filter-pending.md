# Filter pending

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Malformed input returns invalid params (-32602). trace_filter range bounds exclude pending, as eth_getLogs does (-32602).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/h30/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/h30/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/h30/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/h30/manifest.json) |
| [Nethermind · 2.1.0-unstable · 641592d2](../../clients/nethermind_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h15-call-compat/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/h30/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/h30/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h15-call-compat/h30/observations.json) · [Build/run](../../../evidence/2026-09-24/h15-call-compat/h30/manifest.json) |

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

**Besu · 26.9-develop · f9572aa8** (`besu/v26.9-develop-f9572aa/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas
- [H32](../../decisions/H32.md): trace_filter range bounds exclude pending, as eth_getLogs does (-32602).

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas
- [H32](../../decisions/H32.md): trace_filter range bounds exclude pending, as eth_getLogs does (-32602).

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas
- [H32](../../decisions/H32.md): trace_filter range bounds exclude pending, as eth_getLogs does (-32602).

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas
- [H32](../../decisions/H32.md): trace_filter range bounds exclude pending, as eth_getLogs does (-32602).

**Nethermind · 2.1.0-unstable · 641592d2** (`2.1.0-unstable+641592d2`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas
- [H32](../../decisions/H32.md): trace_filter range bounds exclude pending, as eth_getLogs does (-32602).

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H14](../../decisions/H14.md): Malformed input returns invalid params (-32602). 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas
- [H32](../../decisions/H32.md): trace_filter range bounds exclude pending, as eth_getLogs does (-32602).

</details>
