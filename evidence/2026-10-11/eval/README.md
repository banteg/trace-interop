# Eval: published client matrix — 2026-10-11

The nineteen-corpus suite captured **20,349 RPC exchanges** against eleven immutable builds. Its [live freshness preflight](preflight.json) passed at **2026-10-11T12:46:46.611161+00:00** with no lagging development build. [clients.lock.json](clients.lock.json) records exact image digests, image identities and Geth build provenance.

All captures ran on Fedora from harness commit `aec8278dfdd9b5928221284903788d533118418d`. Every manifest records `source_dirty: true`, because the matrix wrote its output inside the clone (`evidence/2026-10-11/eval/`) rather than in the ignored `runs/` directory. `git status` in the capture clone listed only that untracked folder, so the tracked source matched `aec8278d` ([source audit](source-audit.json)). The previous comparison is the [October 5 eval](../../2026-10-05/eval/README.md). The reports assess both matrices with the same code and ledger.

No stable release is new: Besu 26.9.0, Erigon 3.7.1, Nethermind 2.1.0, Reth 2.7.0 and Foundry 1.8.5 are the builds of the October 5 eval, and the Geth draft is still `e67cfd25`. Every development build moved:

- **Anvil** nightly 1.8.6 · `32624734` replaces the lagging `e15c2f1c`. It carries all twelve Anvil trace fixes (#17301–#17312), including #17305 (parent beacon root override) and #17308 (integer trace_get indices), plus figtracer's #17419, which rejects calls priced below the base fee.
- **Besu** develop `d05d8e74` includes #11365 (a transaction boundary before each trace_callMany call), #11407 (blockHash selection in trace_filter) and #11432 (trace_call and trace_callMany validation).
- **Erigon** main `1d3ebbf2` includes #24536. **Nethermind** master `204457ad` and **Reth** nightly `1a4dbbe1` carry no new tracked fix.

Uptake is recorded in the generated [fix catalog](../../../docs/client-fixes.md).

## Measured changes

Fifteen verdicts change, all on development builds: Anvil 13, Besu 2. The native headline stays at **94 of 132**; Besu develop has two fewer differences, so 19 native decisions now differ with no fix, down from 20. Anvil is reported outside the headline: the nightly rises from 17 to 28 decisions in agreement, and 1.8.5 stays at 19.

**Anvil nightly (13 verdicts).**
- H06, H14, H15 and H29 agree, from #17306, #17307 and #17308, #17419 and #17303.
- With #17305 the replica sets each block's parent beacon root, so the nightly replays the whole `mined-probes` chain for the first time. H09, H16–H20 and H28 agree there.
- H23 and H26 now differ. A post-Cancun SELFDESTRUCT to self yields a suicide record with a zero address, balance and refundAddress, because revm passes no payload to the tracer (open [bluealloy/revm#3833](https://github.com/bluealloy/revm/pull/3833)). trace_filter then misses that record by its executing account and its beneficiary. The [#17305 entry](../../../decisions/fixes.json) predicted both.

**Besu develop (2 verdicts).**
- H15 moves from differs to partially assessed: #11432 removes every difference, and two trace_callMany gas witnesses stay blocked.
- H33 moves from differs to partially assessed: #11407 selects exactly the hashed block, rejects an unknown hash and a hash with bounds, and agrees in the reorg scenario. Only the mode union case stays blocked, because Besu rejects union mode without blockHash too.
- #11365 fixes the trace_callMany boundary for H16, which still differs on the block 2 replay's fee accounting and a state-diff fixture.

**Erigon, Nethermind, Reth.** The new development builds change no verdict. The H14 case-variant probe, first captured in the [focused recapture](../h14-case-variant/README.md), agrees on every build again.

## Report registration

[reports.lock.json](../../../reports.lock.json) selects this matrix's nineteen runs and compares them with the October 5 eval. It selects no focused capture; this matrix's `probes-forks` includes `filter-case-variant-member`.

## Capture completeness

| Corpus | Complete | Exchanges | Setup failures |
| --- | --- | --- | --- |
| [initial](initial/summary.json) | Yes | 836 | — |
| [a](a/summary.json) | Yes | 1,034 | — |
| [repeat](repeat/summary.json) | Yes | 484 | — |
| [forks](forks/summary.json) | Yes | 828 | — |
| [fork-followup](fork-followup/summary.json) | Yes | 216 | — |
| [precompiles](precompiles/summary.json) | Yes | 209 | — |
| [precompile-values](precompile-values/summary.json) | Yes | 165 | — |
| [raw-validation](raw-validation/summary.json) | Yes | 781 | — |
| [coverage](coverage/summary.json) | Yes | 264 | — |
| [fee-policy](fee-policy/summary.json) | Yes | 8,316 | — |
| [fee-compat](fee-compat/summary.json) | Yes | 3,300 | — |
| [callmany-isolation](callmany-isolation/summary.json) | Yes | 110 | — |
| [h30](h30/summary.json) | Yes | 495 | — |
| [raw-selector](raw-selector/summary.json) | Yes | 176 | — |
| [probes-prague](probes-prague/summary.json) | Yes | 1,364 | — |
| [probes-forks](probes-forks/summary.json) | Yes | 576 | — |
| [mined-probes](mined-probes/summary.json) | No | 979 | anvil_release |
| [reorg-safe](reorg-safe/summary.json) | No | 188 | erigon_development, erigon_release |
| [pruned](pruned/summary.json) | Yes | 28 | — |

**17 of 19 corpora completed.** The two incomplete scenarios keep their full evidence and remain blocked:
- Anvil 1.8.5 cannot set a parent beacon root, so its `mined-probes` replay differs at block `0x2` (gasUsed, receiptsRoot). The nightly, with #17305, now replays every block.
- Both Erigon builds reject the reorg branch switch with "Invalid forkchoice state" (open [erigon#24032](https://github.com/erigontech/erigon/pull/24032)).

## Reproduction and validation

On Linux with Docker, from capture source commit `aec8278d`:

```sh
uv run python scripts/run_matrix.py --reproduce-lock evidence/2026-10-11/eval/clients.lock.json --output runs/reproduction
```

If the local Geth image is missing, rebuild it from its recorded clean source following [the usage guide](../../../docs/usage.md). The matrix command exits nonzero for the two retained incomplete scenarios; that does not turn captured observation placeholders into conformance verdicts.

[validation.json](validation.json) records the checks run against the selected evidence and the generated assessment. [Cleanup verification](cleanup.json) records what was removed: the task clone and its log, and 33 dangling images, including the October 5 eval's superseded development images. Tagged `trace-interop/*` source builds were kept.
