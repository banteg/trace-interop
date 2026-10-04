# Filter failed create union

`trace_filter` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. Assess the declared property. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Union mode retains the creator match of a failed CREATE.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32602` | 🚧 Blocked | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | RPC error `-32602` | 🚧 Blocked | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | 1 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/mined-probes/manifest.json) |

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

**Anvil · 1.8.4-nightly · 60255eee** (`anvil Version: 1.8.4-nightly+60255eee`)

- [H23](../../decisions/H23.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H23](../../decisions/H23.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): Assess the declared property. The RPC returned an error, so there is no execution result to inspect.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result {"address": "0xd8353791c13be48589d7247c3284625edca5aa72", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'result': {

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result null.
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'subtraces'

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result {"address": "0xd8353791c13be48589d7247c3284625edca5aa72", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'result': {

</details>
