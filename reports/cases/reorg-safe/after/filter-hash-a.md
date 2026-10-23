# After/filter hash a

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** After the switch to branch B, A’s block 0x2d is noncanonical: its hash is an error (-32001), never B’s [] or records.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.1 · e83703cd](../../../clients/besu_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../../clients/besu_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../../clients/erigon_release.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../../clients/erigon_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../../clients/go-ethereum_trace.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../../clients/nethermind_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-10-23/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-23/eval/reorg-safe/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": "0xe6d9078b4964bc1b329fb12242254e21cf88ffa9a88058e515d6e79f7d8fce0d"
    }
  ]
}
```

**Besu · 26.10-develop · 781a7e1d** (`besu/v26.10-develop-781a7e1/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): After the switch to branch B, A’s block 0x2d is noncanonical: its hash is an error (-32001), never B’s [] or records. Rejected (-32000: Block not found); the code must be -32001.

**Besu · 26.10.1 · e83703cd** (`besu/v26.10.1/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): After the switch to branch B, A’s block 0x2d is noncanonical: its hash is an error (-32001), never B’s [] or records. Rejected (-32000: Block not found); the code must be -32001.

**Nethermind · 2.2.1 · c4f1015b** (`2.2.1+c4f1015b`)

- [H33](../../../decisions/H33.md): After the switch to branch B, A’s block 0x2d is noncanonical: its hash is an error (-32001), never B’s [] or records. Rejected (-32000: 0xe6d9078b4964bc1b329fb12242254e21cf88ffa9a88058e515d6e79f7d8fce0d block is not canonical); the code must be -32001.

**Reth · 2.8.0 · 53bf066f** (`Reth Version: 2.8.0+53bf066f`)

- [H33](../../../decisions/H33.md): After the switch to branch B, A’s block 0x2d is noncanonical: its hash is an error (-32001), never B’s [] or records. Rejected (-32602: Invalid params); the code must be -32001.

**Reth · 2.8.1 · d763342f** (`Reth Version: 2.8.1+d763342f`)

- [H33](../../../decisions/H33.md): After the switch to branch B, A’s block 0x2d is noncanonical: its hash is an error (-32001), never B’s [] or records. Rejected (-32602: Invalid params); the code must be -32001.

</details>
