# Besu develop at 1371e0ba — 2026-10-08

A pinned capture of Besu's development build at
[`1371e0ba`](https://github.com/besu-eth/besu/commit/1371e0bab855c05e12164e3587ab1f518b64f93d), the merge of
[besu-eth/besu#11432](https://github.com/besu-eth/besu/pull/11432). That build also carries
[#11365](https://github.com/besu-eth/besu/pull/11365) and [#11407](https://github.com/besu-eth/besu/pull/11407).
The [2026-10-05 eval](../../2026-10-05/eval/README.md) measured `develop` at `1d62d893`, which predates all three. Stable
26.9.0 predates them too. These runs measure Besu's column only, so
[reports.lock.json](../../../reports.lock.json) does not select them and no published verdict changes. The next
eval's development build carries the result into the reports.

## Build

[clients.lock.json](clients.lock.json) pins `hyperledger/besu@sha256:755f6af7…`, the `develop` image published
eighteen minutes after #11432 merged. Its `org.opencontainers.image.revision` label is `1371e0ba`, which was
`main`'s head at capture time, so no source build was needed. The lock's Hive commit `43ea47be` matches the
2026-10-05 matrix. Every corpus ran with `--clients besu_development` from a clean clone at harness commit
`ec51c6c7` on Fedora (`source_dirty: false`).

## Capture completeness

All 18 corpora that capture Besu completed with no missing cases or transport errors. Each run holds exactly as
many Besu responses as the 2026-10-05 matrix run of the same corpus, 1,906 in all.

| Corpus | Responses | Corpus | Responses |
| --- | --- | --- | --- |
| [initial](initial/summary.json) | 76 | [fee-policy](fee-policy/summary.json) | 756 |
| [a](a/summary.json) | 94 | [fee-compat](fee-compat/summary.json) | 300 |
| [repeat](repeat/summary.json) | 44 | [callmany-isolation](callmany-isolation/summary.json) | 10 |
| [forks](forks/summary.json) | 92 | [h30](h30/summary.json) | 45 |
| [fork-followup](fork-followup/summary.json) | 24 | [raw-selector](raw-selector/summary.json) | 16 |
| [precompiles](precompiles/summary.json) | 19 | [probes-prague](probes-prague/summary.json) | 124 |
| [precompile-values](precompile-values/summary.json) | 15 | [probes-forks](probes-forks/summary.json) | 63 |
| [raw-validation](raw-validation/summary.json) | 71 | [mined-probes](mined-probes/summary.json) | 89 |
| [coverage](coverage/summary.json) | 24 | [reorg-safe](reorg-safe/summary.json) | 24 |

## Result

`trace-interop report` assessed these runs together, and the result was compared check by check with Besu's
development column in the current reports. Of the 6,594 checks both builds share, 211 move to agreement and none
regress. The rest are unchanged.

| PR | Decision | Now agreeing |
| --- | --- | --- |
| [#11432](https://github.com/besu-eth/besu/pull/11432) call validation | H14 | 9 shared checks: `probes-prague/combo-gasprice-dynamic`, `combo-gasprice-dynamic-equal`, `combo-gasprice-maxfee`, `combo-auth-gasprice-dynamic` and `combo-blob-gasprice` reject `gasPrice` beside dynamic fees. Four more cases agree with differently shaped checks, because their responses changed kind. `probes-forks/fork-dynamic-fees-before` and `fork-dynamic-fees-priced-before` now reject dynamic fees before London (-32602) instead of running them. `probes-prague/combo-auth-type4-gasprice` and `field-authorization` now run instead of failing with -32603 |
| [#11432](https://github.com/besu-eth/besu/pull/11432) call fees | H15 | 190 checks. 152 fee-policy checks across 19 families (`legacy-one`, `typed-one`, `*-below-base`, `funding-*-short`, `mixed-*-invalid-*`, `typed-tip-over-cap` and others) were blocked because a rejected `trace_callMany` item returned -32603. Each now names its validation error. `defaults-tip-only-positive` and `typed-zero-cap-positive-tip` (fee-policy and fee-compat), the four `blob-fee-*` probes, `field-gas-zero-many` and `field-gas-omitted-allowance-many` agree too |
| [#11365](https://github.com/besu-eth/besu/pull/11365) callMany transaction boundary | H16 | `probes-prague/many-original-value`: the second call's SSTORE is priced from its own original value |
| [#11407](https://github.com/besu-eth/besu/pull/11407) trace_filter blockHash | H33 | 11 shared checks: `h30/filter-blockhash-and-range`, `-genesis`, `-page`, `-unknown` and `-unknown-count-zero`, and the `filter-hash-a` and `filter-hash-b` cases in each `reorg-safe` phase. `h30/filter-blockhash`, `-address-from`, `-address-to` and `-null-bounds` also now trace the named block 2 instead of the head |

### Decision verdicts on 1371e0ba

| Decision | 1d62d893 (2026-10-05) | 1371e0ba |
| --- | --- | --- |
| H15 | Differs | Partially assessed, with no difference in the checked cases. The 2 blocked cases are the `many-storage-write-revert-read` bundle's fees, which have no independent gas witness |
| H33 | Fix submitted (#11407) | Partially assessed, with no difference in the checked cases. `filter-blockhash-union` is blocked because its numeric equivalent uses `mode`, which Besu rejects (H03, [#11436](https://github.com/besu-eth/besu/pull/11436)) |
| H14 | Differs | Differs on 4 checks, down from 17. `a/filter-negative-count`, `a/filter-wrong-address-type` and `probes-forks/filter-null-members` wait on [#11439](https://github.com/besu-eth/besu/pull/11439). `probes-prague/field-chain-id-mismatch` still runs a call whose `chainId` does not match the chain |
| H16 | Differs | Differs, on cases other than `trace_callMany`: `initial/raw-valid-default-block` and the fee split in `mined-probes/replay-block-2`. Twelve replay cases are blocked because `trace_replayTransaction` is missing (H01, [#11406](https://github.com/besu-eth/besu/pull/11406)) |

The headline stays at 6 agreeing decisions. H15 and H33 leave "differs" and "fix submitted", but a decision counts
as agreeing only when it is fully assessed. Four `h30/filter-blockhash*` cases gain H09 checks that differ. They
are the existing failed-frame difference ([#11347](https://github.com/besu-eth/besu/pull/11347)), now reached
because these filters return block 2 instead of the head.

## Reproduction

From a clean checkout at `ec51c6c7` on Linux:

```sh
uv run python -m trace_interop run --lock evidence/2026-10-08/besu-1371e0ba/clients.lock.json \
  --clients besu_development --corpus fee-policy --output runs/besu-1371e0ba/fee-policy
uv run trace-interop report --run evidence/2026-10-08/besu-1371e0ba/fee-policy --output runs/besu-1371e0ba-report
```

Each run keeps its manifest, summary, compact observations and checksums. The capture logs sit beside the runs.
