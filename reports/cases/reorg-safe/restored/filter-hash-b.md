# Restored/filter hash b

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001), never A’s records.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.11.0 · 0e595f9e](../../../clients/besu_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../../clients/besu_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../../clients/erigon_release.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../../clients/erigon_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../../clients/go-ethereum_trace.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../../clients/nethermind_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-11-09/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-11-09/eval/reorg-safe/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": "0xb75975dcf8dc29c9d8f63272511a20eb5c16c8466634e83f6b840d3baaa54110"
    }
  ]
}
```

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001), never A’s records. Rejected (-32000: Block not found); the code must be -32001.

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001), never A’s records. Rejected (-32000: Block not found); the code must be -32001.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H33](../../../decisions/H33.md): Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001), never A’s records. Rejected (-32000: 0xb75975dcf8dc29c9d8f63272511a20eb5c16c8466634e83f6b840d3baaa54110 block is not canonical); the code must be -32001.

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H33](../../../decisions/H33.md): Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001), never A’s records. Rejected (-32602: Invalid params); the code must be -32001.

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H33](../../../decisions/H33.md): Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001), never A’s records. Rejected (-32602: Invalid params); the code must be -32001.

</details>
