# Raw valid

`trace_rawTransaction` · initial · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Record which state an explicit third selector uses. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Anvil · 1.8.6-nightly · 9089a6bf](../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 7590302e](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Erigon · 3.8.0 · 7539da15](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · d23467c5](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.9-unstable · a15b96ff](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Nethermind · 2.3.0-preview · e2e011c8](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |
| [Reth · 2.8.0 · 05ba4812](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-21/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-21/eval/initial/manifest.json) |

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

**Anvil · 1.8.6-nightly · 9089a6bf** (`anvil Version: 1.8.6-nightly+9089a6bf`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Anvil · 1.8.5 · 51a52c59** (`anvil Version: 1.8.5+51a52c59`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Besu · 26.10-develop · 7590302e** (`besu/v26.10-develop-7590302/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: Invalid number of params).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: Invalid number of params).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Erigon · 3.9.0-dev · d23467c5** (`3.9.0-dev-d23467c5`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: too many arguments, want at most 2).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Erigon · 3.8.0 · 7539da15** (`3.8.0-7539da15`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: too many arguments, want at most 2).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Geth draft fork · 1.17.9-unstable · a15b96ff** (`Geth/v1.17.9-unstable-a15b96ff-2026-10-18/linux-amd64/go1.26.1`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: too many arguments, want at most 2).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Nethermind · 2.3.0-preview · e2e011c8** (`2.3.0-preview+e2e011c8`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: Invalid params).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Nethermind · 2.2.0 · 1d2aff00** (`2.2.0+1d2aff00`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: Invalid params).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Reth · 2.8.0 · 05ba4812** (`Reth Version: 2.8.0+05ba4812`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

</details>
