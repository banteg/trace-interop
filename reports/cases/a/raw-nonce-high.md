# Raw nonce high

`trace_rawTransaction` · a · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | RPC error `-32003` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Besu · 26.9-develop · 3cbf077c](../../clients/besu_development.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Erigon · 3.8.0-dev · 85e1ca92](../../clients/erigon_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | RPC error `2` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Nethermind · 2.2.0-preview · f69690c5](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | RPC error `-32000` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/refresh/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b8186847735940082520894000000000000000000000000000000000000123401808718e5bb3abd109fa07088ff5b782a62ee95e868e0cb949f05a4fa52e5dff86136e2d3f5eaa9cfb34ba053f2145a9d3b1d5f726bef1e95aa15db4ab7f50099330d2bbe31dae1e73698ce",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Besu · 26.9-develop · 3cbf077c** (`besu/v26.9-develop-3cbf077/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x0000000000000000000000000000000000001234', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'input': '0x', 'to': '0x0000000000000000000000000000000000001234', 'value': '0x1'}, 'result': {'gasUsed': '0x0', 'output': '0x'}, 'subtraces': 0, 'traceAddress': [], 'type': 'call'} is not valid under any of the gi

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Nethermind · 2.2.0-preview · f69690c5** (`2.2.0-preview+f69690c5`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H13](../../decisions/H13.md): Reject a signed transaction that fails execution validity at the selected state before EVM execution, for its own violation. Known invalid signed-transaction fixture; validation is separate from local transaction-pool policy.
- Result shape at `stateDiff`: {'0x0000000000000000000000000000000000000000': {'balance': {'*': {'from': '0x66863b', 'to': '0x262aafd8968b'}}, 'code': '=', 'nonce': '=', 'storage': {}}, '0x0000000000000000000000000000000000001234': {'balance': {'+': '0x1'}, 'code': '=', 'nonce': {'+': '0x0'}, 'storage': {}}, '0x7435ed30a8b4aeb087

</details>
