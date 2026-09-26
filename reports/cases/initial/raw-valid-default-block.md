# Raw valid default block

`trace_rawTransaction` · initial · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected). Assess the declared property. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. The declared state-diff fixture returns the requested account changes. Inspect account-existence markers in the requested state diff. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · 5a99f1a8](../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 7853b922](../../clients/erigon_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · c8449896](../../clients/go-ethereum_trace.md) | RPC error `1` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Nethermind · 2.1.0-preview · fca93966](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |
| [Reth · 2.5.2 · df7b7fdf](../../clients/reth_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-26/anvil/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-26/anvil/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0xf86a80847735940082520894000000000000000000000000000000000000123401808718e5bb3abd10a0a04c833abdb116ad76fc98610ae0e626d7e35154f1fba38ce6bfdaf69a31eec42ca035ecfb996cc68a2a03df0e1087194e25180b01bf0469f69b4f1d330eea9d027a",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Anvil · 1.8.4-nightly · 5a99f1a8** (`anvil Version: 1.8.4-nightly+5a99f1a8`)

- [H16](../../decisions/H16.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.
- [H17](../../decisions/H17.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H16](../../decisions/H16.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.
- [H17](../../decisions/H17.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.

**Besu · 26.9-develop · accdae00** (`besu/v26.9-develop-accdae0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.
- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.
- [H17](../../decisions/H17.md): Inspect account-existence markers in the requested state diff. No state-diff object was returned; account markers cannot be assessed.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x0000000000000000000000000000000000001234', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.
- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.
- [H17](../../decisions/H17.md): Inspect account-existence markers in the requested state diff. No state-diff object was returned; account markers cannot be assessed.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x0000000000000000000000000000000000001234', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

**Erigon · 3.8.0-dev · 7853b922** (`3.8.0-dev-7853b922`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.
- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

**Geth draft fork · 1.17.7-unstable · c8449896** (`Geth/v1.17.7-unstable-c8449896-2026-09-26/linux-amd64/go1.26.1`)

- [H16](../../decisions/H16.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.
- [H17](../../decisions/H17.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.

**Nethermind · 2.1.0-preview · fca93966** (`2.1.0-preview+fca93966`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.
- [H17](../../decisions/H17.md): State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields. 0x0000000000000000000000000000000000001234: new account lacks creation markers for all fields
- Result shape at `stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x66863b', 'to': '0x262aafd8968b'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000001234': {'balance': {'+': '0x1'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x7435ed30a8b4aeb087

**Reth · 2.5.2 · df7b7fdf** (`Reth Version: 2.5.2+df7b7fdf`)

- [H13](../../decisions/H13.md): Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected). Identified nonce_low; code -32000; accepted [-32003, 1].
- [H16](../../decisions/H16.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.
- [H17](../../decisions/H17.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H13](../../decisions/H13.md): Use the eth_sendRawTransaction error group for the violation, or -32003 (Transaction rejected). Identified nonce_low; code -32000; accepted [-32003, 1].
- [H16](../../decisions/H16.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.
- [H17](../../decisions/H17.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.

</details>
