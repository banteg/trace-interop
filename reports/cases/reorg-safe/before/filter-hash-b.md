# Before/filter hash b

`trace_filter` · reorg-safe · [All reports](../../../README.md)

**What this checks:** Before B’s payloads arrive, B’s block 0x2d is unknown: an error (-32001).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.10.2 · d3e1aea7](../../../clients/besu_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../../clients/besu_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../../clients/erigon_release.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../../clients/erigon_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../../clients/go-ethereum_trace.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../../clients/nethermind_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../../clients/nethermind_development.md) | RPC error `-32001` | ✅ Checked cases agree | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../../clients/reth_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../../clients/reth_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../../evidence/2026-10-29/eval/reorg-safe/observations.json.gz) · [Build/run](../../../../evidence/2026-10-29/eval/reorg-safe/manifest.json) |

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

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Before B’s payloads arrive, B’s block 0x2d is unknown: an error (-32001). Rejected (-32000: Block not found); the code must be -32001.

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H33](../../../decisions/H33.md): Before B’s payloads arrive, B’s block 0x2d is unknown: an error (-32001). Rejected (-32000: Block not found); the code must be -32001.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H33](../../../decisions/H33.md): Before B’s payloads arrive, B’s block 0x2d is unknown: an error (-32001). Rejected (-32000: header not found); the code must be -32001.

**Reth · 2.8.1 · 966010c9** (`Reth Version: 2.8.1+966010c9`)

- [H33](../../../decisions/H33.md): Before B’s payloads arrive, B’s block 0x2d is unknown: an error (-32001). Rejected (-32602: Invalid params); the code must be -32001.

**Reth · 2.9.0 · c9a780f4** (`Reth Version: 2.9.0+c9a780f4`)

- [H33](../../../decisions/H33.md): Before B’s payloads arrive, B’s block 0x2d is unknown: an error (-32001). Rejected (-32602: Invalid params); the code must be -32001.

</details>
