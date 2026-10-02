# Filter destroyed recipient

`trace_filter` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. A created-then-destroyed address matches its creation and its SELFDESTRUCT beneficiary.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-02/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · 328811cb](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-02/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-02/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../clients/besu_development.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-02/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/mined-probes/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/mined-probes/manifest.json) |

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

**Anvil · 1.8.4-nightly · 328811cb** (`anvil Version: 1.8.4-nightly+328811cb`)

- [H23](../../decisions/H23.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H23](../../decisions/H23.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.10-develop · 711f8142** (`besu/v26.10-develop-711f814/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A created-then-destroyed address matches its creation and its SELFDESTRUCT beneficiary. Expected [['0xf27dc2036128a7b56ff5be5e85c989e96865263ac2336aba178a94e8cc8ab284', [0], 'create'], ['0xf27dc2036128a7b56ff5be5e85c989e96865263ac2336aba178a94e8cc8ab284', [0, 0], 'suicide']], got [].

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A created-then-destroyed address matches its creation and its SELFDESTRUCT beneficiary. Expected [['0xf27dc2036128a7b56ff5be5e85c989e96865263ac2336aba178a94e8cc8ab284', [0], 'create'], ['0xf27dc2036128a7b56ff5be5e85c989e96865263ac2336aba178a94e8cc8ab284', [0, 0], 'suicide']], got [].

</details>
