# Geth draft implementation

The experimental [Geth fork](https://github.com/banteg/go-ethereum/tree/feat/trace)
implements all nine `trace_*` methods and the `trace`, `stateDiff` and `vmTrace`
output families. It is a candidate implementation of this project's proposal,
not upstream Geth support or an independent vote for the draft.

The evaluated source is [bb5c4682](https://github.com/banteg/go-ethereum/commit/bb5c4682a5e0765159edefe779f9606db8115483),
reporting version `1.17.7-unstable`. The current matrix resolves this draft branch
head alongside the latest native client images. Its
[build lock](../evidence/2026-09-24/adopted-stances/geth.lock.json) pins the source,
toolchain, base image, binary hash and local image identity.

## Measured coverage

The [client report](../reports/clients/go-ethereum_trace.md) includes **1,559 eligible
RPC observations across fourteen corpora**: `initial`, `a`, `repeat`, `forks`,
`fork-followup`, `reorg-safe`, `precompiles`, `precompile-values`,
`callmany-isolation`, `raw-validation`, `h30`, `coverage`, `fee-policy` and `fee-compat`.
These include 1,322 `trace_*` requests and 237 setup, isolation and comparison queries.

The current checks record 5,588 semantic matches and no differences. Twelve checks
are blocked, where a refund or witness cannot be derived independently, and three
are policy observations: the raw-transaction third argument and the two simulation
`pending` requests. All 861 schema-checked results are valid. Error totals include
deliberate invalid requests and do not directly count conformance failures.

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
assertions match. The earlier Geth validation also exercised chain/filter and RPC-validation regressions uncached.

## Current contract alignment

The fork follows the [adopted source-review stances](source-review/README.md) and the
pinned draft:

- `trace_filter` bounds default to latest/latest; bounds beyond the head, reversed
  ranges and `pending` return -32602, and `earliest` is the lowest available block.
  Unknown single-block selectors return -32001 and pruned history 4444.
- Unsigned calls default omitted fees to 0 and run a zero effective price with
  BASEFEE 0, as `eth_call` does; a supplied nonce is ignored, and gas above the RPC
  cap runs at the cap. Rejections use the `eth_simulateV1` codes, and a failing
  `trace_callMany` item is named in `error.data.index`.
- Signed raw transactions are validated for execution and rejected with the
  `eth_sendRawTransaction` error groups; a gas limit above the cap is -38026.
- Call objects accept block hashes and the reserved state and block override
  parameters; schema-defined fields are honoured or rejected. An explicit null for an
  optional member is omitted (since `c8449896`), except that a null `to` creates a contract.
- Failed frames use the normative labels; REVERT frames carry `{gasUsed, output}`,
  and calls failing their precheck keep a failed frame with no result (since `07a99c67`; earlier
  captures predate it and show the previous rule). Deleted accounts report
  `storage: {}` and surviving accounts' slots use `*`.
- `vmTrace` reports operand-designated memory, including MLOAD and the full CALL
  output window, has no synthetic STOP, returns an object even when no code runs,
  and includes forwarded gas in CREATE cost.

The fork's [usage documentation](https://github.com/banteg/go-ethereum/blob/feat/trace/docs/trace.md)
and its namespace tests record each rule; see the draft PR
[#35791](https://github.com/ethereum/go-ethereum/pull/35791) for the commits.

## Precompile compatibility

Root precompile frames are retained. Nested zero-value frames are omitted;
nonzero transferred or inherited value retains the frame, on success or failure.
This follows Erigon, Reth and Nethermind in both tested release and development
builds. Besu also omits the nonzero-value frames. See [H29](../reports/decisions/H29.md)
for the proposed rule and observations. Omitted children do not consume tree-path
indexes, and caller VM return-memory effects remain available.

## Geth validation

The earlier `c36ee43e` source passed the full Geth suite, including the execution-spec
fixtures and the keeper module, plus race-enabled namespace tests. It also passed
`make all`, `go run ./build/ci.go lint`, `check_generate`, and `check_baddeps`.
Those modified Go files were formatted with `gofmt` and `goimports`. That full suite
ran in an isolated network namespace to avoid fixed test-port collisions. The current
`bb5c4682` source passed the namespace tests, `make all`, `go run ./build/ci.go lint`,
`check_baddeps`, `gofmt` and `goimports` for each stance change, and the retest here
builds it and runs the full interop matrix. It does not repeat the fork’s entire
internal test suite.

For reproduction, follow the [source-build instructions](usage.md#evaluate-the-geth-fork)
and the exact requests linked from the client report. The fork's
[usage documentation](https://github.com/banteg/go-ethereum/blob/feat/trace/docs/trace.md)
explains namespace enabling, method contracts and resource limits.
