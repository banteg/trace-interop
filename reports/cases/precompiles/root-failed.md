# Root failed

`trace_call` · precompiles · [All reports](../../README.md)

**What this checks:** Output remains a byte string under every trace selection. Retain the root precompile frame, even with zero value. A failed root precompile reports its own execution error. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. Failed frames have an error string; an exceptional halt carries result null.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/precompiles/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/precompiles/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/precompiles/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-11-09/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/precompiles/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/precompiles/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/precompiles/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/precompiles/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-11-09/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/precompiles/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/precompiles/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/precompiles/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/precompiles/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/precompiles/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x0000000000000000000000000000000000000006",
      "gas": "0x100000",
      "gasPrice": "0x3b9aca00",
      "data": "0x000000000000000000000000000000000000000000000000000000000000002a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    },
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ],
    "latest"
  ]
}
```

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A failed root precompile reports its own execution error.

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H09](../../decisions/H09.md): A failed root precompile reports its own execution error.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H09](../../decisions/H09.md): Failed frames have an error string; an exceptional halt carries result null. First at traceAddress []: error 'Out of gas', result null.
- Result shape at `trace/0`: {'action': {'callType': 'call', 'from': '0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f', 'gas': '0xfabec', 'input': '0x000000000000000000000000000000000000000000000000000000000000002a000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

</details>
