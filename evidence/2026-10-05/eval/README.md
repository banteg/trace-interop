# Eval: published client matrix — 2026-10-05

The nineteen-corpus suite captured **20,340 RPC exchanges** against eleven immutable builds. Its [live freshness preflight](preflight.json) passed at **2026-10-05T19:51:21.922482+00:00**. [clients.lock.json](clients.lock.json) records exact image digests, image identities and Geth build provenance.

All captures ran on Fedora from clean harness commit `707d0ea107f2477a9b29391a3f4e1384466a2b47`, with output in the clone's ignored `runs/` directory. Every manifest records `source_dirty: false` ([source audit](source-audit.json)). The previous comparison is the [October 4 eval](../../2026-10-04/eval/README.md). The reports assess both matrices with the same code and ledger.

The capture was taken for **Foundry v1.8.5**, released at 18:46 UTC with ten of the twelve Anvil trace fixes: #17301–#17304, #17306, #17307 and #17309–#17312. The other two, #17305 (parent beacon root override) and #17308 (integer trace_get indices), are still open.

- **Anvil**: 1.8.5 · `51a52c59` replaces 1.8.4. The nightly `e15c2f1c` was built at 07:41 UTC from a 2026-10-04 commit. It has the four fixes merged that day (#17301, #17302, #17304, #17311) but not the six merged on 2026-10-05, and the preflight records it under `lagging_development` because it predates the 1.8.5 release.
- **Erigon** main `96188a47`, **Nethermind** master `e8955c4c` and **Reth** nightly `42fa3c56` moved without changing a verdict. Besu develop `1d62d893`, the Geth draft `e67cfd25` and every native stable release are unchanged.

Uptake is recorded in the generated [fix catalog](../../../docs/client-fixes.md).

## Measured changes

Eight verdicts improve, all for Anvil, and none regresses. The native headline stays at **94 of 132**. Anvil is reported outside it: stable rises from 14 to 19 decisions in agreement and the nightly from 14 to 17.

**Anvil 1.8.5 (5 verdicts).**
- H02 agrees: `trace_get` reads its indices as one `traceAddress` path (#17302).
- H06 agrees: an unknown block returns -32001, a filter bound past the head is rejected and an unknown replay returns null (#17306).
- H07 agrees: individual replays carry `transactionHash` (#17301).
- H13 agrees: `trace_rawTransaction` rejects a signed transaction from an account with code (#17304).
- H29 agrees: mined traces omit nested zero-value precompile calls, as simulations do (#17303). The Anvil stable note on law L07 is removed because 1.8.5 no longer violates it.

**Anvil nightly (3 verdicts).** H02, H07 and H13 agree, from the three of those fixes it carries. H06 and H29 wait for a nightly built after 2026-10-05.

**Still differing in 1.8.5.**
- H14: integer trace_get indices are accepted; open #17308 rejects them. #17307's data/input and fee-field rejections are in.
- H15: calls priced below the base fee are executed instead of rejected. #17310–#17312 fixed the fee-free, cap-only and omitted-gas environment.
- H32: the `safe` and `earliest` trace_filter bounds need Alloy's `TraceFilter` to accept tags. #17309's `pending` rejection is in.
- The mined-probes decisions (H09, H16–H20, H23, H26) stay partially assessed: without #17305 the replica mines a zero parent beacon root, so block `0x2` diverges. A checkpoint after #17305 ships will measure them.

## Report registration

[reports.lock.json](../../../reports.lock.json) selects this matrix's nineteen runs and compares them with the October 4 eval. It selects no focused capture.

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
| [probes-forks](probes-forks/summary.json) | Yes | 567 | — |
| [mined-probes](mined-probes/summary.json) | No | 979 | anvil_development, anvil_release |
| [reorg-safe](reorg-safe/summary.json) | No | 188 | erigon_development, erigon_release |
| [pruned](pruned/summary.json) | Yes | 28 | — |

**17 of 19 corpora completed.** The two incomplete scenarios keep their full evidence and remain blocked, for the same reasons as in the previous eval:
- Both Anvil builds mine a zero parent beacon root, so `mined-probes` block `0x2` differs.
- Both Erigon builds reject the reorg branch switch with "Invalid forkchoice state" (open [erigon#24032](https://github.com/erigontech/erigon/pull/24032)).

## Reproduction and validation

On Linux with Docker, from capture source commit `707d0ea1`:

```sh
uv run python scripts/run_matrix.py --reproduce-lock evidence/2026-10-05/eval/clients.lock.json --output runs/reproduction
```

If the local Geth image is missing, rebuild it from its recorded clean source following [the usage guide](../../../docs/usage.md). The matrix command exits nonzero for the two retained incomplete scenarios; that does not turn captured observation placeholders into conformance verdicts.

[validation.json](validation.json) records the checks run against the selected evidence and the generated assessment. [Cleanup verification](cleanup.json) records what was removed: the task clone and its log, and 31 dangling images, including the 2026-10-04 eval's superseded development images. Tagged `trace-interop/*` source builds were kept.
