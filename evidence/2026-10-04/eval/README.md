# Eval: published client matrix — 2026-10-04

The nineteen-corpus suite captured **20,342 RPC exchanges** against eleven immutable builds. Its [live freshness preflight](preflight.json) passed at **2026-10-04T19:36:57.679798+00:00**. No development build predates its stable release, so `lagging_development` is empty. [clients.lock.json](clients.lock.json) records exact image digests, image identities and Geth build provenance.

All captures ran on Fedora from clean harness commit `a7443ef7cfd120cae6f6c187af966eafe1c4550c`, with output in the clone's ignored `runs/` directory. Every manifest records `source_dirty: false` ([source audit](source-audit.json)). The previous comparison is the [October 2 eval](../../2026-10-02/eval/README.md). The reports assess both matrices with the same code and ledger.

Every development build moved. The stable releases are unchanged: Besu 26.9.0, Erigon 3.7.1, Nethermind 2.1.0, Reth 2.7.0 and Foundry 1.8.4.

- **Reth** nightly `10bcf461` (committed 2026-10-03 17:06 UTC) includes #27668, which pins revm-inspectors 0.44.1 and so brings in #530 (H26), #532 (H20) and #533 (H09, H23).
- **Erigon** main `5cb6c867` includes #24435: trace_filter selects a block by `blockHash` and rejects block-hash bounds.
- **Geth draft** `e67cfd25` carries the H14 fee and type rules settled on 2026-10-03.
- **Besu** develop `1d62d893`, **Nethermind** master `6dff813b` and **Foundry** nightly `60255eee`. Foundry merged #17301, #17302, #17304 and #17311 on 2026-10-04 12:56 UTC, after this nightly was built, so none of them is measured yet.

Uptake is recorded in the generated [fix catalog](../../../docs/client-fixes.md).

## Measured changes

Five verdicts improve and one moves the other way, which is new measurement rather than a regression. The headline rises from 85 to **88 of 132** native development decisions in agreement.

**Reth development (2 verdicts).** H09 agrees: a reverted CREATE reports `{gasUsed, output}` with the listed failure labels. H20 agrees: MLOAD memory, no synthetic STOP, empty-code and precompile callees, failed prechecks and undefined opcodes now follow the vmTrace rules. Both come from revm-inspectors 0.44.1. H23 and H26 still differ on the post-Cancun SELFDESTRUCT payload, which waits on revm #3833.

**Erigon development (2 verdicts).** H32 agrees: with #24435, block-hash trace_filter bounds are rejected with -32602, completing #24345's `pending` rejection. H33 moves from differs to partially assessed: the hashed block is selected exactly, and the reorg-phase cases stay blocked because Erigon still rejects the branch switch.

**Geth draft (1 verdict).** H14 agrees with the settled fee, type and fork rules.

**Nethermind development (1 verdict).** H14 moves from agrees to differs, but no response that was measured before changed. This matrix is the first full run to include the `combo-*` and `fork-*` probes, which earlier existed only in focused recaptures. The development build fails eleven of them (2.1.0 fails thirteen, adding two malformed-JSON responses to blob calls):
- an explicit `type` picks the call's class and drops the fields it lacks: type 0 or 1 with dynamic fees runs at GASPRICE 0, and type 2 ignores an authorization list;
- an access or authorization list before its fork fails with -32603;
- a type alone fails before its fork (types 1 and 4 with -32603; type 3 requires a blob);
- dynamic fees and blob hashes run before their forks.

[nethermind#14212](https://github.com/NethermindEth/nethermind/pull/14212) fixes these.

**Anvil.** No verdict changes. The replica now starts Anvil without its default dev accounts (`--accounts 0`, [#2](https://github.com/banteg/trace-interop/pull/2)), and each replayed block records whether its hash matched the fixture's (`same_hash`). Neither Anvil build can set the parent beacon root yet ([foundry#17305](https://github.com/foundry-rs/foundry/pull/17305) is open), so every replayed block still differs from the fixture's hash, as before. A build of #17305 reproduced every `mined-probes` block hash in a trial replay.

## Report registration

[reports.lock.json](../../../reports.lock.json) selects this matrix's nineteen runs and compares them with the October 2 eval. It selects no focused capture: this matrix's `probes-prague` and `probes-forks` include the cases of the [fee-combos](../../2026-10-03/fee-combos/README.md), [fork-features](../../2026-10-03/fork-features/README.md) and [blob-cap](../../2026-10-04/blob-cap/README.md) recaptures they replace.

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
| [pruned](pruned/summary.json) | Yes | 30 | — |

**17 of 19 corpora completed.** The two incomplete scenarios keep their full evidence and remain blocked, for the same reasons as in the previous eval:
- Both Anvil builds mine the zero parent beacon root, so `mined-probes` block `0x2`, which reads its own root, differs.
- Both Erigon builds reject the reorg branch switch with "Invalid forkchoice state" (open [erigon#24032](https://github.com/erigontech/erigon/pull/24032)).

## Reproduction and validation

On Linux with Docker, from capture source commit `a7443ef7`:

```sh
uv run python scripts/run_matrix.py --reproduce-lock evidence/2026-10-04/eval/clients.lock.json --output runs/reproduction
```

If the local Geth image is missing, rebuild it from its recorded clean source following [the usage guide](../../../docs/usage.md). The matrix command exits nonzero for the two retained incomplete scenarios; that does not turn captured observation placeholders into conformance verdicts.

[validation.json](validation.json) records the checks run against the selected evidence and the generated assessment. [Cleanup verification](cleanup.json) records what was removed: the task clone and its log, and 45 dangling images, including the 2026-10-02 eval's superseded development images. Tagged `trace-interop/*` source builds were kept.
