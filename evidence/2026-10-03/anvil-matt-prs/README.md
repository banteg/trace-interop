# Anvil with mattsse's trace PRs — 2026-10-03

A functional check of the twelve open Foundry PRs that implement trace-interop decisions for Anvil,
[foundry-rs/foundry#17301](https://github.com/foundry-rs/foundry/pull/17301) through
[#17312](https://github.com/foundry-rs/foundry/pull/17312), built together and replayed on every
corpus Anvil can capture. The PRs are unmerged, so these runs are not selected by
[reports.lock.json](../../../reports.lock.json) and change no published verdict; the fix catalog keeps
tracking them as open.

## Build

Foundry `master@2620d3b6` with each PR head merged in order (#17306 is stacked on #17301), giving
merge commit `d9858812`. The merges applied without conflicts and the merged tree built, so the twelve
PRs neither conflict textually nor break each other's compilation. [clients.lock.json](clients.lock.json)
records every PR head, the binary hash and the image: a dev-profile `anvil` built with Rust 1.98.1
(`cargo build --locked --bin anvil`) and copied onto `ubuntu:26.04`, with `/bin/sh -c` as entrypoint
like the Foundry image. The lock names it `anvil_development` so the runs assess as Anvil's development
column; its version is `1.8.4-dev+d9858812`. This is a functional check, not a performance comparison.

All runs used harness commit `12ed8fe2`, which sets each block's parent beacon root through #17305's
`anvil_setNextBlockParentBeaconBlockRoot`, from a clean clone on Fedora (`source_dirty: false`).

## Capture completeness

All fourteen corpora Anvil can replay completed, and every replayed block matched its fixture header,
now including the parent beacon root.

| Corpus | Complete | Responses | Blocks replayed |
| --- | --- | --- | --- |
| [initial](initial/summary.json) | Yes | 76 | 48 |
| [a](a/summary.json) | Yes | 94 | 48 |
| [repeat](repeat/summary.json) | Yes | 44 | 48 |
| [raw-validation](raw-validation/summary.json) | Yes | 71 | 2 |
| [raw-selector](raw-selector/summary.json) | Yes | 16 | 48 |
| [coverage](coverage/summary.json) | Yes | 24 | 2 |
| [callmany-isolation](callmany-isolation/summary.json) | Yes | 10 | 48 |
| [h30](h30/summary.json) | Yes | 45 | 48 |
| [probes-prague](probes-prague/summary.json) | Yes | 120 | 2 |
| [precompiles](precompiles/summary.json) | Yes | 19 | 48 |
| [precompile-values](precompile-values/summary.json) | Yes | 15 | 48 |
| [fee-compat](fee-compat/summary.json) | Yes | 300 | 2 |
| [fee-policy](fee-policy/summary.json) | Yes | 756 | 2 |
| [mined-probes](mined-probes/summary.json) | Yes | 89 | 6 |

**mined-probes reproduces.** With #17305 every block replays exactly, so the corpus is eligible for
Anvil for the first time. As a control, the same harness replayed it into the published nightly
`328811cb` ([nightly/mined-probes](nightly/mined-probes/summary.json)): the build answers the new method
with -32601, the replica keeps the zero root (`parent_beacon_roots: false`), and block `0x2` differs in
gas used and receipts root as before, so that run is ineligible.

## Verification by PR

The merged build was assessed with `trace-interop report` over these runs and compared, check by check,
with Anvil's development column in the current reports (nightly `328811cb`). Cases are attributed to
the PR whose described change they exercise. No check regressed, no case is missing, and every
law violation Anvil had (L05 for trace_get, L07 for stored against replayed frames) is gone.

| PR | Decision | Now agreeing | Still differing |
| --- | --- | --- | --- |
| [#17301](https://github.com/foundry-rs/foundry/pull/17301) replay transactionHash | H07 | All 12 replays: `initial/replay-{tree,revert,7702,transfer}-{trace,stateDiff,vmTrace}`. H07 agrees | — |
| [#17302](https://github.com/foundry-rs/foundry/pull/17302) trace_get by trace address | H02 | `initial/get-root`, `get-zero`, `get-one`, `get-transfer-root`, `a/get-nested-parent`; law L05 holds. H02 agrees | — |
| [#17303](https://github.com/foundry-rs/foundry/pull/17303) no nested precompile frames in mined traces | H29 | `initial/block-tree`, `transaction-tree`, `filter-all`; `a/block-2`, `transaction-tree`, `filter-all`, `filter-snapshot`, `filter-two-blocks`; law L07 holds. H29 agrees | — |
| [#17304](https://github.com/foundry-rs/foundry/pull/17304) code senders in trace_rawTransaction | H13 | `raw-validation/raw-validation-code-sender-{all,trace,stateDiff,vmTrace}`. H13 agrees | — |
| [#17305](https://github.com/foundry-rs/foundry/pull/17305) next block's parent beacon root | H09, H16–H20, H23, H26, H28 | mined-probes is measured: H09 (12 cases), H16 (17), H17 (7), H18 (2), H19 (2), H20 (2) and H28 (6) agree, as the PR says, and H16 too with #17312. H23 gains 7 `filter-failed-*` and `filter-destroyed-recipient` cases, H26 the 4 `create-destroy` cases | H26 `block-4`, `replay-block-4`, `replay-selfdestruct-self`, `transaction-selfdestruct-self` and H23 `filter-self-destruct-from`, `-to`: the post-Cancun SELFDESTRUCT frame has a zero address and balance, the same check failures Reth shows (bluealloy/revm#3833), as the PR expects. H23 `a/filter-{both,from,to}-null` stay blocked by H04 list semantics, which no PR here covers |
| [#17306](https://github.com/foundry-rs/foundry/pull/17306) unknown blocks and transactions | H06 | `a/missing-block-block`, `missing-block-replay`, `missing-block-filter-next`, `initial/replay-missing`. H06 agrees | — |
| [#17307](https://github.com/foundry-rs/foundry/pull/17307) conflicting fee and input fields | H14 | `probes-prague/combo-gasprice-dynamic`, `combo-gasprice-dynamic-equal`, `combo-gasprice-maxfee`, `combo-auth-gasprice-dynamic`, `combo-blob-gasprice-capped`, `combo-blob-type3-gasprice`, `field-data-input-differ` | — (with #17308, H14 agrees) |
| [#17308](https://github.com/foundry-rs/foundry/pull/17308) integer trace_get indices | H14 | `a/get-integer-path` | — |
| [#17309](https://github.com/foundry-rs/foundry/pull/17309) pending in block trace methods | H32 | `h30/block-pending`, `h30/replay-pending` | `h30/filter-earliest`, `h30/filter-safe`: Alloy's `TraceFilter` rejects the tags, as the PR says |
| [#17310](https://github.com/foundry-rs/foundry/pull/17310) zero base and blob base fees for fee-free calls | H15 | Every zero-fee family in fee-policy and fee-compat (`legacy-zero`, `typed-zero`, `defaults-omitted`, `defaults-tip-only-zero`, `defaults-cap-only-zero`, `empty-sender-free`, `funding-free-exact`, `funding-typed-free-exact`) and fee-policy's `mixed-{legacy,typed}-{selections,free-priced-free,priced-free-priced}`; `coverage/model-environment-free`; `probes-prague/blob-fee-defaulted`, `blob-fee-zero` and their `-stateDiff` twins | See H15 below |
| [#17311](https://github.com/foundry-rs/foundry/pull/17311) cap-only calls at the base fee | H15 | `defaults-cap-only-positive` in fee-policy and fee-compat | See H15 below |
| [#17312](https://github.com/foundry-rs/foundry/pull/17312) omitted gas capped by the sender's allowance | H15, H16 | `probes-prague/field-gas-omitted-allowance`, `-eth-call`, `-many`, which were blocked; the last was H16's only remaining Anvil case | See H15 below |

**H15 still differs on one rule no PR here addresses:** a positive gas price or fee cap below the base
fee is executed instead of rejected (152 checks in `legacy-one`, `typed-one`, `legacy-below-base`,
`typed-below-base`, `typed-below-base-positive-tip` and fee-policy's
`mixed-{legacy,typed}-{invalid-then-free,free-then-invalid}`). Five priced cases also stay blocked
because their refunds are not independently derived, as before; that is an assessment limit, not a
client difference.

### Decision verdicts on the merged build

| Decision | Nightly `328811cb` | Merged build |
| --- | --- | --- |
| H02, H06, H07, H13, H14, H29 | Differs | Checked cases agree |
| H09, H16, H17, H18, H19, H20 | Partially assessed | Checked cases agree |
| H28 | Blocked | Checked cases agree |
| H23, H26 | Partially assessed | Differs (SELFDESTRUCT payload above) |
| H04, H15, H32, H33 | Differs | Differs |

Every other decision agrees on both builds.

## Reproduction

From a clean checkout at `12ed8fe2` on Linux, with the image rebuilt from the lock:

```sh
uv run python -m trace_interop run --lock evidence/2026-10-03/anvil-matt-prs/clients.lock.json \
  --corpus mined-probes --output runs/anvil-matt-prs/mined-probes
uv run trace-interop report --run evidence/2026-10-03/anvil-matt-prs/mined-probes --output runs/anvil-matt-prs-report
```

Each run keeps its manifest, the per-block replay comparison, compact observations, the exchange
and container logs under `replica/`, and checksums. The capture logs sit beside the runs.
