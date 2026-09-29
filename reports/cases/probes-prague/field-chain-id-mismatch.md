# Field chain id mismatch

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** A chainId that does not match the chain rejects the request. A chainId for another chain is invalid regardless of state, so it is invalid params (-32602). Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Successful creation uses address, code and gasUsed.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Anvil · 1.8.4-nightly · 00989695](../../clients/anvil_development.md) | RPC error `-32003` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Besu · 26.9-develop · c197ac57](../../clients/besu_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · a2a19253](../../clients/erigon_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e26833e3](../../clients/go-ethereum_trace.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · 287f54f0](../../clients/nethermind_development.md) | RPC error `-32602` | ✅ Checked cases agree | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 60aeb532](../../clients/reth_development.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-29/refresh/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-09-29/refresh/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "chainId": "0x1",
      "from": "0x7e5f4552091a69125d5dfcb7b8c2659029395bdf",
      "gas": "0x493e0",
      "gasPrice": "0x77359400",
      "input": "0x602a60005260206000f3"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Anvil · 1.8.4-nightly · 00989695** (`anvil Version: 1.8.4-nightly+00989695`)

- [H14](../../decisions/H14.md): A chainId for another chain is invalid regardless of state, so it is invalid params (-32602). Observed rpc_error -32003: invalid chain id for signer

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H14](../../decisions/H14.md): A chainId for another chain is invalid regardless of state, so it is invalid params (-32602). Observed rpc_error -32003: invalid chain id for signer

**Besu · 26.9-develop · c197ac57** (`besu/v26.9-develop-c197ac5/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): A chainId that does not match the chain rejects the request. Observed result with output 0x000000000000000000000000000000000000000000000000000000000000002a
- [H14](../../decisions/H14.md): A chainId for another chain is invalid regardless of state, so it is invalid params (-32602). Observed result with output 0x000000000000000000000000000000000000000000000000000000000000002a
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c44e', 'init': '0x602a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x000000000000000000000000000000000000000000000000000000000000002a', 'gasUsed': '0x1912'

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H14](../../decisions/H14.md): A chainId that does not match the chain rejects the request. Observed result with output 0x000000000000000000000000000000000000000000000000000000000000002a
- [H14](../../decisions/H14.md): A chainId for another chain is invalid regardless of state, so it is invalid params (-32602). Observed result with output 0x000000000000000000000000000000000000000000000000000000000000002a
- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0x3c44e', 'init': '0x602a60005260206000f3', 'value': '0x0'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x000000000000000000000000000000000000000000000000000000000000002a', 'gasUsed': '0x1912'

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H14](../../decisions/H14.md): A chainId that does not match the chain rejects the request. Observed result with output 0x
- [H14](../../decisions/H14.md): A chainId for another chain is invalid regardless of state, so it is invalid params (-32602). Observed result with output 0x

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H14](../../decisions/H14.md): A chainId that does not match the chain rejects the request. Observed result with output 0x000000000000000000000000000000000000000000000000000000000000002a
- [H14](../../decisions/H14.md): A chainId for another chain is invalid regardless of state, so it is invalid params (-32602). Observed result with output 0x000000000000000000000000000000000000000000000000000000000000002a

**Reth · 2.7.0 · 60aeb532** (`Reth Version: 2.7.0+60aeb532`)

- [H14](../../decisions/H14.md): A chainId for another chain is invalid regardless of state, so it is invalid params (-32602). Observed rpc_error -32000: invalid chain ID

**Reth · 2.7.0 · 3d592ece** (`Reth Version: 2.7.0+3d592ece`)

- [H14](../../decisions/H14.md): A chainId for another chain is invalid regardless of state, so it is invalid params (-32602). Observed rpc_error -32000: invalid chain ID

</details>
