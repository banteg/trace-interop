# Geth draft implementation

The experimental [Geth fork](https://github.com/banteg/go-ethereum/tree/feat/trace)
implements all nine `trace_*` methods and the `trace`, `stateDiff` and `vmTrace`
output families. It is a candidate implementation of this project's proposal,
not upstream Geth support or an independent vote for the draft.

The evaluated source is [c36ee43e38](https://github.com/banteg/go-ethereum/commit/c36ee43e3827331276d045bd56d1297e4c3c9b15).
The [build lock](../locks/geth-trace.json) pins its source, toolchain, base image,
binary hash and local image identity. Rebuilding with that lock reproduced the
same binary hash.

## Measured coverage

The [client report](../reports/clients/go-ethereum_trace.md) includes 439 eligible
RPC observations across eleven corpora: `initial`, `a`, `repeat`, `forks`,
`fork-followup`, `reorg-safe`, `precompiles`, `precompile-values`,
`callmany-isolation`, `raw-validation` and `h30`. These include 304 `trace_*`
requests and 135 setup, state-isolation and comparison queries.

All 875 evaluated semantic assertions match, and all 220 schema-checked results
are valid. Another 87 declared-topic checks remain unassessed; matching evaluated
assertions does not imply complete topic coverage. The raw-transaction third
argument and three pending-tag requests are recorded as policy observations.
The 84 trace RPC errors include deliberate malformed or invalid requests, rather
than indicating 84 conformance failures.

Canonical reorg switching and restoration were verified. The tests include
nested calls, failure isolation, return-memory effects, MCOPY, signed nonce
validation, EIP-7702 authorization changes, creation, selfdestruct across Cancun,
and historical system-operation boundaries.

Passing these selected assertions is not proof of complete conformance. Geth's
unavailable-history behavior has not been verified with the pruning scenario,
which currently has a Reth-specific setup. Large-range performance and resource
exhaustion are not measured by this matrix. The fork implements bounded block
scanning for `trace_filter`, with no address index or database migration.

## Filter modes (H03/H04)

The fork accepts `intersection` (also the default) and explicit `union`,
uses OR within address lists, and leaves an omitted, null or empty side unrestricted.
Unknown modes return `-32602`. The captured cases cover both populated lists, both
one-sided modes, nullable/empty lists and unknown modes; all evaluated H03/H04
assertions match. The Geth chain/filter and RPC-validation regressions passed uncached.

## Current contract alignment

[The contract update](https://github.com/banteg/go-ethereum/commit/c36ee43e3827331276d045bd56d1297e4c3c9b15)
closes the previously measured H06, H13 and H14 differences:

- Unknown selected blocks return `-32001`; pruned transaction lookup history returns
  `4444` when a missing hash cannot establish absence. Complete lookups retain `null`.
- Signed execution-validity failures return `-32003`; malformed encoding remains
  `-32602`, and valid transactions that revert or halt return traces.
- Unknown call fields are ignored. Standard chain ID, blob context and authorization
  fields are supported, with known-field and transaction-type validation.
- `earliest` selects genesis in the trace namespace, including when the backend's
  retention boundary is later. The H30–H32 captures confirm the tested filter bounds,
  latest defaults and safe tag. Pending remains explicitly unsupported.

Real-EVM RPC tests cover unsigned blob and authorization execution, beyond the
current frozen corpora. Lookup-pruning classification is tested with an injected
index boundary; it does not replace a full pruned-node capture. The
[validation record](../evidence/2026-09-23/geth-contract-sync/README.md)
links the before/after regressions, build lock and captured runs.

## Precompile compatibility

Root precompile frames are retained. Nested zero-value frames are omitted;
nonzero transferred or inherited value retains the frame, on success or failure.
This follows Erigon, Reth and Nethermind in both tested release and development
builds. Besu also omits the nonzero-value frames. See [H29](../reports/decisions/H29.md)
for the proposed rule and observations. Omitted children do not consume tree-path
indexes, and caller VM return-memory effects remain available.

## Geth validation

The committed source passed the full Geth suite, including the execution-spec
fixtures and the keeper module, plus race-enabled namespace tests. It also passed
`make all`, `go run ./build/ci.go lint`, `check_generate`, and `check_baddeps`.
All modified Go files were formatted with `gofmt` and `goimports`. The full suite
ran in an isolated network namespace to avoid fixed test-port collisions.

For reproduction, follow the [source-build instructions](usage.md#evaluate-the-geth-fork)
and the exact requests linked from the client report. The fork's
[usage documentation](https://github.com/banteg/go-ethereum/blob/feat/trace/docs/trace.md)
explains namespace enabling, method contracts and resource limits.
