# Nethermind master at d8bb65b — 2026-10-14

A pinned capture of Nethermind's development build at
[`d8bb65b3`](https://github.com/NethermindEth/nethermind/commit/d8bb65b3bfcd580490f9271ee4aaaa1c39c8ae7e), the merge
of [NethermindEth/nethermind#14212](https://github.com/NethermindEth/nethermind/pull/14212). That PR lets a call's
fields decide how it runs and rejects fields the selected block's fork lacks. The
[2026-10-11 eval](../../2026-10-11/eval/README.md) measured `master` at `204457ad`, which predates the merge. These runs
measure Nethermind's column on the six corpora that carry its call-field (H14) and fee (H15) cases, so
[reports.lock.json](../../../reports.lock.json) does not select them and no published verdict changes. The next eval's
development build carries the result into the reports.

## Build

[clients.lock.json](clients.lock.json) pins `nethermindeth/nethermind@sha256:3ffc8605…`, the published
`nethermindeth/nethermind:master-d8bb65b` image. Its `org.opencontainers.image.revision` label is `d8bb65b3`. The lock
was written from that tag the way `trace-interop resolve` records an image, because `resolve` only follows `master`.
Its Hive commit `43ea47be` matches the 2026-10-11 matrix. Every corpus ran with `--clients nethermind_development` from
a clean clone at harness commit `0d538328` on Fedora (`source_dirty: false`).

## Capture completeness

All six corpora completed with no missing cases or transport errors: 1,422 responses.

| Corpus | Responses | Corpus | Responses |
| --- | --- | --- | --- |
| [probes-forks](probes-forks/summary.json) | 72 | [a](a/summary.json) | 94 |
| [probes-prague](probes-prague/summary.json) | 124 | [fee-compat](fee-compat/summary.json) | 300 |
| [initial](initial/summary.json) | 76 | [fee-policy](fee-policy/summary.json) | 756 |

## Result

`trace-interop report` assessed these runs together. The result was compared with Nethermind's development column in
the current reports by counting statuses per corpus, case and decision. None of the 2,719 case–decision pairs both
builds share regresses. Eleven H14 checks move from change needed to agreeing:

- `probes-forks`: an access list, dynamic fees (unpriced and priced), blob fields and an authorization list before
  their forks are now rejected. An explicit type 1, 3 or 4 alone before its fork now runs, since type is not a feature.
- `probes-prague`: an explicit type 0 or 1 with dynamic fee caps now runs priced from those caps, and an explicit type 2
  with an authorization list now runs with the authorization applied. The type no longer changes execution.

The checks that appear or disappear are trace-output checks (H08, H10), which exist only when a call runs. A call
carrying fields its fork lacks is now rejected, so it has none, while a type-only call before its fork now runs.

| Decision | 204457ad (2026-10-11) | d8bb65b3 |
| --- | --- | --- |
| H14 | Differs in 13 checks of these corpora | Differs only on `fork-blob-fee-only-before` and `fork-blob-fee-only-at`: a `maxFeePerBlobGas` without `blobVersionedHashes` runs with the cap ignored |
| H15 | Agrees | Agrees |

The empty `blobVersionedHashes` list is already rejected at both blocks. The lone blob fee cap is the follow-up
promised in #14212's review.

## Reproduction

From a clean checkout at `0d538328` on Linux:

```sh
uv run python -m trace_interop run --lock evidence/2026-10-14/nethermind-d8bb65b/clients.lock.json \
  --clients nethermind_development --corpus probes-forks --output runs/nethermind-d8bb65b/probes-forks
uv run trace-interop report --run evidence/2026-10-14/nethermind-d8bb65b/probes-forks --output runs/nethermind-d8bb65b-report
```

Each run keeps its manifest, summary, compact observations and checksums. The capture logs sit beside the runs.
