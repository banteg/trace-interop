# Filter both unknown mode

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Malformed input returns an error (-32602 recommended). Unknown mode values are rejected (-32602 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 6 records | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2",
      "toBlock": "0x2",
      "fromAddress": [
        "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f"
      ],
      "toAddress": [
        "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      ],
      "mode": "garbage"
    }
  ]
}
```

**Anvil · 1.8.4-nightly · df92604b** (`anvil Version: 1.8.4-nightly+df92604b`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

**Besu · 26.10-develop · 28edf391** (`besu/v26.10-develop-28edf39/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

**Erigon · 3.8.0-dev · 50e2cc4f** (`3.8.0-dev-50e2cc4f`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas
- [H03](../../decisions/H03.md): Unknown mode values are rejected (-32602 recommended).

**Geth draft fork · 1.17.7-unstable · 67f41dea** (`Geth/v1.17.7-unstable-67f41dea-2026-09-30/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

**Nethermind · 2.2.0-preview · 759efed7** (`2.2.0-preview+759efed7`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas
- [H03](../../decisions/H03.md): Unknown mode values are rejected (-32602 recommended).

**Reth · 2.7.0 · 5b686303** (`Reth Version: 2.7.0+5b686303`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

</details>
