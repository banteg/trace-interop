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
or state-setup failures cannot count as semantic mismatches. Filters automatically include
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
`fork-followup` exercise fork boundaries. See [scenario setup](scenarios.md) for reorgs
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
