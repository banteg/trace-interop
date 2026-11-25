# Filter creator from

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Failed frames have an error string; an exceptional halt carries result null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 7 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 7 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 7 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 7 records | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "fromBlock": "0x2",
      "toBlock": "0x2",
      "fromAddress": [
        "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      ]
    }
  ]
}
```

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [1]: error 'Reverted', result null.
- Result shape at `1`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a9
- Result shape at `3`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code. First at traceAddress [1]: error 'Reverted', result null.
- Result shape at `1`: {'action': {'callType': 'call', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x0000000000000000000000000000000000000000000000000000000000000001', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a9
- Result shape at `3`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H09](../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress [3]: error 'Mutable Call In Static Context', result null.
- Result shape at `3`: {'action': {'callType': 'staticcall', 'from': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0', 'gas': '0xea60', 'input': '0x', 'to': '0x7dcd17433742f4c0ca53122ab541d0ba67fc27df', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error

</details>
