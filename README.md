# trace-interop

Reproducible evidence for a proposed Ethereum `trace_*` specification, with per-client change reports.

[![Decision outcomes per client development build](reports/progress.svg)](reports/README.md#progress)

Each bar is one client's development build across every decision in the ledger, regenerated with each capture. See [progress by client](reports/README.md#progress) for the counts, trend and definitions.

## Why this exists

Several Ethereum clients expose the Parity `trace_*` methods, but the same request can mean different things or return different shapes. Tracing tools carry client-specific workarounds, and maintainers have no shared contract to test against.

The [execution-apis standardization discussion (#890)](https://github.com/ethereum/execution-apis/issues/890) needs a concrete proposal and a clear view of its impact on each client. This repository supplies the draft specification, runnable cases on every client, and reports that explain **what would change, why, and where to look in the code**. Observed behavior stays separate from recommended changes, and the draft remains a proposal for review.

Join the [trace working group on Telegram](https://t.me/+2jfwc-YvwkliMzIy) to discuss the proposal and coordinate client work.

## Where to start

**Client maintainers**

1. [Your client's report](reports/README.md): each difference from the draft, with a minimal example, the proposed change and links into your source. 🛠️ marks differences already covered by a submitted fix.
2. [Decision pages](decisions/README.md): the recommendation, rationale and cross-client observations behind each proposed change.
3. [Related pull requests](docs/client-fixes.md): open and merged fixes, with the decisions each one addresses.
4. [Changes since the previous matrix](reports/changes.md): verdicts that changed for each client build since the last capture.

**Specification reviewers**

- [Draft specification PR #895](https://github.com/ethereum/execution-apis/pull/895) and its [source branch](https://github.com/banteg/execution-apis/tree/feat/trace), which this repository pins rather than duplicating.
- [Decision ledger](decisions/README.md): every open question, its policy status and per-client verdicts.
- [Source review](docs/source-review/README.md): the draft compared with Parity, current client source and the sibling `eth_*` methods; its recommendations are adopted in the ledger and draft.
- [Upstream acceptance](docs/upstream-acceptance.md): what execution-apis requires to accept the proposal, and lessons from recent reviews.
- [Geth draft implementation](docs/geth.md): an experimental fork implementing the draft, evaluated separately from the native clients.

**Contributors**

- [Reproduce and review](docs/usage.md): builds, frozen chains, captures, report generation and evidence storage.
- [Reviewing a proposed rule](docs/review.md): how to separate API decisions from execution defects and record a disagreement.

## How it works

1. **Fixtures.** Frozen generated chains ([`fixtures/chains`](fixtures/chains)) and request corpora ([`fixtures/corpora`](fixtures/corpora)) define each case, its setup controls and its independent expectations.
2. **Capture.** Hive runs the corpora against the latest release and development builds of Besu, Erigon, Nethermind and Reth, plus the Geth draft fork, after a freshness preflight. Foundry's Anvil, which has no Engine API, is captured on the same chains by [replaying them block by block](docs/usage.md#replica-captures). [Stateful scenarios](docs/scenarios.md) cover reorg restoration and pruned history.
3. **Evidence.** Each run keeps its requests, raw responses, client logs and build lock under [`evidence/`](evidence), checksummed and never rewritten.
4. **Assessment.** Responses are checked against the pinned draft schemas and against independent models of execution, gas, fees and state. [Assertion models](docs/assertion-models.md) explain what each status means and what remains unassessed. [Consistency laws](reports/laws.md) compare each client with itself across methods that project one execution, and [decision tables](reports/spec-tables.md) enumerate the draft's clauses to find cases it leaves undecided or decides twice.
5. **Reports.** [`scripts/build_reports.py`](scripts/build_reports.py) regenerates the client reports, decision pages and verdict matrix from the evidence selected by [`reports.lock.json`](reports.lock.json).

## Run it

```sh
uv sync --locked
uv run trace-interop verify
uv run python scripts/check_schema.py
uv run python scripts/build_reports.py
```

`scripts/check.sh` runs the whole CI check; see [usage](docs/usage.md#check-before-pushing) for optional prek hooks.

On Linux with Docker, capture a current comparison of the latest stable releases, development images and Geth draft head:

```sh
uv run python scripts/run_matrix.py --output runs/current-matrix
```

## Scope and boundaries

All nine traditional methods are covered: `trace_call`, `trace_callMany`, `trace_rawTransaction`, `trace_replayTransaction`, `trace_replayBlockTransactions`, `trace_block`, `trace_transaction`, `trace_get` and `trace_filter`, with the call-trace, `stateDiff` and `vmTrace` output families.

The [Geth fork](https://github.com/banteg/go-ethereum/tree/feat/trace) is a candidate implementation of the draft, reported as `go-ethereum_trace`. It is not upstream Geth support or an independent vote for the proposal.

This is not a public testnet, performance benchmark, general EVM fuzzer or client ranking. Tests use disposable generated chains, and no mainnet synchronization is required.

## Documentation index

**Methodology:** [reproduce and review](docs/usage.md) · [stateful scenarios](docs/scenarios.md) · [assertion models](docs/assertion-models.md) · [consistency laws and decision tables](docs/assertion-models.md#consistency-laws-and-decision-tables) · [reviewing a proposed rule](docs/review.md)

**Decision studies:** [H13 signed transaction validation](docs/h13-validation.md) · [mined transaction probes](docs/mined-probes.md) · [H15 unsigned simulation fees](docs/h15-fee-policy.md) · [Nethermind truncated validation responses](docs/nethermind-streamed-errors.md)

**Reviews and audits:** [source review](docs/source-review/README.md) · historical records: [harness assertion audit](docs/harness-audit.md) · [H17 assessment audit](docs/h17-assessment-audit.md) · [measurement and draft review corrections](docs/review-corrections.md)

**Upstream work:** [related pull requests](docs/client-fixes.md) · [upstream acceptance](docs/upstream-acceptance.md) · [Geth draft implementation](docs/geth.md)
