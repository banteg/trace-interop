# Raw validation funds gas trace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected). Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | RPC error `809` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf8730a842da282a9830186a0940000000000000000000000000000000000001002880de0b6b3a7640000808718e5bb3abd10a0a08d1dbb3889e631f39d0e1b3c5eb58bc2211229b1e8d400981345f2fe4523c3dda0604a32a2b5e1837b5fb05e9bb78186db1760297eacb2b865f4860f9816aae7f9",
    [
      "trace"
    ]
  ]
}
```

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. value is affordable but upfront gas plus value is not
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0xde0b6b3a7640000'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. value is affordable but upfront gas plus value is not
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'input': '0x', 'to': '0x0000000000000000000000000000000000001002', 'value': '0xde0b6b3a7640000'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H13](../../decisions/H13.md): Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected). Identified funds; code -32000; accepted [-32003, 809].

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. value is affordable but upfront gas plus value is not

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H13](../../decisions/H13.md): Assess the declared property. Cannot inspect this property: malformed_json.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H13](../../decisions/H13.md): Assess the declared property. Cannot inspect this property: malformed_json.

</details>
