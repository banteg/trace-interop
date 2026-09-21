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

The runner imports a disposable chain, verifies its head/state/transaction/receipt roots,
and records the response. Read `summary.json` before interpreting results. Client launch
or state-setup failures cannot count as semantic mismatches. Filters and tree-path queries automatically include
the block/transaction reference queries needed by relational assertions.

## Run the matrix

```sh
uv run trace-interop run --lock locks/clients-2026-09-21.json \
  --corpus a --output runs/semantic
uv run trace-interop run --lock locks/clients-2026-09-21.json \
  --corpus forks --output runs/forks
uv run trace-interop report --run runs/semantic --run runs/forks \
  --output runs/combined-report
```

`initial` covers all nine methods; `a` contains focused semantic discriminators;
`repeat` checks reproducibility and trace-type combinations; `forks` and
`fork-followup` exercise fork boundaries. `precompiles` checks frame inclusion
across root/nested execution, call modes, value and failure. See [scenario setup](scenarios.md) for reorgs
and pruning. A zero-match case selector is an error. A run directory cannot be overwritten.
One runner owns a checkout's Hive build context at a time.

## Refresh versions intentionally

```sh
uv run trace-interop resolve --output clients-next.lock.json
```

The candidate release tags are explicit in `trace_interop/cli.py`; update them after
checking upstream releases. Development tags move, so resolve them to digests once per
comparison. The lock records the requested reference, image ID, digest, architecture,
labels and creation date. Reports show the runtime version, including the actual commit
where the client exposes it. A development build is not another independent client vote.

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
This checks selector consistency; it does not by itself prove tree completeness.

The fork scans blocks for `trace_filter`; no address index or performance claim is
implied. The current pruning scenario has a verified Reth adapter only, so Geth's
unavailable-history behavior is not yet verified by that scenario.
