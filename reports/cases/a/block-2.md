# Block 2

`trace_block` · a · [All reports](../../README.md)

**What this checks:** Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. A PoS block has no synthetic PoW reward records. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. Trace roots preserve the frozen transaction inventory and recovered senders in canonical order.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | 14 records | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | 14 records | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 14 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 14 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 14 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | 13 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_block",
  "params": [
    "0x2"
  ]
}
```

**Anvil · 1.8.4-nightly · 60255eee** (`anvil Version: 1.8.4-nightly+60255eee`)

- [H29](../../decisions/H29.md): Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. frame [6] calls the identity precompile

**Anvil · 1.8.4 · 50af4efe** (`anvil Version: 1.8.4+50af4efe`)

- [H29](../../decisions/H29.md): Mined traces follow the same frame policy as simulations: omit the calltree’s nested zero-value identity call. frame [6] calls the identity precompile

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H05](../../decisions/H05.md): A PoS block has no synthetic PoW reward records.
- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress []: error 'Reverted', result null.
- Result shape at `/`: [{'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

</details>
