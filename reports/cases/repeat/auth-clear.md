# Auth clear

`trace_rawTransaction` · repeat · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth. EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert. The signed authorization changes the recovered authority from its independently reconstructed code to the delegation target. The replay/raw root VM uses the frozen initcode or resolved one-hop execution code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |
| [Nethermind · 2.1.0-unstable · 9d6e8b8d](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-24/h17-retest/repeat/observations.json) · [Build/run](../../../evidence/2026-09-24/h17-retest/repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
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

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H18](../../decisions/H18.md): EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.
- [H18](../../decisions/H18.md): The signed authorization changes the recovered authority from its independently reconstructed code to the delegation target. Authority 0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a; expected {'*': {'from': '0xef01000000000000000000000000000000000000001002', 'to': '0x'}}.
- [H19](../../decisions/H19.md): The replay/raw root VM uses the frozen initcode or resolved one-hop execution code. Expected source 0x.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H18](../../decisions/H18.md): EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.
- [H18](../../decisions/H18.md): The signed authorization changes the recovered authority from its independently reconstructed code to the delegation target. Authority 0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a; expected {'*': {'from': '0xef01000000000000000000000000000000000000001002', 'to': '0x'}}.
- [H19](../../decisions/H19.md): The replay/raw root VM uses the frozen initcode or resolved one-hop execution code. Expected source 0x.

</details>
