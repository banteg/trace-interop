# Raw valid current nonce

`trace_rawTransaction` · initial · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. The two-argument request runs against the latest post-state. State-diff account markers agree with genesis and prior signed-transaction existence, including empty fields; a modelled new account is reported. Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0xf86b8185847735940082520894000000000000000000000000000000000000123401808718e5bb3abd10a0a0a8d391fb09e2f92ffc93fe7ac7b1eb7f1e24289f707eec0f34292c1713f795ffa0554e314f2ec6166290fc977d4bd4c86a9e0cadc2366f6139bd907d893bb4e237",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H16](../../decisions/H16.md): Account balance deltas conserve transferred value, pay the exact miner tip and burn the selected block base fee, blob fee and any wei a same-transaction SELFDESTRUCT destroys. Gas=21000 (root execution gas plus independently calculated Prague intrinsic/floor cost), price=2000000000, expected tip=1998322570/gas, burn=1677430/gas, blob fee and destroyed wei=0.

</details>
