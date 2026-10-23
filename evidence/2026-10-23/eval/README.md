# Eval: published client matrix — 2026-10-23

The twenty-corpus suite captured **20,499 RPC exchanges** against eleven immutable builds. Its [live freshness preflight](preflight.json) passed at **2026-10-23T15:49:32Z**. Every lock entry matched its published image, and the Geth draft matched its branch head. The Reth nightly was built on October 22, before the 2.8.1 release; that release only unschedules Amsterdam on Hoodi, so the nightly still measures the newer trace code.

All captures ran on Fedora from harness commit `daa259ce`. The matrix wrote its output under the clone's ignored `runs/` folder, so every manifest records `source_dirty: false`.

## Builds

Four stable releases are new. Each only unschedules the Amsterdam fork on Hoodi, or carries no tracked fix:

- **Reth 2.8.1** · `d763342f` replaces 2.8.0.
- **Nethermind 2.2.1** · `c4f1015b` replaces 2.2.0.
- **Besu 26.10.1** · `e83703cd` replaces 26.10.0.
- **Foundry 1.8.6** · `6bad0a66` replaces 1.8.5. It still lacks #17305, #17308 and #17419.

Erigon 3.8.0 and the Geth draft `a15b96ff` are unchanged. The development builds moved:

- **Nethermind** master `7192e7f3` (2.3.0-preview) includes #15017, which returns -32001 for a noncanonical trace_filter `blockHash`.
- **Erigon** main `598ba625`, **Reth** nightly `53bf066f`, **Besu** develop `781a7e1d` and **Anvil** nightly `4e8874b2` carry no new tracked fix.

Uptake is recorded in the generated [fix catalog](../../../docs/client-fixes.md), and every build's source revision in [locks/source-revisions.json](../../../locks/source-revisions.json).

## Capture completeness

19 of 20 corpora are complete. As before, `mined-probes` is blocked on the Anvil release, now 1.8.6, which still cannot set a parent beacon root.

## Measured changes

One verdict changes, and none regresses ([changes since the previous matrix](../../../reports/changes.md)). Across the five development builds, **126 of 165** decisions agree, up from 125. 7 more have a submitted fix and 26 differ with no fix yet.

**Nethermind master agrees on all 33 decisions** again: with #15017, H33 moves from differs to agree. Erigon main still agrees on all 33 too.

The new releases return the same verdicts as the ones they replace:

| Release | Agrees on |
| --- | --- |
| Nethermind 2.2.1 | 27 |
| Reth 2.8.1 | 25 |
| Besu 26.10.1 | 6 |
| Foundry 1.8.6 | 18 |

## Reproduction and validation

On Linux with Docker, from capture source commit `daa259ce`:

```sh
uv run python scripts/run_matrix.py --reproduce-lock evidence/2026-10-23/eval/clients.lock.json --output runs/reproduction
```

If the local Geth image is missing, rebuild it from its recorded clean source following [the usage guide](../../../docs/usage.md). The matrix command exits nonzero for the retained incomplete scenario. That exit does not turn captured observation placeholders into conformance verdicts.

[validation.json](validation.json) records the checks run against the selected evidence and the generated assessment. [Cleanup verification](cleanup.json) records what was removed:
- the task clone and its log;
- the dangling images, including the October 21 eval's superseded images;
- build cache older than a day.

Tagged `trace-interop/*` source builds were kept.
