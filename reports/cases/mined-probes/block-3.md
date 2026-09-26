# Block 3

`trace_block` · mined-probes · [All reports](../../README.md)

**What this checks:** Assess this declared topic case. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. A reverted top-level CREATE is one failed create frame. A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. The factory call contains its failed nested create frame. The handled nested failure leaves the root successful; root gasUsed is its execution gas, action.gas excludes intrinsic gas. A reverted nested CREATE reports error Reverted and result {gasUsed, output} without address or code. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | Setup incomplete; not assessed | ⚪ Not assessed | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | 3 records | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 4 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/mined-probes/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/mined-probes/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_block",
  "params": [
    "0x3"
  ]
}
```

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H09](../../decisions/H09.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H09](../../decisions/H09.md): Assess this declared topic case. Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot)

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H09](../../decisions/H09.md): A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. create []: result None != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- [H09](../../decisions/H09.md): A reverted nested CREATE reports error Reverted and result {gasUsed, output} without address or code. create [0]: result None != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23d76', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'revertReas
- Result shape at `2`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'subtraces'

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H09](../../decisions/H09.md): A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. create []: result None != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- [H09](../../decisions/H09.md): A reverted nested CREATE reports error Reverted and result {gasUsed, output} without address or code. create [0]: result None != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23d76', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'revertReas
- Result shape at `2`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'subtraces'

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result {"address": "0x51a240271ab8ab9f9a21c82d9a85396b704e164d", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- [H09](../../decisions/H09.md): A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. create []: result {'address': '0x51a240271ab8ab9f9a21c82d9a85396b704e164d', 'code': '0xdeadbeef', 'gasUsed': '0x11'} != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- [H09](../../decisions/H09.md): A reverted nested CREATE reports error Reverted and result {gasUsed, output} without address or code. create [0]: result {'address': '0xd8353791c13be48589d7247c3284625edca5aa72', 'code': '0xdeadbeef', 'gasUsed': '0x11'} != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23d76', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'result': {
- Result shape at `2`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'result': {

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result {"address": "0x51a240271ab8ab9f9a21c82d9a85396b704e164d", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- [H09](../../decisions/H09.md): A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. create []: result {'address': '0x51a240271ab8ab9f9a21c82d9a85396b704e164d', 'code': '0xdeadbeef', 'gasUsed': '0x11'} != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- [H09](../../decisions/H09.md): A reverted nested CREATE reports error Reverted and result {gasUsed, output} without address or code. create [0]: result {'address': '0xd8353791c13be48589d7247c3284625edca5aa72', 'code': '0xdeadbeef', 'gasUsed': '0x11'} != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23d76', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'result': {
- Result shape at `2`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'result': {

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H09](../../decisions/H09.md): A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. create []: result None != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- [H09](../../decisions/H09.md): A reverted nested CREATE reports error Reverted and result {gasUsed, output} without address or code. create [0]: result None != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23d76', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'subtraces'
- Result shape at `2`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'subtraces'
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- [H09](../../decisions/H09.md): A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. create []: result None != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- [H09](../../decisions/H09.md): A reverted nested CREATE reports error Reverted and result {gasUsed, output} without address or code. create [0]: result None != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23d76', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'subtraces'
- Result shape at `2`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'subtraces'
- Result shape at `3`: 'transactionHash' is a required property
- Result shape at `3`: 'transactionPosition' is a required property

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result {"address": "0x51a240271ab8ab9f9a21c82d9a85396b704e164d", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- [H09](../../decisions/H09.md): A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. create []: result {'address': '0x51a240271ab8ab9f9a21c82d9a85396b704e164d', 'code': '0xdeadbeef', 'gasUsed': '0x11'} != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- [H09](../../decisions/H09.md): A reverted nested CREATE reports error Reverted and result {gasUsed, output} without address or code. create [0]: result {'address': '0xd8353791c13be48589d7247c3284625edca5aa72', 'code': '0xdeadbeef', 'gasUsed': '0x11'} != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23d76', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'result': {
- Result shape at `2`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'result': {

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result {"address": "0x51a240271ab8ab9f9a21c82d9a85396b704e164d", "code": "0xdeadbeef", "gasUsed": "0x11"}.
- [H09](../../decisions/H09.md): A reverted CREATE reports error Reverted and result {gasUsed, output} with its revert bytes and no address or code; root action.gas excludes intrinsic gas. create []: result {'address': '0x51a240271ab8ab9f9a21c82d9a85396b704e164d', 'code': '0xdeadbeef', 'gasUsed': '0x11'} != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- [H09](../../decisions/H09.md): A reverted nested CREATE reports error Reverted and result {gasUsed, output} without address or code. create [0]: result {'address': '0xd8353791c13be48589d7247c3284625edca5aa72', 'code': '0xdeadbeef', 'gasUsed': '0x11'} != {'gasUsed': '0x11', 'output': '0xdeadbeef'}
- Result shape at `0`: {'action': {'creationMethod': 'create', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x23d76', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'result': {
- Result shape at `2`: {'action': {'creationMethod': 'create', 'from': '0x000000000000000000000000000000000000fac0', 'gas': '0x2346c', 'init': '0x63deadbeef5f526004601cfd', 'value': '0x0'}, 'blockHash': '0x68ba9a0733d967eb67f974257a48c57ba432bd29daa4294f52985decf78a51c3', 'blockNumber': 3, 'error': 'Reverted', 'result': {

</details>
