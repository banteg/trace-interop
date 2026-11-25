# Filter hash bounds

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Malformed input returns an error (-32602 recommended). Filter bounds are block numbers or tags, never block hashes: a hash bound is rejected (-32602 recommended), as eth_getLogs range bounds are.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "toBlock": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "count": 3
    }
  ]
}
```

**Anvil · 1.10.1-nightly · 50d75f19** (`anvil Version: 1.10.1-nightly+50d75f19`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas; '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas

**Anvil · 1.10.0 · 083e2299** (`anvil Version: 1.10.0+083e2299`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas; '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas; '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas; '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas

**Erigon · 3.9.0-dev · e91aca7f** (`3.9.0-dev-e91aca7f`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas; '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas

**Erigon · 3.8.2 · 8a3f3b2c** (`3.8.2-8a3f3b2c`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas; '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas

**Geth draft fork · 1.17.11-unstable · edbd5f17** (`Geth/v1.17.11-unstable-edbd5f17-2026-11-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas; '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas

**Nethermind · 2.4.0-preview · e2f069a6** (`2.4.0-preview+e2f069a6`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas; '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas; '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas; '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H32 owns this request’s rejection. '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas; '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas

</details>
