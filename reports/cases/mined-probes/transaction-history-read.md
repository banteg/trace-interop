# Transaction history read

`trace_transaction` · mined-probes · [All reports](../../README.md)

**What this checks:** The reader makes one STATICCALL to the system contract. Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |

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

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H28](../../decisions/H28.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call [0]: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call []: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call [0]: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call []: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d

</details>
