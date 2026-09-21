# Replay revert vmtrace

`trace_replayTransaction` · initial · [All reports](../../README.md)

**What this checks:** Individual replay includes its transactionHash. Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth. trace_replayTransaction

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · Release](../../clients/besu_release.md) | Method unavailable `-32601` | Method unavailable | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Besu · Development](../../clients/besu_development.md) | Method unavailable `-32601` | Method unavailable | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Release](../../clients/erigon_release.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Erigon · Development](../../clients/erigon_development.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Geth draft fork · Draft fork](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/geth-e29edff-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/geth-e29edff-initial/manifest.json) |
| [Nethermind · Release](../../clients/nethermind_release.md) | 0 call frames; nonempty output | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Nethermind · Development](../../clients/nethermind_development.md) | 0 call frames; nonempty output | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 0 call frames; nonempty output | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 0 call frames; nonempty output | Differs; result shape differs | [Response](../../../evidence/2026-09-21/verified-initial/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_replayTransaction",
  "params": [
    "0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae",
    [
      "vmTrace"
    ]
  ]
}
```

**Besu · Development** (`besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.

**Besu · Release** (`besu/v26.8.1/linux-x86_64/openjdk-java-25`)

- [H01](../../decisions/H01.md): trace_replayTransaction Method coverage remains a profile decision.

**Nethermind · Development** (`2.1.0-unstable+a404c4f0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `/`: {'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': None, 'trace': [], 'transactionHash': '0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae', 'vmTra

**Nethermind · Release** (`1.39.3+28cbe2a0`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `/`: {'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': None, 'trace': [], 'transactionHash': '0x827f578f78815feb24e5d992addb5d6d184958aad72d02c213271f4b4ac780ae', 'vmTra

**Reth · Development** (`Reth Version: 2.5.2+03cb186c`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash.
- Result shape at `/`: {'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': None, 'trace': [], 'vmTrace': {'code': '0x6000356142ff54501515603b577f4e487b71000000000000000000000000000000000000

**Reth · Release** (`Reth Version: 2.6.0+73a3a008`)

- [H07](../../decisions/H07.md): Individual replay includes its transactionHash.
- Result shape at `/`: {'output': '0x08c379a00000000000000000000000000000000000000000000000000000000000000020000000000000000000000000000000000000000000000000000000000000000a75736572206572726f72', 'stateDiff': None, 'trace': [], 'vmTrace': {'code': '0x6000356142ff54501515603b577f4e487b71000000000000000000000000000000000000

</details>
