# Raw validation create valid trace

`trace_rawTransaction` · raw-validation · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. The valid signed control executes and returns the marker or constructor ADDRESS bytes under every selection. The valid signed control reports its expected execution success or halt in a root frame. Valid creation uses the address derived from the matching signed and state nonce.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.4 · 50af4efe](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Anvil · 1.8.4-nightly · 60255eee](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Besu · 26.10-develop · 1d62d893](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Erigon · 3.8.0-dev · 5cb6c867](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · e67cfd25](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Nethermind · 2.1.0 · b3e7e84c](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Nethermind · 2.2.0-preview · 6dff813b](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |
| [Reth · 2.7.0 · 10bcf461](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-04/eval/raw-validation/observations.json.gz) · [Build/run](../../../evidence/2026-10-04/eval/raw-validation/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf8600a842da282a9830186a08001893060005260206000f38718e5bb3abd109fa0371d5f6be359abfc8aa07862de5609e2374dea339665f9fcfe54ebfeef4e5d53a00de19f45781c0c3903dca51e8da7bf4ac28cc805e9a63e27c4bf1ef1d00f951a",
    [
      "trace"
    ]
  ]
}
```

**Besu · 26.10-develop · 1d62d893** (`besu/v26.10-develop-1d62d89/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0xb71e', 'init': '0x3060005260206000f3', 'value': '0x1'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000de48310d77a4d56aa400248b0b1613508f5b73', 'gasUsed': '0x1911'},

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x7e5f4552091a69125d5dfcb7b8c2659029395bdf', 'gas': '0xb71e', 'init': '0x3060005260206000f3', 'value': '0x1'}, 'result': {'address': '0x00de48310d77a4d56aa400248b0b1613508f5b73', 'code': '0x00000000000000000000000000de48310d77a4d56aa400248b0b1613508f5b73', 'gasUsed': '0x1911'},

</details>
