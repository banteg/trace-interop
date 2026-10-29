# Raw state default

`trace_rawTransaction` · raw-selector · [All reports](../../README.md)

**What this checks:** Return one complete JSON-RPC response; never wrap an error envelope as a successful result. Unrequested vmTrace is null. Unrequested stateDiff is null. Output remains a byte string under every trace selection. The two-argument request runs against latest: the head block post-state and environment, as trace_call at latest (H31).

| Build | Returned | Compared with draft | Evidence |
| --- | --- | --- | --- |
| [Anvil · 1.8.6 · 6bad0a66](../../clients/anvil_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-selector/manifest.json) |
| [Anvil · 1.8.7-nightly · 716e795c](../../clients/anvil_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-selector/manifest.json) |
| [Besu · 26.10.2 · d3e1aea7](../../clients/besu_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-selector/manifest.json) |
| [Besu · 26.10-develop · 7f08e68a](../../clients/besu_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree; ⚠️ result shape differs | [Response](../../../evidence/2026-10-29/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-selector/manifest.json) |
| [Erigon · 3.8.1 · cf6f1413](../../clients/erigon_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-selector/manifest.json) |
| [Erigon · 3.9.0-dev · 6955d198](../../clients/erigon_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-selector/manifest.json) |
| [Geth draft fork · 1.17.11-unstable · 0f1fb2ae](../../clients/go-ethereum_trace.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-selector/manifest.json) |
| [Nethermind · 2.2.2 · be201120](../../clients/nethermind_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-selector/manifest.json) |
| [Nethermind · 2.3.0-preview · fc9abf09](../../clients/nethermind_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-selector/manifest.json) |
| [Reth · 2.9.0 · c9a780f4](../../clients/reth_release.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-selector/manifest.json) |
| [Reth · 2.8.1 · 966010c9](../../clients/reth_development.md) | 1 call frames; nonempty output | ✅ Checked cases agree | [Response](../../../evidence/2026-10-29/eval/raw-selector/observations.json.gz) · [Build/run](../../../evidence/2026-10-29/eval/raw-selector/manifest.json) |

<details><summary>Request and assertion details</summary>

```json
{
  "id": 1,
  "jsonrpc": "2.0",
  "method": "trace_rawTransaction",
  "params": [
    "0xf87d80847735940083030d408080a643600052734a0f1452281bcec5bd90c3dce6162a5995bfe9df316020524860405260606000f38718e5bb3abd109fa0379dd8d06b2adb0b1c56d2112a5d9be3ce05b49d06ff57de79c26da3d879ea3da0020894ecc2d5844a5e7cd262bcb0190889f17d549a8b230cfa3e10f646e852cf",
    [
      "trace"
    ]
  ]
}
```

**Besu · 26.10-develop · 7f08e68a** (`besu/v26.10-develop-7f08e68/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x84e75c28348fb86acea1a93a39426d7d60f4cc46', 'gas': '0x23bec', 'init': '0x43600052734a0f1452281bcec5bd90c3dce6162a5995bfe9df316020524860405260606000f3', 'value': '0x0'}, 'result': {'address': '0x8f5f2010035e665e196b022236f98b33de7c72ca', 'code': '0x000000000000000000000000000000

**Besu · 26.10.2 · d3e1aea7** (`besu/v26.10.2/linux-x86_64/openjdk-java-25`)

- Result shape at `trace/0`: {'action': {'from': '0x84e75c28348fb86acea1a93a39426d7d60f4cc46', 'gas': '0x23bec', 'init': '0x43600052734a0f1452281bcec5bd90c3dce6162a5995bfe9df316020524860405260606000f3', 'value': '0x0'}, 'result': {'address': '0x8f5f2010035e665e196b022236f98b33de7c72ca', 'code': '0x000000000000000000000000000000

</details>
