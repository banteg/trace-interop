# Field from omitted

`trace_call` · probes-prague · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Every creation names its creationMethod; a successful one uses address, code and gasUsed. An omitted from defaults to the zero address, observed by CALLER.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.5 · 51a52c59](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Anvil · 1.8.6-nightly · de005f70](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Besu · 26.10.0 · 976ca7ea](../../clients/besu_release.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Besu · 26.10-develop · 0776d82f](../../clients/besu_development.md) | 1 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Erigon · 3.7.1 · 8c1e3893](../../clients/erigon_release.md) | 1 call frames; output `0x` | ⚠️ Differs | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Erigon · 3.8.0-dev · 5b452f41](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · 71db3b03](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0 · 1d2aff00](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Nethermind · 2.2.0-preview · cd336c4c](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · 3d592ece](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |
| [Reth · 2.7.0 · ec3e7e42](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-17/eval/probes-prague/observations.json.gz) · [Build/run](../../../evidence/2026-10-17/eval/probes-prague/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "gas": "0x493e0",
      "input": "0x3360005260206000f3"
    },
    [
      "trace"
    ],
    "latest"
  ]
}
```

**Besu · 26.10-develop · 0776d82f** (`besu/v26.10-develop-0776d82/linux-x86_64/openjdk-java-25`)

- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- Result shape at `trace/0`: {'action': {'from': '0x0000000000000000000000000000000000000000', 'gas': '0x3c45e', 'init': '0x3360005260206000f3', 'value': '0x0'}, 'result': {'address': '0xbd770416a3345f91e4b34576cb804a576fa48eb1', 'code': '0x0000000000000000000000000000000000000000000000000000000000000000', 'gasUsed': '0x1911'},

**Besu · 26.10.0 · 976ca7ea** (`besu/v26.10.0/linux-x86_64/openjdk-java-25`)

- [H10](../../decisions/H10.md): Every creation names its creationMethod; a successful one uses address, code and gasUsed. traceAddress []: creationMethod null
- Result shape at `trace/0`: {'action': {'from': '0x0000000000000000000000000000000000000000', 'gas': '0x3c45e', 'init': '0x3360005260206000f3', 'value': '0x0'}, 'result': {'address': '0xbd770416a3345f91e4b34576cb804a576fa48eb1', 'code': '0x0000000000000000000000000000000000000000000000000000000000000000', 'gasUsed': '0x1911'},

**Erigon · 3.7.1 · 8c1e3893** (`3.7.1-8c1e3893`)

- [H14](../../decisions/H14.md): An omitted from defaults to the zero address, observed by CALLER. Expected ['0x0000000000000000000000000000000000000000000000000000000000000000']; got ['0x']

</details>
