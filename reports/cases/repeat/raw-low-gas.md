# Raw low gas

`trace_rawTransaction` · repeat · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected). Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/repeat/manifest.json) |
| [Besu · 26.9-develop · 85b32978](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/adopted-stances/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/repeat/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/repeat/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/repeat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · bb5c4682](../../clients/go-ethereum_trace.md) | RPC error `800` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/adopted-stances/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/repeat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/repeat/manifest.json) |
| [Nethermind · 2.1.0-preview · ce501a97](../../clients/nethermind_development.md) | Incomplete or malformed JSON | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/repeat/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/repeat/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/adopted-stances/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/adopted-stances/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b81858477359400824e2094000000000000000000000000000000000000123401808718e5bb3abd10a0a038e0b48a1022d5c55eea7e525942547d2009224ffa7ab6d1b40a5a16cb70a590a0279569cdb60041c1eac5043486547bdf086c64543c7e2d07870a288096213d33",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Besu · 26.9-develop · 85b32978** (`besu/v26.9-develop-85b3297/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x0000000000000000000000000000000000001234', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

**Besu · 26.8.1 · d97cbd61** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x0000000000000000000000000000000000001234', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

**Erigon · 3.8.0-dev · e26d9bd4** (`3.8.0-dev-e26d9bd4`)

- [H13](../../decisions/H13.md): Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected). Identified intrinsic; code -32000; accepted [-32003, 800].

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H13](../../decisions/H13.md): Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected). Identified intrinsic; code -32000; accepted [-32003, 800].

**Nethermind · 2.1.0-preview · ce501a97** (`2.1.0-preview+ce501a97`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H13](../../decisions/H13.md): Assess the declared property. Cannot inspect this property: malformed_json.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H13](../../decisions/H13.md): Assess the declared property. Cannot inspect this property: malformed_json.

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H13](../../decisions/H13.md): Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected). Identified intrinsic; code -32000; accepted [-32003, 800].

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H13](../../decisions/H13.md): Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected). Identified intrinsic; code -32000; accepted [-32003, 800].

</details>
