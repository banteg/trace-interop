# Filter self destruct from

`trace_filter` · mined-probes · [All reports](../../README.md)

**What this checks:** A SELFDESTRUCT matches fromAddress by its executing account. Assess this declared topic case. Reward and SELFDESTRUCT records carry result null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-23/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.7-nightly · 4e8874b2](../../clients/anvil_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-23/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/mined-probes/manifest.json) |
| [Besu · 26.10.1 · e83703cd](../../clients/besu_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-23/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../clients/besu_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-23/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../clients/nethermind_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-23/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/mined-probes/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/mined-probes/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../clients/reth_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-23/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/mined-probes/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../clients/reth_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-23/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/mined-probes/manifest.json) |

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

**Anvil · 1.8.7-nightly · 4e8874b2** (`anvil Version: 1.8.7-nightly+4e8874b2`)

- [H23](../../decisions/H23.md): A SELFDESTRUCT matches fromAddress by its executing account. Expected [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [0], 'suicide']], got [].

**Anvil · 1.8.6 · 6bad0a66** (`anvil Version: 1.8.6+6bad0a66`)

- [H23](../../decisions/H23.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.10-develop · 781a7e1d** (`besu/v26.10-develop-781a7e1/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A SELFDESTRUCT matches fromAddress by its executing account. Expected [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [0], 'suicide']], got [].

**Besu · 26.10.1 · e83703cd** (`besu/v26.10.1/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A SELFDESTRUCT matches fromAddress by its executing account. Expected [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [0], 'suicide']], got [].

**Nethermind · 2.2.1 · c4f1015b** (`2.2.1+c4f1015b`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [0]: error None, result null.
- Result shape at `0`: {'action': {'address': '0x000000000000000000000000000000000000de57', 'balance': '0x3e8', 'refundAddress': '0x000000000000000000000000000000000000de57'}, 'blockHash': '0xc8c95be3c7677411d196b7ef4b16b998aa6e584f82bd0d360eb5aaf21b40ded4', 'blockNumber': 4, 'subtraces': 0, 'traceAddress': [0], 'transact

**Reth · 2.8.0 · 53bf066f** (`Reth Version: 2.8.0+53bf066f`)

- [H23](../../decisions/H23.md): A SELFDESTRUCT matches fromAddress by its executing account. Expected [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [0], 'suicide']], got [].

**Reth · 2.8.1 · d763342f** (`Reth Version: 2.8.1+d763342f`)

- [H23](../../decisions/H23.md): A SELFDESTRUCT matches fromAddress by its executing account. Expected [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [0], 'suicide']], got [].

</details>
