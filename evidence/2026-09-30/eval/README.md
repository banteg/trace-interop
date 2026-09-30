# Eval: published client matrix — 2026-09-30

The nineteen-corpus suite captured **19,518 RPC exchanges** against eleven immutable builds. Its [live freshness preflight](preflight.json) passed at **2026-09-30T13:03:47.160133+00:00**; no development build predates its stable release, so `lagging_development` is empty. [clients.lock.json](clients.lock.json) records exact image digests, image identities and Geth build provenance. Stable releases remain Reth 2.7.0, Erigon 3.7.0, Nethermind 2.0.0, Besu 26.9.0 and Foundry 1.8.3.

All captures ran on Fedora from clean harness commit `573ea55a5d7d783ab1bb0522c723c700739bfbfe`, with output in the clone's ignored `runs/` directory. Every manifest records `source_dirty: false` ([source audit](source-audit.json)). The previous comparison is the [September 30 refresh](../refresh/README.md). The reports assess both matrices with the same code and ledger, including the policy revisions made since that refresh: recommended error codes, converged H14, H32 and H33 (no hash range bounds; a canonical-only `blockHash` member), the H15 blob split and the recommended H16 index.

Every development build moved: the Reth nightly to `43a93dbc` (main on 2026-09-29, after 2.7.0), Erigon to `923b4d31`, Nethermind to `79173d14`, Besu to `67ce4ab1`, the Foundry nightly to `e3429853`, and the Geth draft fork to `ec1cec0b`. The stable builds keep their previous images. Nethermind `79173d14` newly carries #14060 (reject raw transaction gas above the RPC cap), merged after the refresh; #14039, #14040, #14045, #14046, #14048, #14049 and #14050 were already in the refresh's `f69690c5`. Erigon adds no newly tracked merged fix; #24357 was already measured. revm-inspectors #533 was released in 0.44.1, but the Reth nightly does not pin that release yet. Uptake is recorded in the generated [fix catalog](../../../docs/client-fixes.md).

## Measured changes

One verdict changes and none regresses. The Geth draft fork now agrees on H33 (single-block hash selection in trace_filter). Its follow-up `ec1cec0b` answers each hash case with block 2's records alone, and the genesis hash and a page past the end with `[]`. It rejects a hash with non-null bounds and a malformed hash with -32602, and an unknown hash with -32001, also with `count: 0`. In reorg-safe, A's hash after the switch and B's after the restore return -32001 ("is not canonical"). The refresh's `e26833e3` rejected every well-formed hash as an unknown field.

Apart from their client-version strings, the other five updated development builds return byte-identical responses to the refresh. Their verdicts, and the headline of 81 of 132 native development decisions in agreement, are unchanged. Nethermind #14060 has no measured effect: no corpus sends a signed raw transaction whose gas exceeds the RPC cap. Nethermind's H13 difference (`raw-nonce-high`) remains, with #14091 submitted.

## Report registration

[reports.lock.json](../../../reports.lock.json) selects this matrix's nineteen runs and compares them with the refresh. It selects no focused capture. `h30` (with H33's `blockHash` cases), `reorg-safe` and `raw-selector` are default corpora, captured here with this matrix's builds. The focused [h33-blockhash](../../2026-09-29/h33-blockhash/README.md) and [raw-selector](../../2026-09-29/raw-selector/README.md) runs used the September 29 builds and remain retained as history only.

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
| [probes-prague](probes-prague/summary.json) | Yes | 792 | — |
| [probes-forks](probes-forks/summary.json) | Yes | 315 | — |
| [mined-probes](mined-probes/summary.json) | No | 979 | anvil_development, anvil_release |
| [reorg-safe](reorg-safe/summary.json) | No | 188 | erigon_development, erigon_release |
| [pruned](pruned/summary.json) | Yes | 30 | — |

**17 of 19 corpora completed.** The two incomplete scenarios retain their full evidence and remain blocked, for the same reasons as in the refresh. Both Anvil builds replay mined-probes block `0x2` with different gas used and receipts root (the fixture uses a parent beacon root that this replica cannot set). Both Erigon builds reject the reorg branch switch with “Invalid forkchoice state” (open [erigon#24032](https://github.com/erigontech/erigon/pull/24032)).

## Reproduction and validation

On Linux with Docker, from capture source commit `573ea55a`:

```sh
uv run python scripts/run_matrix.py --reproduce-lock evidence/2026-09-30/eval/clients.lock.json --output runs/reproduction
```

Rebuild the recorded clean Geth source image if the local image is absent, following [the usage guide](../../../docs/usage.md). The matrix command exits nonzero for the two retained incomplete scenarios; this does not turn captured observation placeholders into conformance verdicts.

[validation.json](validation.json) records checks against the selected evidence and generated assessment.

[Cleanup verification](cleanup.json): removed the task clone and its logs, the development adapter and simulator tags this run built, and the five superseded development images whose tags this run's pulls moved. The runner had already removed the replaced Hive adapter images. No test containers or anonymous volumes remained, and unrelated Docker services were unchanged. Published base images and every `trace-interop/*` image, including the new source-built Geth image, remain available for reproduction.
