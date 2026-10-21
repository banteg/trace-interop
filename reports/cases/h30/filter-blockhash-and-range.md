# Filter blockhash and range

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Malformed input returns an error (-32602 recommended). A non-null blockHash with a non-null fromBlock or toBlock is rejected (-32602 recommended), never answered by either selector.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "fromBlock": "0x2",
      "count": 3
    }
  ]
}
```

**Anvil · 1.8.6-nightly · 9089a6bf** (`anvil Version: 1.8.6-nightly+9089a6bf`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

**Erigon · 3.9.0-dev · d23467c5** (`3.9.0-dev-d23467c5`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

**Geth draft fork · 1.17.9-unstable · a15b96ff** (`Geth/v1.17.9-unstable-a15b96ff-2026-10-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

**Nethermind · 2.3.0-preview · e2e011c8** (`2.3.0-preview+e2e011c8`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

</details>
