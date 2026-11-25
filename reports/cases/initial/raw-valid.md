# Raw valid

`trace_rawTransaction` · initial · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Record which state an explicit third selector uses. Assess the declared property.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/initial/manifest.json) |

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

**Anvil · 1.10.1-nightly · 50d75f19** (`anvil Version: 1.10.1-nightly+50d75f19`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Anvil · 1.10.0 · 083e2299** (`anvil Version: 1.10.0+083e2299`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Besu · 26.11-develop · f58f40e2** (`besu/v26.11-develop-f58f40e/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: Invalid number of params).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Besu · 26.11.2 · 09b9e94d** (`besu/v26.11.2/linux-x86_64/openjdk-java-25`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: Invalid number of params).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Erigon · 3.9.0-dev · e91aca7f** (`3.9.0-dev-e91aca7f`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: too many arguments, want at most 2).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Erigon · 3.8.2 · 8a3f3b2c** (`3.8.2-8a3f3b2c`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: too many arguments, want at most 2).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Geth draft fork · 1.17.11-unstable · edbd5f17** (`Geth/v1.17.11-unstable-edbd5f17-2026-11-18/linux-amd64/go1.26.1`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: too many arguments, want at most 2).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Nethermind · 2.4.0-preview · e2f069a6** (`2.4.0-preview+e2f069a6`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: too many arguments, want at most 2).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Nethermind · 2.2.2 · be201120** (`2.2.2+be201120`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: rejected as invalid params (-32602: Invalid params).
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Reth · 2.11.0 · 7f5e740c** (`Reth Version: 2.11.0+7f5e740c`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

**Reth · 2.11.0 · b9abbcc1** (`Reth Version: 2.11.0+b9abbcc1`)

- [H12](../../decisions/H12.md): Record which state an explicit third selector uses. Selector block 0x0 by number: honored: the block 0x0 post-state, sender nonce 0.
- [H17](../../decisions/H17.md): Assess the declared property. The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects.

</details>
