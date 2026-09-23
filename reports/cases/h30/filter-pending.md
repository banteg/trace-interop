# Filter pending

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Record pending behavior without assuming a settled state or localization policy. A valid pending tag must not trigger an internal error; support remains a policy choice.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | RPC error `-32603` | Differs | [Response](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | RPC error `-32603` | Differs | [Response](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 3 records | Policy open | [Response](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | RPC error `-32000` | Policy open | [Response](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 3 records | Policy open | [Response](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 3 records | Policy open | [Response](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | RPC error `-32602` | Policy open | [Response](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-release-controlled-20260923/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | RPC error `-32602` | Policy open | [Response](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/observations.json) · [Build/run](../../../evidence/2026-09-23/h30-code-review/h30-dev-controlled-20260923/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "count": 3,
      "fromBlock": "pending",
      "toBlock": "pending"
    }
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. filter-pending: RPC error -32603.
- [H32](../../decisions/H32.md): A valid pending tag must not trigger an internal error; support remains a policy choice.

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. filter-pending: RPC error -32000.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. filter-pending: 3 records from blocks [48].

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. filter-pending: RPC error -32602.

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. filter-pending: RPC error -32603.
- [H32](../../decisions/H32.md): A valid pending tag must not trigger an internal error; support remains a policy choice.

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. filter-pending: 3 records from blocks [48].

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. filter-pending: 3 records from blocks [48].

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H32](../../decisions/H32.md): Record pending behavior without assuming a settled state or localization policy. filter-pending: RPC error -32602.

</details>
