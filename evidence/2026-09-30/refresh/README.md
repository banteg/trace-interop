# Refresh: published client matrix — 2026-09-30

The nineteen-corpus suite captured **19,518 RPC exchanges** against eleven immutable builds. Its [live freshness preflight](preflight.json) passed at **2026-09-29T21:59:40.336677+00:00**; no development build predates its stable release. [clients.lock.json](clients.lock.json) records exact image digests, image identities and Geth build provenance. Stable releases remain Reth 2.7.0, Erigon 3.7.0, Nethermind 2.0.0, Besu 26.9.0 and Foundry 1.8.3.

All captures ran on Fedora from clean harness commit `e5b50e4f8efebe70d85f22dd5adaf64148bb4755`, with output outside the checkout. Every manifest records `source_dirty: false`. Reports reassess the wire responses with the fee/accounting corrections in `9171832a`; capture metadata and original checksums remain unchanged. The previous comparison is the [September 29 refresh](../../2026-09-29/refresh/README.md).

The development source updates are Nethermind `f69690c5`, Erigon `85e1ca92` and Besu `3cbf077c`. The other builds retain their previous pins. This snapshot includes the eight newly captured tracked Nethermind fixes (#14037, #14039, #14040, #14045, #14046, #14048, #14049 and #14050) and Erigon fixes #24344 and #24357. Uptake and measured outcomes are recorded separately in the generated [fix catalog](../../../docs/client-fixes.md).

The new priced omitted-gas/cap probes in `probes-prague` were captured on all eleven builds. The new write-then-delete storage probe in `probes-forks` was captured on all nine Hive-capable builds; Anvil cannot reproduce that fork-transition chain.

## Measured changes

Erigon development gains agreement on H06 (missing lookups/filter bounds) and H20 (executed vmTrace steps), reaching 28 agreeing decisions. Nethermind development gains H06 and H23 (failed CREATE filtering), reaching 27. All four wrong-chain raw transaction trace-type variants now pass Nethermind #14048's check.

The new funded omitted-gas probe confirms the existing Reth defect: both stable and development agree with their own eth_call output but use a 100M default above the explicit 50M RPC cap. The allowance-priced family is admission-rejected by several clients, so gas defaulting and sequential state cannot be assessed there. This newly exposed setup dependency makes H16 partially assessed for Erigon development, Nethermind development and Geth; it does not show a regression in their executed state diffs. Every supported build uses empty deleted storage for the H26 write/delete probe; Nethermind stable still emits its already-known malformed deleted-account fields.

The changes page also shows H33 differences on unchanged builds. The old base matrix lacked the separate focused H33 captures selected by the old report lock, while this matrix includes the expanded cases directly. Those entries reflect comparison coverage, not newly changed client behavior.

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

**17 of 19 corpora completed.** The two incomplete scenarios retain their full evidence and remain blocked. Both Anvil builds replay mined-probes block `0x2` with different gas used and receipts root (the fixture uses a parent beacon root that this replica cannot set). Both Erigon builds reject the reorg branch switch with “Invalid forkchoice state”. These limitations also occurred in the previous matrix.

## Reproduction and validation

On Linux with Docker, from capture source commit `e5b50e4f`:

```sh
uv run python scripts/run_matrix.py --reproduce-lock evidence/2026-09-30/refresh/clients.lock.json --output runs/reproduction
```

Rebuild the recorded clean Geth source image if the local image is absent, following [the usage guide](../../../docs/usage.md). The matrix command exits nonzero for the two retained incomplete scenarios; this does not turn captured observation placeholders into conformance verdicts.

[validation.json](validation.json) records checks against the selected evidence and generated assessment.
