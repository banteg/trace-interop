# Pending block with a pooled transaction — 2026-10-18

The first capture of the [`pending` corpus](../../../docs/scenarios.md#pending-block), with the builds of the
[2026-10-17 eval](../../2026-10-17/eval/README.md). On the frozen chain an empty pending block traces as `[]`, which
names no block, so the h30 `block-pending` and `replay-pending` cases could not show a pending environment (H32).
This ordered scenario first sends one signed transfer from Hive's public key 0x84E75c28…, checks that it is pooled
and not mined, and then calls `trace_block` and `trace_replayBlockTransactions` at `pending`. The h30 cases are
retired, and [reports.lock.json](../../../reports.lock.json) selects this run beside the eval's.

## Build

The run uses the eval's [clients.lock.json](../../2026-10-17/eval/clients.lock.json) unchanged, with Hive commit
`43ea47be`, from a clean clone at harness commit `fee3f8b2` on Fedora (`source_dirty: false`). Both Anvil builds
are excluded: a replica mines the transaction at once, so it has no pending block to trace.

## Result

All nine builds accepted the transaction and showed it pooled; every build is eligible and the run is complete.

| Build | `trace_block` and `trace_replayBlockTransactions` at pending | H32 |
| --- | --- | --- |
| Reth 2.7.0 · 3d592ece and · ec3e7e42 | block 49 holding the transfer, under a non-canonical hash | ✅ |
| Geth draft · 71db3b03 | block 49 holding the transfer, under a non-canonical hash | ✅ |
| Erigon 3.8.0-dev · 5b452f41 | rejected, -32602 | ✅ |
| Erigon 3.7.1 · 8c1e3893 | rejected, -32000 | ✅ (-32602 recommended) |
| Nethermind 2.2.0 · 1d2aff00 and 2.2.0-preview · cd336c4c | rejected, -32602 | ✅ |
| Besu 26.10.0 · 976ca7ea and 26.10-develop · 0776d82f | head block 48 and its three canonical transactions, as latest | ⚠️ |

The Geth draft's H32 cases were blocked only by the empty pending block, so it now agrees on all 33 decisions in the
reports. Reth's two blocked H32 cases now agree as well; it still differs on H32 for its filter bounds.

## Reproduction

From a clean checkout at `fee3f8b2` on Linux:

```sh
uv run python -m trace_interop run --lock evidence/2026-10-17/eval/clients.lock.json \
  --corpus pending --output runs/pending
uv run trace-interop report --run evidence/2026-10-18/eval-pending/pending --output runs/pending-report
```

The run keeps its manifest, summary, compact observations and checksums. The capture log sits beside it.
