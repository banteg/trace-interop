# Stateful scenarios

All mutations below target disposable Hive databases. They never connect to an existing node.

The explicit dated locks below reproduce historical builds. For a current comparison,
use `uv run python scripts/run_matrix.py --output runs/current-matrix`; it refreshes
and checks all builds before running these scenarios.

## Canonical reorg and restoration

```sh
uv run trace-interop run --lock locks/clients-2026-09-21.json \
  --corpus reorg-safe --output runs/reorg
```

The small adapter imports branch A, queries it, submits branch B's alternate tail through
the Engine API, changes forkchoice, queries B, then restores A and queries it again. The
safe marker is on the common prefix. The runner waits for both RPC ports at startup and for the canonical RPC head after each accepted forkchoice. All three phase controls are mandatory, so a case
selector selects the complete scenario. `reorg` retains the earlier strict-marker variant.

Each phase must expose the expected canonical hash. An Engine rejection or an unverified
switch is a setup/coverage failure, not evidence that a client returned a wrong trace.
Rejected Engine transitions remain setup failures and are retained as coverage gaps.

## Unavailable historical state

```sh
uv run trace-interop run --lock locks/clients-2026-09-21.json \
  --clients reth_release,reth_development --corpus pruned --output runs/pruned
```

Only Reth has a verified pruning adapter in this milestone. It imports the tiny chain,
prunes account/storage history before block 44, and starts the RPC node. Old headers and
receipts must remain readable and a latest-state call must succeed. A separate nonce
query must establish that the old state is unavailable, using a recognized unavailable-state
code or the pinned client's legacy pruning diagnostic. Historical trace responses do not
control eligibility: null, empty results and unexpected errors remain eligible and are
assessed by H06 against the draft. Merely enabling a pruning flag is not proof.

Erigon, Nethermind and Besu retention scenarios remain an explicit coverage gap. Selecting
them with `pruned` fails before client execution. This limitation does not affect their
ordinary replay or historical-query probes on fully retained fixture chains.

## Tested matrix

Both release and development builds of Besu and Nethermind, plus the release build of
Erigon, complete the canonical switch and restoration. Scenario runs whose setup fails
are excluded from trace assessments; the Engine and head-control logs are retained with
their runs.

The Erigon development build fails deterministically at the first branch switch: every
`engine_newPayloadV4` is VALID, then `engine_forkchoiceUpdatedV3` to the sibling head
returns -38002 `Invalid forkchoice state`. All nine captured runs of `c25b8e47` and
`e26d9bd4` fail there, and 3.6.1 passes. In source, Erigon
[#23612](https://github.com/erigontech/erigon/pull/23612) (`de2a956a`) marks the imported
tip as safe and finalized; Hive's startup forkchoice update with an earlier finalized
block takes a short-circuit path that does not commit it, and the new finality guard
then rejects a sibling branch forking below the imported tip. The update's own
finalized block is an ancestor of its head, so -38002 is the wrong response. This
reading comes from logs and source and awaits an upstream report.

Reth accepts the restoring forkchoice update as VALID but intermittently never moves its
head back, on identical builds: development failed five of eight captures and release
three of eight. The source suggests a race between restoration and the background removal
of the abandoned branch's blocks, during which a stale on-disk header is treated as
already canonical. The failure is intermittent, not a property of a particular build.

Both pinned Reth builds retain old headers and receipts after pruning, allow latest-state
execution, and reject old state access. Their trace errors use -32603 with an insufficient
changesets message; the draft proposes the existing execution-apis pruned-history code 4444.

### Crossed precompile values

`precompile-values` uses the same frozen chain as `precompiles`, with separate
CALL/CALLCODE operands and outer creation values: `(outer=1, child=0)` and
`(outer=0, child=1)`, for successful and failed BN254 addition. The latter is a
`trace_callMany` sequence: fund the future creation address with one wei, then
create with zero outer value. The constructor returns the call success bit as its
runtime bytes, so insufficient funds cannot masquerade as successful execution.

The first simulated transfer uses sender nonce 133 and the creation uses nonce 134.
`cast compute-address 0x7435ed30a8b4aeb0877cef0c6e8cffe834eb865f --nonce 134`
computes `0x93216e4a663e3a680a0fe006285935f47caa5738`. Independent nonce, balance and
code controls require that sender nonce and an empty unfunded target before scoring.
The H29 rule uses the fixture's explicit precompile value, verifies the funding
transfer and actual creation address, and checks the returned success bit. This is
separate from the inherited DELEGATECALL compatibility rule.

### Signed transaction validation

`raw-validation` uses independent chain ID, nonce, balance, sender code, base fee and
marker storage controls. Actual output, storage writes and CREATE ADDRESS bytes
distinguish execution from result-shaped failures. See the [H13 study](h13-validation.md)
for the client matrix, fixture generator and reproduction commands.

### Multi-call simulation isolation

`callmany-isolation` uses an explicit phase plan on the frozen chain-a head:
independent nonce, contract code and storage controls; write/read simulation;
`eth_getStorageAt`; write/revert/read simulation; another `eth_getStorageAt`.
The same disposable client handles all phases, synchronously. Selecting one case
retains the whole scenario. The recorded plan and requests are required for setup
eligibility; a missing or failed simulation leaves its isolation check unassessed.
An after-read returning changed storage is a behavior failure, not a setup failure.

```sh
uv run trace-interop run --lock locks/clients-2026-09-21.json \
  --corpus callmany-isolation --output runs/callmany-isolation
```

The older `a/control-storage-after-many` observation runs before the multi-call
probes in Hive's lexical order and has no isolation assertion. It remains in the
historical evidence but is not used as proof that simulations leave state unchanged.
The new scenario also checks per-call nonce progression and storage transitions;
fee amounts and warm-access/refund semantics remain outside these assertions.
