# Geth draft implementation

The experimental [Geth fork](https://github.com/banteg/go-ethereum/tree/feat/trace)
implements all nine `trace_*` methods and the `trace`, `stateDiff` and `vmTrace`
output families. It is a candidate implementation of this project's proposal,
not upstream Geth support or an independent vote for the draft.

The evaluated source is [40eecf3647](https://github.com/banteg/go-ethereum/commit/40eecf3647f26546df9dbf72ce48f372df469ef2).
The [build lock](../locks/geth-trace.json) pins its source, toolchain, base image,
binary hash and local image identity. Rebuilding with that lock reproduced the
same binary hash.

## Measured coverage

The [client report](../reports/clients/go-ethereum_trace.md) includes 334 eligible
RPC observations across `initial`, `a`, `repeat`, `forks`, `fork-followup`,
`reorg-safe`, `precompiles` and `precompile-values`. Of 592 evaluated semantic assertions,
562 matched and 30 differ: proposed transaction-validation error codes (H13, 26 checks),
unknown-block error codes (H06, three) and an unknown `trace_call` field (H14, one).
All 191 schema-checked results were valid. Another 88 declared-topic checks remain
unassessed; matching evaluated assertions does not imply complete topic coverage. The extra raw-transaction block
argument is recorded separately as an extension observation. The 42 RPC errors include the
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

## Filter modes (H03/H04)

The pushed fix accepts `intersection` (also the default) and explicit `union`,
uses OR within address lists, and leaves an omitted, null or empty side unrestricted.
Unknown modes return `-32602`. The captured cases cover both populated lists, both
one-sided modes, nullable/empty lists and unknown modes; all evaluated H03/H04
assertions match. The Geth chain/filter and RPC-validation regressions were rerun
uncached on Fedora at the published commit and passed.

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
