# Transaction history read

`trace_transaction` · mined-probes · [All reports](../../README.md)

**What this checks:** The reader makes one STATICCALL to the system contract. Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 2 records | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/mined-probes/manifest.json) |

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

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call [0]: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call []: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call [0]: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d
- [H28](../../decisions/H28.md): Replay applies the block’s pre-transaction system call, so the read returns the value the block stored. call []: result.output 0x0000000000000000000000000000000000000000000000000000000000000000 != 0x2bbb1ec4c4b7d44e05e437734ee13d193a22291da15db8b43316bfa0376b206d

</details>
