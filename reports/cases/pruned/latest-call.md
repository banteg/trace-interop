# Latest call

`trace_call` · pruned · [All reports](../../README.md)

**What this checks:** Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection.

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Reth · Release](../../clients/reth_release.md) | Setup incomplete; not assessed | Not assessed | [Response](../../../evidence/2026-09-21/verified-pruned/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-pruned/manifest.json) |
| [Reth · Release](../../clients/reth_release.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-pruned-ready/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-pruned-ready/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | Setup incomplete; not assessed | Not assessed | [Response](../../../evidence/2026-09-21/verified-pruned/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-pruned/manifest.json) |
| [Reth · Development](../../clients/reth_development.md) | 1 call frames; nonempty output | Checked cases agree | [Response](../../../evidence/2026-09-21/verified-pruned-ready/observations.json) · [Build/run](../../../evidence/2026-09-21/verified-pruned-ready/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_call",
  "params": [
    {
      "from": "0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f",
      "gas": "0x927c0",
      "to": "0x0000000000000000000000000000000000001002"
    },
    [
      "trace"
    ],
    "0x30"
  ]
}
```

</details>
