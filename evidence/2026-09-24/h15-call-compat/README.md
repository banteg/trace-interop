# H15 call compatibility: fresh client matrix — 2026-09-24

The fifteen-corpus suite resolved all nine published builds together and passed
its live [freshness preflight](preflight.json) at **2026-09-24 12:56:09 UTC**.
[clients.lock.json](clients.lock.json) freezes that snapshot across every corpus.
Nethermind development advanced from `9d6e8b8d` to `641592d2`; the other eight
image identities are unchanged from the [12:21 UTC matrix](../h17-retest/README.md).

Every capture uses harness commit `f66bc2b` on Fedora and disposable Hive chains.
Manifests retain `source_dirty: true`: the matrix created its untracked output
folder before each corpus checked git status. The [source audit](source-audit.json)
confirms that output folder is the only dirty path, tracked source equals the
commit, and the CLI hash matches every capture. No manifest was rewritten.

Original requests, responses, client logs and checksums are retained.
[reports.lock.json](../../../reports.lock.json) selects this entire snapshot,
including incomplete runs. Report assessment source hashes are recorded separately
in [assessment.json](../../../reports/assessment.json), including the final
handling of blocked paired comparisons. The production node was not used.

## Tested builds

| Client | Version | Commit |
| --- | --- | --- |
| Besu | `26.8.1` | [`d97cbd61`](https://github.com/besu-eth/besu/commit/d97cbd61976a52bb109e637196fef9a8ebf2b617) |
| Besu | `26.9-develop` | [`f9572aa8`](https://github.com/besu-eth/besu/commit/f9572aa82a2dadb3dd1b218d3ca97101540faf97) |
| Erigon | `3.6.1` | [`0c4d9c91`](https://github.com/erigontech/erigon/commit/0c4d9c91dbaffd52890235f7ea395b0231738501) |
| Erigon | `3.8.0-dev` | [`e26d9bd4`](https://github.com/erigontech/erigon/commit/e26d9bd4056586e004488c31b561fb2663d46019) |
| Nethermind | `2.0.0` | [`bec830cd`](https://github.com/NethermindEth/nethermind/commit/bec830cdfbd28c3a4d6040bc967c68c49d19dc9f) |
| Nethermind | `2.1.0-unstable` | [`641592d2`](https://github.com/NethermindEth/nethermind/commit/641592d2b96fa1e2fa8e8a0b1761582a1728bd51) |
| Reth | `2.6.0` | [`73a3a008`](https://github.com/paradigmxyz/reth/commit/73a3a00862a8f14f89e30da8de001456f18cfae0) |
| Reth | `2.5.2` | [`58a51b3e`](https://github.com/paradigmxyz/reth/commit/58a51b3ee3f6714ded9207b244a273c8afb592fd) |
| Geth draft fork | `1.17.7-unstable` | [`fa8ecb92`](https://github.com/banteg/go-ethereum/commit/fa8ecb9242dda61858c44cf43c70d00548fbd7cd) |

## Capture completeness

The suite retained **14,046 RPC responses**;
**14 of 15 corpora completed**. Both H15 corpora are complete and all nine builds
passed their independent setup controls.

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
| [fee-compat](fee-compat/summary.json) | Yes | 2,700 | — |
| [callmany-isolation](callmany-isolation/summary.json) | Yes | 90 | — |
| [h30](h30/summary.json) | Yes | 171 | — |
| [reorg-safe](reorg-safe/summary.json) | No | 147 | erigon_development, reth_development |
| [pruned](pruned/summary.json) | Yes | 30 | — |

The reorg capture is missing 15 exchanges. Erigon development and Reth development
failed setup controls; Reth release passed. The preceding snapshot instead had
Reth release blocked and development eligible at the same client revisions.
This is an observed setup/run difference, not evidence of a client fix. Failed
setup remains blocked; older successful observations never fill current gaps.

## Paired call findings

The `fee-compat` corpus contains 32 `eth_call` baselines and 256 `trace_call`
counterparts per build, plus 12 independent controls. Each pair uses an identical
call object and block selector. The seven returned words witness GASPRICE,
BASEFEE, NUMBER, TIMESTAMP, GASLIMIT, sender BALANCE after upfront payment/value,
and beneficiary BALANCE before this call's tip.

- Every tested `eth_call` uses BASEFEE 0 for explicit legacy/typed zero fees.
- Reth's trace path agrees. Nethermind and the Geth draft preserve B in trace_call.
- Besu trace_call returns internal errors for zero fees. Erigon rejects legacy
  zero and reprices typed zero to B.
- At legacy price B+1, eth_call debits the sender upfront in Besu, Erigon,
  Nethermind and Geth. Reth omits this debit in both methods. Erigon's trace_call
  also omits it and changes GASLIMIT to 2^256−1.
- Positive legacy prices below B execute in both Reth methods; positive typed
  caps below B are rejected. Other eth_call implementations reject both.
  Nethermind's trace rejection responses are truncated; Besu's are generic errors.

[H15](../../../reports/decisions/H15.md) contains the detailed runtime table,
exact probes, source links and revised recommendation. Method agreement is
separate from independent policy compliance: two methods can agree on a result
that fails the gas/balance oracle.

### Method comparison counts

One comparison per trace selection, 256 per build. Defaults stay observational
when interpretable; malformed, generic-error and unavailable comparisons are
blocked, including unresolved defaults whose responses cannot be compared.
These counts are comparisons, not independent policy passes or client votes.

| Tested build | Matches | Differs | Blocked | Policy open |
| --- | ---: | ---: | ---: | ---: |
| Besu 26.9-develop · f9572aa8 | 72 | 0 | 168 | 16 |
| Besu 26.8.1 · d97cbd61 | 72 | 0 | 168 | 16 |
| Erigon 3.8.0-dev · e26d9bd4 | 56 | 160 | 0 | 40 |
| Erigon 3.6.1 · 0c4d9c91 | 56 | 144 | 20 | 36 |
| Geth draft 1.17.7-unstable · fa8ecb92 | 176 | 40 | 0 | 40 |
| Nethermind 2.1.0-unstable · 641592d2 | 88 | 40 | 96 | 32 |
| Nethermind 2.0.0 · bec830cd | 70 | 30 | 132 | 24 |
| Reth 2.5.2 · 58a51b3e | 200 | 0 | 16 | 40 |
| Reth 2.6.0 · 73a3a008 | 200 | 0 | 16 | 40 |

Reth's 16 blocked comparisons are the two free-but-underfunded value families:
eth_call reports an EVM OutOfFunds failure, while trace_call returns an execution
failure envelope. Those are not treated as identifiable admission rejections.
Erigon release's 20 blocked pairs are empty-selection handler crashes; development
has none in this corpus. Nethermind malformed responses remain blocked regardless
of the validation exceptions visible in server logs.

## Revised independent policy

Zero-fee simulations use GASPRICE 0 and BASEFEE 0 with no gas-fee effects. Positive
prices retain base-fee/funding validation and normal simulated gas accounting.
A free → priced → free callMany sequence must observe BASEFEE 0 → B → 0 while
carrying balances forward. The 744-request-per-build `fee-policy` corpus checks
these requirements across both trace methods and all selections.

The Geth draft now differs on 128 of its 664 defined-policy fee-policy requests;
its earlier all-664 agreement was against the former BASEFEE-preserving proposal.
That change is in the recommendation/oracle, not the client. Omitted/incomplete
fee defaults, blob fees and explicit overrides remain separate policy work.
The pinned OpenRPC prose still describes the former proposal; its generated
artifact has not been rewritten independently of its source repository.

## Repeat and validation

```sh
uv run python scripts/run_matrix.py --output runs/next-matrix
uv run python scripts/build_reports.py
uv run python -m unittest discover -s tests
uv run trace-interop verify
```

Use `--reproduce-lock` only for an explicitly historical reproduction. The
[validation manifest](validation.json), [test log](harness-tests.log), and
[verification log](harness-verify.log) retain the final harness validation.

All **157 harness tests passed on Fedora**. Inventory verification passed for
**59 frozen inputs and 32 decisions**. All 2,304 trace pairs have exactly one
explicit method-comparison outcome in the final report.
