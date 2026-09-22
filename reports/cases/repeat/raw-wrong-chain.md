# Raw wrong chain

`trace_rawTransaction` · repeat · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Assess this declared topic case. Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | 1 call frames; output `0x` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | 1 call frames; output `0x` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | RPC error `-32000` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | RPC error `-32000` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | RPC error `-32602` | Partially assessed | [Response](../../../evidence/2026-09-21/geth-e29edff-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-repeat/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | Incomplete or malformed JSON | Differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | Incomplete or malformed JSON | Differs | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | RPC error `-32000` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | RPC error `-32000` | Partially assessed | [Response](../../../evidence/2026-09-21/verified-repeat/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-repeat/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf86481858477359400825208940000000000000000000000000000000000001234018026a0680e20ade3f3bfbbb3d8e2246c26a13efb3a8e886c182c159cd240b4636342b8a027a25d70c994f869fa5abe6b841ddfff0ab32944d6e9719c830ace909c024a3b",
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

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · Development** (`3.8.0-dev-c25b8e47`)

- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Erigon · Release** (`3.6.1-0c4d9c91`)

- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H25](../../decisions/H25.md): Return one complete JSON-RPC response; never wrap an error envelope as a successful result.
- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H13](../../decisions/H13.md): Assess this declared topic case. No semantic assertion evaluated this topic for the captured response.

</details>
