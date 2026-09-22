# Technical appendix

[Back to the maintainer overview](README.md)

The human reports summarize selected assertions against a proposed specification. Agreement is not full conformance, and an RPC error can be the correct result for an invalid-input case. Setup failures are excluded from semantic assessment. Release and development labels refer to the captured builds; they do not imply version ordering.

The experimental Geth fork implements the draft and is not an independent vote for its decisions. No verified pruning scenario is included for that fork.

## Reproduction and machine-readable results

See [usage](../docs/usage.md) for commands and [stateful scenarios](../docs/scenarios.md) for setup requirements. [checks.json](checks.json) retains every assertion; [comparisons.json](comparisons.json) groups exact responses; [assessment.json](assessment.json) pins the specification and assessment source hashes. Each case links its original response and run manifest.

To reproduce one case, use its linked manifest and the exact client, corpus and case name:

```sh
uv run trace-interop run --lock evidence/2026-09-21/RUN/manifest.json \
  --clients CLIENT --corpus CORPUS --case "^CASE$" --output runs/reproduce
```

## Assertion coverage

Coverage below counts eligible trace observations, separately from schema validation. Partially assessed means at least one declared topic was not checked. A checked assertion is not proof of the rest of the topic.

| Coverage | Observations |
| --- | --- |
| assessed | 1401 |
| partial | 509 |
| unassessed | 223 |

Eligibility is recomputed from the frozen head and independent scenario controls. `capture_eligible` in checks.json preserves the original capture decision; original summaries and wire observations are unchanged.

## Setup gaps

| Build | Scenario | Run evidence |
| --- | --- | --- |
| Besu · Development | fork-followup | [verified-fork-followup](../evidence/2026-09-21/verified-fork-followup/summary.json) |
| Besu · Release | a | [verified-a](../evidence/2026-09-21/verified-a/summary.json) |
| Erigon · Development | reorg-safe | [verified-reorg-ready](../evidence/2026-09-21/verified-reorg-ready/summary.json) |
| Erigon · Development | reorg-safe | [verified-reorg-safe](../evidence/2026-09-21/verified-reorg-safe/summary.json) |
| Reth · Development | reorg-safe | [verified-reorg-ready](../evidence/2026-09-21/verified-reorg-ready/summary.json) |
| Reth · Development | reorg-safe | [verified-reorg-safe](../evidence/2026-09-21/verified-reorg-safe/summary.json) |

## Result-shape checks

These cases returned results that differ from the draft schema. The case pages retain the validation details; an unclassified schema failure is not silently counted as agreement.

| Case | Affected builds |
| --- | --- |
| [a/auth-replace](cases/a/auth-replace.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [a/auth-set](cases/a/auth-set.md) | Nethermind Development, Nethermind Release |
| [a/auth-set-revert](cases/a/auth-set-revert.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [a/block-2](cases/a/block-2.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [a/block-3](cases/a/block-3.md) | Nethermind Development, Nethermind Release |
| [a/call-gas7400](cases/a/call-gas7400.md) | Nethermind Development, Nethermind Release |
| [a/call-mcopy](cases/a/call-mcopy.md) | Nethermind Development, Nethermind Release |
| [a/call-mixed-create](cases/a/call-mixed-create.md) | Nethermind Development, Nethermind Release |
| [a/call-return42](cases/a/call-return42.md) | Nethermind Development, Nethermind Release |
| [a/call-siblings-ok-revert](cases/a/call-siblings-ok-revert.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [a/call-siblings-revert-ok](cases/a/call-siblings-revert-ok.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [a/filter-all](cases/a/filter-all.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [a/filter-both-null](cases/a/filter-both-null.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [a/filter-creator-from](cases/a/filter-creator-from.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [a/filter-from-null](cases/a/filter-from-null.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [a/filter-from-only-intersection](cases/a/filter-from-only-intersection.md) | Nethermind Development, Nethermind Release |
| [a/filter-page-0](cases/a/filter-page-0.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [a/filter-page-1](cases/a/filter-page-1.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [a/filter-page-2](cases/a/filter-page-2.md) | Besu Development, Besu Release |
| [a/filter-snapshot](cases/a/filter-snapshot.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [a/filter-to-empty-from-set](cases/a/filter-to-empty-from-set.md) | Besu Development, Besu Release |
| [a/filter-to-null](cases/a/filter-to-null.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [a/filter-two-blocks](cases/a/filter-two-blocks.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [a/filter-unknown-field](cases/a/filter-unknown-field.md) | Nethermind Development, Nethermind Release |
| [a/filter-wrong-address-type](cases/a/filter-wrong-address-type.md) | Besu Development, Besu Release |
| [a/get-integer-path](cases/a/get-integer-path.md) | Nethermind Release |
| [a/get-nested-parent](cases/a/get-nested-parent.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [a/get-nested-positive](cases/a/get-nested-positive.md) | Nethermind Development, Nethermind Release |
| [a/many-storage-write-revert-read](cases/a/many-storage-write-revert-read.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [a/missing-block-block](cases/a/missing-block-block.md) | Besu Development, Besu Release |
| [a/raw-below-basefee](cases/a/raw-below-basefee.md) | Besu Development, Besu Release |
| [a/raw-insufficient-funds](cases/a/raw-insufficient-funds.md) | Besu Development, Besu Release |
| [a/raw-low-gas](cases/a/raw-low-gas.md) | Besu Development, Besu Release |
| [a/raw-nonce-high](cases/a/raw-nonce-high.md) | Besu Development, Besu Release |
| [a/state-only-nonempty-output](cases/a/state-only-nonempty-output.md) | Nethermind Development, Nethermind Release |
| [a/transaction-tree](cases/a/transaction-tree.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [a/vm-only-nonempty-output](cases/a/vm-only-nonempty-output.md) | Nethermind Development, Nethermind Release |
| [fork-followup/beacon-call-55](cases/fork-followup/beacon-call-55.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [fork-followup/destroy-trace-55](cases/fork-followup/destroy-trace-55.md) | Nethermind Development, Nethermind Release |
| [forks/block-35](cases/forks/block-35.md) | Erigon Development, Erigon Release, Nethermind Development, Nethermind Release, Reth Development, Reth Release |
| [forks/block-36](cases/forks/block-36.md) | Besu Development, Besu Release, Erigon Development, Erigon Release, Nethermind Development, Nethermind Release, Reth Development, Reth Release |
| [forks/block-47](cases/forks/block-47.md) | Erigon Development, Erigon Release, Nethermind Development, Nethermind Release, Reth Development, Reth Release |
| [forks/block-48](cases/forks/block-48.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [forks/block-51](cases/forks/block-51.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [forks/block-52](cases/forks/block-52.md) | Nethermind Development, Nethermind Release |
| [forks/block-55](cases/forks/block-55.md) | Nethermind Development, Nethermind Release |
| [forks/block-56](cases/forks/block-56.md) | Nethermind Development, Nethermind Release |
| [forks/block-59](cases/forks/block-59.md) | Nethermind Development, Nethermind Release |
| [forks/block-60](cases/forks/block-60.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [forks/destroy-trace-55](cases/forks/destroy-trace-55.md) | Nethermind Development, Nethermind Release |
| [forks/filter-35](cases/forks/filter-35.md) | Erigon Development, Erigon Release, Nethermind Development, Nethermind Release, Reth Development, Reth Release |
| [forks/filter-36](cases/forks/filter-36.md) | Besu Development, Besu Release, Erigon Development, Erigon Release, Nethermind Development, Nethermind Release, Reth Development, Reth Release |
| [forks/filter-47](cases/forks/filter-47.md) | Erigon Development, Erigon Release, Nethermind Development, Nethermind Release, Reth Development, Reth Release |
| [forks/filter-48](cases/forks/filter-48.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [forks/filter-51](cases/forks/filter-51.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [forks/filter-52](cases/forks/filter-52.md) | Nethermind Development, Nethermind Release |
| [forks/filter-55](cases/forks/filter-55.md) | Nethermind Development, Nethermind Release |
| [forks/filter-56](cases/forks/filter-56.md) | Nethermind Development, Nethermind Release |
| [forks/filter-59](cases/forks/filter-59.md) | Nethermind Development, Nethermind Release |
| [forks/filter-60](cases/forks/filter-60.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [forks/filter-across-36](cases/forks/filter-across-36.md) | Besu Development, Besu Release, Erigon Development, Erigon Release, Nethermind Development, Nethermind Release, Reth Development, Reth Release |
| [forks/filter-across-48](cases/forks/filter-across-48.md) | Besu Development, Besu Release, Erigon Development, Erigon Release, Nethermind Development, Nethermind Release, Reth Development, Reth Release |
| [forks/filter-across-52](cases/forks/filter-across-52.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [forks/filter-across-56](cases/forks/filter-across-56.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [forks/filter-across-60](cases/forks/filter-across-60.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [forks/mcopy-trace-55](cases/forks/mcopy-trace-55.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [forks/mcopy-trace-56](cases/forks/mcopy-trace-56.md) | Nethermind Development, Nethermind Release |
| [forks/replay-36](cases/forks/replay-36.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [forks/replay-48](cases/forks/replay-48.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [forks/replay-51](cases/forks/replay-51.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [forks/replay-60](cases/forks/replay-60.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [initial/block-transfer](cases/initial/block-transfer.md) | Nethermind Development, Nethermind Release |
| [initial/block-tree](cases/initial/block-tree.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [initial/call-constructor](cases/initial/call-constructor.md) | Nethermind Development, Nethermind Release |
| [initial/call-constructor-priced](cases/initial/call-constructor-priced.md) | Nethermind Development, Nethermind Release |
| [initial/call-many](cases/initial/call-many.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [initial/call-many-priced](cases/initial/call-many-priced.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [initial/call-transfer-stateDiff](cases/initial/call-transfer-stateDiff.md) | Nethermind Development, Nethermind Release |
| [initial/call-tree-stateDiff](cases/initial/call-tree-stateDiff.md) | Nethermind Development, Nethermind Release |
| [initial/call-tree-stateDiff-priced](cases/initial/call-tree-stateDiff-priced.md) | Nethermind Development, Nethermind Release |
| [initial/call-tree-trace](cases/initial/call-tree-trace.md) | Nethermind Development, Nethermind Release |
| [initial/call-tree-trace-priced](cases/initial/call-tree-trace-priced.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [initial/call-tree-vmTrace](cases/initial/call-tree-vmTrace.md) | Nethermind Development, Nethermind Release |
| [initial/call-tree-vmTrace-priced](cases/initial/call-tree-vmTrace-priced.md) | Nethermind Development, Nethermind Release |
| [initial/filter-all](cases/initial/filter-all.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [initial/filter-empty](cases/initial/filter-empty.md) | Besu Development, Besu Release |
| [initial/filter-from](cases/initial/filter-from.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [initial/get-missing](cases/initial/get-missing.md) | Nethermind Development, Nethermind Release |
| [initial/get-nested](cases/initial/get-nested.md) | Nethermind Development, Nethermind Release |
| [initial/get-one](cases/initial/get-one.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [initial/get-root](cases/initial/get-root.md) | Nethermind Development, Nethermind Release |
| [initial/get-transfer-root](cases/initial/get-transfer-root.md) | Nethermind Development, Nethermind Release |
| [initial/get-zero](cases/initial/get-zero.md) | Nethermind Development, Nethermind Release |
| [initial/raw-valid-default-block](cases/initial/raw-valid-default-block.md) | Besu Development, Besu Release |
| [initial/replay-7702-stateDiff](cases/initial/replay-7702-stateDiff.md) | Nethermind Development, Nethermind Release, Reth Development, Reth Release |
| [initial/replay-7702-trace](cases/initial/replay-7702-trace.md) | Reth Development, Reth Release |
| [initial/replay-7702-vmTrace](cases/initial/replay-7702-vmTrace.md) | Reth Development, Reth Release |
| [initial/replay-block-tree](cases/initial/replay-block-tree.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [initial/replay-revert-stateDiff](cases/initial/replay-revert-stateDiff.md) | Nethermind Development, Nethermind Release, Reth Development, Reth Release |
| [initial/replay-revert-trace](cases/initial/replay-revert-trace.md) | Nethermind Development, Nethermind Release, Reth Development, Reth Release |
| [initial/replay-revert-vmTrace](cases/initial/replay-revert-vmTrace.md) | Nethermind Development, Nethermind Release, Reth Development, Reth Release |
| [initial/replay-transfer-stateDiff](cases/initial/replay-transfer-stateDiff.md) | Nethermind Development, Nethermind Release, Reth Development, Reth Release |
| [initial/replay-transfer-trace](cases/initial/replay-transfer-trace.md) | Reth Development, Reth Release |
| [initial/replay-transfer-vmTrace](cases/initial/replay-transfer-vmTrace.md) | Reth Development, Reth Release |
| [initial/replay-tree-stateDiff](cases/initial/replay-tree-stateDiff.md) | Nethermind Development, Nethermind Release, Reth Development, Reth Release |
| [initial/replay-tree-trace](cases/initial/replay-tree-trace.md) | Nethermind Development, Nethermind Release, Reth Development, Reth Release |
| [initial/replay-tree-vmTrace](cases/initial/replay-tree-vmTrace.md) | Nethermind Development, Nethermind Release, Reth Development, Reth Release |
| [initial/transaction-revert](cases/initial/transaction-revert.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [initial/transaction-tree](cases/initial/transaction-tree.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [precompile-values/nested-call-outer0-value1-failed](cases/precompile-values/nested-call-outer0-value1-failed.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [precompile-values/nested-call-outer0-value1-success](cases/precompile-values/nested-call-outer0-value1-success.md) | Nethermind Development, Nethermind Release |
| [precompile-values/nested-call-outer1-value0-failed](cases/precompile-values/nested-call-outer1-value0-failed.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [precompile-values/nested-call-outer1-value0-success](cases/precompile-values/nested-call-outer1-value0-success.md) | Nethermind Development, Nethermind Release |
| [precompile-values/nested-callcode-outer0-value1-failed](cases/precompile-values/nested-callcode-outer0-value1-failed.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [precompile-values/nested-callcode-outer0-value1-success](cases/precompile-values/nested-callcode-outer0-value1-success.md) | Nethermind Development, Nethermind Release |
| [precompile-values/nested-callcode-outer1-value0-failed](cases/precompile-values/nested-callcode-outer1-value0-failed.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [precompile-values/nested-callcode-outer1-value0-success](cases/precompile-values/nested-callcode-outer1-value0-success.md) | Nethermind Development, Nethermind Release |
| [precompiles/nested-call-value0-failed](cases/precompiles/nested-call-value0-failed.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [precompiles/nested-call-value0-success](cases/precompiles/nested-call-value0-success.md) | Nethermind Development, Nethermind Release |
| [precompiles/nested-call-value1-failed](cases/precompiles/nested-call-value1-failed.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [precompiles/nested-call-value1-success](cases/precompiles/nested-call-value1-success.md) | Nethermind Development, Nethermind Release |
| [precompiles/nested-callcode-value0-failed](cases/precompiles/nested-callcode-value0-failed.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [precompiles/nested-callcode-value0-success](cases/precompiles/nested-callcode-value0-success.md) | Nethermind Development, Nethermind Release |
| [precompiles/nested-callcode-value1-failed](cases/precompiles/nested-callcode-value1-failed.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [precompiles/nested-callcode-value1-success](cases/precompiles/nested-callcode-value1-success.md) | Nethermind Development, Nethermind Release |
| [precompiles/nested-delegatecall-value0-failed](cases/precompiles/nested-delegatecall-value0-failed.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [precompiles/nested-delegatecall-value0-success](cases/precompiles/nested-delegatecall-value0-success.md) | Nethermind Development, Nethermind Release |
| [precompiles/nested-delegatecall-value1-failed](cases/precompiles/nested-delegatecall-value1-failed.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [precompiles/nested-delegatecall-value1-success](cases/precompiles/nested-delegatecall-value1-success.md) | Nethermind Development, Nethermind Release |
| [precompiles/nested-staticcall-value0-failed](cases/precompiles/nested-staticcall-value0-failed.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [precompiles/nested-staticcall-value0-success](cases/precompiles/nested-staticcall-value0-success.md) | Nethermind Development, Nethermind Release |
| [precompiles/root-failed](cases/precompiles/root-failed.md) | Nethermind Development, Nethermind Release |
| [reorg-safe/after/block-tail](cases/reorg-safe/after/block-tail.md) | Nethermind Development, Nethermind Release |
| [reorg-safe/after/filter-tail](cases/reorg-safe/after/filter-tail.md) | Nethermind Development, Nethermind Release |
| [reorg-safe/before/block-tail](cases/reorg-safe/before/block-tail.md) | Nethermind Development, Nethermind Release |
| [reorg-safe/before/filter-tail](cases/reorg-safe/before/filter-tail.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [reorg-safe/restored/block-tail](cases/reorg-safe/restored/block-tail.md) | Nethermind Development, Nethermind Release |
| [reorg-safe/restored/filter-tail](cases/reorg-safe/restored/filter-tail.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [repeat/auth-set-revert](cases/repeat/auth-set-revert.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [repeat/call-gas7400](cases/repeat/call-gas7400.md) | Nethermind Development, Nethermind Release |
| [repeat/call-mcopy](cases/repeat/call-mcopy.md) | Nethermind Development, Nethermind Release |
| [repeat/call-mixed-create](cases/repeat/call-mixed-create.md) | Nethermind Development, Nethermind Release |
| [repeat/call-return42](cases/repeat/call-return42.md) | Nethermind Development, Nethermind Release |
| [repeat/call-siblings-revert-ok](cases/repeat/call-siblings-revert-ok.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [repeat/constructor](cases/repeat/constructor.md) | Nethermind Development, Nethermind Release |
| [repeat/many-storage-write-revert-read](cases/repeat/many-storage-write-revert-read.md) | Besu Development, Besu Release, Nethermind Development, Nethermind Release |
| [repeat/raw-below-basefee](cases/repeat/raw-below-basefee.md) | Besu Development, Besu Release |
| [repeat/raw-below-basefee-trace](cases/repeat/raw-below-basefee-trace.md) | Besu Development, Besu Release |
| [repeat/raw-insufficient-funds](cases/repeat/raw-insufficient-funds.md) | Besu Development, Besu Release |
| [repeat/raw-insufficient-funds-trace](cases/repeat/raw-insufficient-funds-trace.md) | Besu Development, Besu Release |
| [repeat/raw-low-gas](cases/repeat/raw-low-gas.md) | Besu Development, Besu Release |
| [repeat/raw-low-gas-trace](cases/repeat/raw-low-gas-trace.md) | Besu Development, Besu Release |
| [repeat/raw-nonce-high](cases/repeat/raw-nonce-high.md) | Besu Development, Besu Release |
| [repeat/raw-nonce-high-stateDiff](cases/repeat/raw-nonce-high-stateDiff.md) | Nethermind Development, Nethermind Release |
| [repeat/raw-nonce-high-trace](cases/repeat/raw-nonce-high-trace.md) | Besu Development, Besu Release |
| [repeat/raw-valid-stateDiff](cases/repeat/raw-valid-stateDiff.md) | Nethermind Development, Nethermind Release |
| [repeat/state-only-nonempty-output](cases/repeat/state-only-nonempty-output.md) | Nethermind Development, Nethermind Release |

## Runs

| Run | Corpus | Capture complete |
| --- | --- | --- |
| [geth-e29edff-a](../evidence/2026-09-21/geth-e29edff-a/manifest.json) | a | Yes |
| [geth-e29edff-fork-followup](../evidence/2026-09-21/geth-e29edff-fork-followup/manifest.json) | fork-followup | Yes |
| [geth-e29edff-forks](../evidence/2026-09-21/geth-e29edff-forks/manifest.json) | forks | Yes |
| [geth-e29edff-initial](../evidence/2026-09-21/geth-e29edff-initial/manifest.json) | initial | Yes |
| [geth-e29edff-precompiles](../evidence/2026-09-21/geth-e29edff-precompiles/manifest.json) | precompiles | Yes |
| [geth-e29edff-reorg-safe](../evidence/2026-09-21/geth-e29edff-reorg-safe/manifest.json) | reorg-safe | Yes |
| [geth-e29edff-repeat](../evidence/2026-09-21/geth-e29edff-repeat/manifest.json) | repeat | Yes |
| [precompiles-final](../evidence/2026-09-21/precompiles-final/manifest.json) | precompiles | Yes |
| [verified-a](../evidence/2026-09-21/verified-a/manifest.json) | a | No |
| [verified-a-besu-retry](../evidence/2026-09-21/verified-a-besu-retry/manifest.json) | a | Yes |
| [verified-fork-followup](../evidence/2026-09-21/verified-fork-followup/manifest.json) | fork-followup | No |
| [verified-fork-followup-besu-retry](../evidence/2026-09-21/verified-fork-followup-besu-retry/manifest.json) | fork-followup | Yes |
| [verified-forks](../evidence/2026-09-21/verified-forks/manifest.json) | forks | Yes |
| [verified-initial](../evidence/2026-09-21/verified-initial/manifest.json) | initial | Yes |
| [verified-pruned](../evidence/2026-09-21/verified-pruned/manifest.json) | pruned | No |
| [verified-pruned-ready](../evidence/2026-09-21/verified-pruned-ready/manifest.json) | pruned | Yes |
| [verified-reorg-ready](../evidence/2026-09-21/verified-reorg-ready/manifest.json) | reorg-safe | No |
| [verified-reorg-safe](../evidence/2026-09-21/verified-reorg-safe/manifest.json) | reorg-safe | No |
| [verified-repeat](../evidence/2026-09-21/verified-repeat/manifest.json) | repeat | Yes |
| [precompile-values-geth](../evidence/2026-09-23/precompile-values-geth/manifest.json) | precompile-values | Yes |
| [precompile-values-native](../evidence/2026-09-23/precompile-values-native/manifest.json) | precompile-values | Yes |
| [pruned-review](../evidence/2026-09-23/pruned-review/manifest.json) | pruned | Yes |
