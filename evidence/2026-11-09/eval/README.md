# Eval: published client matrix — 2026-11-09

The twenty-corpus suite captured **20,499 RPC exchanges** against eleven immutable builds. Its [live freshness preflight](preflight.json) passed at **2026-11-09T13:27:57Z**. Every lock entry matched its published image, and the Geth draft matched its branch head.

All captures ran on Fedora from harness commit `09e214ab`. The matrix wrote its output under the clone's ignored `runs/` folder, so every manifest records `source_dirty: false`.

## Builds

Three stable releases are new:

- **Foundry 1.9.0** · `6056c584` replaces 1.8.6. It ships `anvil_setNextBlockParentBeaconBlockRoot` (#17305), integer trace_get index rejection (#17308), rejection of calls priced below the base fee (#17419, by figtracer) and -32001 for unknown trace blocks (#17777).
- **Besu 26.11.0** · `0e595f9e` replaces 26.10.2. It carries no new tracked fix: #11406, #11439 and #11441 merged after it was cut.
- **Reth 2.10.1** · `58ebce14` replaces 2.9.0. Its evm2 pin does not include evm2#744.

Erigon 3.8.1 and Nethermind 2.2.2 are unchanged. The Geth draft moved to `e487da1e`: the #35791 rework rebased on master, which applies the DAO fork in pre-execution (#36036), plus EIP-8024 stack effects in the trace. The development builds moved:

- **Besu** develop `3f41096a` carries trace_replayTransaction (#11406), malformed trace_filter member and foreign-chain legacy call rejection (#11439), and safe trace_filter bounds with `pending` rejected (#11441).
- **Reth** nightly `5efe80f5` takes evm2 past #744.
- **Anvil** nightly `6165f031` carries #17777.
- **Erigon** main `cf91acee` and **Nethermind** master `4079edfa` carry no new tracked fix.

Uptake is recorded in the generated [fix catalog](../../../docs/client-fixes.md), and every build's source revision in [locks/source-revisions.json](../../../locks/source-revisions.json).

## Capture completeness

All 20 corpora are complete. Foundry 1.9.0 can set a parent beacon root (#17305), so `mined-probes` now replays on the Anvil release as well as the nightly.

## Measured changes

Twenty verdicts change for two clients ([changes since the previous matrix](../../../reports/changes.md)). Across the five development builds, **133 of 165** decisions agree, up from 125. 8 more have a submitted fix, 22 differ with no fix yet, and 2 are not fully measured.

**Besu develop goes from 8 to 15 agreements.**
- trace_replayTransaction (#11406) makes H01 agree. It also lets the replay cases of H07, H08, H18 and H19 run, and all four agree.
- #11439 makes H14 agree.
- #11441 makes H32 agree.
- The 26.11.0 release has none of these and stays at 8.

**Foundry 1.9.0 goes from 18 to 28 and matches the nightly.**
- 1.8.6 could not replay mined-probes, so 1.9.0 is measured on it for the first time. As a result H09, H16 to H20 and H28 agree.
- #17777, #17308 and #17419 make H06, H14 and H15 agree.
- H23 and H26 move from partially assessed to differs, as on the nightly: revm still passes no payload for a post-Cancun SELFDESTRUCT to self (revm #3833).
- The nightly gains H06 through #17777 and agrees on 28.

**Reth's nightly CALL costs agree again, but H20 still differs.** With evm2 past #744, the replay-tree root CALL costs 71,624, as on Erigon, Nethermind, Anvil and the Geth draft. The CREATE in `call-tree-vmTrace` still costs 32,002 where they report 480,269, which evm2 #876 fixes. 2.10.1 still reports 9,396 for the root CALL. Both Reth builds agree on 25 decisions, as before.

Nethermind master and the Geth draft agree on all 33 decisions. Erigon main agrees on 32. Before Cancun, it rejects a call with an empty `blobVersionedHashes` list as an inactive blob feature instead of for the field combination (H14). It has done this since the 10-31 probe fix (`b45972d4`), which requires that rejection to name its own defect.

| Release | Agrees on | Previous release |
| --- | --- | --- |
| Erigon 3.8.1 | 29 | 29 |
| Foundry 1.9.0 | 28 | 18 |
| Nethermind 2.2.2 | 27 | 27 |
| Reth 2.10.1 | 25 | 25 |
| Besu 26.11.0 | 8 | 8 |

## Reproduction and validation

On Linux with Docker, from capture source commit `09e214ab`:

```sh
uv run python scripts/run_matrix.py --reproduce-lock evidence/2026-11-09/eval/clients.lock.json --output runs/reproduction
```

If the local Geth image is missing, rebuild it from its recorded clean source following [the usage guide](../../../docs/usage.md).

[validation.json](validation.json) records the checks run against the selected evidence and the generated assessment. [Cleanup verification](cleanup.json) records what was removed:
- the task clone and its log;
- the dangling images, including the October 29 eval's superseded images;
- build cache older than a day.

Tagged `trace-interop/*` source builds were kept.
