# Call empty types

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. An empty trace-type selection executes and preserves the fixture return bytes. Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately. Successful creation uses address, code and gasUsed. Failed frames have an error string; an exceptional halt omits result or sets it to null. A REVERT frame keeps result {gasUsed, output}; a reverted CREATE has no address or code.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.3 · cae51ad4](../../clients/anvil_release.md) | 9 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Anvil · 1.8.4-nightly · e3429853](../../clients/anvil_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Besu · 26.9.0 · ee9c64c8](../../clients/besu_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Besu · 26.9-develop · 67ce4ab1](../../clients/besu_development.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Erigon · 3.7.0 · bdc78cc4](../../clients/erigon_release.md) | RPC error `-32000` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Erigon · 3.8.0-dev · 923b4d31](../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · ec1cec0b](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | RPC error `-32603` | ⚠️ Differs | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Nethermind · 2.2.0-preview · 79173d14](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |
| [Reth · 2.7.0 · 43a93dbc](../../clients/reth_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-30/eval/initial/observations.json.gz) · [Build/run](../../../evidence/2026-09-30/eval/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0",
      "gas": "0x927c0",
      "gasPrice": "0x0",
      "data": "0x"
    },
    [],
    "0x30"
  ]
}
```

**Anvil · 1.8.3 · cae51ad4** (`anvil Version: 1.8.3+cae51ad4`)

- [H08](../../decisions/H08.md): Unrequested trace is an empty array.

**Besu · 26.9-develop · 67ce4ab1** (`besu/v26.9-develop-67ce4ab/linux-x86_64/openjdk-java-25`)

- [H11](../../decisions/H11.md): An empty trace-type selection executes and preserves the fixture return bytes. Expected 0xffee
- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.

**Besu · 26.9.0 · ee9c64c8** (`besu/v26.9.0/linux-x86_64/openjdk-java-25`)

- [H11](../../decisions/H11.md): An empty trace-type selection executes and preserves the fixture return bytes. Expected 0xffee
- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.

**Erigon · 3.7.0 · bdc78cc4** (`3.7.0-bdc78cc4`)

- [H11](../../decisions/H11.md): An empty trace-type selection executes and preserves the fixture return bytes. H15 owns this error, a base_fee validation rejection: fee cap less than block base fee: address 0x7435ed30A8b4AEb0877CEf0c6E8cFFe834eb865f, feeCap: 0 baseFee: 1677430. There is no executed result to inspect.
- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H11](../../decisions/H11.md): An empty trace-type selection executes and preserves the fixture return bytes. Expected 0xffee
- [H15](../../decisions/H15.md): Explicit zero-fee unsigned execution is accepted; fee environment and accounting are checked separately.

</details>
