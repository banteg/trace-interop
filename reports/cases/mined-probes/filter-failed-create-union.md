# Filter failed create union

`trace_filter` · mined-probes · [All reports](../../README.md)

**What this checks:** Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Union mode retains the creator match of a failed CREATE. Assess this declared topic case. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32602` | 🚧 Blocked | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | RPC error `-32602` | 🚧 Blocked | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_filter",
  "params": [
    {
      "fromAddress": [
        "0x000000000000000000000000000000000000fac0"
      ],
      "fromBlock": "0x3",
      "mode": "union",
      "toAddress": [
        "0xd8353791c13be48589d7247c3284625edca5aa72"
      ],
      "toBlock": "0x3"
    }
  ]
}
```

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H23](../../decisions/H23.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result {"address": "0xd8353791c13be48589d7247c3284625edca5aa72", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'result': {

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result {"address": "0xd8353791c13be48589d7247c3284625edca5aa72", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'result': {

</details>
