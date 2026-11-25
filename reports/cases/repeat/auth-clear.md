# Auth clear

`trace_rawTransaction` · repeat · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Output remains a byte string under every trace selection. Every operation names its op and has only the specified members; stack words and storage operands use minimal hex quantities at every depth. EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert. Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.10.0 · 083e2299](../../clients/anvil_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Anvil · 1.10.1-nightly · 50d75f19](../../clients/anvil_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Besu · 26.11.2 · 09b9e94d](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Besu · 26.11-develop · f58f40e2](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Erigon · 3.8.2 · 8a3f3b2c](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Erigon · 3.9.0-dev · e91aca7f](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · edbd5f17](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Nethermind · 2.4.0-preview · e2f069a6](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Reth · 2.11.0 · b9abbcc1](../../clients/reth_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |
| [Reth · 2.11.0 · 7f5e740c](../../clients/reth_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-11-25/eval/repeat/observations.json.gz) · [Build/run](../../../evidence/2026-11-25/eval/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_rawTransaction",
  "params": [
    "0x04f8d4870c72dd9d5e883e818501847735940083030d409419e7e376e7c213b7e7e7e46cc70a5dd086daff2a8080c0f863f861870c72dd9d5e883e9400000000000000000000000000000000000000008080a098be4e1c8200ba8e16556d95b598148f7ec1c6e18b76142e70007dfa5d18cf58a018a787b683426bb748bb03664d04512e382dca461e0e442f1d4c39c255f8dde501a0c0e27e354c443878b62ef28229d90a05e8414a30869bef4c3ddcf07fa205c734a0503d6a2d2293f18f5bcbb4330ac6dbeeae67c364b12a58294b8494b29782af51",
    [
      "trace",
      "stateDiff",
      "vmTrace"
    ]
  ]
}
```

</details>
