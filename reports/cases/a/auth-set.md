# Auth set

`trace_rawTransaction` · a · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth. EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert. The signed authorization changes the recovered authority from its independently reconstructed code to the delegation target. The replay/raw root VM uses the frozen initcode or resolved one-hop execution code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Nethermind · 2.1.0-unstable · 2a3b2531](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/a/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/a/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
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

**Nethermind · 2.1.0-unstable · 2a3b2531** (`2.1.0-unstable+2a3b2531`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 153997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 153994}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x000000000

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x602a60005260206000f3', 'ops': [{'cost': 3, 'ex': {'mem': None, 'push': ['0x2a'], 'store': None, 'used': 153997}, 'pc': 0, 'sub': None}, {'cost': 3, 'ex': {'mem': None, 'push': ['0x00'], 'store': None, 'used': 153994}, 'pc': 2, 'sub': None}, {'cost': 6, 'ex': {'mem': {'data': '0x000000000

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H18](../../decisions/H18.md): EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.
- [H18](../../decisions/H18.md): The signed authorization changes the recovered authority from its independently reconstructed code to the delegation target. Authority 0x1563915e194d8cfba1943570603f7606a3115508; expected {'*': {'from': '0x', 'to': '0xef01000000000000000000000000000000000000001002'}}.
- [H19](../../decisions/H19.md): The replay/raw root VM uses the frozen initcode or resolved one-hop execution code. Expected source 0x602a60005260206000f3.

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H18](../../decisions/H18.md): EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.
- [H18](../../decisions/H18.md): The signed authorization changes the recovered authority from its independently reconstructed code to the delegation target. Authority 0x1563915e194d8cfba1943570603f7606a3115508; expected {'*': {'from': '0x', 'to': '0xef01000000000000000000000000000000000000001002'}}.
- [H19](../../decisions/H19.md): The replay/raw root VM uses the frozen initcode or resolved one-hop execution code. Expected source 0x602a60005260206000f3.

</details>
