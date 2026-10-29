# Raw valid default block

`trace_rawTransaction` · initial · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Assess the declared property. Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. The declared state-diff fixture returns the requested account changes. Inspect account-existence markers in the requested state diff.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | RPC error `1` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/initial/manifest.json) |

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

**Anvil · 1.8.7-nightly · 716e795c** (`anvil Version: 1.8.7-nightly+716e795c`)

- [H16](../../decisions/H16.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.
- [H17](../../decisions/H17.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.

**Anvil · 1.8.6 · 6bad0a66** (`anvil Version: 1.8.6+6bad0a66`)

- [H16](../../decisions/H16.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.
- [H17](../../decisions/H17.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.
- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.
- [H17](../../decisions/H17.md): Inspect account-existence markers in the requested state diff. No state-diff object was returned; account markers cannot be assessed.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x0000000000000000000000000000000000001234', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.
- [H16](../../decisions/H16.md): The declared state-diff fixture returns the requested account changes.
- [H17](../../decisions/H17.md): Inspect account-existence markers in the requested state diff. No state-diff object was returned; account markers cannot be assessed.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x0000000000000000000000000000000000001234', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

**Erigon · 3.9.0-dev · 6955d198** (`3.9.0-dev-6955d198`)

- [H16](../../decisions/H16.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.
- [H17](../../decisions/H17.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H16](../../decisions/H16.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.
- [H17](../../decisions/H17.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.

**Geth draft fork · 1.17.11-unstable · 0f1fb2ae** (`Geth/v1.17.11-unstable-0f1fb2ae-2026-10-28/linux-amd64/go1.26.1`)

- [H16](../../decisions/H16.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.
- [H17](../../decisions/H17.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.

**Nethermind · 2.3.0-preview · fc9abf09** (`2.3.0-preview+fc9abf09`)

- [H16](../../decisions/H16.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.
- [H17](../../decisions/H17.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H16](../../decisions/H16.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.
- [H17](../../decisions/H17.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.

**Reth · 2.8.1 · 966010c9** (`Reth Version: 2.8.1+966010c9`)

- [H16](../../decisions/H16.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.
- [H17](../../decisions/H17.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.

**Reth · 2.9.0 · c9a780f4** (`Reth Version: 2.9.0+c9a780f4`)

- [H16](../../decisions/H16.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.
- [H17](../../decisions/H17.md): Assess the declared property. The signed transaction was correctly rejected before execution; execution-result properties do not apply.

</details>
