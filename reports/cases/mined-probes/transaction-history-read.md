# Transaction history read

`trace_transaction` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. The reader makes one STATICCALL to the system contract. Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-30/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/mined-probes/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/mined-probes/manifest.json) |

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

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H28](../../decisions/H28.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H28](../../decisions/H28.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call [0]: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call []: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call [0]: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call []: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d

</details>
