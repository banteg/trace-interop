# H17 retest: fresh client matrix — 2026-09-24

The full fourteen-corpus suite resolved all nine published builds together and
passed its live [freshness preflight](preflight.json) at **2026-09-24 12:21:08 UTC**.
[clients.lock.json](clients.lock.json) freezes that snapshot across the suite.
Nethermind development advanced from `2a3b2531` to `9d6e8b8d`; the other eight
image identities are unchanged from the [11:07 UTC matrix](../current-matrix/README.md).

Every corpus uses clean harness commit `038a11f` on Fedora and disposable Hive
chains. Manifests, original requests/responses and checksums are retained per
corpus. The [active report inventory](../../../reports.lock.json) selects this
entire snapshot, including incomplete runs. The production node was not used.
The Reth inspector patch is tested [separately](../h17-client-fix/README.md) and
is not substituted for either published Reth build.

## Tested builds

| Client | Version | Commit |
| --- | --- | --- |
| Besu | `26.8.1` | [`d97cbd61`](https://github.com/besu-eth/besu/commit/d97cbd61976a52bb109e637196fef9a8ebf2b617) |
| Besu | `26.9-develop` | [`f9572aa8`](https://github.com/besu-eth/besu/commit/f9572aa82a2dadb3dd1b218d3ca97101540faf97) |
| Erigon | `3.6.1` | [`0c4d9c91`](https://github.com/erigontech/erigon/commit/0c4d9c91dbaffd52890235f7ea395b0231738501) |
| Erigon | `3.8.0-dev` | [`e26d9bd4`](https://github.com/erigontech/erigon/commit/e26d9bd4056586e004488c31b561fb2663d46019) |
| Nethermind | `2.0.0` | [`bec830cd`](https://github.com/NethermindEth/nethermind/commit/bec830cdfbd28c3a4d6040bc967c68c49d19dc9f) |
| Nethermind | `2.1.0-unstable` | [`9d6e8b8d`](https://github.com/NethermindEth/nethermind/commit/9d6e8b8d4f8f1d3518cfbc852725d8ab35c8f027) |
| Reth | `2.6.0` | [`73a3a008`](https://github.com/paradigmxyz/reth/commit/73a3a00862a8f14f89e30da8de001456f18cfae0) |
| Reth | `2.5.2` | [`58a51b3e`](https://github.com/paradigmxyz/reth/commit/58a51b3ee3f6714ded9207b244a273c8afb592fd) |
| Geth draft fork | `1.17.7-unstable` | [`fa8ecb92`](https://github.com/banteg/go-ethereum/commit/fa8ecb9242dda61858c44cf43c70d00548fbd7cd) |

## Capture completeness

The suite retained **11,346 RPC responses**; **13 of 14** corpora completed.
[Matrix summary](matrix.json) and per-corpus logs retain all results.

| Corpus | Complete | Responses | Builds failing setup controls |
| --- | --- | --- | --- |
| [initial](initial/summary.json) | Yes | 684 | — |
| [a](a/summary.json) | Yes | 819 | — |
| [repeat](repeat/summary.json) | Yes | 396 | — |
| [forks](forks/summary.json) | Yes | 828 | — |
| [fork-followup](fork-followup/summary.json) | Yes | 216 | — |
| [precompiles](precompiles/summary.json) | Yes | 171 | — |
| [precompile-values](precompile-values/summary.json) | Yes | 135 | — |
| [raw-validation](raw-validation/summary.json) | Yes | 639 | — |
| [coverage](coverage/summary.json) | Yes | 216 | — |
| [fee-policy](fee-policy/summary.json) | Yes | 6,804 | — |
| [callmany-isolation](callmany-isolation/summary.json) | Yes | 90 | — |
| [h30](h30/summary.json) | Yes | 171 | — |
| [reorg-safe](reorg-safe/summary.json) | No | 147 | erigon_development, reth_release |
| [pruned](pruned/summary.json) | Yes | 30 | — |

The reorg capture is missing 15 exchanges. Erigon development and Reth release
failed its setup controls; Reth development passed in this rerun, unlike the
earlier snapshot at the same revision. That is an observed run difference, not
evidence of an intervening client fix.

Incomplete setup is blocked evidence. An earlier successful capture never fills
a gap in this current snapshot. Policy mismatches in completed captures are
separate from transport/setup completeness.

## H17 findings

The independent transfer, sequential-transfer and empty-runtime CREATE probes
confirm Nethermind `9d6e8b8d` includes the fix from
[PR #13668](https://github.com/NethermindEth/nethermind/pull/13668). Fresh transfer
and fee recipients and empty-runtime contracts now have `code: {"+":"0x"}`.
The second transfer retains existing-account markers. Release `bec830cd` still
omits those code-birth markers. Both published Reth builds still misclassify fresh
transfer accounts; the proposed inspector fix passes 34 Parity integration tests.

[H17 decision](../../../reports/decisions/H17.md) includes the exact field table,
source paths, assessment corrections, blocked-case reasons and patch boundaries.
[Harness regressions](../../../tests/test_h17.py) retain historical failing and
newly fixed responses and reject marker/runtime mutations.

## Other changes from the refreshed image

Nethermind `9d6e8b8d` also contains the minimal VM stack-word encoding fix
(PR #13750), account-deletion markers (PR #13668), and preserved trace_get error
handling (PR #13676). The regenerated reports assess those captured results.
The streamed-validation error fix (PR #13666) remains pending.

## Repeat

```sh
uv run python scripts/run_matrix.py --output runs/next-matrix
```

Resolve fresh builds once and keep their immutable identities for every corpus.
Use `--reproduce-lock` only for an explicitly historical reproduction.

## Harness validation

All **148 tests passed on Fedora** after report regeneration, and inventory
verification passed for **58 frozen inputs and 32 decisions**.
[Validation manifest](validation.json) pins the assessed report and H17 test
source hashes; [test log](harness-tests.log) and [verification log](harness-verify.log)
retain the commands' output.
