# Raw valid current nonce

`trace_rawTransaction` · initial · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Output remains a byte string under every trace selection. Assess this declared topic case. Stack words use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 1 call frames; output `0x` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 1 call frames; output `0x` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 1 call frames; output `0x` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 1 call frames; output `0x` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 1 call frames; output `0x` | Partially assessed | [Response](../../../evidence/2026-09-21/geth-e29edff-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-initial/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 1 call frames; output `0x` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 1 call frames; output `0x` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 1 call frames; output `0x` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 1 call frames; output `0x` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
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

**Geth draft fork · Draft fork** (`Geth/v1.17.6-unstable-e29edff5-2026-09-21/linux-amd64/go1.26.1`)

- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H16](../../decisions/H16.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.
- [H17](../../decisions/H17.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

</details>
