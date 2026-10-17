# Eval: published client matrix — 2026-10-17

The nineteen-corpus suite captured **20,435 RPC exchanges** against eleven immutable builds. Its [live freshness preflight](preflight.json) passed at **2026-10-16T23:48:59Z** with no lagging development build: every lock entry matched its published image, and the Geth draft matched its branch head.

All captures ran on Fedora from harness commit `9e7848e2`. The matrix wrote its output under the clone's ignored `runs/` folder, so every manifest records `source_dirty: false`.

## Builds

Two stable releases are new:

- **Besu 26.10.0** · `976ca7ea` replaces 26.9.0. It carries every Besu trace fix merged since 26.9.0: #11365, #11379, #11381, #11401, #11404, #11407 and #11432.
- **Nethermind 2.2.0** · `1d2aff00` replaces 2.1.0. Its release branch left master on September 25 and received cherry-picks, which include 45 of the 49 merged Nethermind fixes the tracker lists, through #14123 and #14158. It lacks #13834 and #13835, neither tied to a decision, and #14212 and #14663, which merged after the branch.

Reth 2.7.0, Erigon 3.7.1 and Foundry 1.8.5 are unchanged. Every development build moved:

- **Nethermind** master `cd336c4c` includes #14212 (a call's fields decide its type, and a field its fork lacks is rejected) and #14663 (a lone `maxFeePerBlobGas` is rejected).
- **Erigon** main `5b452f41` includes #24032 (safe and finalized hashes from a same-head forkchoice update) and #24706 (an unknown trace_filter member is rejected).
- **Besu** develop `0776d82f` includes #11379 and #11381.
- **Reth** nightly `ec3e7e42`, **Anvil** nightly `de005f70` and the **Geth draft** `71db3b03` (null trace_filter members in any case) carry no new tracked fix.

Uptake is recorded in the generated [fix catalog](../../../docs/client-fixes.md), and every build's source revision in [locks/source-revisions.json](../../../locks/source-revisions.json).

## Capture completeness

17 of 19 corpora are complete. As in the previous eval, `mined-probes` is blocked on Anvil 1.8.5, which cannot set a parent beacon root, and `reorg-safe` on Erigon 3.7.1, which fails the scenario's setup controls. Every other build answers both. `probes-forks` carries the lone blob fee cap and empty blob hash list probes added on October 12, so [reports.lock.json](../../../reports.lock.json) selects this run in place of that day's recapture.

## Measured changes

Twenty-three verdicts change, and none regresses ([changes since the previous matrix](../../../reports/changes.md)). Across the five development builds, **124 of 165** decisions agree, up from 122. 9 more have a submitted fix and **23 differ with no fix yet**, down from 10 and 24. Agreements that only development builds have fall from 45 to 30, because the new releases ship them.

**Nethermind master agrees on all 33 decisions**, the first build to do so: H14 moves from differs to agree with #14212 and #14663.

**Nethermind 2.2.0 (15 verdicts).** H02, H03, H04, H05, H06, H09, H13, H15, H20, H21, H23, H25, H29, H32 and H33 move from differs to agree: the release now agrees on 32 decisions. H14 is its one difference: before #14212 an explicit type adds requirements, fields the call's fork lacks run, and a lone blob fee cap is ignored. The laws notes for its L04 and L08 violations are dropped, since 2.2.0 no longer violates either law.

**Besu 26.10.0 (5 verdicts).** H11 and H25 move from differs to agree. H06, H15 and H33 move to partially assessed: no checked case differs, and blocked cases remain.

**Besu develop (1 verdict).** H06 moves to partially assessed with #11379 and #11381.

**Erigon main (1 verdict).** H33 moves from partially assessed to agree: with #24032 the reorg scenario's setup controls pass, as the [b5f10db capture](../../2026-10-12/erigon-b5f10db/README.md) found. Its one remaining difference is H14: a call with `maxFeePerBlobGas` and no blob hashes runs with the cap ignored.

## Reproduction and validation

On Linux with Docker, from capture source commit `9e7848e2`:

```sh
uv run python scripts/run_matrix.py --reproduce-lock evidence/2026-10-17/eval/clients.lock.json --output runs/reproduction
```

If the local Geth image is missing, rebuild it from its recorded clean source following [the usage guide](../../../docs/usage.md). The matrix command exits nonzero for the two retained incomplete scenarios; that does not turn captured observation placeholders into conformance verdicts.

[validation.json](validation.json) records the checks run against the selected evidence and the generated assessment. [Cleanup verification](cleanup.json) records what was removed: the task clone and its log, and the dangling images, including the October 11 eval's superseded development images. Tagged `trace-interop/*` source builds were kept.
