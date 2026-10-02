# Filter both unknown mode

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Malformed input returns an error (-32602 recommended). Unknown mode values are rejected (-32602 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Anvil · 1.8.4-nightly · 328811cb](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 6 records | ⚠️ Differs | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |

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

**Anvil · 1.8.4-nightly · 328811cb** (`anvil Version: 1.8.4-nightly+328811cb`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

**Besu · 26.10-develop · 711f8142** (`besu/v26.10-develop-711f814/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

**Erigon · 3.8.0-dev · 6da806cb** (`3.8.0-dev-6da806cb`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas
- [H03](../../decisions/H03.md): Unknown mode values are rejected (-32602 recommended).

**Geth draft fork · 1.17.7-unstable · 67f41dea** (`Geth/v1.17.7-unstable-67f41dea-2026-09-30/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

**Nethermind · 2.2.0-preview · 3370d566** (`2.2.0-preview+3370d566`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas
- [H03](../../decisions/H03.md): Unknown mode values are rejected (-32602 recommended).

**Reth · 2.7.0 · 078d0262** (`Reth Version: 2.7.0+078d0262`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas

</details>
