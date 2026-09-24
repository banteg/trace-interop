# Filter failed create intersection

`trace_filter` · mined-probes · [All reports](../../README.md)

**What this checks:** A failed CREATE has no recipient side, so an intersection with its would-be address is empty. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Besu · 26.9-develop · cf89071f](../../clients/besu_development.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 01c118ee](../../clients/erigon_development.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | `[]` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · 54b760cd](../../clients/nethermind_development.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-25/fixture-wave/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/fixture-wave/mined-probes/manifest.json) |

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
      "toAddress": [
        "0xd8353791c13be48589d7247c3284625edca5aa72"
      ],
      "toBlock": "0x3"
    }
  ]
}
```

**Erigon · 3.8.0-dev · 01c118ee** (`3.8.0-dev-01c118ee`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result {"address": "0xd8353791c13be48589d7247c3284625edca5aa72", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- [H23](../../decisions/H23.md): A failed CREATE has no recipient side, so an intersection with its would-be address is empty. Expected [], got [['0xffba49c281a4842a09a763f7723d4d6d210f1c6c33463e4c7828e50e27dc2b74', [0], 'create']].
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'result': {

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result {"address": "0xd8353791c13be48589d7247c3284625edca5aa72", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- [H23](../../decisions/H23.md): A failed CREATE has no recipient side, so an intersection with its would-be address is empty. Expected [], got [['0xffba49c281a4842a09a763f7723d4d6d210f1c6c33463e4c7828e50e27dc2b74', [0], 'create']].
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'result': {

**Nethermind · 2.1.0-preview · 54b760cd** (`2.1.0-preview+54b760cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result null.
- [H23](../../decisions/H23.md): A failed CREATE has no recipient side, so an intersection with its would-be address is empty. Expected [], got [['0xffba49c281a4842a09a763f7723d4d6d210f1c6c33463e4c7828e50e27dc2b74', [0], 'create']].
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'subtraces'

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result null.
- [H23](../../decisions/H23.md): A failed CREATE has no recipient side, so an intersection with its would-be address is empty. Expected [], got [['0xffba49c281a4842a09a763f7723d4d6d210f1c6c33463e4c7828e50e27dc2b74', [0], 'create']].
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'subtraces'

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result {"address": "0xd8353791c13be48589d7247c3284625edca5aa72", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- [H23](../../decisions/H23.md): A failed CREATE has no recipient side, so an intersection with its would-be address is empty. Expected [], got [['0xffba49c281a4842a09a763f7723d4d6d210f1c6c33463e4c7828e50e27dc2b74', [0], 'create']].
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'result': {

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [0]: error 'Reverted', result {"address": "0xd8353791c13be48589d7247c3284625edca5aa72", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- [H23](../../decisions/H23.md): A failed CREATE has no recipient side, so an intersection with its would-be address is empty. Expected [], got [['0xffba49c281a4842a09a763f7723d4d6d210f1c6c33463e4c7828e50e27dc2b74', [0], 'create']].
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'result': {

</details>
