# trace-interop

Reproducible evidence for a proposed Ethereum `trace_*` specification, with per-client change reports.

The draft is a proposal, not an adopted standard. Observations, execution defects and proposed API contracts are tracked separately. Agreement among clients is evidence, not a correctness oracle.

## Scope

All nine traditional methods: `trace_call`, `trace_callMany`, `trace_rawTransaction`, `trace_replayTransaction`, `trace_replayBlockTransactions`, `trace_block`, `trace_transaction`, `trace_get`, and `trace_filter`. Output families include call traces, `stateDiff`, and `vmTrace`.

Erigon, Reth, Nethermind and Besu are the initial clients. An experimental [Geth fork](https://github.com/banteg/go-ethereum/tree/feat/trace) implements the draft and is evaluated separately as `go-ethereum_trace`; it is not upstream Geth support or an independent vote for the proposal. Hive owns client startup and fixture execution. This project owns case selection, immutable observations, proposed assertions and generated impact reports.

## Start here

- [Client impact reports](reports/README.md): changes proposed for each client, with linked assertions.
- [Run a case or the matrix](docs/usage.md): pinned images, frozen chains, and exact commands.
- [Stateful scenarios](docs/scenarios.md): reorg restoration and verified pruning.
- [Review workflow](docs/review.md): distinguish API decisions from execution defects.

```sh
uv sync --locked
uv run trace-interop verify
uv run python scripts/check_schema.py
uv run python scripts/build_reports.py
```

## Decisions and evidence

The [decision ledger](decisions/README.md) tracks 29 questions with recommended behavior, rationale, evidence and remaining review work. [Comparison reports](reports/README.md) show how the draft affects each tested client build.

## Review target

Each proposed requirement should link to a minimal reproducer, the evidence behind it, and an explanation of changes required by each client. Untested claims and unresolved decisions stay explicit.

The YAML specification lives in [banteg/execution-apis, feat/trace](https://github.com/banteg/execution-apis/tree/feat/trace). This repository pins it rather than maintaining a second specification.

## Boundaries

This is not a public testnet, performance benchmark, general EVM fuzzer, or client ranking. Tests use disposable generated chains. No mainnet synchronization is required.
