# Filter self destruct to

`trace_filter` · mined-probes · [All reports](../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. A SELFDESTRUCT to self also matches toAddress as its own beneficiary.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/mined-probes/manifest.json) |

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

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A SELFDESTRUCT to self also matches toAddress as its own beneficiary. Expected [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [], 'call'], ['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [0], 'suicide']], got [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [], 'call']].

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A SELFDESTRUCT to self also matches toAddress as its own beneficiary. Expected [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [], 'call'], ['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [0], 'suicide']], got [['0x87cfeb711c34353c96b0d55c58aaf1b02f602aff3baa854ee9ba1feb1ca2c3a2', [], 'call']].

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [0]: error None, result null.
- Result shape at `1`: {'action': {'address': '0x000000000000000000000000000000000000de57', 'balance': '0x3e8', 'refundAddress': '0x000000000000000000000000000000000000de57'}, 'blockHash': '0xc8c95be3c7677411d196b7ef4b16b998aa6e584f82bd0d360eb5aaf21b40ded4', 'blockNumber': 4, 'subtraces': 0, 'traceAddress': [0], 'transact

</details>
