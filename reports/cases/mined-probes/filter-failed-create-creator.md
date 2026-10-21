# Filter failed create creator

`trace_filter` · mined-probes · [All reports](../../README.md)

**What this checks:** Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. A failed CREATE still matches its creator. Assess this declared topic case.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-21/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/mined-probes/manifest.json) |
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
  "method": "trace_filter",
  "params": [
    {
      "fromAddress": [
        "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf"
      ],
      "fromBlock": "0x3",
      "toBlock": "0x3"
    }
  ]
}
```

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H23](../../decisions/H23.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23d76', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'revertReas

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23d76', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'revertReas

</details>
