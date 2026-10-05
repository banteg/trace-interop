# Filter blockhash and range

`trace_filter` · h30 · [All reports](../../README.md)

**What this checks:** Malformed input returns an error (-32602 recommended). A non-null blockHash with a non-null fromBlock or toBlock is rejected (-32602 recommended), never answered by either selector.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Anvil · 1.8.4-nightly · e15c2f1c](../../clients/anvil_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 3 records | ⚠️ Differs | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Erigon · 3.8.0-dev · 96188a47](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 3 records | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Nethermind · 2.2.0-preview · e8955c4c](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |
| [Reth · 2.7.0 · 42fa3c56](../../clients/reth_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-05/eval/h30/observations.json.gz) · [Build/run](../../../evidence/2026-10-05/eval/h30/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_filter",
  "params": [
    {
      "blockHash": "0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e",
      "fromBlock": "0x2",
      "count": 3
    }
  ]
}
```

**Anvil · 1.8.4-nightly · e15c2f1c** (`anvil Version: 1.8.4-nightly+e15c2f1c`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'
- [H33](../../decisions/H33.md): A non-null blockHash with a non-null fromBlock or toBlock is rejected (-32602 recommended), never answered by either selector. Accepted: answered block 0x2’s 3 records.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'
- [H33](../../decisions/H33.md): A non-null blockHash with a non-null fromBlock or toBlock is rejected (-32602 recommended), never answered by either selector. Accepted: answered block 0x2’s 3 records.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Erigon · 3.8.0-dev · 96188a47** (`3.8.0-dev-96188a47`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'
- [H33](../../decisions/H33.md): A non-null blockHash with a non-null fromBlock or toBlock is rejected (-32602 recommended), never answered by either selector. Accepted: answered block 0x2’s 3 records.

**Geth draft fork · 1.17.7-unstable · e67cfd25** (`Geth/v1.17.7-unstable-e67cfd25-2026-10-03/linux-amd64/go1.26.1`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

**Nethermind · 2.2.0-preview · e8955c4c** (`2.2.0-preview+e8955c4c`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

**Nethermind · 2.1.0 · b3e7e84c** (`2.1.0+b3e7e84c`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'
- [H33](../../decisions/H33.md): A non-null blockHash with a non-null fromBlock or toBlock is rejected (-32602 recommended), never answered by either selector. Accepted: answered block 0x2’s 3 records.
- Result shape at `0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0x13488', 'input': '0x01', 'to': '0x9dcd17433742f4c0ca53122ab541d0ba67fc27d3', 'value': '0x0'}, 'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e', 'blockNumber': 2, 'error':

**Reth · 2.7.0 · 42fa3c56** (`Reth Version: 2.7.0+42fa3c56`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): Malformed input returns an error (-32602 recommended). H33 owns this request’s rejection. '0x2' is not of type 'null'

</details>
