# Geth draft implementation

The experimental [Geth fork](https://github.com/banteg/go-ethereum/tree/feat/trace)
implements all nine `trace_*` methods and the `trace`, `stateDiff` and `vmTrace`
output families. It is a candidate implementation of this project's proposal,
not upstream Geth support or an independent vote for the draft.

The evaluated source is [e29edff514](https://github.com/banteg/go-ethereum/commit/e29edff514a08c38ed0b08ab67d26a0644c79548).
The [build lock](../locks/geth-trace.json) pins its source, toolchain, base image,
binary hash and local image identity. Rebuilding with that lock reproduced the
same binary hash.

## Measured coverage

The [client report](../reports/clients/go-ethereum_trace.md) includes 318 eligible
RPC observations across `initial`, `a`, `repeat`, `forks`, `fork-followup`,
`reorg-safe` and `precompiles`. All 429 applicable semantic assertions matched,
and all 174 schema-checked results were valid. The 49 RPC errors include the
corpora's deliberate malformed or invalid requests; controls and out-of-profile
queries are recorded separately from result-schema checks.

Canonical reorg switching and restoration were verified. The tests include
nested calls, failure isolation, return-memory effects, MCOPY, signed nonce
validation, EIP-7702 authorization changes, creation, selfdestruct across Cancun,
and historical system-operation boundaries.

Passing these selected assertions is not proof of complete conformance. Geth's
unavailable-history behavior has not been verified with the pruning scenario,
which currently has a Reth-specific setup. Large-range performance and resource
exhaustion are not measured by this matrix. The fork implements bounded block
scanning for `trace_filter`, with no address index or database migration.

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
