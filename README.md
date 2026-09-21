# trace-interop

Reproducible evidence for a proposed Ethereum `trace_*` specification, with per-client change reports.

The draft is a proposal, not an adopted standard. Observations, execution defects and proposed API contracts are tracked separately. Agreement among clients is evidence, not a correctness oracle.

## Scope

All nine traditional methods: `trace_call`, `trace_callMany`, `trace_rawTransaction`, `trace_replayTransaction`, `trace_replayBlockTransactions`, `trace_block`, `trace_transaction`, `trace_get`, and `trace_filter`. Output families include call traces, `stateDiff`, and `vmTrace`.

Erigon, Reth, Nethermind and Besu are the initial clients. Hive owns client startup and fixture execution. This project owns case selection, immutable observations, proposed assertions and generated impact reports.

## Existing evidence

The [decision ledger](decisions/README.md) imports 28 proposals from the September 15 investigation. [Historical evidence](evidence/2026-09-15/) retains exact responses and provenance. It is dated evidence, not a statement about current releases.

## Review target

Each proposed requirement should link to a minimal reproducer, the evidence behind it, and an explanation of changes required by each client. Untested claims and unresolved decisions stay explicit.

The YAML specification lives in [banteg/execution-apis, feat/trace](https://github.com/banteg/execution-apis/tree/feat/trace). This repository pins it rather than maintaining a second specification.

## Boundaries

This is not a public testnet, performance benchmark, general EVM fuzzer, or client ranking. Tests use disposable generated chains. No mainnet synchronization is required.
