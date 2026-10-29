# Eval: published client matrix — 2026-10-29

The twenty-corpus suite captured **20,499 RPC exchanges** against eleven immutable builds. Its [live freshness preflight](preflight.json) passed at **2026-10-29T12:46:43Z**. Every lock entry matched its published image, and the Geth draft matched its branch head. The Reth nightly `966010c9` is one commit behind the 2.9.0 release, and both include evm2.

All captures ran on Fedora from harness commit `885c193a`. The matrix wrote its output under the clone's ignored `runs/` folder, so every manifest records `source_dirty: false`.

## Builds

Four stable releases are new:

- **Reth 2.9.0** · `c9a780f4` replaces 2.8.1. It replaces revm and revm-inspectors with [evm2](https://github.com/alloy-rs/evm2) across execution, RPC and inspectors ([#25002](https://github.com/paradigmxyz/reth/pull/25002)). evm2's Parity tracer carries ports of the revm-inspectors fixes.
- **Besu 26.10.2** · `d3e1aea7` replaces 26.10.1. It ships the trace_filter `mode` member (#11436) and the omitted trace_callMany block (#11440).
- **Erigon 3.8.1** · `cf6f1413` replaces 3.8.0.
- **Nethermind 2.2.2** · `be201120` replaces 2.2.1.

Foundry 1.8.6 is unchanged. The Geth draft moved to `0f1fb2ae`, the rework of go-ethereum#35791 for review: the capture is now a registered `parityTracer`, replays go through `StateAtTransaction`, and calls run under `--rpc.evmtimeout`. The development builds moved:

- **Reth** nightly `966010c9` runs evm2, like 2.9.0.
- **Erigon** main `6955d198`, **Nethermind** master `fc9abf09`, **Besu** develop `7f08e68a` and **Anvil** nightly `716e795c` carry no new tracked fix. Foundry #17777, which returns -32001 for unknown trace blocks, merged after that nightly.

Uptake is recorded in the generated [fix catalog](../../../docs/client-fixes.md), and every build's source revision in [locks/source-revisions.json](../../../locks/source-revisions.json).

## Capture completeness

19 of 20 corpora are complete. As before, `mined-probes` is blocked on the Anvil release 1.8.6, which cannot set a parent beacon root.

## Measured changes

Eight verdicts change for two clients ([changes since the previous matrix](../../../reports/changes.md)). Across the five development builds, **126 of 165** decisions agree, as before. 10 more have a submitted fix, 23 differ with no fix yet, and 6 are unmeasured.

**Reth's move to evm2 trades one decision for another.** 2.9.0 and the nightly still agree on 25 decisions:

- **H26 (account deletion across Cancun) now agrees.** evm2 reports the post-Cancun SELFDESTRUCT-to-self payload that revm skips, so Reth no longer waits on revm #3833. Foundry still runs revm and still needs it.
- **H23 (special-action address matching)** moves from differs to partially assessed. Its SELFDESTRUCT records now carry their addresses. Three filter cases stay blocked by the H04 null-list difference.
- **H20 (vmTrace) regresses.** evm2's vmTrace reports a CALL or CREATE `cost` without the gas forwarded to the child, including after a failed precheck. On the replay-tree root CALL, Reth reports cost 9,396, while Erigon, Nethermind, Anvil and the Geth draft report 71,624. Every client reports the same `ex.used`. The decision page still lists the merged revm-inspectors fixes as submitted, but 2.9.0 no longer uses revm-inspectors, so this needs an evm2 change.

**Besu 26.10.2 catches up with develop**: H03 and H31 move from differs to agree, so the release agrees on 8 decisions, like develop.

The Geth draft rework agrees on all 33 decisions, as did `a15b96ff`. Erigon main and Nethermind master still agree on all 33.

| Release | Agrees on | Previous release |
| --- | --- | --- |
| Erigon 3.8.1 | 29 | 29 |
| Nethermind 2.2.2 | 27 | 27 |
| Reth 2.9.0 | 25 | 25 |
| Foundry 1.8.6 | 18 | 18 |
| Besu 26.10.2 | 8 | 6 |

## Reproduction and validation

On Linux with Docker, from capture source commit `885c193a`:

```sh
uv run python scripts/run_matrix.py --reproduce-lock evidence/2026-10-29/eval/clients.lock.json --output runs/reproduction
```

If the local Geth image is missing, rebuild it from its recorded clean source following [the usage guide](../../../docs/usage.md). The matrix command exits nonzero for the retained incomplete scenario. That exit does not turn captured observation placeholders into conformance verdicts.

[validation.json](validation.json) records the checks run against the selected evidence and the generated assessment. [Cleanup verification](cleanup.json) records what was removed:
- the task clone and its log;
- the dangling images, including the October 23 eval's superseded images;
- build cache older than a day.

Tagged `trace-interop/*` source builds were kept.
