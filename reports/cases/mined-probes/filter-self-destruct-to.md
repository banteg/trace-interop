# Filter self destruct to

`trace_filter` · mined-probes · [All reports](../../README.md)

**What this checks:** A SELFDESTRUCT to self also matches toAddress as its own beneficiary.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x4",
      "toAddress": [
        "0x000000000000000000000000000000000000de57"
      ],
      "toBlock": "0x4"
    }
  ]
}
```

**Besu · 26.9-develop · cf89071f** (`besu/v26.9-develop-cf89071/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A SELFDESTRUCT to self also matches toAddress as its own beneficiary. Expected [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [], 'call'], ['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [0], 'suicide']], got [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [], 'call']].

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A SELFDESTRUCT to self also matches toAddress as its own beneficiary. Expected [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [], 'call'], ['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [0], 'suicide']], got [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [], 'call']].

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H23](../../decisions/H23.md): A SELFDESTRUCT to self also matches toAddress as its own beneficiary. Expected [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [], 'call'], ['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [0], 'suicide']], got [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [], 'call']].

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H23](../../decisions/H23.md): A SELFDESTRUCT to self also matches toAddress as its own beneficiary. Expected [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [], 'call'], ['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [0], 'suicide']], got [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [], 'call']].

</details>
