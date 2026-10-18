# Eval: published client matrix — 2026-10-18

The twenty-corpus suite captured **20,476 RPC exchanges** against eleven immutable builds. Its [live freshness preflight](preflight.json) passed at **2026-10-18T13:06:24Z** with no lagging development build: every lock entry matched its published image, and the Geth draft matched its branch head.

All captures ran on Fedora from harness commit `39e2322f`. The matrix wrote its output under the clone's ignored `runs/` folder, so every manifest records `source_dirty: false`.

## Builds

The stable releases are unchanged: Reth 2.7.0, Erigon 3.7.1, Nethermind 2.2.0, Besu 26.10.0 and Foundry 1.8.5. Every development build moved:

- **Erigon** main `1ee57924` includes #24990, which rejects a call's `maxFeePerBlobGas` without `blobVersionedHashes`.
- **Geth draft** `fdbb46a5` is rebased on upstream master and follows its call defaults (`4e1bd7a0`). It also rechecks that each replayed trace_filter range block is still canonical, replays the transactions before a traced one without tracer hooks, and reports a missing ancestor block or genesis state as unavailable history (4444).
- **Nethermind** master `159862be`, **Reth** nightly `e6679687`, **Besu** develop `abdf1419` and **Anvil** nightly `6c21ffe2` carry no new tracked fix.

Uptake is recorded in the generated [fix catalog](../../../docs/client-fixes.md), and every build's source revision in [locks/source-revisions.json](../../../locks/source-revisions.json).

## Capture completeness

18 of 20 corpora are complete. As in the previous eval, `mined-probes` is blocked on Anvil 1.8.5, whose replayed chain differs from the fixture at block 0x2, and `reorg-safe` on Erigon 3.7.1, which stops at the branch switch with "Invalid forkchoice state". Every other build answers both.

The new [`pending` corpus](../../../docs/scenarios.md#pending-block) pools one signed transfer before tracing the pending block (H32), and replaces the h30 `block-pending` and `replay-pending` cases, whose empty pending block could not show a pending environment. All nine Hive builds are eligible; Anvil is excluded, since a replica mines the transaction at once. Reth and the Geth draft trace block 49 holding the transfer, Erigon and Nethermind reject pending, and Besu traces head block 48, as latest. The [first capture](../eval-pending/README.md) with the previous eval's builds found the same.

## Measured changes

One verdict changes, and none regresses ([changes since the previous matrix](../../../reports/changes.md)). Across the five development builds, **125 of 165** decisions agree, up from 124. 9 more have a submitted fix and **22 differ with no fix yet**.

**Erigon main agrees on all 33 decisions**, the second development build to do so after Nethermind master: H14 moves from differs to agree with #24990, as the [dbaf982 capture](../erigon-dbaf982/README.md) found.

The Geth draft at `fdbb46a5` agrees on all 33 decisions, as `71db3b03` does once the pending corpus measures H32.

## Reproduction and validation

On Linux with Docker, from capture source commit `39e2322f`:

```sh
uv run python scripts/run_matrix.py --reproduce-lock evidence/2026-10-18/eval/clients.lock.json --output runs/reproduction
```

If the local Geth image is missing, rebuild it from its recorded clean source following [the usage guide](../../../docs/usage.md). The matrix command exits nonzero for the two retained incomplete scenarios; that does not turn captured observation placeholders into conformance verdicts.

[validation.json](validation.json) records the checks run against the selected evidence and the generated assessment. [Cleanup verification](cleanup.json) records what was removed: the task clone and its log, and the dangling images, including the October 17 eval's superseded development images. Tagged `trace-interop/*` source builds were kept.
