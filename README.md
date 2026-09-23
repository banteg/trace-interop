# trace-interop

Reproducible evidence for a proposed Ethereum `trace_*` specification, with per-client change reports.

## Why this exists

Several Ethereum clients expose the Parity `trace_*` methods, but the same request can mean different things or return different shapes. That makes tracing tools carry client-specific workarounds and leaves maintainers without a shared contract to test against.

The [execution-apis standardization discussion (#890)](https://github.com/ethereum/execution-apis/issues/890) needs a concrete proposal and a clear view of its impact on each client. This repository supplies runnable examples, a draft specification, and reports that explain **what would change, why, and where to look in the code**. Client teams can review the choices that affect them without reading the entire specification first.

The draft is a proposal for review. The reports keep observed behavior separate from recommended changes.

Join the [trace working group on Telegram](https://t.me/+2jfwc-YvwkliMzIy) to discuss the proposal and coordinate client work.

## Scope

All nine traditional methods: `trace_call`, `trace_callMany`, `trace_rawTransaction`, `trace_replayTransaction`, `trace_replayBlockTransactions`, `trace_block`, `trace_transaction`, `trace_get`, and `trace_filter`. Output families include call traces, `stateDiff`, and `vmTrace`.

Erigon, Reth, Nethermind and Besu are the initial clients. An experimental [Geth fork](https://github.com/banteg/go-ethereum/tree/feat/trace) implements the draft and is evaluated separately as `go-ethereum_trace`; it is not upstream Geth support or an independent vote for the proposal.

## Start here

- [Draft specification PR #895](https://github.com/ethereum/execution-apis/pull/895): review the proposed requirements and unresolved compatibility choices.
- [Client impact reports](reports/README.md): observed differences, proposed changes, and links to client source code.
- [Related pull requests](docs/client-fixes.md): open and merged client, specification and test-suite changes.
- [Upstream acceptance](docs/upstream-acceptance.md): documented requirements and lessons from recent reviews.
- [Geth draft implementation](docs/geth.md): evaluated fork, coverage and build reproduction.
- [Run a case or the matrix](docs/usage.md): pinned images, frozen chains, and exact commands.
- [Stateful scenarios](docs/scenarios.md): reorg restoration and verified pruning.
- [Harness assertion audit](docs/harness-audit.md): false-positive regressions and independent fixture checks.
- [Review workflow](docs/review.md): distinguish API decisions from execution defects.

```sh
uv sync --locked
uv run trace-interop verify
uv run python scripts/check_schema.py
uv run python scripts/build_reports.py
```

## Decisions and evidence

The [decision ledger](decisions/README.md) tracks questions with recommended behavior, rationale, evidence and remaining review work. [Comparison reports](reports/README.md) show how the draft affects each tested client build.

## Review target

Each proposed requirement should link to a minimal reproducer, the evidence behind it, and an explanation of changes required by each client. Untested claims and unresolved decisions stay explicit.

The YAML specification lives in [banteg/execution-apis, feat/trace](https://github.com/banteg/execution-apis/tree/feat/trace). This repository pins it rather than maintaining a second specification.

## Boundaries

This is not a public testnet, performance benchmark, general EVM fuzzer, or client ranking. Tests use disposable generated chains. No mainnet synchronization is required.
