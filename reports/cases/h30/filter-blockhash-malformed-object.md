# Filter blockhash malformed object

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Malformed input returns an error (-32602 recommended). blockHash takes a bare 32-byte hash, not an EIP-1898 object: it is rejected (-32602 recommended).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 245 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": {
        "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e"
      }
    }
  ]
}
```

**Anvil · 1.8.4-nightly · e3429853** (`anvil Version: 1.8.4-nightly+e3429853`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. {'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e'} is not valid under any of the given schemas

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. {'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e'} is not valid under any of the given schemas

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. {'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e'} is not valid under any of the given schemas

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. {'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e'} is not valid under any of the given schemas

**Erigon · 3.8.0-dev · 923b4d31** (`3.8.0-dev-923b4d31`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. {'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e'} is not valid under any of the given schemas
- [H33](../../decisions/H33.md): blockHash takes a bare 32-byte hash, not an EIP-1898 object: it is rejected (-32602 recommended). Accepted: answered another block, 3 records from block 0x30 (the head).

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. {'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e'} is not valid under any of the given schemas
- [H33](../../decisions/H33.md): blockHash takes a bare 32-byte hash, not an EIP-1898 object: it is rejected (-32602 recommended). Accepted: answered another block, 245 records from 48 blocks, block 0x1 to block 0x30 (the head).

**Geth draft fork · 1.17.7-unstable · ec1cec0b** (`Geth/v1.17.7-unstable-ec1cec0b-2026-09-30/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. {'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e'} is not valid under any of the given schemas

**Nethermind · 2.2.0-preview · 79173d14** (`2.2.0-preview+79173d14`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. {'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e'} is not valid under any of the given schemas

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. {'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e'} is not valid under any of the given schemas
- [H33](../../decisions/H33.md): blockHash takes a bare 32-byte hash, not an EIP-1898 object: it is rejected (-32602 recommended). Accepted: answered another block, 4 records from block 0x30 (the head).
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Reth · 2.7.0 · 43a93dbc** (`Reth Version: 2.7.0+43a93dbc`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. {'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e'} is not valid under any of the given schemas

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. {'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e'} is not valid under any of the given schemas

</details>
