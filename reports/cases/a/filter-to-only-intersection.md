# Filter to only intersection

`trace_filter` · a · [All reports](../../README.md)

**What this checks:** Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. Reward and SELFDESTRUCT records carry result null. Retain supporting reference evidence.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Anvil · 1.8.6-nightly · 6c21ffe2](../../clients/anvil_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Besu · 26.10-develop · abdf1419](../../clients/besu_development.md) | RPC error `-32602` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | `[]` | ⚠️ Differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Erigon · 3.9.0-dev · 1ee57924](../../clients/erigon_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · fdbb46a5](../../clients/go-ethereum_trace.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · 159862be](../../clients/nethermind_development.md) | 2 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |
| [Reth · 2.7.0 · e6679687](../../clients/reth_development.md) | 2 records | ✅ Checked cases agree | [Response](../../../evidence/2026-10-18/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-18/eval/a/manifest.json) |

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

**Anvil · 1.8.6-nightly · 6c21ffe2** (`anvil Version: 1.8.6-nightly+6c21ffe2`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10-develop · abdf1419** (`besu/v26.10-develop-abdf141/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 ordinary records from this client's block trace.
- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. The H03 list semantics differ, so the special-action records cannot be judged separately.
- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 ordinary records from this client's block trace.
- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. The H03 list semantics differ, so the special-action records cannot be judged separately.
- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.9.0-dev · 1ee57924** (`3.9.0-dev-1ee57924`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H03](../../decisions/H03.md): Compare address bytes: OR within each list, AND across lists by default and OR under mode union; missing/null/empty lists are unrestricted. Expected 1 ordinary records from this client's block trace.
- [H23](../../decisions/H23.md): A CREATE, SELFDESTRUCT or reward record matches the lists by its own from/to equivalents. The H03 list semantics differ, so the special-action records cannot be judged separately.
- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Geth draft fork · 1.17.9-unstable · fdbb46a5** (`Geth/v1.17.9-unstable-fdbb46a5-2026-10-18/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Nethermind · 2.2.0-preview · 159862be** (`2.2.0-preview+159862be`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [6, 0]: error None, result null.
- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `1`: {'action': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'balance': '0x0', 'refundAddress': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [6, 0], 'transac

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H09](../../decisions/H09.md): Reward and SELFDESTRUCT records carry result null. First at traceAddress [6, 0]: error None, result null.
- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.
- Result shape at `1`: {'action': {'address': '0x2d303c5b7911d87d594bf1b31fbb9aa187888893', 'balance': '0x0', 'refundAddress': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'subtraces': 0, 'traceAddress': [6, 0], 'transac

**Reth · 2.7.0 · e6679687** (`Reth Version: 2.7.0+e6679687`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): Retain supporting reference evidence. Ledger reference; executable requirements are assessed by the linked topic cases.

</details>
