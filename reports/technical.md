# Technical appendix

[Back to the maintainer overview](README.md)

The human reports summarize selected assertions against a proposed specification. Agreement is not full conformance, and an RPC error can be the correct result for an invalid-input case. Setup failures are excluded from semantic assessment. Release and development labels refer to the captured builds; they do not imply version ordering.

The experimental Geth fork implements the draft and is not an independent vote for its decisions. No verified pruning scenario is included for that fork.

## Test status key

- ✅ **Checked cases agree:** the evaluated cases match the proposed contract; not full conformance.
- ⚠️ **Differs:** at least one checked assertion differs from the proposal.
- ⛔ **Method unavailable:** the tested method is unsupported.
- 🟡 **Partially assessed:** some declared cases or topics were not evaluated.
- ⚪ **Not assessed:** no evaluated assertion establishes an outcome.
- 🚧 **Blocked:** a missing response, failed setup or earlier failure prevents this check.
- 🔎 **Control / not applicable:** reference evidence or a property that does not apply; never a semantic pass.
- ❔ **Policy open:** observed behavior is recorded without a settled assertion.

Build labels: 📦 **Release** · 🛠️ **Development** · 🧪 **Draft fork**. These identify build channels, not test outcomes. Test outcomes are separate from [policy agreement and harmonization](../decisions/README.md#status-key).

## Reproduction and machine-readable results

See [usage](../docs/usage.md) for commands and [stateful scenarios](../docs/scenarios.md) for setup requirements. [checks.json](checks.json) retains every assertion; [comparisons.json](comparisons.json) groups exact responses; [assessment.json](assessment.json) pins the specification and assessment source hashes. Each case links its original response and run manifest.

To reproduce one case, use its linked manifest and the exact client, corpus and case name:

```sh
uv run trace-interop run --lock evidence/2026-09-21/RUN/manifest.json \
  --clients CLIENT --corpus CORPUS --case "^CASE$" --output runs/reproduce
```

## Assertion coverage

Coverage below counts all selected trace observations, including missing responses and failed setup, separately from schema validation. Partially assessed means at least one declared topic was not checked. A checked assertion is not proof of the rest of the topic.

| Coverage | Observations |
| --- | --- |
| 🔎 Assessed | 8090 |
| 🟡 Partial | 1112 |
| ⚪ Unassessed | 120 |
| 🚧 Blocked | 275 |
| 🔎 Control | 9 |


### Unevaluated properties

Each row names the reason; controls and inapplicable properties do not count as passes. Counts are topic obligations, so one response may appear more than once.

| Topic | Disposition | Reason | Observations |
| --- | --- | --- | --- |
| H06 | blocked | Cannot inspect this property: unsupported. | 2 |
| H06 | control | Ledger reference; executable requirements are assessed by the linked topic cases. | 2 |
| H07 | blocked | Cannot inspect this property: unsupported. | 24 |
| H07 | control | Ledger reference; executable requirements are assessed by the linked topic cases. | 9 |
| H08 | blocked | Cannot inspect this property: unsupported. | 8 |
| H08 | blocked | The RPC returned an error, so there is no execution result to inspect. | 4 |
| H09 | blocked | Address selection differs from its reference; failure-bearing frame selection is not established. | 4 |
| H09 | blocked | Cannot inspect this property: unsupported. | 4 |
| H09 | blocked | The RPC returned an error, so there is no execution result to inspect. | 8 |
| H09 | not_applicable | No failed frame is selected; the address-filter assertion independently checks the selected inventory. | 7 |
| H13 | blocked | Cannot inspect this property: malformed_json. | 72 |
| H14 | control | Ledger reference; executable requirements are assessed by the linked topic cases. | 18 |
| H15 | blocked | A generic/internal/crash error does not prove validation: internal error | 262 |
| H15 | blocked | A generic/internal/crash error does not prove validation: method handler crashed | 5 |
| H15 | blocked | Cannot inspect this property: malformed_json. | 406 |
| H15 | unassessed | Omitted/incomplete fee fields have no agreed normalization rule; no conformance verdict. | 692 |
| H16 | blocked | Cannot inspect this property: unsupported. | 2 |
| H16 | blocked | No receipt gas or execution-gas witness was captured. | 8 |
| H16 | blocked | The RPC returned an error, so there is no execution result to inspect. | 4 |
| H16 | not_applicable | The signed transaction was correctly rejected before execution; execution-result properties do not apply. | 3 |
| H17 | blocked | Cannot inspect this property: unsupported. | 2 |
| H17 | blocked | The RPC returned an error, so there is no execution result to inspect. | 8 |
| H17 | not_applicable | The explicit block-selector extension is outside the two-argument baseline; H12 records its unresolved behavior. | 9 |
| H17 | not_applicable | The signed transaction was correctly rejected before execution; execution-result properties do not apply. | 3 |
| H18 | blocked | Cannot inspect this property: unsupported. | 2 |
| H19 | blocked | Cannot inspect this property: unsupported. | 2 |
| H19 | blocked | The RPC returned an error, so there is no execution result to inspect. | 12 |
| H20 | blocked | Cannot inspect this property: unsupported. | 4 |
| H20 | blocked | The RPC returned an error, so there is no execution result to inspect. | 12 |
| H21 | blocked | Cannot inspect this property: unsupported. | 4 |
| H21 | blocked | The RPC returned an error, so there is no execution result to inspect. | 12 |
| H23 | control | Ledger reference; executable requirements are assessed by the linked topic cases. | 9 |
| H27 | blocked | Per-block reference unavailable: rpc_error | 2 |
| H27 | control | Ledger reference; executable requirements are assessed by the linked topic cases. | 18 |
| H27 | control | Per-block reference response for the filter comparison. | 54 |
| H30 | control | Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion. | 9 |
| H32 | control | Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion. | 9 |

Eligibility is recomputed from the frozen head and independent scenario controls. `capture_eligible` in checks.json preserves the original capture decision; original summaries and wire observations are unchanged.

## Setup gaps

| Build | Scenario | Run evidence |
| --- | --- | --- |
| Erigon · 🛠️ Development | reorg-safe | [reorg-safe](../evidence/2026-09-24/coverage-matrix/reorg-safe/summary.json) |

## Result-shape checks

These cases returned results that differ from the draft schema. The case pages retain the validation details; an unclassified schema failure is not silently counted as agreement.

| Case | Affected builds |
| --- | --- |
| [a/auth-replace](cases/a/auth-replace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/auth-set](cases/a/auth-set.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/auth-set-revert](cases/a/auth-set-revert.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/block-2](cases/a/block-2.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/block-3](cases/a/block-3.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/call-gas7400](cases/a/call-gas7400.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/call-mcopy](cases/a/call-mcopy.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/call-mixed-create](cases/a/call-mixed-create.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/call-return42](cases/a/call-return42.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/call-siblings-ok-revert](cases/a/call-siblings-ok-revert.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/call-siblings-revert-ok](cases/a/call-siblings-revert-ok.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/filter-all](cases/a/filter-all.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/filter-both-null](cases/a/filter-both-null.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/filter-creator-from](cases/a/filter-creator-from.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/filter-from-null](cases/a/filter-from-null.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/filter-from-only-intersection](cases/a/filter-from-only-intersection.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/filter-from-only-union](cases/a/filter-from-only-union.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/filter-page-0](cases/a/filter-page-0.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/filter-page-1](cases/a/filter-page-1.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/filter-page-2](cases/a/filter-page-2.md) | Besu 🛠️ Development, Besu 📦 Release |
| [a/filter-snapshot](cases/a/filter-snapshot.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/filter-to-empty-from-set](cases/a/filter-to-empty-from-set.md) | Besu 🛠️ Development, Besu 📦 Release |
| [a/filter-to-null](cases/a/filter-to-null.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/filter-two-blocks](cases/a/filter-two-blocks.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/filter-unknown-field](cases/a/filter-unknown-field.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/filter-wrong-address-type](cases/a/filter-wrong-address-type.md) | Besu 🛠️ Development, Besu 📦 Release |
| [a/get-integer-path](cases/a/get-integer-path.md) | Nethermind 📦 Release |
| [a/get-nested-parent](cases/a/get-nested-parent.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/get-nested-positive](cases/a/get-nested-positive.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/many-storage-write-revert-read](cases/a/many-storage-write-revert-read.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/missing-block-block](cases/a/missing-block-block.md) | Besu 🛠️ Development, Besu 📦 Release |
| [a/raw-below-basefee](cases/a/raw-below-basefee.md) | Besu 🛠️ Development, Besu 📦 Release |
| [a/raw-insufficient-funds](cases/a/raw-insufficient-funds.md) | Besu 🛠️ Development, Besu 📦 Release |
| [a/raw-low-gas](cases/a/raw-low-gas.md) | Besu 🛠️ Development, Besu 📦 Release |
| [a/raw-nonce-high](cases/a/raw-nonce-high.md) | Besu 🛠️ Development, Besu 📦 Release |
| [a/state-only-nonempty-output](cases/a/state-only-nonempty-output.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/transaction-tree](cases/a/transaction-tree.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [a/vm-only-nonempty-output](cases/a/vm-only-nonempty-output.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [callmany-isolation/write-revert-read/many-storage-write-revert-read](cases/callmany-isolation/write-revert-read/many-storage-write-revert-read.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [coverage/model-empty-runtime](cases/coverage/model-empty-runtime.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [coverage/model-environment](cases/coverage/model-environment.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [coverage/model-environment-free](cases/coverage/model-environment-free.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [coverage/model-mcopy](cases/coverage/model-mcopy.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [coverage/model-mcopy-overlap](cases/coverage/model-mcopy-overlap.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [coverage/model-mcopy-zero](cases/coverage/model-mcopy-zero.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [coverage/model-mload-existing](cases/coverage/model-mload-existing.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [coverage/model-mload-expansion](cases/coverage/model-mload-expansion.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [coverage/model-return42](cases/coverage/model-return42.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [coverage/model-revert](cases/coverage/model-revert.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/defaults-cap-only-positive/call/stateDiff](cases/fee-policy/defaults-cap-only-positive/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-positive/call/stateDiff-vmTrace](cases/fee-policy/defaults-cap-only-positive/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-positive/call/trace-stateDiff-vmTrace](cases/fee-policy/defaults-cap-only-positive/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-positive/call/trace-vmTrace](cases/fee-policy/defaults-cap-only-positive/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-positive/call/vmTrace](cases/fee-policy/defaults-cap-only-positive/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-positive/many/stateDiff](cases/fee-policy/defaults-cap-only-positive/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-positive/many/stateDiff-vmTrace](cases/fee-policy/defaults-cap-only-positive/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-positive/many/trace-stateDiff-vmTrace](cases/fee-policy/defaults-cap-only-positive/many/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-positive/many/trace-vmTrace](cases/fee-policy/defaults-cap-only-positive/many/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-positive/many/vmTrace](cases/fee-policy/defaults-cap-only-positive/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-zero/call/stateDiff](cases/fee-policy/defaults-cap-only-zero/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-zero/call/stateDiff-vmTrace](cases/fee-policy/defaults-cap-only-zero/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-zero/call/trace-stateDiff-vmTrace](cases/fee-policy/defaults-cap-only-zero/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-zero/call/trace-vmTrace](cases/fee-policy/defaults-cap-only-zero/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-zero/call/vmTrace](cases/fee-policy/defaults-cap-only-zero/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-zero/many/none](cases/fee-policy/defaults-cap-only-zero/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/defaults-cap-only-zero/many/stateDiff](cases/fee-policy/defaults-cap-only-zero/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-zero/many/stateDiff-vmTrace](cases/fee-policy/defaults-cap-only-zero/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-zero/many/trace](cases/fee-policy/defaults-cap-only-zero/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/defaults-cap-only-zero/many/trace-stateDiff](cases/fee-policy/defaults-cap-only-zero/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/defaults-cap-only-zero/many/trace-stateDiff-vmTrace](cases/fee-policy/defaults-cap-only-zero/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-zero/many/trace-vmTrace](cases/fee-policy/defaults-cap-only-zero/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-cap-only-zero/many/vmTrace](cases/fee-policy/defaults-cap-only-zero/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-omitted/call/stateDiff](cases/fee-policy/defaults-omitted/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-omitted/call/stateDiff-vmTrace](cases/fee-policy/defaults-omitted/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-omitted/call/trace-stateDiff-vmTrace](cases/fee-policy/defaults-omitted/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-omitted/call/trace-vmTrace](cases/fee-policy/defaults-omitted/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-omitted/call/vmTrace](cases/fee-policy/defaults-omitted/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-omitted/many/stateDiff](cases/fee-policy/defaults-omitted/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-omitted/many/stateDiff-vmTrace](cases/fee-policy/defaults-omitted/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-omitted/many/trace-stateDiff-vmTrace](cases/fee-policy/defaults-omitted/many/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-omitted/many/trace-vmTrace](cases/fee-policy/defaults-omitted/many/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-omitted/many/vmTrace](cases/fee-policy/defaults-omitted/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-tip-only-positive/many/none](cases/fee-policy/defaults-tip-only-positive/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/defaults-tip-only-positive/many/stateDiff](cases/fee-policy/defaults-tip-only-positive/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/defaults-tip-only-positive/many/stateDiff-vmTrace](cases/fee-policy/defaults-tip-only-positive/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/defaults-tip-only-positive/many/trace](cases/fee-policy/defaults-tip-only-positive/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/defaults-tip-only-positive/many/trace-stateDiff](cases/fee-policy/defaults-tip-only-positive/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/defaults-tip-only-positive/many/trace-stateDiff-vmTrace](cases/fee-policy/defaults-tip-only-positive/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/defaults-tip-only-positive/many/trace-vmTrace](cases/fee-policy/defaults-tip-only-positive/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/defaults-tip-only-positive/many/vmTrace](cases/fee-policy/defaults-tip-only-positive/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/defaults-tip-only-zero/call/stateDiff](cases/fee-policy/defaults-tip-only-zero/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-tip-only-zero/call/stateDiff-vmTrace](cases/fee-policy/defaults-tip-only-zero/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-tip-only-zero/call/trace-stateDiff-vmTrace](cases/fee-policy/defaults-tip-only-zero/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-tip-only-zero/call/trace-vmTrace](cases/fee-policy/defaults-tip-only-zero/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-tip-only-zero/call/vmTrace](cases/fee-policy/defaults-tip-only-zero/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-tip-only-zero/many/none](cases/fee-policy/defaults-tip-only-zero/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/defaults-tip-only-zero/many/stateDiff](cases/fee-policy/defaults-tip-only-zero/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-tip-only-zero/many/stateDiff-vmTrace](cases/fee-policy/defaults-tip-only-zero/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-tip-only-zero/many/trace](cases/fee-policy/defaults-tip-only-zero/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/defaults-tip-only-zero/many/trace-stateDiff](cases/fee-policy/defaults-tip-only-zero/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/defaults-tip-only-zero/many/trace-stateDiff-vmTrace](cases/fee-policy/defaults-tip-only-zero/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-tip-only-zero/many/trace-vmTrace](cases/fee-policy/defaults-tip-only-zero/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/defaults-tip-only-zero/many/vmTrace](cases/fee-policy/defaults-tip-only-zero/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/empty-sender-free/call/stateDiff](cases/fee-policy/empty-sender-free/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/empty-sender-free/call/stateDiff-vmTrace](cases/fee-policy/empty-sender-free/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/empty-sender-free/call/trace-stateDiff-vmTrace](cases/fee-policy/empty-sender-free/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/empty-sender-free/call/trace-vmTrace](cases/fee-policy/empty-sender-free/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/empty-sender-free/call/vmTrace](cases/fee-policy/empty-sender-free/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/empty-sender-free/many/none](cases/fee-policy/empty-sender-free/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/empty-sender-free/many/stateDiff](cases/fee-policy/empty-sender-free/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/empty-sender-free/many/stateDiff-vmTrace](cases/fee-policy/empty-sender-free/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/empty-sender-free/many/trace](cases/fee-policy/empty-sender-free/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/empty-sender-free/many/trace-stateDiff](cases/fee-policy/empty-sender-free/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/empty-sender-free/many/trace-stateDiff-vmTrace](cases/fee-policy/empty-sender-free/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/empty-sender-free/many/trace-vmTrace](cases/fee-policy/empty-sender-free/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/empty-sender-free/many/vmTrace](cases/fee-policy/empty-sender-free/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/empty-sender-priced/many/none](cases/fee-policy/empty-sender-priced/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/empty-sender-priced/many/stateDiff](cases/fee-policy/empty-sender-priced/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/empty-sender-priced/many/stateDiff-vmTrace](cases/fee-policy/empty-sender-priced/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/empty-sender-priced/many/trace](cases/fee-policy/empty-sender-priced/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/empty-sender-priced/many/trace-stateDiff](cases/fee-policy/empty-sender-priced/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/empty-sender-priced/many/trace-stateDiff-vmTrace](cases/fee-policy/empty-sender-priced/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/empty-sender-priced/many/trace-vmTrace](cases/fee-policy/empty-sender-priced/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/empty-sender-priced/many/vmTrace](cases/fee-policy/empty-sender-priced/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-free-exact/call/stateDiff](cases/fee-policy/funding-free-exact/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-free-exact/call/stateDiff-vmTrace](cases/fee-policy/funding-free-exact/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-free-exact/call/trace-stateDiff-vmTrace](cases/fee-policy/funding-free-exact/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-free-exact/call/trace-vmTrace](cases/fee-policy/funding-free-exact/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-free-exact/call/vmTrace](cases/fee-policy/funding-free-exact/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-free-exact/many/none](cases/fee-policy/funding-free-exact/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-free-exact/many/stateDiff](cases/fee-policy/funding-free-exact/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-free-exact/many/stateDiff-vmTrace](cases/fee-policy/funding-free-exact/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-free-exact/many/trace](cases/fee-policy/funding-free-exact/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-free-exact/many/trace-stateDiff](cases/fee-policy/funding-free-exact/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-free-exact/many/trace-stateDiff-vmTrace](cases/fee-policy/funding-free-exact/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-free-exact/many/trace-vmTrace](cases/fee-policy/funding-free-exact/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-free-exact/many/vmTrace](cases/fee-policy/funding-free-exact/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-free-short/many/none](cases/fee-policy/funding-free-short/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-free-short/many/stateDiff](cases/fee-policy/funding-free-short/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-free-short/many/stateDiff-vmTrace](cases/fee-policy/funding-free-short/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-free-short/many/trace](cases/fee-policy/funding-free-short/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-free-short/many/trace-stateDiff](cases/fee-policy/funding-free-short/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-free-short/many/trace-stateDiff-vmTrace](cases/fee-policy/funding-free-short/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-free-short/many/trace-vmTrace](cases/fee-policy/funding-free-short/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-free-short/many/vmTrace](cases/fee-policy/funding-free-short/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-legacy-exact/call/stateDiff](cases/fee-policy/funding-legacy-exact/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-legacy-exact/call/stateDiff-vmTrace](cases/fee-policy/funding-legacy-exact/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-legacy-exact/call/trace-stateDiff-vmTrace](cases/fee-policy/funding-legacy-exact/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-legacy-exact/call/trace-vmTrace](cases/fee-policy/funding-legacy-exact/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-legacy-exact/call/vmTrace](cases/fee-policy/funding-legacy-exact/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-legacy-exact/many/stateDiff](cases/fee-policy/funding-legacy-exact/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-legacy-exact/many/stateDiff-vmTrace](cases/fee-policy/funding-legacy-exact/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-legacy-exact/many/trace-stateDiff-vmTrace](cases/fee-policy/funding-legacy-exact/many/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-legacy-exact/many/trace-vmTrace](cases/fee-policy/funding-legacy-exact/many/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-legacy-exact/many/vmTrace](cases/fee-policy/funding-legacy-exact/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-legacy-short/many/none](cases/fee-policy/funding-legacy-short/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-legacy-short/many/stateDiff](cases/fee-policy/funding-legacy-short/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-legacy-short/many/stateDiff-vmTrace](cases/fee-policy/funding-legacy-short/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-legacy-short/many/trace](cases/fee-policy/funding-legacy-short/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-legacy-short/many/trace-stateDiff](cases/fee-policy/funding-legacy-short/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-legacy-short/many/trace-stateDiff-vmTrace](cases/fee-policy/funding-legacy-short/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-legacy-short/many/trace-vmTrace](cases/fee-policy/funding-legacy-short/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-legacy-short/many/vmTrace](cases/fee-policy/funding-legacy-short/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-effective-only/many/none](cases/fee-policy/funding-typed-effective-only/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-effective-only/many/stateDiff](cases/fee-policy/funding-typed-effective-only/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-effective-only/many/stateDiff-vmTrace](cases/fee-policy/funding-typed-effective-only/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-effective-only/many/trace](cases/fee-policy/funding-typed-effective-only/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-effective-only/many/trace-stateDiff](cases/fee-policy/funding-typed-effective-only/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-effective-only/many/trace-stateDiff-vmTrace](cases/fee-policy/funding-typed-effective-only/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-effective-only/many/trace-vmTrace](cases/fee-policy/funding-typed-effective-only/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-effective-only/many/vmTrace](cases/fee-policy/funding-typed-effective-only/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-exact/call/stateDiff](cases/fee-policy/funding-typed-exact/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-exact/call/stateDiff-vmTrace](cases/fee-policy/funding-typed-exact/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-exact/call/trace-stateDiff-vmTrace](cases/fee-policy/funding-typed-exact/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-exact/call/trace-vmTrace](cases/fee-policy/funding-typed-exact/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-exact/call/vmTrace](cases/fee-policy/funding-typed-exact/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-exact/many/stateDiff](cases/fee-policy/funding-typed-exact/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-exact/many/stateDiff-vmTrace](cases/fee-policy/funding-typed-exact/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-exact/many/trace-stateDiff-vmTrace](cases/fee-policy/funding-typed-exact/many/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-exact/many/trace-vmTrace](cases/fee-policy/funding-typed-exact/many/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-exact/many/vmTrace](cases/fee-policy/funding-typed-exact/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-free-exact/call/stateDiff](cases/fee-policy/funding-typed-free-exact/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-free-exact/call/stateDiff-vmTrace](cases/fee-policy/funding-typed-free-exact/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-free-exact/call/trace-stateDiff-vmTrace](cases/fee-policy/funding-typed-free-exact/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-free-exact/call/trace-vmTrace](cases/fee-policy/funding-typed-free-exact/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-free-exact/call/vmTrace](cases/fee-policy/funding-typed-free-exact/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-free-exact/many/none](cases/fee-policy/funding-typed-free-exact/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-free-exact/many/stateDiff](cases/fee-policy/funding-typed-free-exact/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-free-exact/many/stateDiff-vmTrace](cases/fee-policy/funding-typed-free-exact/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-free-exact/many/trace](cases/fee-policy/funding-typed-free-exact/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-free-exact/many/trace-stateDiff](cases/fee-policy/funding-typed-free-exact/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-free-exact/many/trace-stateDiff-vmTrace](cases/fee-policy/funding-typed-free-exact/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-free-exact/many/trace-vmTrace](cases/fee-policy/funding-typed-free-exact/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-free-exact/many/vmTrace](cases/fee-policy/funding-typed-free-exact/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/funding-typed-free-short/many/none](cases/fee-policy/funding-typed-free-short/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-free-short/many/stateDiff](cases/fee-policy/funding-typed-free-short/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-free-short/many/stateDiff-vmTrace](cases/fee-policy/funding-typed-free-short/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-free-short/many/trace](cases/fee-policy/funding-typed-free-short/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-free-short/many/trace-stateDiff](cases/fee-policy/funding-typed-free-short/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-free-short/many/trace-stateDiff-vmTrace](cases/fee-policy/funding-typed-free-short/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-free-short/many/trace-vmTrace](cases/fee-policy/funding-typed-free-short/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-free-short/many/vmTrace](cases/fee-policy/funding-typed-free-short/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-short/many/none](cases/fee-policy/funding-typed-short/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-short/many/stateDiff](cases/fee-policy/funding-typed-short/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-short/many/stateDiff-vmTrace](cases/fee-policy/funding-typed-short/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-short/many/trace](cases/fee-policy/funding-typed-short/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-short/many/trace-stateDiff](cases/fee-policy/funding-typed-short/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-short/many/trace-stateDiff-vmTrace](cases/fee-policy/funding-typed-short/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-short/many/trace-vmTrace](cases/fee-policy/funding-typed-short/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/funding-typed-short/many/vmTrace](cases/fee-policy/funding-typed-short/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-above-base/call/stateDiff](cases/fee-policy/legacy-above-base/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-above-base/call/stateDiff-vmTrace](cases/fee-policy/legacy-above-base/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-above-base/call/trace-stateDiff-vmTrace](cases/fee-policy/legacy-above-base/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-above-base/call/trace-vmTrace](cases/fee-policy/legacy-above-base/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-above-base/call/vmTrace](cases/fee-policy/legacy-above-base/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-above-base/many/stateDiff](cases/fee-policy/legacy-above-base/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-above-base/many/stateDiff-vmTrace](cases/fee-policy/legacy-above-base/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-above-base/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-above-base/many/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-above-base/many/trace-vmTrace](cases/fee-policy/legacy-above-base/many/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-above-base/many/vmTrace](cases/fee-policy/legacy-above-base/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-at-base/call/stateDiff](cases/fee-policy/legacy-at-base/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-at-base/call/stateDiff-vmTrace](cases/fee-policy/legacy-at-base/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-at-base/call/trace-stateDiff-vmTrace](cases/fee-policy/legacy-at-base/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-at-base/call/trace-vmTrace](cases/fee-policy/legacy-at-base/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-at-base/call/vmTrace](cases/fee-policy/legacy-at-base/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-at-base/many/stateDiff](cases/fee-policy/legacy-at-base/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-at-base/many/stateDiff-vmTrace](cases/fee-policy/legacy-at-base/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-at-base/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-at-base/many/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-at-base/many/trace-vmTrace](cases/fee-policy/legacy-at-base/many/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-at-base/many/vmTrace](cases/fee-policy/legacy-at-base/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-below-base/many/none](cases/fee-policy/legacy-below-base/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-below-base/many/stateDiff](cases/fee-policy/legacy-below-base/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-below-base/many/stateDiff-vmTrace](cases/fee-policy/legacy-below-base/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-below-base/many/trace](cases/fee-policy/legacy-below-base/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-below-base/many/trace-stateDiff](cases/fee-policy/legacy-below-base/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-below-base/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-below-base/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-below-base/many/trace-vmTrace](cases/fee-policy/legacy-below-base/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-below-base/many/vmTrace](cases/fee-policy/legacy-below-base/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-one/many/none](cases/fee-policy/legacy-one/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-one/many/stateDiff](cases/fee-policy/legacy-one/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-one/many/stateDiff-vmTrace](cases/fee-policy/legacy-one/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-one/many/trace](cases/fee-policy/legacy-one/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-one/many/trace-stateDiff](cases/fee-policy/legacy-one/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-one/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-one/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-one/many/trace-vmTrace](cases/fee-policy/legacy-one/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-one/many/vmTrace](cases/fee-policy/legacy-one/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-out-of-gas-then-observe/many/stateDiff](cases/fee-policy/legacy-out-of-gas-then-observe/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-out-of-gas-then-observe/many/stateDiff-vmTrace](cases/fee-policy/legacy-out-of-gas-then-observe/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-out-of-gas-then-observe/many/trace](cases/fee-policy/legacy-out-of-gas-then-observe/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-out-of-gas-then-observe/many/trace-stateDiff](cases/fee-policy/legacy-out-of-gas-then-observe/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-out-of-gas-then-observe/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-out-of-gas-then-observe/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-out-of-gas-then-observe/many/trace-vmTrace](cases/fee-policy/legacy-out-of-gas-then-observe/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-out-of-gas-then-observe/many/vmTrace](cases/fee-policy/legacy-out-of-gas-then-observe/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-out-of-gas/call/stateDiff](cases/fee-policy/legacy-out-of-gas/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-out-of-gas/call/stateDiff-vmTrace](cases/fee-policy/legacy-out-of-gas/call/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-out-of-gas/call/trace](cases/fee-policy/legacy-out-of-gas/call/trace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-out-of-gas/call/trace-stateDiff](cases/fee-policy/legacy-out-of-gas/call/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-out-of-gas/call/trace-stateDiff-vmTrace](cases/fee-policy/legacy-out-of-gas/call/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-out-of-gas/call/trace-vmTrace](cases/fee-policy/legacy-out-of-gas/call/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-out-of-gas/call/vmTrace](cases/fee-policy/legacy-out-of-gas/call/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-out-of-gas/many/stateDiff](cases/fee-policy/legacy-out-of-gas/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-out-of-gas/many/stateDiff-vmTrace](cases/fee-policy/legacy-out-of-gas/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-out-of-gas/many/trace](cases/fee-policy/legacy-out-of-gas/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-out-of-gas/many/trace-stateDiff](cases/fee-policy/legacy-out-of-gas/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-out-of-gas/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-out-of-gas/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-out-of-gas/many/trace-vmTrace](cases/fee-policy/legacy-out-of-gas/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-out-of-gas/many/vmTrace](cases/fee-policy/legacy-out-of-gas/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-refund-then-observe/many/stateDiff](cases/fee-policy/legacy-refund-then-observe/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-refund-then-observe/many/stateDiff-vmTrace](cases/fee-policy/legacy-refund-then-observe/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-refund-then-observe/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-refund-then-observe/many/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-refund-then-observe/many/trace-vmTrace](cases/fee-policy/legacy-refund-then-observe/many/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-refund-then-observe/many/vmTrace](cases/fee-policy/legacy-refund-then-observe/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-refund/call/stateDiff](cases/fee-policy/legacy-refund/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-refund/call/stateDiff-vmTrace](cases/fee-policy/legacy-refund/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-refund/call/trace-stateDiff-vmTrace](cases/fee-policy/legacy-refund/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-refund/call/trace-vmTrace](cases/fee-policy/legacy-refund/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-refund/call/vmTrace](cases/fee-policy/legacy-refund/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-refund/many/stateDiff](cases/fee-policy/legacy-refund/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-refund/many/stateDiff-vmTrace](cases/fee-policy/legacy-refund/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-refund/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-refund/many/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-refund/many/trace-vmTrace](cases/fee-policy/legacy-refund/many/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-refund/many/vmTrace](cases/fee-policy/legacy-refund/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-revert-then-observe/many/stateDiff](cases/fee-policy/legacy-revert-then-observe/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-revert-then-observe/many/stateDiff-vmTrace](cases/fee-policy/legacy-revert-then-observe/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-revert-then-observe/many/trace](cases/fee-policy/legacy-revert-then-observe/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/legacy-revert-then-observe/many/trace-stateDiff](cases/fee-policy/legacy-revert-then-observe/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/legacy-revert-then-observe/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-revert-then-observe/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/legacy-revert-then-observe/many/trace-vmTrace](cases/fee-policy/legacy-revert-then-observe/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/legacy-revert-then-observe/many/vmTrace](cases/fee-policy/legacy-revert-then-observe/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-revert/call/stateDiff](cases/fee-policy/legacy-revert/call/stateDiff.md) | Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-revert/call/stateDiff-vmTrace](cases/fee-policy/legacy-revert/call/stateDiff-vmTrace.md) | Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-revert/call/trace](cases/fee-policy/legacy-revert/call/trace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/legacy-revert/call/trace-stateDiff](cases/fee-policy/legacy-revert/call/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/legacy-revert/call/trace-stateDiff-vmTrace](cases/fee-policy/legacy-revert/call/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/legacy-revert/call/trace-vmTrace](cases/fee-policy/legacy-revert/call/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/legacy-revert/call/vmTrace](cases/fee-policy/legacy-revert/call/vmTrace.md) | Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-revert/many/stateDiff](cases/fee-policy/legacy-revert/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-revert/many/stateDiff-vmTrace](cases/fee-policy/legacy-revert/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-revert/many/trace](cases/fee-policy/legacy-revert/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/legacy-revert/many/trace-stateDiff](cases/fee-policy/legacy-revert/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/legacy-revert/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-revert/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/legacy-revert/many/trace-vmTrace](cases/fee-policy/legacy-revert/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/legacy-revert/many/vmTrace](cases/fee-policy/legacy-revert/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-zero/call/stateDiff](cases/fee-policy/legacy-zero/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-zero/call/stateDiff-vmTrace](cases/fee-policy/legacy-zero/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-zero/call/trace-stateDiff-vmTrace](cases/fee-policy/legacy-zero/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-zero/call/trace-vmTrace](cases/fee-policy/legacy-zero/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-zero/call/vmTrace](cases/fee-policy/legacy-zero/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-zero/many/none](cases/fee-policy/legacy-zero/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-zero/many/stateDiff](cases/fee-policy/legacy-zero/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-zero/many/stateDiff-vmTrace](cases/fee-policy/legacy-zero/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-zero/many/trace](cases/fee-policy/legacy-zero/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-zero/many/trace-stateDiff](cases/fee-policy/legacy-zero/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/legacy-zero/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-zero/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-zero/many/trace-vmTrace](cases/fee-policy/legacy-zero/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/legacy-zero/many/vmTrace](cases/fee-policy/legacy-zero/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-legacy-free-priced-free/many/none](cases/fee-policy/mixed-legacy-free-priced-free/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-free-priced-free/many/stateDiff](cases/fee-policy/mixed-legacy-free-priced-free/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-legacy-free-priced-free/many/stateDiff-vmTrace](cases/fee-policy/mixed-legacy-free-priced-free/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-legacy-free-priced-free/many/trace](cases/fee-policy/mixed-legacy-free-priced-free/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-free-priced-free/many/trace-stateDiff](cases/fee-policy/mixed-legacy-free-priced-free/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-free-priced-free/many/trace-stateDiff-vmTrace](cases/fee-policy/mixed-legacy-free-priced-free/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-legacy-free-priced-free/many/trace-vmTrace](cases/fee-policy/mixed-legacy-free-priced-free/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-legacy-free-priced-free/many/vmTrace](cases/fee-policy/mixed-legacy-free-priced-free/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-legacy-free-then-invalid/many/none](cases/fee-policy/mixed-legacy-free-then-invalid/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-free-then-invalid/many/stateDiff](cases/fee-policy/mixed-legacy-free-then-invalid/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-free-then-invalid/many/stateDiff-vmTrace](cases/fee-policy/mixed-legacy-free-then-invalid/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-free-then-invalid/many/trace](cases/fee-policy/mixed-legacy-free-then-invalid/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-free-then-invalid/many/trace-stateDiff](cases/fee-policy/mixed-legacy-free-then-invalid/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-free-then-invalid/many/trace-stateDiff-vmTrace](cases/fee-policy/mixed-legacy-free-then-invalid/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-free-then-invalid/many/trace-vmTrace](cases/fee-policy/mixed-legacy-free-then-invalid/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-free-then-invalid/many/vmTrace](cases/fee-policy/mixed-legacy-free-then-invalid/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-invalid-then-free/many/none](cases/fee-policy/mixed-legacy-invalid-then-free/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-invalid-then-free/many/stateDiff](cases/fee-policy/mixed-legacy-invalid-then-free/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-invalid-then-free/many/stateDiff-vmTrace](cases/fee-policy/mixed-legacy-invalid-then-free/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-invalid-then-free/many/trace](cases/fee-policy/mixed-legacy-invalid-then-free/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-invalid-then-free/many/trace-stateDiff](cases/fee-policy/mixed-legacy-invalid-then-free/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-invalid-then-free/many/trace-stateDiff-vmTrace](cases/fee-policy/mixed-legacy-invalid-then-free/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-invalid-then-free/many/trace-vmTrace](cases/fee-policy/mixed-legacy-invalid-then-free/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-invalid-then-free/many/vmTrace](cases/fee-policy/mixed-legacy-invalid-then-free/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-priced-free-priced/many/none](cases/fee-policy/mixed-legacy-priced-free-priced/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-priced-free-priced/many/stateDiff](cases/fee-policy/mixed-legacy-priced-free-priced/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-legacy-priced-free-priced/many/stateDiff-vmTrace](cases/fee-policy/mixed-legacy-priced-free-priced/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-legacy-priced-free-priced/many/trace](cases/fee-policy/mixed-legacy-priced-free-priced/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-priced-free-priced/many/trace-stateDiff](cases/fee-policy/mixed-legacy-priced-free-priced/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-priced-free-priced/many/trace-stateDiff-vmTrace](cases/fee-policy/mixed-legacy-priced-free-priced/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-legacy-priced-free-priced/many/trace-vmTrace](cases/fee-policy/mixed-legacy-priced-free-priced/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-legacy-priced-free-priced/many/vmTrace](cases/fee-policy/mixed-legacy-priced-free-priced/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-legacy-selections/many/none](cases/fee-policy/mixed-legacy-selections/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-selections/many/stateDiff](cases/fee-policy/mixed-legacy-selections/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-legacy-selections/many/stateDiff-vmTrace](cases/fee-policy/mixed-legacy-selections/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-selections/many/trace](cases/fee-policy/mixed-legacy-selections/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-legacy-selections/many/trace-stateDiff](cases/fee-policy/mixed-legacy-selections/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-legacy-selections/many/trace-stateDiff-vmTrace](cases/fee-policy/mixed-legacy-selections/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-legacy-selections/many/trace-vmTrace](cases/fee-policy/mixed-legacy-selections/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-legacy-selections/many/vmTrace](cases/fee-policy/mixed-legacy-selections/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-typed-free-priced-free/many/none](cases/fee-policy/mixed-typed-free-priced-free/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-free-priced-free/many/stateDiff](cases/fee-policy/mixed-typed-free-priced-free/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-typed-free-priced-free/many/stateDiff-vmTrace](cases/fee-policy/mixed-typed-free-priced-free/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-typed-free-priced-free/many/trace](cases/fee-policy/mixed-typed-free-priced-free/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-free-priced-free/many/trace-stateDiff](cases/fee-policy/mixed-typed-free-priced-free/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-free-priced-free/many/trace-stateDiff-vmTrace](cases/fee-policy/mixed-typed-free-priced-free/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-typed-free-priced-free/many/trace-vmTrace](cases/fee-policy/mixed-typed-free-priced-free/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-typed-free-priced-free/many/vmTrace](cases/fee-policy/mixed-typed-free-priced-free/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-typed-free-then-invalid/many/none](cases/fee-policy/mixed-typed-free-then-invalid/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-free-then-invalid/many/stateDiff](cases/fee-policy/mixed-typed-free-then-invalid/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-free-then-invalid/many/stateDiff-vmTrace](cases/fee-policy/mixed-typed-free-then-invalid/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-free-then-invalid/many/trace](cases/fee-policy/mixed-typed-free-then-invalid/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-free-then-invalid/many/trace-stateDiff](cases/fee-policy/mixed-typed-free-then-invalid/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-free-then-invalid/many/trace-stateDiff-vmTrace](cases/fee-policy/mixed-typed-free-then-invalid/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-free-then-invalid/many/trace-vmTrace](cases/fee-policy/mixed-typed-free-then-invalid/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-free-then-invalid/many/vmTrace](cases/fee-policy/mixed-typed-free-then-invalid/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-invalid-then-free/many/none](cases/fee-policy/mixed-typed-invalid-then-free/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-invalid-then-free/many/stateDiff](cases/fee-policy/mixed-typed-invalid-then-free/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-invalid-then-free/many/stateDiff-vmTrace](cases/fee-policy/mixed-typed-invalid-then-free/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-invalid-then-free/many/trace](cases/fee-policy/mixed-typed-invalid-then-free/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-invalid-then-free/many/trace-stateDiff](cases/fee-policy/mixed-typed-invalid-then-free/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-invalid-then-free/many/trace-stateDiff-vmTrace](cases/fee-policy/mixed-typed-invalid-then-free/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-invalid-then-free/many/trace-vmTrace](cases/fee-policy/mixed-typed-invalid-then-free/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-invalid-then-free/many/vmTrace](cases/fee-policy/mixed-typed-invalid-then-free/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-priced-free-priced/many/none](cases/fee-policy/mixed-typed-priced-free-priced/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-priced-free-priced/many/stateDiff](cases/fee-policy/mixed-typed-priced-free-priced/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-typed-priced-free-priced/many/stateDiff-vmTrace](cases/fee-policy/mixed-typed-priced-free-priced/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-typed-priced-free-priced/many/trace](cases/fee-policy/mixed-typed-priced-free-priced/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-priced-free-priced/many/trace-stateDiff](cases/fee-policy/mixed-typed-priced-free-priced/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-priced-free-priced/many/trace-stateDiff-vmTrace](cases/fee-policy/mixed-typed-priced-free-priced/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-typed-priced-free-priced/many/trace-vmTrace](cases/fee-policy/mixed-typed-priced-free-priced/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-typed-priced-free-priced/many/vmTrace](cases/fee-policy/mixed-typed-priced-free-priced/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-typed-selections/many/none](cases/fee-policy/mixed-typed-selections/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-selections/many/stateDiff](cases/fee-policy/mixed-typed-selections/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-typed-selections/many/stateDiff-vmTrace](cases/fee-policy/mixed-typed-selections/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-selections/many/trace](cases/fee-policy/mixed-typed-selections/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-typed-selections/many/trace-stateDiff](cases/fee-policy/mixed-typed-selections/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-typed-selections/many/trace-stateDiff-vmTrace](cases/fee-policy/mixed-typed-selections/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/mixed-typed-selections/many/trace-vmTrace](cases/fee-policy/mixed-typed-selections/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/mixed-typed-selections/many/vmTrace](cases/fee-policy/mixed-typed-selections/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/sequential-funding/many/none](cases/fee-policy/sequential-funding/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/sequential-funding/many/stateDiff](cases/fee-policy/sequential-funding/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/sequential-funding/many/stateDiff-vmTrace](cases/fee-policy/sequential-funding/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/sequential-funding/many/trace](cases/fee-policy/sequential-funding/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/sequential-funding/many/trace-stateDiff](cases/fee-policy/sequential-funding/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/sequential-funding/many/trace-stateDiff-vmTrace](cases/fee-policy/sequential-funding/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/sequential-funding/many/trace-vmTrace](cases/fee-policy/sequential-funding/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/sequential-funding/many/vmTrace](cases/fee-policy/sequential-funding/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-at-base/call/stateDiff](cases/fee-policy/typed-at-base/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-at-base/call/stateDiff-vmTrace](cases/fee-policy/typed-at-base/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-at-base/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-at-base/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-at-base/call/trace-vmTrace](cases/fee-policy/typed-at-base/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-at-base/call/vmTrace](cases/fee-policy/typed-at-base/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-at-base/many/stateDiff](cases/fee-policy/typed-at-base/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-at-base/many/stateDiff-vmTrace](cases/fee-policy/typed-at-base/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-at-base/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-at-base/many/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-at-base/many/trace-vmTrace](cases/fee-policy/typed-at-base/many/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-at-base/many/vmTrace](cases/fee-policy/typed-at-base/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-below-base-positive-tip/many/none](cases/fee-policy/typed-below-base-positive-tip/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-below-base-positive-tip/many/stateDiff](cases/fee-policy/typed-below-base-positive-tip/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-below-base-positive-tip/many/stateDiff-vmTrace](cases/fee-policy/typed-below-base-positive-tip/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-below-base-positive-tip/many/trace](cases/fee-policy/typed-below-base-positive-tip/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-below-base-positive-tip/many/trace-stateDiff](cases/fee-policy/typed-below-base-positive-tip/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-below-base-positive-tip/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-below-base-positive-tip/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-below-base-positive-tip/many/trace-vmTrace](cases/fee-policy/typed-below-base-positive-tip/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-below-base-positive-tip/many/vmTrace](cases/fee-policy/typed-below-base-positive-tip/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-below-base/many/none](cases/fee-policy/typed-below-base/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-below-base/many/stateDiff](cases/fee-policy/typed-below-base/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-below-base/many/stateDiff-vmTrace](cases/fee-policy/typed-below-base/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-below-base/many/trace](cases/fee-policy/typed-below-base/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-below-base/many/trace-stateDiff](cases/fee-policy/typed-below-base/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-below-base/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-below-base/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-below-base/many/trace-vmTrace](cases/fee-policy/typed-below-base/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-below-base/many/vmTrace](cases/fee-policy/typed-below-base/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-cap-limited/call/stateDiff](cases/fee-policy/typed-cap-limited/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-cap-limited/call/stateDiff-vmTrace](cases/fee-policy/typed-cap-limited/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-cap-limited/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-cap-limited/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-cap-limited/call/trace-vmTrace](cases/fee-policy/typed-cap-limited/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-cap-limited/call/vmTrace](cases/fee-policy/typed-cap-limited/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-cap-limited/many/stateDiff](cases/fee-policy/typed-cap-limited/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-cap-limited/many/stateDiff-vmTrace](cases/fee-policy/typed-cap-limited/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-cap-limited/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-cap-limited/many/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-cap-limited/many/trace-vmTrace](cases/fee-policy/typed-cap-limited/many/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-cap-limited/many/vmTrace](cases/fee-policy/typed-cap-limited/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-one/many/none](cases/fee-policy/typed-one/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-one/many/stateDiff](cases/fee-policy/typed-one/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-one/many/stateDiff-vmTrace](cases/fee-policy/typed-one/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-one/many/trace](cases/fee-policy/typed-one/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-one/many/trace-stateDiff](cases/fee-policy/typed-one/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-one/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-one/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-one/many/trace-vmTrace](cases/fee-policy/typed-one/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-one/many/vmTrace](cases/fee-policy/typed-one/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-out-of-gas-then-observe/many/stateDiff](cases/fee-policy/typed-out-of-gas-then-observe/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-out-of-gas-then-observe/many/stateDiff-vmTrace](cases/fee-policy/typed-out-of-gas-then-observe/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-out-of-gas-then-observe/many/trace](cases/fee-policy/typed-out-of-gas-then-observe/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-out-of-gas-then-observe/many/trace-stateDiff](cases/fee-policy/typed-out-of-gas-then-observe/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-out-of-gas-then-observe/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-out-of-gas-then-observe/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-out-of-gas-then-observe/many/trace-vmTrace](cases/fee-policy/typed-out-of-gas-then-observe/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-out-of-gas-then-observe/many/vmTrace](cases/fee-policy/typed-out-of-gas-then-observe/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-out-of-gas/call/stateDiff](cases/fee-policy/typed-out-of-gas/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-out-of-gas/call/stateDiff-vmTrace](cases/fee-policy/typed-out-of-gas/call/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-out-of-gas/call/trace](cases/fee-policy/typed-out-of-gas/call/trace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-out-of-gas/call/trace-stateDiff](cases/fee-policy/typed-out-of-gas/call/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-out-of-gas/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-out-of-gas/call/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-out-of-gas/call/trace-vmTrace](cases/fee-policy/typed-out-of-gas/call/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-out-of-gas/call/vmTrace](cases/fee-policy/typed-out-of-gas/call/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-out-of-gas/many/stateDiff](cases/fee-policy/typed-out-of-gas/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-out-of-gas/many/stateDiff-vmTrace](cases/fee-policy/typed-out-of-gas/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-out-of-gas/many/trace](cases/fee-policy/typed-out-of-gas/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-out-of-gas/many/trace-stateDiff](cases/fee-policy/typed-out-of-gas/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-out-of-gas/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-out-of-gas/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-out-of-gas/many/trace-vmTrace](cases/fee-policy/typed-out-of-gas/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-out-of-gas/many/vmTrace](cases/fee-policy/typed-out-of-gas/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-refund-then-observe/many/stateDiff](cases/fee-policy/typed-refund-then-observe/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-refund-then-observe/many/stateDiff-vmTrace](cases/fee-policy/typed-refund-then-observe/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-refund-then-observe/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-refund-then-observe/many/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-refund-then-observe/many/trace-vmTrace](cases/fee-policy/typed-refund-then-observe/many/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-refund-then-observe/many/vmTrace](cases/fee-policy/typed-refund-then-observe/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-refund/call/stateDiff](cases/fee-policy/typed-refund/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-refund/call/stateDiff-vmTrace](cases/fee-policy/typed-refund/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-refund/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-refund/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-refund/call/trace-vmTrace](cases/fee-policy/typed-refund/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-refund/call/vmTrace](cases/fee-policy/typed-refund/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-refund/many/stateDiff](cases/fee-policy/typed-refund/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-refund/many/stateDiff-vmTrace](cases/fee-policy/typed-refund/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-refund/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-refund/many/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-refund/many/trace-vmTrace](cases/fee-policy/typed-refund/many/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-refund/many/vmTrace](cases/fee-policy/typed-refund/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-revert-then-observe/many/stateDiff](cases/fee-policy/typed-revert-then-observe/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-revert-then-observe/many/stateDiff-vmTrace](cases/fee-policy/typed-revert-then-observe/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-revert-then-observe/many/trace](cases/fee-policy/typed-revert-then-observe/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/typed-revert-then-observe/many/trace-stateDiff](cases/fee-policy/typed-revert-then-observe/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/typed-revert-then-observe/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-revert-then-observe/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/typed-revert-then-observe/many/trace-vmTrace](cases/fee-policy/typed-revert-then-observe/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/typed-revert-then-observe/many/vmTrace](cases/fee-policy/typed-revert-then-observe/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-revert/call/stateDiff](cases/fee-policy/typed-revert/call/stateDiff.md) | Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-revert/call/stateDiff-vmTrace](cases/fee-policy/typed-revert/call/stateDiff-vmTrace.md) | Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-revert/call/trace](cases/fee-policy/typed-revert/call/trace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/typed-revert/call/trace-stateDiff](cases/fee-policy/typed-revert/call/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/typed-revert/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-revert/call/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/typed-revert/call/trace-vmTrace](cases/fee-policy/typed-revert/call/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/typed-revert/call/vmTrace](cases/fee-policy/typed-revert/call/vmTrace.md) | Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-revert/many/stateDiff](cases/fee-policy/typed-revert/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-revert/many/stateDiff-vmTrace](cases/fee-policy/typed-revert/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-revert/many/trace](cases/fee-policy/typed-revert/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/typed-revert/many/trace-stateDiff](cases/fee-policy/typed-revert/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/typed-revert/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-revert/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/typed-revert/many/trace-vmTrace](cases/fee-policy/typed-revert/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [fee-policy/typed-revert/many/vmTrace](cases/fee-policy/typed-revert/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-equals-cap/call/stateDiff](cases/fee-policy/typed-tip-equals-cap/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-equals-cap/call/stateDiff-vmTrace](cases/fee-policy/typed-tip-equals-cap/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-equals-cap/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-tip-equals-cap/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-equals-cap/call/trace-vmTrace](cases/fee-policy/typed-tip-equals-cap/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-equals-cap/call/vmTrace](cases/fee-policy/typed-tip-equals-cap/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-equals-cap/many/stateDiff](cases/fee-policy/typed-tip-equals-cap/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-equals-cap/many/stateDiff-vmTrace](cases/fee-policy/typed-tip-equals-cap/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-equals-cap/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-tip-equals-cap/many/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-equals-cap/many/trace-vmTrace](cases/fee-policy/typed-tip-equals-cap/many/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-equals-cap/many/vmTrace](cases/fee-policy/typed-tip-equals-cap/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-limited/call/stateDiff](cases/fee-policy/typed-tip-limited/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-limited/call/stateDiff-vmTrace](cases/fee-policy/typed-tip-limited/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-limited/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-tip-limited/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-limited/call/trace-vmTrace](cases/fee-policy/typed-tip-limited/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-limited/call/vmTrace](cases/fee-policy/typed-tip-limited/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-limited/many/stateDiff](cases/fee-policy/typed-tip-limited/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-limited/many/stateDiff-vmTrace](cases/fee-policy/typed-tip-limited/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-limited/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-tip-limited/many/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-limited/many/trace-vmTrace](cases/fee-policy/typed-tip-limited/many/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-limited/many/vmTrace](cases/fee-policy/typed-tip-limited/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-tip-over-cap/many/none](cases/fee-policy/typed-tip-over-cap/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-tip-over-cap/many/stateDiff](cases/fee-policy/typed-tip-over-cap/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-tip-over-cap/many/stateDiff-vmTrace](cases/fee-policy/typed-tip-over-cap/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-tip-over-cap/many/trace](cases/fee-policy/typed-tip-over-cap/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-tip-over-cap/many/trace-stateDiff](cases/fee-policy/typed-tip-over-cap/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-tip-over-cap/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-tip-over-cap/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-tip-over-cap/many/trace-vmTrace](cases/fee-policy/typed-tip-over-cap/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-tip-over-cap/many/vmTrace](cases/fee-policy/typed-tip-over-cap/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-zero-cap-positive-tip/many/none](cases/fee-policy/typed-zero-cap-positive-tip/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-zero-cap-positive-tip/many/stateDiff](cases/fee-policy/typed-zero-cap-positive-tip/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-zero-cap-positive-tip/many/stateDiff-vmTrace](cases/fee-policy/typed-zero-cap-positive-tip/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-zero-cap-positive-tip/many/trace](cases/fee-policy/typed-zero-cap-positive-tip/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-zero-cap-positive-tip/many/trace-stateDiff](cases/fee-policy/typed-zero-cap-positive-tip/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-zero-cap-positive-tip/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-zero-cap-positive-tip/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-zero-cap-positive-tip/many/trace-vmTrace](cases/fee-policy/typed-zero-cap-positive-tip/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-zero-cap-positive-tip/many/vmTrace](cases/fee-policy/typed-zero-cap-positive-tip/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-zero-tip/call/stateDiff](cases/fee-policy/typed-zero-tip/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero-tip/call/stateDiff-vmTrace](cases/fee-policy/typed-zero-tip/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero-tip/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-zero-tip/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero-tip/call/trace-vmTrace](cases/fee-policy/typed-zero-tip/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero-tip/call/vmTrace](cases/fee-policy/typed-zero-tip/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero-tip/many/stateDiff](cases/fee-policy/typed-zero-tip/many/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero-tip/many/stateDiff-vmTrace](cases/fee-policy/typed-zero-tip/many/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero-tip/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-zero-tip/many/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero-tip/many/trace-vmTrace](cases/fee-policy/typed-zero-tip/many/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero-tip/many/vmTrace](cases/fee-policy/typed-zero-tip/many/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero/call/stateDiff](cases/fee-policy/typed-zero/call/stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero/call/stateDiff-vmTrace](cases/fee-policy/typed-zero/call/stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-zero/call/trace-stateDiff-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero/call/trace-vmTrace](cases/fee-policy/typed-zero/call/trace-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero/call/vmTrace](cases/fee-policy/typed-zero/call/vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero/many/none](cases/fee-policy/typed-zero/many/none.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-zero/many/stateDiff](cases/fee-policy/typed-zero/many/stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero/many/stateDiff-vmTrace](cases/fee-policy/typed-zero/many/stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero/many/trace](cases/fee-policy/typed-zero/many/trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-zero/many/trace-stateDiff](cases/fee-policy/typed-zero/many/trace-stateDiff.md) | Besu 🛠️ Development, Besu 📦 Release |
| [fee-policy/typed-zero/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-zero/many/trace-stateDiff-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero/many/trace-vmTrace](cases/fee-policy/typed-zero/many/trace-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fee-policy/typed-zero/many/vmTrace](cases/fee-policy/typed-zero/many/vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fork-followup/_reference/block/0x33](cases/fork-followup/_reference/block/0x33.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fork-followup/_reference/block/0x34](cases/fork-followup/_reference/block/0x34.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fork-followup/_reference/block/0x35](cases/fork-followup/_reference/block/0x35.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fork-followup/beacon-call-55](cases/fork-followup/beacon-call-55.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [fork-followup/destroy-trace-55](cases/fork-followup/destroy-trace-55.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/block-35](cases/forks/block-35.md) | Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [forks/block-36](cases/forks/block-36.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [forks/block-47](cases/forks/block-47.md) | Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [forks/block-48](cases/forks/block-48.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/block-51](cases/forks/block-51.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/block-52](cases/forks/block-52.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/block-55](cases/forks/block-55.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/block-56](cases/forks/block-56.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/block-59](cases/forks/block-59.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/block-60](cases/forks/block-60.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/destroy-trace-55](cases/forks/destroy-trace-55.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/filter-35](cases/forks/filter-35.md) | Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [forks/filter-36](cases/forks/filter-36.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [forks/filter-47](cases/forks/filter-47.md) | Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [forks/filter-48](cases/forks/filter-48.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/filter-51](cases/forks/filter-51.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/filter-52](cases/forks/filter-52.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/filter-55](cases/forks/filter-55.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/filter-56](cases/forks/filter-56.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/filter-59](cases/forks/filter-59.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/filter-60](cases/forks/filter-60.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/filter-across-36](cases/forks/filter-across-36.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [forks/filter-across-48](cases/forks/filter-across-48.md) | Besu 🛠️ Development, Besu 📦 Release, Erigon 🛠️ Development, Erigon 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [forks/filter-across-52](cases/forks/filter-across-52.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/filter-across-56](cases/forks/filter-across-56.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/filter-across-60](cases/forks/filter-across-60.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/mcopy-trace-55](cases/forks/mcopy-trace-55.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/mcopy-trace-56](cases/forks/mcopy-trace-56.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/replay-36](cases/forks/replay-36.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/replay-48](cases/forks/replay-48.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/replay-51](cases/forks/replay-51.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [forks/replay-60](cases/forks/replay-60.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [h30/_reference/block/0x1](cases/h30/_reference/block/0x1.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [h30/_reference/block/0x2](cases/h30/_reference/block/0x2.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [h30/_reference/block/0x30](cases/h30/_reference/block/0x30.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/block-transfer](cases/initial/block-transfer.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/block-tree](cases/initial/block-tree.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/call-constructor](cases/initial/call-constructor.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/call-constructor-priced](cases/initial/call-constructor-priced.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/call-many](cases/initial/call-many.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/call-many-priced](cases/initial/call-many-priced.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/call-transfer-stateDiff](cases/initial/call-transfer-stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/call-tree-stateDiff](cases/initial/call-tree-stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/call-tree-stateDiff-priced](cases/initial/call-tree-stateDiff-priced.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/call-tree-trace](cases/initial/call-tree-trace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/call-tree-trace-priced](cases/initial/call-tree-trace-priced.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/call-tree-vmTrace](cases/initial/call-tree-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/call-tree-vmTrace-priced](cases/initial/call-tree-vmTrace-priced.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/filter-all](cases/initial/filter-all.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/filter-empty](cases/initial/filter-empty.md) | Besu 🛠️ Development, Besu 📦 Release |
| [initial/filter-from](cases/initial/filter-from.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/get-missing](cases/initial/get-missing.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/get-nested](cases/initial/get-nested.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/get-one](cases/initial/get-one.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/get-root](cases/initial/get-root.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/get-transfer-root](cases/initial/get-transfer-root.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/get-zero](cases/initial/get-zero.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/raw-valid-default-block](cases/initial/raw-valid-default-block.md) | Besu 🛠️ Development, Besu 📦 Release |
| [initial/replay-7702-stateDiff](cases/initial/replay-7702-stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [initial/replay-7702-trace](cases/initial/replay-7702-trace.md) | Reth 🛠️ Development, Reth 📦 Release |
| [initial/replay-7702-vmTrace](cases/initial/replay-7702-vmTrace.md) | Reth 🛠️ Development, Reth 📦 Release |
| [initial/replay-block-tree](cases/initial/replay-block-tree.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/replay-revert-stateDiff](cases/initial/replay-revert-stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [initial/replay-revert-trace](cases/initial/replay-revert-trace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [initial/replay-revert-vmTrace](cases/initial/replay-revert-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [initial/replay-transfer-stateDiff](cases/initial/replay-transfer-stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [initial/replay-transfer-trace](cases/initial/replay-transfer-trace.md) | Reth 🛠️ Development, Reth 📦 Release |
| [initial/replay-transfer-vmTrace](cases/initial/replay-transfer-vmTrace.md) | Reth 🛠️ Development, Reth 📦 Release |
| [initial/replay-tree-stateDiff](cases/initial/replay-tree-stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [initial/replay-tree-trace](cases/initial/replay-tree-trace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [initial/replay-tree-vmTrace](cases/initial/replay-tree-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release, Reth 🛠️ Development, Reth 📦 Release |
| [initial/transaction-revert](cases/initial/transaction-revert.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [initial/transaction-tree](cases/initial/transaction-tree.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompile-values/nested-call-outer0-value1-failed](cases/precompile-values/nested-call-outer0-value1-failed.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompile-values/nested-call-outer0-value1-success](cases/precompile-values/nested-call-outer0-value1-success.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompile-values/nested-call-outer1-value0-failed](cases/precompile-values/nested-call-outer1-value0-failed.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompile-values/nested-call-outer1-value0-success](cases/precompile-values/nested-call-outer1-value0-success.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompile-values/nested-callcode-outer0-value1-failed](cases/precompile-values/nested-callcode-outer0-value1-failed.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompile-values/nested-callcode-outer0-value1-success](cases/precompile-values/nested-callcode-outer0-value1-success.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompile-values/nested-callcode-outer1-value0-failed](cases/precompile-values/nested-callcode-outer1-value0-failed.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompile-values/nested-callcode-outer1-value0-success](cases/precompile-values/nested-callcode-outer1-value0-success.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompiles/nested-call-value0-failed](cases/precompiles/nested-call-value0-failed.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompiles/nested-call-value0-success](cases/precompiles/nested-call-value0-success.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompiles/nested-call-value1-failed](cases/precompiles/nested-call-value1-failed.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompiles/nested-call-value1-success](cases/precompiles/nested-call-value1-success.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompiles/nested-callcode-value0-failed](cases/precompiles/nested-callcode-value0-failed.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompiles/nested-callcode-value0-success](cases/precompiles/nested-callcode-value0-success.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompiles/nested-callcode-value1-failed](cases/precompiles/nested-callcode-value1-failed.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompiles/nested-callcode-value1-success](cases/precompiles/nested-callcode-value1-success.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompiles/nested-delegatecall-value0-failed](cases/precompiles/nested-delegatecall-value0-failed.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompiles/nested-delegatecall-value0-success](cases/precompiles/nested-delegatecall-value0-success.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompiles/nested-delegatecall-value1-failed](cases/precompiles/nested-delegatecall-value1-failed.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompiles/nested-delegatecall-value1-success](cases/precompiles/nested-delegatecall-value1-success.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompiles/nested-staticcall-value0-failed](cases/precompiles/nested-staticcall-value0-failed.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompiles/nested-staticcall-value0-success](cases/precompiles/nested-staticcall-value0-success.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [precompiles/root-failed](cases/precompiles/root-failed.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-below-basefee-all](cases/raw-validation/raw-validation-below-basefee-all.md) | Besu 🛠️ Development, Besu 📦 Release |
| [raw-validation/raw-validation-below-basefee-trace](cases/raw-validation/raw-validation-below-basefee-trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [raw-validation/raw-validation-code-sender-all](cases/raw-validation/raw-validation-code-sender-all.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-code-sender-stateDiff](cases/raw-validation/raw-validation-code-sender-stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-code-sender-vmTrace](cases/raw-validation/raw-validation-code-sender-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-create-nonce-high-all](cases/raw-validation/raw-validation-create-nonce-high-all.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-create-nonce-high-stateDiff](cases/raw-validation/raw-validation-create-nonce-high-stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-create-nonce-high-trace](cases/raw-validation/raw-validation-create-nonce-high-trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [raw-validation/raw-validation-create-nonce-high-vmTrace](cases/raw-validation/raw-validation-create-nonce-high-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-create-nonce-low-all](cases/raw-validation/raw-validation-create-nonce-low-all.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-create-nonce-low-stateDiff](cases/raw-validation/raw-validation-create-nonce-low-stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-create-nonce-low-trace](cases/raw-validation/raw-validation-create-nonce-low-trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [raw-validation/raw-validation-create-nonce-low-vmTrace](cases/raw-validation/raw-validation-create-nonce-low-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-create-valid-all](cases/raw-validation/raw-validation-create-valid-all.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-create-valid-stateDiff](cases/raw-validation/raw-validation-create-valid-stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-create-valid-vmTrace](cases/raw-validation/raw-validation-create-valid-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-delegated-sender-valid-all](cases/raw-validation/raw-validation-delegated-sender-valid-all.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-delegated-sender-valid-stateDiff](cases/raw-validation/raw-validation-delegated-sender-valid-stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-delegated-sender-valid-vmTrace](cases/raw-validation/raw-validation-delegated-sender-valid-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-execution-oog-valid-all](cases/raw-validation/raw-validation-execution-oog-valid-all.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-execution-oog-valid-stateDiff](cases/raw-validation/raw-validation-execution-oog-valid-stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-execution-oog-valid-trace](cases/raw-validation/raw-validation-execution-oog-valid-trace.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-execution-oog-valid-vmTrace](cases/raw-validation/raw-validation-execution-oog-valid-vmTrace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [raw-validation/raw-validation-funds-gas-all](cases/raw-validation/raw-validation-funds-gas-all.md) | Besu 🛠️ Development, Besu 📦 Release |
| [raw-validation/raw-validation-funds-gas-trace](cases/raw-validation/raw-validation-funds-gas-trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [raw-validation/raw-validation-funds-value-all](cases/raw-validation/raw-validation-funds-value-all.md) | Besu 🛠️ Development, Besu 📦 Release |
| [raw-validation/raw-validation-funds-value-trace](cases/raw-validation/raw-validation-funds-value-trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [raw-validation/raw-validation-intrinsic-gas-all](cases/raw-validation/raw-validation-intrinsic-gas-all.md) | Besu 🛠️ Development, Besu 📦 Release |
| [raw-validation/raw-validation-intrinsic-gas-trace](cases/raw-validation/raw-validation-intrinsic-gas-trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [raw-validation/raw-validation-nonce-high-all](cases/raw-validation/raw-validation-nonce-high-all.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-nonce-high-stateDiff](cases/raw-validation/raw-validation-nonce-high-stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-nonce-high-trace](cases/raw-validation/raw-validation-nonce-high-trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [raw-validation/raw-validation-nonce-high-vmTrace](cases/raw-validation/raw-validation-nonce-high-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-nonce-low-all](cases/raw-validation/raw-validation-nonce-low-all.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-nonce-low-stateDiff](cases/raw-validation/raw-validation-nonce-low-stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-nonce-low-trace](cases/raw-validation/raw-validation-nonce-low-trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [raw-validation/raw-validation-nonce-low-vmTrace](cases/raw-validation/raw-validation-nonce-low-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-valid-all](cases/raw-validation/raw-validation-valid-all.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-valid-stateDiff](cases/raw-validation/raw-validation-valid-stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [raw-validation/raw-validation-valid-vmTrace](cases/raw-validation/raw-validation-valid-vmTrace.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [reorg-safe/after/block-tail](cases/reorg-safe/after/block-tail.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [reorg-safe/after/filter-tail](cases/reorg-safe/after/filter-tail.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [reorg-safe/before/block-tail](cases/reorg-safe/before/block-tail.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [reorg-safe/before/filter-tail](cases/reorg-safe/before/filter-tail.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [reorg-safe/restored/block-tail](cases/reorg-safe/restored/block-tail.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [reorg-safe/restored/filter-tail](cases/reorg-safe/restored/filter-tail.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [repeat/auth-set-revert](cases/repeat/auth-set-revert.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [repeat/call-gas7400](cases/repeat/call-gas7400.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [repeat/call-mcopy](cases/repeat/call-mcopy.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [repeat/call-mixed-create](cases/repeat/call-mixed-create.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [repeat/call-return42](cases/repeat/call-return42.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [repeat/call-siblings-revert-ok](cases/repeat/call-siblings-revert-ok.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [repeat/constructor](cases/repeat/constructor.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [repeat/many-storage-write-revert-read](cases/repeat/many-storage-write-revert-read.md) | Besu 🛠️ Development, Besu 📦 Release, Nethermind 🛠️ Development, Nethermind 📦 Release |
| [repeat/raw-below-basefee](cases/repeat/raw-below-basefee.md) | Besu 🛠️ Development, Besu 📦 Release |
| [repeat/raw-below-basefee-trace](cases/repeat/raw-below-basefee-trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [repeat/raw-insufficient-funds](cases/repeat/raw-insufficient-funds.md) | Besu 🛠️ Development, Besu 📦 Release |
| [repeat/raw-insufficient-funds-trace](cases/repeat/raw-insufficient-funds-trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [repeat/raw-low-gas](cases/repeat/raw-low-gas.md) | Besu 🛠️ Development, Besu 📦 Release |
| [repeat/raw-low-gas-trace](cases/repeat/raw-low-gas-trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [repeat/raw-nonce-high](cases/repeat/raw-nonce-high.md) | Besu 🛠️ Development, Besu 📦 Release |
| [repeat/raw-nonce-high-stateDiff](cases/repeat/raw-nonce-high-stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [repeat/raw-nonce-high-trace](cases/repeat/raw-nonce-high-trace.md) | Besu 🛠️ Development, Besu 📦 Release |
| [repeat/raw-valid-stateDiff](cases/repeat/raw-valid-stateDiff.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |
| [repeat/state-only-nonempty-output](cases/repeat/state-only-nonempty-output.md) | Nethermind 🛠️ Development, Nethermind 📦 Release |

## Runs

Capture completeness records whether requests finished, not whether their results match the proposal.

| Run | Corpus | Capture complete |
| --- | --- | --- |
| [initial-clean](../evidence/2026-09-24/coverage-matrix/initial-clean/manifest.json) | initial | ✅ Yes |
| [a](../evidence/2026-09-24/coverage-matrix/a/manifest.json) | a | ✅ Yes |
| [repeat](../evidence/2026-09-24/coverage-matrix/repeat/manifest.json) | repeat | ✅ Yes |
| [forks](../evidence/2026-09-24/coverage-matrix/forks/manifest.json) | forks | ✅ Yes |
| [fork-followup](../evidence/2026-09-24/coverage-matrix/fork-followup/manifest.json) | fork-followup | ✅ Yes |
| [precompiles](../evidence/2026-09-24/coverage-matrix/precompiles/manifest.json) | precompiles | ✅ Yes |
| [precompile-values](../evidence/2026-09-24/coverage-matrix/precompile-values/manifest.json) | precompile-values | ✅ Yes |
| [raw-validation](../evidence/2026-09-24/coverage-matrix/raw-validation/manifest.json) | raw-validation | ✅ Yes |
| [coverage](../evidence/2026-09-24/coverage-matrix/coverage/manifest.json) | coverage | ✅ Yes |
| [callmany-isolation](../evidence/2026-09-24/coverage-matrix/callmany-isolation/manifest.json) | callmany-isolation | ✅ Yes |
| [h30](../evidence/2026-09-24/coverage-matrix/h30/manifest.json) | h30 | ✅ Yes |
| [reorg-safe](../evidence/2026-09-24/coverage-matrix/reorg-safe/manifest.json) | reorg-safe | ⚠️ No |
| [pruned](../evidence/2026-09-24/coverage-matrix/pruned/manifest.json) | pruned | ✅ Yes |
| [h15-matrix](../evidence/2026-09-24/h15-fee-policy/h15-matrix/manifest.json) | fee-policy | ✅ Yes |
