# Call tree vmtrace priced

`trace_call` · initial · [All reports](../../README.md)

**What this checks:** Unrequested trace is an empty array. Unrequested stateDiff is null. Output remains a byte string under every trace selection. Stack words use minimal hex quantities at every depth. Unsigned execution accepts the supplied nonzero fee and returns one envelope per call; exact environment values are checked by coverage/model-environment. The replay/raw root VM uses the frozen initcode or resolved one-hop execution code. At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. Root VM bytecode equals the independently frozen execution source. Successful creation uses address, code and gasUsed. Failed frames have an error string and an explicit object or null result.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Besu · 26.8.1 · d97cbd61](../../clients/besu_release.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Besu · 26.9-develop · f9572aa8](../../clients/besu_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Erigon · 3.6.1 · 0c4d9c91](../../clients/erigon_release.md) | 9 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Erigon · 3.8.0-dev · e26d9bd4](../../clients/erigon_development.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Geth draft fork · 1.17.7-unstable · fa8ecb92](../../clients/go-ethereum_trace.md) | 0 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Nethermind · 2.0.0 · bec830cd](../../clients/nethermind_release.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Nethermind · 2.1.0-unstable · 2a3b2531](../../clients/nethermind_development.md) | 0 call frames; nonempty output | ⚠️ Differs; ⚠️ result shape differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Reth · 2.6.0 · 73a3a008](../../clients/reth_release.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |
| [Reth · 2.5.2 · 58a51b3e](../../clients/reth_development.md) | 0 call frames; nonempty output | ⚠️ Differs | [Response](../../../evidence/2026-09-24/current-matrix/initial/observations.json) · [Build/run](../../../evidence/2026-09-24/current-matrix/initial/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "data": "0x",
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "gasPrice": "0x77359400",
      "to": "0x9dcd17433742f4c0ca53122ab541d0ba67fc27d0"
    },
    [
      "vmTrace"
    ],
    "0x30"
  ]
}
```

**Erigon · 3.6.1 · 0c4d9c91** (`3.6.1-0c4d9c91`)

- [H08](../../decisions/H08.md): Unrequested trace is an empty array.

**Nethermind · 2.1.0-unstable · 2a3b2531** (`2.1.0-unstable+2a3b2531`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261

**Nethermind · 2.0.0 · bec830cd** (`2.0.0+bec830cd`)

- [H21](../../decisions/H21.md): Stack words use minimal hex quantities at every depth.
- Result shape at `vmTrace`: {'code': '0x7fff010000000000000000000000000000000000000000000000000000000000006000526020610100600260006001739dcd17433742f4c0ca53122ab541d0ba67fc27d161ea60f150600160005260006000602060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d361ea60f1506000600060006000739dcd17433742f4c0ca53122ab541d0ba67fc27d261

**Reth · 2.5.2 · 58a51b3e** (`Reth Version: 2.5.2+58a51b3e`)

- [H20](../../decisions/H20.md): At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. operation 2 post-step gas does not deduct this operation cost; operation 3 post-step gas does not deduct this operation cost; subtrace 10: operation 1 post-step gas does not deduct this operation cost; subtrace 10: operation 4 post-step gas does not deduct this operation cost

**Reth · 2.6.0 · 73a3a008** (`Reth Version: 2.6.0+73a3a008`)

- [H20](../../decisions/H20.md): At every VM depth, PUSH matches bytecode, non-call gas advances after the same operation, and reads/returns do not claim memory writes; CALL/CREATE gas boundaries are excluded. operation 2 post-step gas does not deduct this operation cost; operation 3 post-step gas does not deduct this operation cost; subtrace 10: operation 1 post-step gas does not deduct this operation cost; subtrace 10: operation 4 post-step gas does not deduct this operation cost

</details>
