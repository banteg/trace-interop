# Eval: published client matrix — 2026-10-21

The twenty-corpus suite captured **20,499 RPC exchanges** against eleven immutable builds. Its [live freshness preflight](preflight.json) passed at **2026-10-21T12:45:09Z** with no lagging development build: every lock entry matched its published image, and the Geth draft matched its branch head.

All captures ran on Fedora from harness commit `58e64754`. The matrix wrote its output under the clone's ignored `runs/` folder, so every manifest records `source_dirty: false`.

## Builds

Two stable releases are new:

- **Erigon 3.8.0** · `7539da15` replaces 3.7.1. It carries every Erigon trace fix merged before its branch, including the reverted-CREATE results and labels (#24355, #24356), the filter, fee, fork and pending fixes, and the safe and finalized handling (#24032). It lacks #24990 (the lone blob fee cap) and #25030 (the pinned forms), which merged after the branch.
- **Reth 2.8.0** · `05ba4812` replaces 2.7.0. The nightly is the same build. It ships revm-inspectors 0.44.1 (#27668), with the reverted-CREATE results, failure labels and vmTrace fixes.

Nethermind 2.2.0, Besu 26.10.0 and Foundry 1.8.5 are unchanged. The development builds moved:

- **Nethermind** master `e2e011c8` (2.3.0-preview) includes #14888, the forms the draft pinned for exact fixtures.
- **Erigon** main `d23467c5` includes #25030, which covers the same pins for Erigon.
- **Besu** develop `7590302e` includes the trace_filter `mode` member (#11436) and the omitted trace_callMany block (#11440).
- **Anvil** nightly `9089a6bf` and the **Geth draft** `a15b96ff` (comments and docs only since `fdbb46a5`) carry no new tracked fix.

Uptake is recorded in the generated [fix catalog](../../../docs/client-fixes.md), and every build's source revision in [locks/source-revisions.json](../../../locks/source-revisions.json).

## Capture completeness

19 of 20 corpora are complete. As before, `mined-probes` is blocked on Anvil 1.8.5, which cannot set a parent beacon root. `reorg-safe` is now complete: Erigon 3.8.0 carries #24032, so its branch switch no longer stops at "Invalid forkchoice state".

## Measured changes

Twenty-six verdicts change, and none regresses ([changes since the previous matrix](../../../reports/changes.md)). The previous matrix is assessed under the current rules, which include the forms the draft pinned on 2026-10-18. Across the five development builds, **125 of 165** decisions agree, up from 116. 7 more have a submitted fix and 27 differ with no fix yet.

**Erigon main agrees on all 33 decisions** again: #25030 adds the pinned forms (H05, H06, H21).

**Erigon 3.8.0 (15 verdicts).** H03, H08, H09, H11, H13, H15, H16, H17, H19, H20, H23, H28, H30, H32 and H33 move to agree, so the release agrees on 29 decisions. Its four differences are the forms #24990 and #25030 fix on main (H05, H06, H14, H21). The laws notes for its L09 and L10 violations are dropped, since 3.8.0 no longer violates either law.

**Nethermind master (4 verdicts).** H05, H06, H09 and H21 move to agree with #14888, so master agrees on 32 decisions. Its one difference is a noncanonical trace_filter `blockHash`, which returns -32000 where the draft requires -32001 (H33). The laws note for its L07 violation is dropped.

**Reth 2.8.0 (2 verdicts).** H09 and H20 move to agree with revm-inspectors 0.44.1, so the release agrees on 25 decisions, as the nightly did.

**Besu develop (2 verdicts).** H03 and H31 move to agree with #11436 and #11440.

## Reproduction and validation

On Linux with Docker, from capture source commit `58e64754`:

```sh
uv run python scripts/run_matrix.py --reproduce-lock evidence/2026-10-21/eval/clients.lock.json --output runs/reproduction
```

If the local Geth image is missing, rebuild it from its recorded clean source following [the usage guide](../../../docs/usage.md). The matrix command exits nonzero for the retained incomplete scenario; that does not turn captured observation placeholders into conformance verdicts.

[validation.json](validation.json) records the checks run against the selected evidence and the generated assessment. [Cleanup verification](cleanup.json) records what was removed: the task clone and its log, the dangling images, including the October 18 eval's superseded development images, and day-old build cache. Tagged `trace-interop/*` source builds were kept.
