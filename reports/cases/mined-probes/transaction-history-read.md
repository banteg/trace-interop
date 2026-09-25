# Transaction history read

`trace_transaction` · mined-probes · [All reports](../../README.md)

**What this checks:** The reader makes one STATICCALL to the system contract. Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_transaction",
  "params": [
    "0x5bff67694ccfbfa88f7d81a185ee437e5b484809505cc49446810603b5f823f2"
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call [0]: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call []: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call [0]: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call []: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d

</details>
