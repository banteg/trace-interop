# Filter blockhash malformed short

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Malformed input returns an error (-32602 recommended). A blockHash that is not a 32-byte hash is rejected (-32602 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 245 records | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": "0xf5de2a84"
    }
  ]
}
```

**Anvil · 1.8.4-nightly · e15c2f1c** (`anvil Version: 1.8.4-nightly+e15c2f1c`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0xf5de2a84' is not valid under any of the given schemas

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0xf5de2a84' is not valid under any of the given schemas

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0xf5de2a84' is not valid under any of the given schemas

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0xf5de2a84' is not valid under any of the given schemas

**Erigon · 3.8.0-dev · 96188a47** (`3.8.0-dev-96188a47`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0xf5de2a84' is not valid under any of the given schemas

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0xf5de2a84' is not valid under any of the given schemas
- [H33](../../decisions/H33.md): A blockHash that is not a 32-byte hash is rejected (-32602 recommended). Accepted: answered another block, 245 records from 48 blocks, block 0x1 to block 0x30 (the head).

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0xf5de2a84' is not valid under any of the given schemas

**Nethermind · 2.2.0-preview · e8955c4c** (`2.2.0-preview+e8955c4c`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0xf5de2a84' is not valid under any of the given schemas

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0xf5de2a84' is not valid under any of the given schemas
- [H33](../../decisions/H33.md): A blockHash that is not a 32-byte hash is rejected (-32602 recommended). Accepted: answered another block, 4 records from block 0x30 (the head).
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Reth · 2.7.0 · 42fa3c56** (`Reth Version: 2.7.0+42fa3c56`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0xf5de2a84' is not valid under any of the given schemas

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0xf5de2a84' is not valid under any of the given schemas

</details>
