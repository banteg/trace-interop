# Nethermind master at d8b6a53 — 2026-10-15

A pinned capture of Nethermind's development build at
[`d8b6a53b`](https://github.com/NethermindEth/nethermind/commit/d8b6a53b047041d939e8a4c5e5ff0ba234f8aeec), the merge
of [NethermindEth/nethermind#14663](https://github.com/NethermindEth/nethermind/pull/14663), which rejects a call's
`maxFeePerBlobGas` without `blobVersionedHashes`. It repeats the two probe corpora of the
[d8bb65b capture](../../2026-10-14/nethermind-d8bb65b/README.md), where that lone cap was Nethermind's last H14
difference. [reports.lock.json](../../../reports.lock.json) does not select these runs, and no published verdict
changes.

## Build

[clients.lock.json](clients.lock.json) pins `nethermindeth/nethermind@sha256:e271a156…`, the published
`nethermindeth/nethermind:master-d8b6a53` image, with `org.opencontainers.image.revision` `d8b6a53b`. It was written
the way the d8bb65b lock was. Hive commit `43ea47be`. Both corpora ran with `--clients nethermind_development` from a
clean clone at harness commit `32c67922` on Fedora (`source_dirty: false`).

## Capture completeness

Both corpora completed with no missing cases or transport errors: 196 responses
([probes-forks](probes-forks/summary.json) 72, [probes-prague](probes-prague/summary.json) 124).

## Result

Compared with the d8bb65b capture by status per corpus, case and decision, the two lone cap probes
`fork-blob-fee-only-before` and `fork-blob-fee-only-at` move from change needed to agreeing: the call is now rejected
at both blocks. Their H08 trace checks disappear because the call no longer runs. No other check changes.

Against Nethermind's development column in the current reports (`204457ad`), all 13 H14 checks that differed in these
corpora now agree, and no check regresses. No H14 check in these corpora differs any more. The published reports give
the development build 32 of 33 decisions with H14 the only difference, so a full capture of a build at or after
`d8b6a53b` should show it agreeing on all 33. The next eval measures that.

## Reproduction

From a clean checkout at `32c67922` on Linux:

```sh
uv run python -m trace_interop run --lock evidence/2026-10-15/nethermind-d8b6a53/clients.lock.json \
  --clients nethermind_development --corpus probes-forks --output runs/nethermind-d8b6a53/probes-forks
uv run trace-interop report --run evidence/2026-10-15/nethermind-d8b6a53/probes-forks --output runs/nethermind-d8b6a53-report
```
