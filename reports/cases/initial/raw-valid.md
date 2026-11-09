# Raw valid

`trace_rawTransaction` · initial · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Record which state an explicit third selector uses. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.9.0 · 6056c584](../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Anvil · 1.9.1-nightly · 6165f031](../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Besu · 26.11.0 · 0e595f9e](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Besu · 26.11-develop · 3f41096a](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · cf91acee](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · e487da1e](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Nethermind · 2.3.0-preview · 4079edfa](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Reth · 2.10.1 · 58ebce14](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |
| [Reth · 2.10.1 · 5efe80f5](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-09/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-09/eval/initial/manifest.json) |

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
    ],
    "0x0"
  ]
}
```

**Anvil · 1.9.1-nightly · 6165f031** (`anvil Version: 1.9.1-nightly+6165f031`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Anvil · 1.9.0 · 6056c584** (`anvil Version: 1.9.0+6056c584`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Besu · 26.11-develop · 3f41096a** (`besu/v26.11-develop-3f41096/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: Invalid number of params).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Besu · 26.11.0 · 0e595f9e** (`besu/v26.11.0/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: Invalid number of params).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Erigon · 3.9.0-dev · cf91acee** (`3.9.0-dev-cf91acee`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: too many arguments, want at most 2).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Erigon · 3.8.1 · cf6f1413** (`3.8.1-cf6f1413`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: too many arguments, want at most 2).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Geth draft fork · 1.17.11-unstable · e487da1e** (`Geth/v1.17.11-unstable-e487da1e-2026-11-01/linux-amd64/go1.26.1`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: too many arguments, want at most 2).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Nethermind · 2.3.0-preview · 4079edfa** (`2.3.0-preview+4079edfa`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: too many arguments, want at most 2).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: Invalid params).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Reth · 2.10.1 · 5efe80f5** (`Reth Version: 2.10.1+5efe80f5`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Reth · 2.10.1 · 58ebce14** (`Reth Version: 2.10.1+58ebce14`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

</details>
