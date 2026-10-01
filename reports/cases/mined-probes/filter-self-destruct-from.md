# Filter self destruct from

`trace_filter` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. A SELFDESTRUCT matches fromAddress by its executing account.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · df92604b](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · 28edf391](../../clients/besu_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 50e2cc4f](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · 759efed7](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 5b686303](../../clients/reth_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-01/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-01/eval/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromAddress": [
        "0x000000000000000000000000000000000000de57"
      ],
      "fromBlock": "0x4",
      "toBlock": "0x4"
    }
  ]
}
```

**Anvil · 1.8.4-nightly · df92604b** (`anvil Version: 1.8.4-nightly+df92604b`)

- [H23](../../decisions/H23.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H23](../../decisions/H23.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.10-develop · 28edf391** (`besu/v26.10-develop-28edf39/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A SELFDESTRUCT matches fromAddress by its executing account. Expected [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [0], 'suicide']], got [].

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A SELFDESTRUCT matches fromAddress by its executing account. Expected [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [0], 'suicide']], got [].

**Reth · 2.7.0 · 5b686303** (`Reth Version: 2.7.0+5b686303`)

- [H23](../../decisions/H23.md): A SELFDESTRUCT matches fromAddress by its executing account. Expected [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [0], 'suicide']], got [].

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H23](../../decisions/H23.md): A SELFDESTRUCT matches fromAddress by its executing account. Expected [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [0], 'suicide']], got [].

</details>
