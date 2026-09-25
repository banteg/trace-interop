# Auth clear

`trace_rawTransaction` · a · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Output remains a byte string under every trace selection. Stack words and storage operands use minimal hex quantities at every depth. EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert. Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Besu · 26.9-develop · accdae00](../../clients/besu_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Erigon · 3.8.0-dev · f8cfe5a7](../../clients/erigon_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 0a663f3c](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Nethermind · 2.1.0-preview · ee1f57da](../../clients/nethermind_development.md) | 1 call frames; output `0x` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |
| [Reth · 2.5.2 · 4630cc58](../../clients/reth_development.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-25/refresh/a/observations.json.gz) · [Build/run](../../../evidence/2026-09-25/refresh/a/manifest.json) |

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

**Reth · 2.5.2 · 4630cc58** (`Reth Version: 2.5.2+4630cc58`)

- [H18](../../decisions/H18.md): EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.
- [H18](../../decisions/H18.md): Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. Authority 0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a; 1 of 1 tuples valid; expected {'code': {'*': {'from': '0xef01000000000000000000000000000000000000001002', 'to': '0x'}}, 'nonce': {'*': {'from': '0x0', 'to': '0x1'}}}.
- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H18](../../decisions/H18.md): EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.
- [H18](../../decisions/H18.md): Valid authorization tuples, folded per authority in order, change the recovered authority from its independently reconstructed code and nonce; invalid tuples change nothing. Authority 0x19e7e376e7c213b7e7e7e46cc70a5dd086daff2a; 1 of 1 tuples valid; expected {'code': {'*': {'from': '0xef01000000000000000000000000000000000000001002', 'to': '0x'}}, 'nonce': {'*': {'from': '0x0', 'to': '0x1'}}}.
- [H19](../../decisions/H19.md): The replay/raw root VM is an object with the frozen initcode or resolved one-hop execution code, 0x when no code runs. Expected source 0x.

</details>
