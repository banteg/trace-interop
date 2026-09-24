# Geth draft implementation

The experimental [Geth fork](https://github.com/banteg/go-ethereum/tree/feat/trace)
implements all nine `trace_*` methods and the `trace`, `stateDiff` and `vmTrace`
output families. It is a candidate implementation of this project's proposal,
not upstream Geth support or an independent vote for the draft.

The evaluated source is [fa8ecb92](https://github.com/banteg/go-ethereum/commit/fa8ecb9242dda61858c44cf43c70d00548fbd7cd),
reporting version `1.17.7-unstable`. The current matrix resolves this draft branch
head alongside the latest native client images. Its
[build lock](../evidence/2026-09-24/h15-call-compat/geth.lock.json) pins the source,
toolchain, base image, binary hash and local image identity. This was a fresh build;
the identical-binary reproduction check documented for the earlier `c36ee43e`
capture applies only to that historical build.

## Measured coverage

The [client report](../reports/clients/go-ethereum_trace.md) includes **1,559 eligible
RPC observations across fourteen corpora**: `initial`, `a`, `repeat`, `forks`,
`fork-followup`, `reorg-safe`, `precompiles`, `precompile-values`,
`callmany-isolation`, `raw-validation`, `h30`, `coverage`, `fee-policy` and `fee-compat`.
These include 1,322 `trace_*` requests and 237 setup, isolation and comparison queries.

The current checks record 4,918 semantic matches and 229 differences. Of those
differences, 225 are H15 checks, two are the zero-fee environment witness as seen
through output/VM assertions (H08/H20), and two concern H30 filter bounds.
All 862 schema-checked results are valid. The 120 unresolved fee-default requests
are policy-open observations. The raw-transaction third argument and three
pending-tag requests also remain policy observations. Error totals include deliberate
invalid requests and do not directly count conformance failures.

The paired calls confirm `eth_call` returns BASEFEE 0 for explicit zero fees,
while this experimental `trace_call` preserves the original base fee. Its priced
validation and upfront accounting agree across both methods. The changed H15
verdict reflects the revised recommendation; the fork revision is unchanged.
See [H15](../reports/decisions/H15.md) for the paired evidence and remaining work.

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

[The contract update](https://github.com/banteg/go-ethereum/commit/c36ee43e3827331276d045bd56d1297e4c3c9b15)
closes the previously measured H06, H13 and H14 differences:

- Unknown selected blocks return `-32001`; pruned transaction lookup history returns
  `4444` when a missing hash cannot establish absence. Complete lookups retain `null`.
- Signed execution-validity failures return `-32003`; malformed encoding remains
  `-32602`, and valid transactions that revert or halt return traces.
- Unknown call fields are ignored. Standard chain ID, blob context and authorization
  fields are supported, with known-field and transaction-type validation.
- `earliest` selects genesis in the trace namespace, including when the backend's
  retention boundary is later. The H30 capture shows that omitted filter bounds
  also start at genesis; this differs from the revised latest/latest proposal.
  H31 and H32 cover call defaults and the safe tag. Pending remains explicitly
  unsupported.

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

The earlier `c36ee43e` source passed the full Geth suite, including the execution-spec
fixtures and the keeper module, plus race-enabled namespace tests. It also passed
`make all`, `go run ./build/ci.go lint`, `check_generate`, and `check_baddeps`.
Those modified Go files were formatted with `gofmt` and `goimports`. That full suite
ran in an isolated network namespace to avoid fixed test-port collisions. The current
`fa8ecb92` retest here builds the fork and runs the full interop matrix; it does not
repeat the fork’s entire internal test suite.

For reproduction, follow the [source-build instructions](usage.md#evaluate-the-geth-fork)
and the exact requests linked from the client report. The fork's
[usage documentation](https://github.com/banteg/go-ethereum/blob/feat/trace/docs/trace.md)
explains namespace enabling, method contracts and resource limits.
