# Reproduce and review

Requirements: Linux, Docker, Git, Go, and [uv](https://docs.astral.sh/uv/).
The runner downloads Go 1.26.1 for Hive when necessary. Run from a checkout of this
repository. Reports and unit checks also work on macOS without Docker.

```sh
uv sync --locked
uv run trace-interop verify
uv run python -m unittest discover -s tests -v
uv run python scripts/check_schema.py
```

## Reproduce one disagreement

The committed lock selects immutable client image digests, not moving tags:

```sh
uv run trace-interop run --lock locks/clients-2026-09-21.json \
  --clients reth_release --corpus initial --case '^get-root$' \
  --output runs/reth-root
uv run trace-interop report --run runs/reth-root --output runs/reth-root-report
```

The runner imports a disposable chain, waits for the canonical RPC head, verifies its hash and state/transaction/receipt roots both by number and via `latest`,
and records the response. Read `summary.json` before interpreting results. Client launch
or state-setup failures cannot count as semantic mismatches. Filters and tree-path queries automatically include
the block/transaction reference queries needed by relational assertions. Case selection also retains independent setup controls; each must have a valid, correlated JSON-RPC result before its value can establish eligibility.

## Run the matrix

```sh
uv run python scripts/run_matrix.py --output runs/current-matrix
```

This is the default command for a new comparison. It discovers the latest published
stable release of each native client through GitHub, pulls the moving development
images, and builds the current `banteg/go-ethereum` `feat/trace` head in an isolated
cache. Before any corpus starts, a live preflight checks release references, image
digests and the Geth branch head again. Missing network/registry data and stale
builds stop the suite. No old lock is used as a fallback.

`clients.lock.json` freezes those nine builds for the entire matrix; `preflight.json`
records when they were checked. Tags are not refreshed between corpora. Thus results
show the current published builds **as of the preflight**, not a promise that upstream
has stayed unchanged since then. The Geth cache refuses dirty source.

For an intentional historical reproduction, supply the combined nine-build lock:

```sh
uv run python scripts/run_matrix.py --reproduce-lock runs/current-matrix/clients.lock.json \
  --output runs/reproduction
```

Historical mode is explicit in its preflight artifact and does not claim freshness.
A Geth local image must still exist, or be rebuilt using its recorded source/base
image and the resulting image identity (see below). Single-corpus `run --lock` is
also a frozen-build reproduction tool; use the matrix command for current comparisons.

`initial` covers all nine methods; `a` contains focused semantic discriminators;
`repeat` checks reproducibility and trace-type combinations; `forks` and
`fork-followup` exercise fork boundaries. `precompiles` checks frame inclusion
across root/nested execution, call modes, value and failure. See [scenario setup](scenarios.md) for reorgs
and pruning. A zero-match case selector is an error. A run directory cannot be overwritten.
One runner owns a checkout's Hive build context at a time.

`fee-policy` covers H15's legacy/typed fee boundaries, funding, environment and
accounting across every trace selection. `fee-compat` pairs identical `eth_call`
and `trace_call` requests, with opcode and balance witnesses. Both are included
in the default matrix. See [the H15 probe guide](h15-fee-policy.md)
for independent gas models, sequential checks and unresolved-default captures.

## Check or resolve versions

```sh
uv run trace-interop check-versions --lock runs/current-matrix/clients.lock.json
uv run trace-interop resolve --output runs/native-next.lock.json
```

`check-versions` contacts upstream and exits nonzero on drift. `resolve` discovers
and locks current native images; the matrix command also builds Geth. Release and
development remain internal update channels. Reports identify tested builds by their
runtime **version and source commit**, with source and capture dates. A development
build is not another independent client vote.

## Observation and proposal checks

`run` is an observation operation. It uses Hive's request/response logging with deliberate
placeholder expectations. Hive's raw failed-test count is therefore **not a conformance
result**. The command succeeds when all requested observations and scenario controls are
complete, even when clients disagree or return malformed JSON. Missing transport exchanges
or failed state setup produce a nonzero exit and retain the evidence.

`report` groups exact observations and separately applies explicitly coded proposed
assertions plus the pinned result schemas. It never adopts a majority response as an
expected answer. JSON key order and RPC IDs are excluded from observation grouping;
null/omitted values, array ordering, numbers, error text and byte strings are preserved.

Schema validity alone cannot establish execution correctness. Assertion matches apply to
the named case and property, not the whole method or decision. Unsupported, malformed,
transport-failed, untested and unresolved states stay separate.

## Artifacts

Each run includes the exact selected requests, chain identity, source revision and runner
hash, base-image lock, Hive binary hash, timestamps, raw logs, parsed observations,
eligibility checks and SHA-256 manifest. Report generation verifies every retained hash.
Keep original run directories unchanged. Reassess them against another draft by producing
a new report; do not rewrite observations. A run with `source_dirty` is explicitly a
development capture and must not be represented as a clean commit reproduction.

## Change the draft

Edit the execution-apis fork, run its build/tests, commit and push `feat/trace`, then:

```sh
uv run python scripts/pin_spec.py ../execution-apis
uv run python scripts/check_schema.py
uv run python scripts/build_reports.py
```

Pass the actual checkout path. Pinning refuses a dirty spec checkout and checks that its
generated file agrees with a fresh build. The generated trace-only OpenRPC document is an
immutable build artifact; edit YAML in the fork, not this file. Commit the new lock, artifact,
assertion updates and regenerated reports together.

## Track client fixes

[`decisions/fixes.json`](../decisions/fixes.json) lists related PRs with their client family
(`null` for specification and test-suite repositories) and the decisions they address.
List a decision under `partial` as well when the PR leaves part of that client’s measured
difference unaddressed, and set `awaiting_uptake` when the fix reaches the client through a
library it pins at an older release; remove it once a captured build contains the fix.
Report generation renders [client fixes](client-fixes.md) from it and shows 🛠️ Fix submitted
for a differing or partially assessed build when a non-partial tagged PR is open, merged after
the build’s commit, or awaiting uptake; partial PRs are linked without replacing ⚠️ or 🟡.
Captured checks and harmonization milestones are unchanged. Refresh PR titles and states from
GitHub, then regenerate:

```sh
uv run python scripts/refresh_fixes.py
uv run python scripts/build_reports.py
```

## Evaluate the Geth fork

The experimental `banteg/go-ethereum` branch `feat/trace` is built locally on Linux.
It is identified separately from upstream Geth and evaluated with the same cases,
schemas and assertions. The runner adds `trace` to the pinned Hive Geth adapter's
HTTP/WebSocket API lists. It does not change any running node configuration.

```sh
git clone --branch feat/trace https://github.com/banteg/go-ethereum ../geth-trace
# For an exact reproduction, check out source.commit from the recorded Geth lock.
uv run python scripts/build_geth.py --source ../geth-trace \
  --output runs/geth.lock.json
uv run trace-interop run --lock runs/geth.lock.json \
  --corpus initial --output runs/geth-initial
```

The builder copies a source snapshot, compiles with Go 1.26.1 and CGO disabled,
and records the source commit, content hash, binary hash, base-image digest,
recipe and local Docker image ID. Dirty builds require `--allow-dirty` and are
marked as development captures. Published comparison runs use committed source.
No image is pushed to a registry. The runner checks the exact local image ID
before starting Hive.

To reproduce a published binary, check out its clean source commit and pass
`--reference locks/geth-trace.json` to the builder with a fresh `--output` path.
This reuses the recorded base image and checks source and binary hashes. Docker
metadata may give the rebuilt image a new ID; use the newly generated lock for
that run. Retain the original lock and observations unchanged.

`trace_get` assertions compare with the same transaction's `trace_transaction`
response where available. Precompile inclusion can shift sibling indexes, so a
path called “positive” in a frozen corpus is not assumed to exist in every client.
The reference must first contain the frozen transaction roots and the call-tree fixture’s required ordinary calls, creation and self-destruct. A missing or unanchored reference is unassessed. These minimum anchors prevent joint omission from passing; they are not a general proof of full trace correctness.

The fork scans blocks for `trace_filter`; no address index or performance claim is
implied. The current pruning scenario has a verified Reth adapter only, so Geth's
unavailable-history behavior is not yet verified by that scenario.

## Report inventory and assertion coverage

`reports.lock.json` selects the retained run directories used by both report generation
and `trace-interop verify`. Ledger references use `corpus/case` identities and must be
nonempty and present in those runs. Original evidence is checksum verified and never
rewritten. A captured case is assessed with the current corpus definition when its request
is identical, so a corrected expectation in a regenerated corpus reassesses old evidence;
a case whose request has changed keeps the definition it was captured with. Report eligibility is recalculated from the recorded head and independent
scenario controls; `capture_eligible` keeps the old decision for comparison.

Malformed requests are checked against the pinned request schemas. Semantic assertions
and result-schema validation remain separate: valid JSON does not prove correct execution.
A declared topic case without an evaluated assertion is `unassessed`; mixing it with
matching checks yields “Partially assessed”, not agreement. The technical appendix also
counts all selected trace observations, including missing responses and ineligible setup, with no assertion at all. This makes remaining coverage
gaps explicit rather than implying that every ledger recommendation is implemented.


Harmonization requires every declared case on one immutable image per client/channel.
The most recently captured build is selected using capture timestamps across all corpora;
passing cases from earlier builds cannot fill its gaps. Missing build identity or timestamps
prevent a harmonization badge. Historical run completeness is retained separately from
current report eligibility, so stronger setup rules can make an old capture unassessed.

Fixture-specific checks compare known REVERT bytes and gas, signed marker storage and
executed VM opcodes, and retained precompile child identity/value/outcome. Their independent
anchors live in `trace_interop/oracles.py` and the frozen corpora. Regression tests jointly
corrupt references and target responses, remove requested outputs, and preserve schema-valid
shapes so schema validation cannot mask weak semantic assertions.

See [assertion models](assertion-models.md) for independent chain decoding, bounded
VM execution, exact fee/account models, blocked/control dispositions and model
limits. `scripts/run_matrix.py --output runs/coverage-matrix` runs the complete
freshly resolved matrix and retains every incomplete capture for inspection.
