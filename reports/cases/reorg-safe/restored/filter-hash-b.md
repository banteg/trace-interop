# Restored/filter hash b

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001), never A’s records. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.0 · 976ca7ea](../../../clients/besu_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../../clients/besu_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../../clients/erigon_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../../clients/erigon_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../../clients/go-ethereum_trace.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../../clients/nethermind_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-10-18/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-18/eval/reorg-safe/manifest.json) |

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

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001), never A’s records. Rejected (-32000: Block not found); the code must be -32001.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001), never A’s records. Rejected (-32000: Block not found); the code must be -32001.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H33](../../../decisions/H33.md): Assess this declared topic case. Scenario setup stopped: Invalid forkchoice state

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H33](../../../decisions/H33.md): Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001), never A’s records. Rejected (-32000: 0xb75975dcf8dc29c9d8f63272511a20eb5c16c8466634e83f6b840d3baaa54110 block is not canonical); the code must be -32001.

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H33](../../../decisions/H33.md): Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001), never A’s records. Rejected (-32000: 0xb75975dcf8dc29c9d8f63272511a20eb5c16c8466634e83f6b840d3baaa54110 block is not canonical); the code must be -32001.

**Reth · 2.7.0 · e6679687** (`Reth Version: 2.7.0+e6679687`)

- [H33](../../../decisions/H33.md): Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001), never A’s records. Rejected (-32602: Invalid params); the code must be -32001.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H33](../../../decisions/H33.md): Once branch A is restored, B’s block 0x2d is noncanonical: an error (-32001), never A’s records. Rejected (-32602: Invalid params); the code must be -32001.

</details>
