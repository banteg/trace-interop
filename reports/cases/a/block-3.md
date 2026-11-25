# Block 3

`trace_block` · a · [All reports](../../README.md)

**What this checks:** A PoS block has no synthetic PoW reward records. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order. Reward and SELFDESTRUCT records carry result null. Reward records carry null transactionHash and transactionPosition.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 4 records | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 4 records | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_block",
  "params": [
    "0x3"
  ]
}
```

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records. 1 reward records.

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records. 1 reward records.

</details>
