# Auth set

`trace_rawTransaction` · a · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert. Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Anvil · 1.8.4-nightly · 328811cb](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Besu · 26.10-develop · 711f8142](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Erigon · 3.8.0-dev · 6da806cb](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 67f41dea](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Nethermind · 2.2.0-preview · 3370d566](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |
| [Reth · 2.7.0 · 078d0262](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-02/eval/a/observations.json.gz) · [Build/run](../../../evidence/2026-10-02/eval/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0x04f8d4870c72dd9d5e883e818501847735940083030d40941563915e194d8cfba1943570603f7606a31155088080c0f863f861870c72dd9d5e883e9400000000000000000000000000000000000010028001a0909ccd479b49d4de221beaed4e2b48ee8623d1efe6c9ba4f10653c26855123d8a0489bae47a8c46d50d536a34d9695a07668c64e89e2e17e1df04d37acb228601501a0138e133d330b2ac9573aef02e8182d29d97e5669e09079e1828d4ffe7abb73b2a018efb64c0af5c267645bd3de711a50fa787eece3679231a6843a23b3f29892c1",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

</details>
