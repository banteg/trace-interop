# Filter destroyed recipient

`trace_filter` · mined-probes · [All reports](../../README.md)

**What this checks:** Reward and SELFDESTRUCT records carry result null. A created-then-destroyed address matches its creation and its SELFDESTRUCT beneficiary. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |

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
        "0xeac0306941fda13b06e9e7a41c79b5f618cc67ce"
      ],
      "toBlock": "0x4"
    }
  ]
}
```

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H23](../../decisions/H23.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A created-then-destroyed address matches its creation and its SELFDESTRUCT beneficiary. Expected [['0xf27dc2036128a7b56ff5be5e85c989e96865263ac2336aba178a94e8cc8ab284', [0], 'create'], ['0xf27dc2036128a7b56ff5be5e85c989e96865263ac2336aba178a94e8cc8ab284', [0, 0], 'suicide']], got [].

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A created-then-destroyed address matches its creation and its SELFDESTRUCT beneficiary. Expected [['0xf27dc2036128a7b56ff5be5e85c989e96865263ac2336aba178a94e8cc8ab284', [0], 'create'], ['0xf27dc2036128a7b56ff5be5e85c989e96865263ac2336aba178a94e8cc8ab284', [0, 0], 'suicide']], got [].

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [0, 0]: error None, result null.
- Result shape at `1`: {'action': {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'balance': '0x100', 'refundAddress': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce'}, 'blockHash': '0xc8c95be3c7677411d196b7ef4b16b998aa6e584f82bd0d360eb5aaf21b40ded4', 'blockNumber': 4, 'subtraces': 0, 'traceAddress': [0, 0], 'trans

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [0, 0]: error None, result null.
- Result shape at `1`: {'action': {'address': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce', 'balance': '0x100', 'refundAddress': '0xeac0306941fda13b06e9e7a41c79b5f618cc67ce'}, 'blockHash': '0xc8c95be3c7677411d196b7ef4b16b998aa6e584f82bd0d360eb5aaf21b40ded4', 'blockNumber': 4, 'subtraces': 0, 'traceAddress': [0, 0], 'trans

</details>
