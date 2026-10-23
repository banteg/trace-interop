# Filter to only intersection

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Reward and SELFDESTRUCT records carry result null. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/a/manifest.json) |
| [Anvil · 1.8.7-nightly · 4e8874b2](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/a/manifest.json) |
| [Besu · 26.10.1 · e83703cd](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-23/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/a/manifest.json) |
| [Besu · 26.10-develop · 781a7e1d](../../clients/besu_development.md) | 1 records | ⚠️ Differs | [Response](../../../evidence/2026-10-23/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/a/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · 598ba625](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/a/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/a/manifest.json) |
| [Nethermind · 2.2.1 · c4f1015b](../../clients/nethermind_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-23/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/a/manifest.json) |
| [Nethermind · 2.3.0-preview · 7192e7f3](../../clients/nethermind_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/a/manifest.json) |
| [Reth · 2.8.1 · d763342f](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/a/manifest.json) |
| [Reth · 2.8.0 · 53bf066f](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-23/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-23/eval/a/manifest.json) |

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
      "toAddress": [
        "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
      ],
      "mode": "intersection"
    }
  ]
}
```

**Anvil · 1.8.7-nightly · 4e8874b2** (`anvil Version: 1.8.7-nightly+4e8874b2`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.6 · 6bad0a66** (`anvil Version: 1.8.6+6bad0a66`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10-develop · 781a7e1d** (`besu/v26.10-develop-781a7e1/linux-x86_64/openjdk-java-25`)

- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Expected 1 such records from this client's block trace; got 0.
- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10.1 · e83703cd** (`besu/v26.10.1/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 ordinary records from this client's block trace.
- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. The H03 list semantics differ, so the special-action records cannot be judged separately.
- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.9.0-dev · 598ba625** (`3.9.0-dev-598ba625`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.9-unstable · a15b96ff** (`Geth/v1.17.9-unstable-a15b96ff-2026-10-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.3.0-preview · 7192e7f3** (`2.3.0-preview+7192e7f3`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.1 · c4f1015b** (`2.2.1+c4f1015b`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [6, 0]: error None, result null.
- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `1`: {'action': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'balance': '0x0', 'refundAddress': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [6, 0], 'transac

**Reth · 2.8.0 · 53bf066f** (`Reth Version: 2.8.0+53bf066f`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.8.1 · d763342f** (`Reth Version: 2.8.1+d763342f`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
