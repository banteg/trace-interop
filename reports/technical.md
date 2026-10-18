# Technical appendix

[Back to the maintainer overview](README.md)

Published builds checked at **2026-10-16T23:48:59.042359+00:00**. [Freshness preflight](../evidence/2026-10-17/eval/preflight.json) · [Build lock](../evidence/2026-10-17/eval/clients.lock.json). All corpora use this snapshot; later upstream changes require a new capture.

The human reports summarize selected assertions against a proposed specification. Agreement is not full conformance, and an RPC error can be the correct result for an invalid-input case. Setup failures are excluded from semantic assessment. Version and commit labels identify captured builds; channel identifiers in raw artifacts describe how updates are discovered.

The experimental Geth fork implements the draft and is not an independent vote for its decisions. No verified pruning scenario is included for that fork.

Anvil has no Engine API, so it is captured by [replaying each chain](../docs/usage.md#replica-captures) rather than through Hive. Every replayed block is compared with the fixture header; chains whose forks activate after genesis, reorgs and pruning are not captured for it.

## Test status key

- ✅ **Checked cases agree:** the evaluated cases match the proposed contract; not full conformance.
- ⚠️ **Differs:** at least one checked assertion differs from the proposal.
- 🛠️ **Fix submitted:** the build differs, lacks the method or is partially assessed, and linked PRs for its client and decision cover the measured difference. Each is open, or merged but not yet in the build: its commit, or for a library its release, is not in the build’s source or lockfile. The captured checks are unchanged; the marker leaves a build once the recorded uptake facts show the fix in it. A difference with only partial fixes keeps ⚠️, ⛔ or 🟡 and links them as “partial fix”. [Related PRs](../docs/client-fixes.md).
- ⛔ **Method unavailable:** the tested method is unsupported.
- 🟡 **Partially assessed:** some declared cases or topics were not evaluated.
- ⚪ **Not assessed:** no evaluated assertion establishes an outcome.
- 🚧 **Blocked:** a missing response, failed setup or earlier failure prevents this check.
- 🔎 **Control / not applicable:** reference evidence or a property that does not apply; never a semantic pass.
- ❔ **Policy open:** observed behavior is recorded without a settled assertion.

Build labels show versions and source commits. Test outcomes are separate from [policy agreement and harmonization](../decisions/README.md#status-key).

## Reproduction and machine-readable results

See [usage](../docs/usage.md) for commands and [stateful scenarios](../docs/scenarios.md) for setup requirements. [checks.json](checks.json) retains every assertion; [comparisons.json](comparisons.json) groups exact responses; [assessment.json](assessment.json) pins the specification and assessment source hashes. Each case links its original response and run manifest.

To reproduce one case, use its linked manifest and the exact client, corpus and case name:

```sh
uv run trace-interop run --lock evidence/2026-09-21/RUN/manifest.json \
  --clients CLIENT --corpus CORPUS --case "^CASE$" --output runs/reproduce
```

## Assertion coverage

Coverage below counts all selected trace observations, including missing responses and failed setup, separately from schema validation. Partially assessed means at least one assertion has a verdict and another is blocked or unassessed. This includes follow-on properties blocked by a client defect, unsupported methods, and missing independent evidence; it is a coverage label, not a client verdict. A checked assertion is not proof of the rest of the topic.

| Coverage | Observations |
| --- | --- |
| 🔎 Assessed | 16363 |
| 🟡 Partial | 111 |
| ⚪ Unassessed | 0 |
| 🚧 Blocked | 57 |
| 🔎 Control | 34 |


Of the partial observations, 63 already have a differing assertion; 48 have only support or evidence gaps alongside their checked assertions. Result-schema validation is reported separately.


### Unevaluated properties

Each row names the reason; controls and inapplicable properties do not count as passes. Counts are topic obligations, so one response may appear more than once.

| Topic | Disposition | Reason | Observations |
| --- | --- | --- | --- |
| H02 | not_applicable | The transaction is not in the chain: a missing transaction lookup is H06’s rule, not path selection. | 11 |
| H06 | blocked | Cannot inspect this property: unsupported. | 2 |
| H06 | control | Ledger reference; executable requirements are assessed by the linked topic cases. | 2 |
| H06 | not_applicable | The transaction exists: which frame a path selects, including null for a missing path, is H02’s rule. | 22 |
| H07 | blocked | Cannot inspect this property: unsupported. | 24 |
| H07 | control | Ledger reference; executable requirements are assessed by the linked topic cases. | 11 |
| H08 | blocked | Cannot inspect this property: unsupported. | 8 |
| H08 | blocked | The RPC returned an error, so there is no execution result to inspect. | 1 |
| H09 | blocked | Address selection differs from its reference; failure-bearing frame selection is not established. | 2 |
| H09 | blocked | Cannot inspect this property: unsupported. | 12 |
| H09 | blocked | No failed attempts ['call', 'create'] under the deepest executed frame at depth 1025. | 2 |
| H09 | blocked | No frame matches {'action': {'value': '0x1'}, 'traceAddress': [0], 'type': 'call'}. | 2 |
| H09 | blocked | No frame matches {'action': {'value': '0x1'}, 'traceAddress': [0], 'type': 'create'}. | 2 |
| H09 | blocked | Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot) | 12 |
| H09 | blocked | The RPC returned an error, so there is no execution result to inspect. | 4 |
| H09 | not_applicable | No failed frame is selected; the address-filter assertion independently checks the selected inventory. | 9 |
| H11 | blocked | H15 owns this error, a base_fee validation rejection: fee cap less than block base fee: address 0x7435ed30A8b4AEb0877CEf0c6E8cFFe834eb865f, feeCap: 0 baseFee: 1677430. There is no executed result to inspect. | 1 |
| H14 | control | Ledger reference; executable requirements are assessed by the linked topic cases. | 40 |
| H14 | not_applicable | H03 owns this request’s rejection. 'garbage' is not valid under any of the given schemas | 11 |
| H14 | not_applicable | H32 owns this request’s rejection. '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas; '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e' is not valid under any of the given schemas | 11 |
| H14 | not_applicable | H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas | 8 |
| H14 | not_applicable | H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas. Code -32000 (-32602 recommended). | 1 |
| H14 | not_applicable | H32 owns this request’s rejection. 'pending' is not valid under any of the given schemas; 'pending' is not valid under any of the given schemas. Code -32603 (-32602 recommended). | 2 |
| H14 | not_applicable | H32 owns this request’s rejection. {'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e'} is not valid under any of the given schemas; {'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e'} is not valid under any of the given schemas | 11 |
| H14 | not_applicable | H33 owns this request’s rejection. '0x2' is not of type 'null' | 11 |
| H14 | not_applicable | H33 owns this request’s rejection. '0xf5de2a84' is not valid under any of the given schemas | 11 |
| H14 | not_applicable | H33 owns this request’s rejection. {'blockHash': '0xf5de2a84c954882baa45ac90c79baa2a966ddf7d8ea14d8a87e1e17c449d123e'} is not valid under any of the given schemas | 11 |
| H14 | not_applicable | Rejected for base_fee, so there is no executed result to judge: rpc_error -32000 fee cap less than block base fee: address <nil>, feeCap: 0 baseFee: 765625000. | 1 |
| H15 | blocked | No receipt gas or execution-gas witness was captured. | 4 |
| H15 | blocked | The reference field-gas-omitted-allowance-eth-call returned no successful output. | 2 |
| H15 | blocked | eth_call: funds execution halt; trace_call: No root trace was returned to distinguish an execution halt from empty output. | 16 |
| H15 | not_applicable | Rejected for funds, so there is no executed result to judge: rpc_error -32004 Upfront gas cost exceeds account balance (transaction up-front gas cost 0x1b1ae4d6e2ef500000 exceeds transaction sender. | 4 |
| H15 | not_applicable | Rejected for funds, so there is no executed result to judge: rpc_error -38014 call 0: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 100000000000. | 1 |
| H15 | not_applicable | Rejected for funds, so there is no executed result to judge: rpc_error -38014 first run for txIndex 0 error: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C26590293. | 1 |
| H15 | not_applicable | Rejected for funds, so there is no executed result to judge: rpc_error -38014 insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000. | 6 |
| H16 | blocked | Cannot inspect this property: unsupported. | 24 |
| H16 | blocked | H15 owns this error, a base_fee validation rejection: first run for txIndex 0 error: fee cap less than block base fee: address 0x7435ed30A8b4AEb0877CEf0c6E8cFFe834eb865f, fee. There is no executed result to inspect. | 1 |
| H16 | blocked | Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot) | 17 |
| H16 | not_applicable | For unsigned calls H16 defers to H15’s policy; this call’s fee accounting is judged under H15. | 33 |
| H16 | not_applicable | H15 owns this error, a funds validation rejection: Upfront gas cost exceeds account balance (transaction up-front gas cost 0x1b1ae4d6e2ef500000 exceeds transaction sender . There is no executed result to inspect. | 2 |
| H16 | not_applicable | H15 owns this error, a funds validation rejection: call 0: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 100000000000. There is no executed result to inspect. | 1 |
| H16 | not_applicable | H15 owns this error, a funds validation rejection: first run for txIndex 0 error: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C26590293. There is no executed result to inspect. | 1 |
| H16 | not_applicable | H15 owns this error, a funds validation rejection: insufficient funds for gas * price + value: address 0x7E5F4552091A69125d5DfCb7b8C2659029395Bdf have 1000000000000000000 . There is no executed result to inspect. | 2 |
| H16 | not_applicable | The signed transaction was correctly rejected before execution; execution-result properties do not apply. | 8 |
| H17 | blocked | Cannot inspect this property: unsupported. | 10 |
| H17 | blocked | No state-diff object was returned; account markers cannot be assessed. | 2 |
| H17 | blocked | Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot) | 7 |
| H17 | blocked | The RPC returned an error, so there is no execution result to inspect. | 2 |
| H17 | not_applicable | The explicit block-selector extension is outside the two-argument baseline; H12 records which state it selects. | 11 |
| H17 | not_applicable | The signed transaction was correctly rejected before execution; execution-result properties do not apply. | 8 |
| H18 | blocked | Cannot inspect this property: unsupported. | 4 |
| H18 | blocked | Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot) | 2 |
| H19 | blocked | Cannot inspect this property: unsupported. | 6 |
| H19 | blocked | Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot) | 2 |
| H19 | blocked | The RPC returned an error, so there is no execution result to inspect. | 3 |
| H20 | blocked | Cannot inspect this property: unsupported. | 8 |
| H20 | blocked | Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot) | 2 |
| H20 | blocked | The RPC returned an error, so there is no execution result to inspect. | 3 |
| H21 | blocked | Cannot inspect this property: unsupported. | 4 |
| H21 | blocked | The RPC returned an error, so there is no execution result to inspect. | 3 |
| H23 | blocked | Depends on H03: The request names the default mode explicitly, so a server that rejects the mode field fails before matching rewards. Observed rpc_error -32602 Invalid filter params. | 2 |
| H23 | blocked | Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot) | 9 |
| H23 | blocked | The H03 list semantics differ, so the special-action records cannot be judged separately. | 13 |
| H23 | blocked | The H04 list semantics differ, so the special-action records cannot be judged separately. | 12 |
| H23 | blocked | The RPC returned an error, so there is no execution result to inspect. | 2 |
| H23 | control | Ledger reference; executable requirements are assessed by the linked topic cases. | 11 |
| H26 | blocked | Cannot inspect this property: unsupported. | 6 |
| H26 | blocked | Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot) | 8 |
| H27 | control | Ledger reference; executable requirements are assessed by the linked topic cases. | 18 |
| H27 | control | Per-block reference response for the filter comparison. | 125 |
| H28 | blocked | Cannot inspect this property: unsupported. | 4 |
| H28 | blocked | Replayed chain differs from the fixture at block 0x2 (gasUsed, receiptsRoot) | 6 |
| H29 | blocked | Cannot inspect this property: unsupported. | 2 |
| H30 | control | Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion. | 11 |
| H32 | control | Explicit-range reference for the earliest/default-range comparison; not a standalone default-selection assertion. | 11 |
| H33 | blocked | Scenario setup stopped: Invalid forkchoice state | 9 |
| H33 | blocked | The numeric equivalent filter-block-2-union returned no result. | 2 |
| H33 | control | Ledger reference; executable requirements are assessed by the linked topic cases. | 101 |

Eligibility is recomputed from the frozen head and independent scenario controls. `capture_eligible` in checks.json preserves the original capture decision; original summaries and wire observations are unchanged.

## Setup gaps

| Build | Scenario | Run evidence |
| --- | --- | --- |
| Anvil · 1.8.5 · 51a52c59 | mined-probes | [mined-probes](../evidence/2026-10-17/eval/mined-probes/summary.json) |
| Erigon · 3.7.1 · 8c1e3893 | reorg-safe | [reorg-safe](../evidence/2026-10-17/eval/reorg-safe/summary.json) |

## Result-shape checks

These cases returned results that differ from the draft schema. The case pages retain the validation details; an unclassified schema failure is not silently counted as agreement.

| Case | Affected builds |
| --- | --- |
| [a/auth-replace](cases/a/auth-replace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/auth-set-revert](cases/a/auth-set-revert.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/block-2](cases/a/block-2.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/call-mixed-create](cases/a/call-mixed-create.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/call-siblings-ok-revert](cases/a/call-siblings-ok-revert.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/call-siblings-revert-ok](cases/a/call-siblings-revert-ok.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/filter-all](cases/a/filter-all.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/filter-both-null](cases/a/filter-both-null.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/filter-creator-from](cases/a/filter-creator-from.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/filter-from-null](cases/a/filter-from-null.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/filter-page-0](cases/a/filter-page-0.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/filter-page-2](cases/a/filter-page-2.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/filter-snapshot](cases/a/filter-snapshot.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/filter-to-empty-from-set](cases/a/filter-to-empty-from-set.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/filter-to-null](cases/a/filter-to-null.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/filter-two-blocks](cases/a/filter-two-blocks.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/filter-wrong-address-type](cases/a/filter-wrong-address-type.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/get-nested-parent](cases/a/get-nested-parent.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/many-storage-write-revert-read](cases/a/many-storage-write-revert-read.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/raw-below-basefee](cases/a/raw-below-basefee.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/raw-insufficient-funds](cases/a/raw-insufficient-funds.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/raw-low-gas](cases/a/raw-low-gas.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/raw-nonce-high](cases/a/raw-nonce-high.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [a/transaction-tree](cases/a/transaction-tree.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [callmany-isolation/write-revert-read/many-storage-write-revert-read](cases/callmany-isolation/write-revert-read/many-storage-write-revert-read.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [coverage/model-empty-runtime](cases/coverage/model-empty-runtime.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [coverage/model-environment](cases/coverage/model-environment.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [coverage/model-environment-free](cases/coverage/model-environment-free.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [coverage/model-mcopy](cases/coverage/model-mcopy.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [coverage/model-mcopy-overlap](cases/coverage/model-mcopy-overlap.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [coverage/model-mcopy-zero](cases/coverage/model-mcopy-zero.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [coverage/model-mload-existing](cases/coverage/model-mload-existing.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [coverage/model-mload-expansion](cases/coverage/model-mload-expansion.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [coverage/model-return42](cases/coverage/model-return42.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [coverage/model-revert](cases/coverage/model-revert.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-compat/defaults-cap-only-positive/trace/trace](cases/fee-compat/defaults-cap-only-positive/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/defaults-cap-only-positive/trace/trace-stateDiff](cases/fee-compat/defaults-cap-only-positive/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/defaults-cap-only-positive/trace/trace-stateDiff-vmTrace](cases/fee-compat/defaults-cap-only-positive/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/defaults-cap-only-positive/trace/trace-vmTrace](cases/fee-compat/defaults-cap-only-positive/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/defaults-cap-only-zero/trace/trace](cases/fee-compat/defaults-cap-only-zero/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/defaults-cap-only-zero/trace/trace-stateDiff](cases/fee-compat/defaults-cap-only-zero/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/defaults-cap-only-zero/trace/trace-stateDiff-vmTrace](cases/fee-compat/defaults-cap-only-zero/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/defaults-cap-only-zero/trace/trace-vmTrace](cases/fee-compat/defaults-cap-only-zero/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/defaults-omitted/trace/trace](cases/fee-compat/defaults-omitted/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/defaults-omitted/trace/trace-stateDiff](cases/fee-compat/defaults-omitted/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/defaults-omitted/trace/trace-stateDiff-vmTrace](cases/fee-compat/defaults-omitted/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/defaults-omitted/trace/trace-vmTrace](cases/fee-compat/defaults-omitted/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/defaults-tip-only-zero/trace/trace](cases/fee-compat/defaults-tip-only-zero/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/defaults-tip-only-zero/trace/trace-stateDiff](cases/fee-compat/defaults-tip-only-zero/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/defaults-tip-only-zero/trace/trace-stateDiff-vmTrace](cases/fee-compat/defaults-tip-only-zero/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/defaults-tip-only-zero/trace/trace-vmTrace](cases/fee-compat/defaults-tip-only-zero/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/empty-sender-free/trace/trace](cases/fee-compat/empty-sender-free/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/empty-sender-free/trace/trace-stateDiff](cases/fee-compat/empty-sender-free/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/empty-sender-free/trace/trace-stateDiff-vmTrace](cases/fee-compat/empty-sender-free/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/empty-sender-free/trace/trace-vmTrace](cases/fee-compat/empty-sender-free/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/funding-free-exact/trace/trace](cases/fee-compat/funding-free-exact/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/funding-free-exact/trace/trace-stateDiff](cases/fee-compat/funding-free-exact/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/funding-free-exact/trace/trace-stateDiff-vmTrace](cases/fee-compat/funding-free-exact/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/funding-free-exact/trace/trace-vmTrace](cases/fee-compat/funding-free-exact/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/funding-legacy-exact/trace/trace](cases/fee-compat/funding-legacy-exact/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/funding-legacy-exact/trace/trace-stateDiff](cases/fee-compat/funding-legacy-exact/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/funding-legacy-exact/trace/trace-stateDiff-vmTrace](cases/fee-compat/funding-legacy-exact/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/funding-legacy-exact/trace/trace-vmTrace](cases/fee-compat/funding-legacy-exact/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/funding-typed-exact/trace/trace](cases/fee-compat/funding-typed-exact/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/funding-typed-exact/trace/trace-stateDiff](cases/fee-compat/funding-typed-exact/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/funding-typed-exact/trace/trace-stateDiff-vmTrace](cases/fee-compat/funding-typed-exact/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/funding-typed-exact/trace/trace-vmTrace](cases/fee-compat/funding-typed-exact/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/funding-typed-free-exact/trace/trace](cases/fee-compat/funding-typed-free-exact/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/funding-typed-free-exact/trace/trace-stateDiff](cases/fee-compat/funding-typed-free-exact/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/funding-typed-free-exact/trace/trace-stateDiff-vmTrace](cases/fee-compat/funding-typed-free-exact/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/funding-typed-free-exact/trace/trace-vmTrace](cases/fee-compat/funding-typed-free-exact/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/legacy-above-base/trace/trace](cases/fee-compat/legacy-above-base/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/legacy-above-base/trace/trace-stateDiff](cases/fee-compat/legacy-above-base/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/legacy-above-base/trace/trace-stateDiff-vmTrace](cases/fee-compat/legacy-above-base/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/legacy-above-base/trace/trace-vmTrace](cases/fee-compat/legacy-above-base/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/legacy-at-base/trace/trace](cases/fee-compat/legacy-at-base/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/legacy-at-base/trace/trace-stateDiff](cases/fee-compat/legacy-at-base/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/legacy-at-base/trace/trace-stateDiff-vmTrace](cases/fee-compat/legacy-at-base/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/legacy-at-base/trace/trace-vmTrace](cases/fee-compat/legacy-at-base/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/legacy-zero/trace/trace](cases/fee-compat/legacy-zero/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/legacy-zero/trace/trace-stateDiff](cases/fee-compat/legacy-zero/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/legacy-zero/trace/trace-stateDiff-vmTrace](cases/fee-compat/legacy-zero/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/legacy-zero/trace/trace-vmTrace](cases/fee-compat/legacy-zero/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-at-base/trace/trace](cases/fee-compat/typed-at-base/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-at-base/trace/trace-stateDiff](cases/fee-compat/typed-at-base/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-at-base/trace/trace-stateDiff-vmTrace](cases/fee-compat/typed-at-base/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-at-base/trace/trace-vmTrace](cases/fee-compat/typed-at-base/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-cap-limited/trace/trace](cases/fee-compat/typed-cap-limited/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-cap-limited/trace/trace-stateDiff](cases/fee-compat/typed-cap-limited/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-cap-limited/trace/trace-stateDiff-vmTrace](cases/fee-compat/typed-cap-limited/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-cap-limited/trace/trace-vmTrace](cases/fee-compat/typed-cap-limited/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-tip-equals-cap/trace/trace](cases/fee-compat/typed-tip-equals-cap/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-tip-equals-cap/trace/trace-stateDiff](cases/fee-compat/typed-tip-equals-cap/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-tip-equals-cap/trace/trace-stateDiff-vmTrace](cases/fee-compat/typed-tip-equals-cap/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-tip-equals-cap/trace/trace-vmTrace](cases/fee-compat/typed-tip-equals-cap/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-tip-limited/trace/trace](cases/fee-compat/typed-tip-limited/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-tip-limited/trace/trace-stateDiff](cases/fee-compat/typed-tip-limited/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-tip-limited/trace/trace-stateDiff-vmTrace](cases/fee-compat/typed-tip-limited/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-tip-limited/trace/trace-vmTrace](cases/fee-compat/typed-tip-limited/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-zero-tip/trace/trace](cases/fee-compat/typed-zero-tip/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-zero-tip/trace/trace-stateDiff](cases/fee-compat/typed-zero-tip/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-zero-tip/trace/trace-stateDiff-vmTrace](cases/fee-compat/typed-zero-tip/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-zero-tip/trace/trace-vmTrace](cases/fee-compat/typed-zero-tip/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-zero/trace/trace](cases/fee-compat/typed-zero/trace/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-zero/trace/trace-stateDiff](cases/fee-compat/typed-zero/trace/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-zero/trace/trace-stateDiff-vmTrace](cases/fee-compat/typed-zero/trace/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-compat/typed-zero/trace/trace-vmTrace](cases/fee-compat/typed-zero/trace/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-cap-only-positive/call/trace](cases/fee-policy/defaults-cap-only-positive/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-cap-only-positive/call/trace-stateDiff](cases/fee-policy/defaults-cap-only-positive/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-cap-only-positive/call/trace-stateDiff-vmTrace](cases/fee-policy/defaults-cap-only-positive/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-cap-only-positive/call/trace-vmTrace](cases/fee-policy/defaults-cap-only-positive/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-cap-only-positive/many/trace](cases/fee-policy/defaults-cap-only-positive/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-cap-only-positive/many/trace-stateDiff](cases/fee-policy/defaults-cap-only-positive/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-cap-only-positive/many/trace-stateDiff-vmTrace](cases/fee-policy/defaults-cap-only-positive/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-cap-only-positive/many/trace-vmTrace](cases/fee-policy/defaults-cap-only-positive/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-cap-only-zero/call/trace](cases/fee-policy/defaults-cap-only-zero/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-cap-only-zero/call/trace-stateDiff](cases/fee-policy/defaults-cap-only-zero/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-cap-only-zero/call/trace-stateDiff-vmTrace](cases/fee-policy/defaults-cap-only-zero/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-cap-only-zero/call/trace-vmTrace](cases/fee-policy/defaults-cap-only-zero/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-cap-only-zero/many/trace](cases/fee-policy/defaults-cap-only-zero/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-cap-only-zero/many/trace-stateDiff](cases/fee-policy/defaults-cap-only-zero/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-cap-only-zero/many/trace-stateDiff-vmTrace](cases/fee-policy/defaults-cap-only-zero/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-cap-only-zero/many/trace-vmTrace](cases/fee-policy/defaults-cap-only-zero/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-omitted/call/trace](cases/fee-policy/defaults-omitted/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-omitted/call/trace-stateDiff](cases/fee-policy/defaults-omitted/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-omitted/call/trace-stateDiff-vmTrace](cases/fee-policy/defaults-omitted/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-omitted/call/trace-vmTrace](cases/fee-policy/defaults-omitted/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-omitted/many/trace](cases/fee-policy/defaults-omitted/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-omitted/many/trace-stateDiff](cases/fee-policy/defaults-omitted/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-omitted/many/trace-stateDiff-vmTrace](cases/fee-policy/defaults-omitted/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-omitted/many/trace-vmTrace](cases/fee-policy/defaults-omitted/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-tip-only-zero/call/trace](cases/fee-policy/defaults-tip-only-zero/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-tip-only-zero/call/trace-stateDiff](cases/fee-policy/defaults-tip-only-zero/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-tip-only-zero/call/trace-stateDiff-vmTrace](cases/fee-policy/defaults-tip-only-zero/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-tip-only-zero/call/trace-vmTrace](cases/fee-policy/defaults-tip-only-zero/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-tip-only-zero/many/trace](cases/fee-policy/defaults-tip-only-zero/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-tip-only-zero/many/trace-stateDiff](cases/fee-policy/defaults-tip-only-zero/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-tip-only-zero/many/trace-stateDiff-vmTrace](cases/fee-policy/defaults-tip-only-zero/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/defaults-tip-only-zero/many/trace-vmTrace](cases/fee-policy/defaults-tip-only-zero/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/empty-sender-free/call/trace](cases/fee-policy/empty-sender-free/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/empty-sender-free/call/trace-stateDiff](cases/fee-policy/empty-sender-free/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/empty-sender-free/call/trace-stateDiff-vmTrace](cases/fee-policy/empty-sender-free/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/empty-sender-free/call/trace-vmTrace](cases/fee-policy/empty-sender-free/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/empty-sender-free/many/trace](cases/fee-policy/empty-sender-free/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/empty-sender-free/many/trace-stateDiff](cases/fee-policy/empty-sender-free/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/empty-sender-free/many/trace-stateDiff-vmTrace](cases/fee-policy/empty-sender-free/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/empty-sender-free/many/trace-vmTrace](cases/fee-policy/empty-sender-free/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-free-exact/call/trace](cases/fee-policy/funding-free-exact/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-free-exact/call/trace-stateDiff](cases/fee-policy/funding-free-exact/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-free-exact/call/trace-stateDiff-vmTrace](cases/fee-policy/funding-free-exact/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-free-exact/call/trace-vmTrace](cases/fee-policy/funding-free-exact/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-free-exact/many/trace](cases/fee-policy/funding-free-exact/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-free-exact/many/trace-stateDiff](cases/fee-policy/funding-free-exact/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-free-exact/many/trace-stateDiff-vmTrace](cases/fee-policy/funding-free-exact/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-free-exact/many/trace-vmTrace](cases/fee-policy/funding-free-exact/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-legacy-exact/call/trace](cases/fee-policy/funding-legacy-exact/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-legacy-exact/call/trace-stateDiff](cases/fee-policy/funding-legacy-exact/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-legacy-exact/call/trace-stateDiff-vmTrace](cases/fee-policy/funding-legacy-exact/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-legacy-exact/call/trace-vmTrace](cases/fee-policy/funding-legacy-exact/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-legacy-exact/many/trace](cases/fee-policy/funding-legacy-exact/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-legacy-exact/many/trace-stateDiff](cases/fee-policy/funding-legacy-exact/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-legacy-exact/many/trace-stateDiff-vmTrace](cases/fee-policy/funding-legacy-exact/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-legacy-exact/many/trace-vmTrace](cases/fee-policy/funding-legacy-exact/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-typed-exact/call/trace](cases/fee-policy/funding-typed-exact/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-typed-exact/call/trace-stateDiff](cases/fee-policy/funding-typed-exact/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-typed-exact/call/trace-stateDiff-vmTrace](cases/fee-policy/funding-typed-exact/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-typed-exact/call/trace-vmTrace](cases/fee-policy/funding-typed-exact/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-typed-exact/many/trace](cases/fee-policy/funding-typed-exact/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-typed-exact/many/trace-stateDiff](cases/fee-policy/funding-typed-exact/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-typed-exact/many/trace-stateDiff-vmTrace](cases/fee-policy/funding-typed-exact/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-typed-exact/many/trace-vmTrace](cases/fee-policy/funding-typed-exact/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-typed-free-exact/call/trace](cases/fee-policy/funding-typed-free-exact/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-typed-free-exact/call/trace-stateDiff](cases/fee-policy/funding-typed-free-exact/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-typed-free-exact/call/trace-stateDiff-vmTrace](cases/fee-policy/funding-typed-free-exact/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-typed-free-exact/call/trace-vmTrace](cases/fee-policy/funding-typed-free-exact/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-typed-free-exact/many/trace](cases/fee-policy/funding-typed-free-exact/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-typed-free-exact/many/trace-stateDiff](cases/fee-policy/funding-typed-free-exact/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-typed-free-exact/many/trace-stateDiff-vmTrace](cases/fee-policy/funding-typed-free-exact/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/funding-typed-free-exact/many/trace-vmTrace](cases/fee-policy/funding-typed-free-exact/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-above-base/call/trace](cases/fee-policy/legacy-above-base/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-above-base/call/trace-stateDiff](cases/fee-policy/legacy-above-base/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-above-base/call/trace-stateDiff-vmTrace](cases/fee-policy/legacy-above-base/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-above-base/call/trace-vmTrace](cases/fee-policy/legacy-above-base/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-above-base/many/trace](cases/fee-policy/legacy-above-base/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-above-base/many/trace-stateDiff](cases/fee-policy/legacy-above-base/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-above-base/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-above-base/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-above-base/many/trace-vmTrace](cases/fee-policy/legacy-above-base/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-at-base/call/trace](cases/fee-policy/legacy-at-base/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-at-base/call/trace-stateDiff](cases/fee-policy/legacy-at-base/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-at-base/call/trace-stateDiff-vmTrace](cases/fee-policy/legacy-at-base/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-at-base/call/trace-vmTrace](cases/fee-policy/legacy-at-base/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-at-base/many/trace](cases/fee-policy/legacy-at-base/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-at-base/many/trace-stateDiff](cases/fee-policy/legacy-at-base/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-at-base/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-at-base/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-at-base/many/trace-vmTrace](cases/fee-policy/legacy-at-base/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas-then-observe/many/stateDiff-vmTrace](cases/fee-policy/legacy-out-of-gas-then-observe/many/stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas-then-observe/many/trace](cases/fee-policy/legacy-out-of-gas-then-observe/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas-then-observe/many/trace-stateDiff](cases/fee-policy/legacy-out-of-gas-then-observe/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas-then-observe/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-out-of-gas-then-observe/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas-then-observe/many/trace-vmTrace](cases/fee-policy/legacy-out-of-gas-then-observe/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas-then-observe/many/vmTrace](cases/fee-policy/legacy-out-of-gas-then-observe/many/vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas/call/stateDiff-vmTrace](cases/fee-policy/legacy-out-of-gas/call/stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas/call/trace](cases/fee-policy/legacy-out-of-gas/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas/call/trace-stateDiff](cases/fee-policy/legacy-out-of-gas/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas/call/trace-stateDiff-vmTrace](cases/fee-policy/legacy-out-of-gas/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas/call/trace-vmTrace](cases/fee-policy/legacy-out-of-gas/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas/call/vmTrace](cases/fee-policy/legacy-out-of-gas/call/vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas/many/stateDiff-vmTrace](cases/fee-policy/legacy-out-of-gas/many/stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas/many/trace](cases/fee-policy/legacy-out-of-gas/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas/many/trace-stateDiff](cases/fee-policy/legacy-out-of-gas/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-out-of-gas/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas/many/trace-vmTrace](cases/fee-policy/legacy-out-of-gas/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-out-of-gas/many/vmTrace](cases/fee-policy/legacy-out-of-gas/many/vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-refund-then-observe/many/trace](cases/fee-policy/legacy-refund-then-observe/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-refund-then-observe/many/trace-stateDiff](cases/fee-policy/legacy-refund-then-observe/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-refund-then-observe/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-refund-then-observe/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-refund-then-observe/many/trace-vmTrace](cases/fee-policy/legacy-refund-then-observe/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-refund/call/trace](cases/fee-policy/legacy-refund/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-refund/call/trace-stateDiff](cases/fee-policy/legacy-refund/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-refund/call/trace-stateDiff-vmTrace](cases/fee-policy/legacy-refund/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-refund/call/trace-vmTrace](cases/fee-policy/legacy-refund/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-refund/many/trace](cases/fee-policy/legacy-refund/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-refund/many/trace-stateDiff](cases/fee-policy/legacy-refund/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-refund/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-refund/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-refund/many/trace-vmTrace](cases/fee-policy/legacy-refund/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-revert-then-observe/many/trace](cases/fee-policy/legacy-revert-then-observe/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/legacy-revert-then-observe/many/trace-stateDiff](cases/fee-policy/legacy-revert-then-observe/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/legacy-revert-then-observe/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-revert-then-observe/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/legacy-revert-then-observe/many/trace-vmTrace](cases/fee-policy/legacy-revert-then-observe/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/legacy-revert/call/trace](cases/fee-policy/legacy-revert/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/legacy-revert/call/trace-stateDiff](cases/fee-policy/legacy-revert/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/legacy-revert/call/trace-stateDiff-vmTrace](cases/fee-policy/legacy-revert/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/legacy-revert/call/trace-vmTrace](cases/fee-policy/legacy-revert/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/legacy-revert/many/trace](cases/fee-policy/legacy-revert/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/legacy-revert/many/trace-stateDiff](cases/fee-policy/legacy-revert/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/legacy-revert/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-revert/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/legacy-revert/many/trace-vmTrace](cases/fee-policy/legacy-revert/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/legacy-zero/call/trace](cases/fee-policy/legacy-zero/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-zero/call/trace-stateDiff](cases/fee-policy/legacy-zero/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-zero/call/trace-stateDiff-vmTrace](cases/fee-policy/legacy-zero/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-zero/call/trace-vmTrace](cases/fee-policy/legacy-zero/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-zero/many/trace](cases/fee-policy/legacy-zero/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-zero/many/trace-stateDiff](cases/fee-policy/legacy-zero/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-zero/many/trace-stateDiff-vmTrace](cases/fee-policy/legacy-zero/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/legacy-zero/many/trace-vmTrace](cases/fee-policy/legacy-zero/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-legacy-free-priced-free/many/trace](cases/fee-policy/mixed-legacy-free-priced-free/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-legacy-free-priced-free/many/trace-stateDiff](cases/fee-policy/mixed-legacy-free-priced-free/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-legacy-free-priced-free/many/trace-stateDiff-vmTrace](cases/fee-policy/mixed-legacy-free-priced-free/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-legacy-free-priced-free/many/trace-vmTrace](cases/fee-policy/mixed-legacy-free-priced-free/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-legacy-priced-free-priced/many/trace](cases/fee-policy/mixed-legacy-priced-free-priced/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-legacy-priced-free-priced/many/trace-stateDiff](cases/fee-policy/mixed-legacy-priced-free-priced/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-legacy-priced-free-priced/many/trace-stateDiff-vmTrace](cases/fee-policy/mixed-legacy-priced-free-priced/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-legacy-priced-free-priced/many/trace-vmTrace](cases/fee-policy/mixed-legacy-priced-free-priced/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-legacy-selections/many/none](cases/fee-policy/mixed-legacy-selections/many/none.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-legacy-selections/many/stateDiff](cases/fee-policy/mixed-legacy-selections/many/stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-legacy-selections/many/stateDiff-vmTrace](cases/fee-policy/mixed-legacy-selections/many/stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-legacy-selections/many/trace](cases/fee-policy/mixed-legacy-selections/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-legacy-selections/many/trace-stateDiff](cases/fee-policy/mixed-legacy-selections/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-legacy-selections/many/trace-stateDiff-vmTrace](cases/fee-policy/mixed-legacy-selections/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-legacy-selections/many/trace-vmTrace](cases/fee-policy/mixed-legacy-selections/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-legacy-selections/many/vmTrace](cases/fee-policy/mixed-legacy-selections/many/vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-typed-free-priced-free/many/trace](cases/fee-policy/mixed-typed-free-priced-free/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-typed-free-priced-free/many/trace-stateDiff](cases/fee-policy/mixed-typed-free-priced-free/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-typed-free-priced-free/many/trace-stateDiff-vmTrace](cases/fee-policy/mixed-typed-free-priced-free/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-typed-free-priced-free/many/trace-vmTrace](cases/fee-policy/mixed-typed-free-priced-free/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-typed-priced-free-priced/many/trace](cases/fee-policy/mixed-typed-priced-free-priced/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-typed-priced-free-priced/many/trace-stateDiff](cases/fee-policy/mixed-typed-priced-free-priced/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-typed-priced-free-priced/many/trace-stateDiff-vmTrace](cases/fee-policy/mixed-typed-priced-free-priced/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-typed-priced-free-priced/many/trace-vmTrace](cases/fee-policy/mixed-typed-priced-free-priced/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-typed-selections/many/none](cases/fee-policy/mixed-typed-selections/many/none.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-typed-selections/many/stateDiff](cases/fee-policy/mixed-typed-selections/many/stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-typed-selections/many/stateDiff-vmTrace](cases/fee-policy/mixed-typed-selections/many/stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-typed-selections/many/trace](cases/fee-policy/mixed-typed-selections/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-typed-selections/many/trace-stateDiff](cases/fee-policy/mixed-typed-selections/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-typed-selections/many/trace-stateDiff-vmTrace](cases/fee-policy/mixed-typed-selections/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-typed-selections/many/trace-vmTrace](cases/fee-policy/mixed-typed-selections/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/mixed-typed-selections/many/vmTrace](cases/fee-policy/mixed-typed-selections/many/vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-at-base/call/trace](cases/fee-policy/typed-at-base/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-at-base/call/trace-stateDiff](cases/fee-policy/typed-at-base/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-at-base/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-at-base/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-at-base/call/trace-vmTrace](cases/fee-policy/typed-at-base/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-at-base/many/trace](cases/fee-policy/typed-at-base/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-at-base/many/trace-stateDiff](cases/fee-policy/typed-at-base/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-at-base/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-at-base/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-at-base/many/trace-vmTrace](cases/fee-policy/typed-at-base/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-cap-limited/call/trace](cases/fee-policy/typed-cap-limited/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-cap-limited/call/trace-stateDiff](cases/fee-policy/typed-cap-limited/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-cap-limited/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-cap-limited/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-cap-limited/call/trace-vmTrace](cases/fee-policy/typed-cap-limited/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-cap-limited/many/trace](cases/fee-policy/typed-cap-limited/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-cap-limited/many/trace-stateDiff](cases/fee-policy/typed-cap-limited/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-cap-limited/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-cap-limited/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-cap-limited/many/trace-vmTrace](cases/fee-policy/typed-cap-limited/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas-then-observe/many/stateDiff-vmTrace](cases/fee-policy/typed-out-of-gas-then-observe/many/stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas-then-observe/many/trace](cases/fee-policy/typed-out-of-gas-then-observe/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas-then-observe/many/trace-stateDiff](cases/fee-policy/typed-out-of-gas-then-observe/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas-then-observe/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-out-of-gas-then-observe/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas-then-observe/many/trace-vmTrace](cases/fee-policy/typed-out-of-gas-then-observe/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas-then-observe/many/vmTrace](cases/fee-policy/typed-out-of-gas-then-observe/many/vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas/call/stateDiff-vmTrace](cases/fee-policy/typed-out-of-gas/call/stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas/call/trace](cases/fee-policy/typed-out-of-gas/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas/call/trace-stateDiff](cases/fee-policy/typed-out-of-gas/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-out-of-gas/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas/call/trace-vmTrace](cases/fee-policy/typed-out-of-gas/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas/call/vmTrace](cases/fee-policy/typed-out-of-gas/call/vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas/many/stateDiff-vmTrace](cases/fee-policy/typed-out-of-gas/many/stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas/many/trace](cases/fee-policy/typed-out-of-gas/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas/many/trace-stateDiff](cases/fee-policy/typed-out-of-gas/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-out-of-gas/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas/many/trace-vmTrace](cases/fee-policy/typed-out-of-gas/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-out-of-gas/many/vmTrace](cases/fee-policy/typed-out-of-gas/many/vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-refund-then-observe/many/trace](cases/fee-policy/typed-refund-then-observe/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-refund-then-observe/many/trace-stateDiff](cases/fee-policy/typed-refund-then-observe/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-refund-then-observe/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-refund-then-observe/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-refund-then-observe/many/trace-vmTrace](cases/fee-policy/typed-refund-then-observe/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-refund/call/trace](cases/fee-policy/typed-refund/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-refund/call/trace-stateDiff](cases/fee-policy/typed-refund/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-refund/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-refund/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-refund/call/trace-vmTrace](cases/fee-policy/typed-refund/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-refund/many/trace](cases/fee-policy/typed-refund/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-refund/many/trace-stateDiff](cases/fee-policy/typed-refund/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-refund/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-refund/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-refund/many/trace-vmTrace](cases/fee-policy/typed-refund/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-revert-then-observe/many/trace](cases/fee-policy/typed-revert-then-observe/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/typed-revert-then-observe/many/trace-stateDiff](cases/fee-policy/typed-revert-then-observe/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/typed-revert-then-observe/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-revert-then-observe/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/typed-revert-then-observe/many/trace-vmTrace](cases/fee-policy/typed-revert-then-observe/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/typed-revert/call/trace](cases/fee-policy/typed-revert/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/typed-revert/call/trace-stateDiff](cases/fee-policy/typed-revert/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/typed-revert/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-revert/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/typed-revert/call/trace-vmTrace](cases/fee-policy/typed-revert/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/typed-revert/many/trace](cases/fee-policy/typed-revert/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/typed-revert/many/trace-stateDiff](cases/fee-policy/typed-revert/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/typed-revert/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-revert/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/typed-revert/many/trace-vmTrace](cases/fee-policy/typed-revert/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [fee-policy/typed-tip-equals-cap/call/trace](cases/fee-policy/typed-tip-equals-cap/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-tip-equals-cap/call/trace-stateDiff](cases/fee-policy/typed-tip-equals-cap/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-tip-equals-cap/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-tip-equals-cap/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-tip-equals-cap/call/trace-vmTrace](cases/fee-policy/typed-tip-equals-cap/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-tip-equals-cap/many/trace](cases/fee-policy/typed-tip-equals-cap/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-tip-equals-cap/many/trace-stateDiff](cases/fee-policy/typed-tip-equals-cap/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-tip-equals-cap/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-tip-equals-cap/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-tip-equals-cap/many/trace-vmTrace](cases/fee-policy/typed-tip-equals-cap/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-tip-limited/call/trace](cases/fee-policy/typed-tip-limited/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-tip-limited/call/trace-stateDiff](cases/fee-policy/typed-tip-limited/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-tip-limited/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-tip-limited/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-tip-limited/call/trace-vmTrace](cases/fee-policy/typed-tip-limited/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-tip-limited/many/trace](cases/fee-policy/typed-tip-limited/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-tip-limited/many/trace-stateDiff](cases/fee-policy/typed-tip-limited/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-tip-limited/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-tip-limited/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-tip-limited/many/trace-vmTrace](cases/fee-policy/typed-tip-limited/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-zero-tip/call/trace](cases/fee-policy/typed-zero-tip/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-zero-tip/call/trace-stateDiff](cases/fee-policy/typed-zero-tip/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-zero-tip/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-zero-tip/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-zero-tip/call/trace-vmTrace](cases/fee-policy/typed-zero-tip/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-zero-tip/many/trace](cases/fee-policy/typed-zero-tip/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-zero-tip/many/trace-stateDiff](cases/fee-policy/typed-zero-tip/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-zero-tip/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-zero-tip/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-zero-tip/many/trace-vmTrace](cases/fee-policy/typed-zero-tip/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-zero/call/trace](cases/fee-policy/typed-zero/call/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-zero/call/trace-stateDiff](cases/fee-policy/typed-zero/call/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-zero/call/trace-stateDiff-vmTrace](cases/fee-policy/typed-zero/call/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-zero/call/trace-vmTrace](cases/fee-policy/typed-zero/call/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-zero/many/trace](cases/fee-policy/typed-zero/many/trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-zero/many/trace-stateDiff](cases/fee-policy/typed-zero/many/trace-stateDiff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-zero/many/trace-stateDiff-vmTrace](cases/fee-policy/typed-zero/many/trace-stateDiff-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fee-policy/typed-zero/many/trace-vmTrace](cases/fee-policy/typed-zero/many/trace-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fork-followup/_reference/block/0x33](cases/fork-followup/_reference/block/0x33.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fork-followup/_reference/block/0x35](cases/fork-followup/_reference/block/0x35.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [fork-followup/beacon-call-55](cases/fork-followup/beacon-call-55.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [forks/block-35](cases/forks/block-35.md) | Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [forks/block-36](cases/forks/block-36.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [forks/block-47](cases/forks/block-47.md) | Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [forks/block-48](cases/forks/block-48.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [forks/block-51](cases/forks/block-51.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [forks/block-60](cases/forks/block-60.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [forks/filter-35](cases/forks/filter-35.md) | Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [forks/filter-36](cases/forks/filter-36.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [forks/filter-47](cases/forks/filter-47.md) | Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [forks/filter-48](cases/forks/filter-48.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [forks/filter-51](cases/forks/filter-51.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [forks/filter-60](cases/forks/filter-60.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [forks/filter-across-36](cases/forks/filter-across-36.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [forks/filter-across-48](cases/forks/filter-across-48.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [forks/filter-across-52](cases/forks/filter-across-52.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [forks/filter-across-56](cases/forks/filter-across-56.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [forks/filter-across-60](cases/forks/filter-across-60.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [forks/replay-36](cases/forks/replay-36.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [forks/replay-48](cases/forks/replay-48.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [forks/replay-51](cases/forks/replay-51.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [forks/replay-60](cases/forks/replay-60.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [h30/_reference/block/0x2](cases/h30/_reference/block/0x2.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [h30/call-number-default](cases/h30/call-number-default.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [h30/call-number-latest](cases/h30/call-number-latest.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [h30/call-number-pending](cases/h30/call-number-pending.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [h30/filter-block-2](cases/h30/filter-block-2.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [h30/filter-block-2-address-from](cases/h30/filter-block-2-address-from.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [h30/filter-block-2-address-to](cases/h30/filter-block-2-address-to.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [h30/filter-blockhash](cases/h30/filter-blockhash.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [h30/filter-blockhash-address-from](cases/h30/filter-blockhash-address-from.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [h30/filter-blockhash-address-to](cases/h30/filter-blockhash-address-to.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [h30/filter-blockhash-null](cases/h30/filter-blockhash-null.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [h30/filter-blockhash-null-bounds](cases/h30/filter-blockhash-null-bounds.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [h30/many-number-latest](cases/h30/many-number-latest.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [h30/many-number-pending](cases/h30/many-number-pending.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [initial/block-tree](cases/initial/block-tree.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [initial/call-constructor](cases/initial/call-constructor.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [initial/call-constructor-priced](cases/initial/call-constructor-priced.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [initial/call-many](cases/initial/call-many.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [initial/call-many-priced](cases/initial/call-many-priced.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [initial/call-tree-trace](cases/initial/call-tree-trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [initial/call-tree-trace-priced](cases/initial/call-tree-trace-priced.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [initial/filter-all](cases/initial/filter-all.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [initial/filter-empty](cases/initial/filter-empty.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [initial/filter-from](cases/initial/filter-from.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [initial/get-one](cases/initial/get-one.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [initial/raw-valid-default-block](cases/initial/raw-valid-default-block.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [initial/replay-block-tree](cases/initial/replay-block-tree.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [initial/transaction-revert](cases/initial/transaction-revert.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [initial/transaction-tree](cases/initial/transaction-tree.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [mined-probes/block-2](cases/mined-probes/block-2.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [mined-probes/block-3](cases/mined-probes/block-3.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [mined-probes/block-4](cases/mined-probes/block-4.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [mined-probes/filter-failed-create-creator](cases/mined-probes/filter-failed-create-creator.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [mined-probes/filter-failed-create-intersection](cases/mined-probes/filter-failed-create-intersection.md) | Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [mined-probes/filter-failed-create-recipient](cases/mined-probes/filter-failed-create-recipient.md) | Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [mined-probes/filter-failed-create-union](cases/mined-probes/filter-failed-create-union.md) | Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [mined-probes/filter-failed-nested-create-creator](cases/mined-probes/filter-failed-nested-create-creator.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [mined-probes/filter-failed-nested-create-recipient](cases/mined-probes/filter-failed-nested-create-recipient.md) | Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [mined-probes/replay-block-2](cases/mined-probes/replay-block-2.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [mined-probes/replay-block-3](cases/mined-probes/replay-block-3.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [mined-probes/replay-block-4](cases/mined-probes/replay-block-4.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [mined-probes/replay-create-revert](cases/mined-probes/replay-create-revert.md) | Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [mined-probes/replay-factory-create-revert](cases/mined-probes/replay-factory-create-revert.md) | Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [mined-probes/transaction-beacon-root-read](cases/mined-probes/transaction-beacon-root-read.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [mined-probes/transaction-create-destroy-absent](cases/mined-probes/transaction-create-destroy-absent.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [mined-probes/transaction-create-destroy-prefunded](cases/mined-probes/transaction-create-destroy-prefunded.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [mined-probes/transaction-create-revert](cases/mined-probes/transaction-create-revert.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [mined-probes/transaction-factory-create-revert](cases/mined-probes/transaction-factory-create-revert.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [precompile-values/nested-call-outer0-value1-failed](cases/precompile-values/nested-call-outer0-value1-failed.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompile-values/nested-call-outer0-value1-success](cases/precompile-values/nested-call-outer0-value1-success.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompile-values/nested-call-outer1-value0-failed](cases/precompile-values/nested-call-outer1-value0-failed.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompile-values/nested-call-outer1-value0-success](cases/precompile-values/nested-call-outer1-value0-success.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompile-values/nested-callcode-outer0-value1-failed](cases/precompile-values/nested-callcode-outer0-value1-failed.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompile-values/nested-callcode-outer0-value1-success](cases/precompile-values/nested-callcode-outer0-value1-success.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompile-values/nested-callcode-outer1-value0-failed](cases/precompile-values/nested-callcode-outer1-value0-failed.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompile-values/nested-callcode-outer1-value0-success](cases/precompile-values/nested-callcode-outer1-value0-success.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompiles/nested-call-value0-failed](cases/precompiles/nested-call-value0-failed.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompiles/nested-call-value0-success](cases/precompiles/nested-call-value0-success.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompiles/nested-call-value1-failed](cases/precompiles/nested-call-value1-failed.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompiles/nested-call-value1-success](cases/precompiles/nested-call-value1-success.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompiles/nested-callcode-value0-failed](cases/precompiles/nested-callcode-value0-failed.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompiles/nested-callcode-value0-success](cases/precompiles/nested-callcode-value0-success.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompiles/nested-callcode-value1-failed](cases/precompiles/nested-callcode-value1-failed.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompiles/nested-callcode-value1-success](cases/precompiles/nested-callcode-value1-success.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompiles/nested-delegatecall-value0-failed](cases/precompiles/nested-delegatecall-value0-failed.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompiles/nested-delegatecall-value0-success](cases/precompiles/nested-delegatecall-value0-success.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompiles/nested-delegatecall-value1-failed](cases/precompiles/nested-delegatecall-value1-failed.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompiles/nested-delegatecall-value1-success](cases/precompiles/nested-delegatecall-value1-success.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompiles/nested-staticcall-value0-failed](cases/precompiles/nested-staticcall-value0-failed.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [precompiles/nested-staticcall-value0-success](cases/precompiles/nested-staticcall-value0-success.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-forks/_reference/block/0x1](cases/probes-forks/_reference/block/0x1.md) | Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [probes-forks/_reference/block/0x2](cases/probes-forks/_reference/block/0x2.md) | Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [probes-forks/_reference/block/0x3](cases/probes-forks/_reference/block/0x3.md) | Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [probes-forks/_reference/block/0x4](cases/probes-forks/_reference/block/0x4.md) | Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [probes-forks/_reference/block/0x5](cases/probes-forks/_reference/block/0x5.md) | Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [probes-forks/beacon-many-55](cases/probes-forks/beacon-many-55.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-forks/beacon-trace-55](cases/probes-forks/beacon-trace-55.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-forks/depth-limit](cases/probes-forks/depth-limit.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-forks/filter-case-variant-member](cases/probes-forks/filter-case-variant-member.md) | Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [probes-forks/filter-null-fromBlock](cases/probes-forks/filter-null-fromBlock.md) | Erigon 3.7.1 · 8c1e3893 |
| [probes-forks/filter-null-members](cases/probes-forks/filter-null-members.md) | Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [probes-forks/filter-null-toBlock](cases/probes-forks/filter-null-toBlock.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [probes-forks/filter-omitted-fromBlock](cases/probes-forks/filter-omitted-fromBlock.md) | Erigon 3.7.1 · 8c1e3893 |
| [probes-forks/filter-omitted-toBlock](cases/probes-forks/filter-omitted-toBlock.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [probes-forks/fork-dynamic-fees-priced-at](cases/probes-forks/fork-dynamic-fees-priced-at.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-forks/genesis-filter](cases/probes-forks/genesis-filter.md) | Erigon 3.7.1 · 8c1e3893 |
| [probes-forks/genesis-range-rewards](cases/probes-forks/genesis-range-rewards.md) | Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [probes-forks/many-write-delete-storage](cases/probes-forks/many-write-delete-storage.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-forks/rewards-intersection-default](cases/probes-forks/rewards-intersection-default.md) | Erigon 3.7.1 · 8c1e3893 |
| [probes-forks/rewards-to](cases/probes-forks/rewards-to.md) | Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [probes-forks/rewards-union](cases/probes-forks/rewards-union.md) | Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [probes-forks/rewards-window](cases/probes-forks/rewards-window.md) | Erigon 3.8.0-dev · 5b452f41, Erigon 3.7.1 · 8c1e3893, Nethermind 2.2.0-preview · cd336c4c, Nethermind 2.2.0 · 1d2aff00 |
| [probes-prague/blob-fee-cap-unpriced](cases/probes-prague/blob-fee-cap-unpriced.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/blob-fee-defaulted](cases/probes-prague/blob-fee-defaulted.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/blob-fee-none](cases/probes-prague/blob-fee-none.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/blob-fee-priced](cases/probes-prague/blob-fee-priced.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/blob-fee-zero](cases/probes-prague/blob-fee-zero.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/callmany-null-block](cases/probes-prague/callmany-null-block.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/combo-blob-gasprice](cases/probes-prague/combo-blob-gasprice.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/combo-blob-gasprice-capped](cases/probes-prague/combo-blob-gasprice-capped.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/combo-blob-type2-dynamic](cases/probes-prague/combo-blob-type2-dynamic.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/combo-blob-type3-dynamic](cases/probes-prague/combo-blob-type3-dynamic.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/combo-blob-type3-gasprice](cases/probes-prague/combo-blob-type3-gasprice.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/combo-type0-dynamic](cases/probes-prague/combo-type0-dynamic.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/combo-type0-gasprice](cases/probes-prague/combo-type0-gasprice.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/combo-type1-dynamic](cases/probes-prague/combo-type1-dynamic.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/combo-type1-gasprice](cases/probes-prague/combo-type1-gasprice.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/combo-type2-dynamic](cases/probes-prague/combo-type2-dynamic.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/combo-type2-gasprice](cases/probes-prague/combo-type2-gasprice.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/combo-untyped-dynamic](cases/probes-prague/combo-untyped-dynamic.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/create-code-deposit-oog](cases/probes-prague/create-code-deposit-oog.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/create-code-size-limit](cases/probes-prague/create-code-size-limit.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/create-ef-prefix](cases/probes-prague/create-ef-prefix.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/create-reverted](cases/probes-prague/create-reverted.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea, Erigon 3.7.1 · 8c1e3893, Reth 2.7.0 · 3d592ece |
| [probes-prague/create2-collision](cases/probes-prague/create2-collision.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-access-list](cases/probes-prague/field-access-list.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-access-list-absent](cases/probes-prague/field-access-list-absent.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-chain-id](cases/probes-prague/field-chain-id.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-chain-id-mismatch](cases/probes-prague/field-chain-id-mismatch.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-data-input-equal](cases/probes-prague/field-data-input-equal.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-from-omitted](cases/probes-prague/field-from-omitted.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-from-omitted-zero-fee](cases/probes-prague/field-from-omitted-zero-fee.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-gas-null](cases/probes-prague/field-gas-null.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-gas-omitted](cases/probes-prague/field-gas-omitted.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-gas-omitted-funded](cases/probes-prague/field-gas-omitted-funded.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-gas-omitted-funded-many](cases/probes-prague/field-gas-omitted-funded-many.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-input-only](cases/probes-prague/field-input-only.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-nonce-above](cases/probes-prague/field-nonce-above.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-nonce-below](cases/probes-prague/field-nonce-below.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-null-accessList-unpriced](cases/probes-prague/field-null-accessList-unpriced.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-null-authorizationList-unpriced](cases/probes-prague/field-null-authorizationList-unpriced.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-null-blobVersionedHashes-unpriced](cases/probes-prague/field-null-blobVersionedHashes-unpriced.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-null-block](cases/probes-prague/field-null-block.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/field-null-members](cases/probes-prague/field-null-members.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/many-original-value](cases/probes-prague/many-original-value.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/many-selfdestruct](cases/probes-prague/many-selfdestruct.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/many-selfdestruct-diff](cases/probes-prague/many-selfdestruct-diff.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/many-transient](cases/probes-prague/many-transient.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/many-warm](cases/probes-prague/many-warm.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/precheck-call-value](cases/probes-prague/precheck-call-value.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/precheck-create-value](cases/probes-prague/precheck-create-value.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/vm-off-end](cases/probes-prague/vm-off-end.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/vm-push-order](cases/probes-prague/vm-push-order.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [probes-prague/vm-store](cases/probes-prague/vm-store.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-selector/raw-state-default](cases/raw-selector/raw-state-default.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-below-basefee-all](cases/raw-validation/raw-validation-below-basefee-all.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-below-basefee-trace](cases/raw-validation/raw-validation-below-basefee-trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-create-nonce-high-all](cases/raw-validation/raw-validation-create-nonce-high-all.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-create-nonce-high-trace](cases/raw-validation/raw-validation-create-nonce-high-trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-create-nonce-low-all](cases/raw-validation/raw-validation-create-nonce-low-all.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-create-nonce-low-trace](cases/raw-validation/raw-validation-create-nonce-low-trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-create-valid-all](cases/raw-validation/raw-validation-create-valid-all.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-create-valid-trace](cases/raw-validation/raw-validation-create-valid-trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-execution-oog-valid-all](cases/raw-validation/raw-validation-execution-oog-valid-all.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-execution-oog-valid-vmTrace](cases/raw-validation/raw-validation-execution-oog-valid-vmTrace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-funds-gas-all](cases/raw-validation/raw-validation-funds-gas-all.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-funds-gas-trace](cases/raw-validation/raw-validation-funds-gas-trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-funds-value-all](cases/raw-validation/raw-validation-funds-value-all.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-funds-value-trace](cases/raw-validation/raw-validation-funds-value-trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-intrinsic-gas-all](cases/raw-validation/raw-validation-intrinsic-gas-all.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-intrinsic-gas-trace](cases/raw-validation/raw-validation-intrinsic-gas-trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-nonce-high-all](cases/raw-validation/raw-validation-nonce-high-all.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-nonce-high-trace](cases/raw-validation/raw-validation-nonce-high-trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-nonce-low-all](cases/raw-validation/raw-validation-nonce-low-all.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [raw-validation/raw-validation-nonce-low-trace](cases/raw-validation/raw-validation-nonce-low-trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [reorg-safe/before/filter-tail](cases/reorg-safe/before/filter-tail.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [reorg-safe/restored/filter-tail](cases/reorg-safe/restored/filter-tail.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [repeat/auth-set-revert](cases/repeat/auth-set-revert.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [repeat/call-mixed-create](cases/repeat/call-mixed-create.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [repeat/call-siblings-revert-ok](cases/repeat/call-siblings-revert-ok.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [repeat/constructor](cases/repeat/constructor.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [repeat/many-storage-write-revert-read](cases/repeat/many-storage-write-revert-read.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [repeat/raw-below-basefee](cases/repeat/raw-below-basefee.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [repeat/raw-below-basefee-trace](cases/repeat/raw-below-basefee-trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [repeat/raw-insufficient-funds](cases/repeat/raw-insufficient-funds.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [repeat/raw-insufficient-funds-trace](cases/repeat/raw-insufficient-funds-trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [repeat/raw-low-gas](cases/repeat/raw-low-gas.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [repeat/raw-low-gas-trace](cases/repeat/raw-low-gas-trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [repeat/raw-nonce-high](cases/repeat/raw-nonce-high.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |
| [repeat/raw-nonce-high-trace](cases/repeat/raw-nonce-high-trace.md) | Besu 26.10-develop · 0776d82f, Besu 26.10.0 · 976ca7ea |

## Runs

Capture completeness records whether requests finished, not whether their results match the proposal.

| Run | Corpus | Capture complete |
| --- | --- | --- |
| [initial](../evidence/2026-10-17/eval/initial/manifest.json) | initial | ✅ Yes |
| [a](../evidence/2026-10-17/eval/a/manifest.json) | a | ✅ Yes |
| [repeat](../evidence/2026-10-17/eval/repeat/manifest.json) | repeat | ✅ Yes |
| [forks](../evidence/2026-10-17/eval/forks/manifest.json) | forks | ✅ Yes |
| [fork-followup](../evidence/2026-10-17/eval/fork-followup/manifest.json) | fork-followup | ✅ Yes |
| [precompiles](../evidence/2026-10-17/eval/precompiles/manifest.json) | precompiles | ✅ Yes |
| [precompile-values](../evidence/2026-10-17/eval/precompile-values/manifest.json) | precompile-values | ✅ Yes |
| [raw-validation](../evidence/2026-10-17/eval/raw-validation/manifest.json) | raw-validation | ✅ Yes |
| [coverage](../evidence/2026-10-17/eval/coverage/manifest.json) | coverage | ✅ Yes |
| [fee-policy](../evidence/2026-10-17/eval/fee-policy/manifest.json) | fee-policy | ✅ Yes |
| [fee-compat](../evidence/2026-10-17/eval/fee-compat/manifest.json) | fee-compat | ✅ Yes |
| [callmany-isolation](../evidence/2026-10-17/eval/callmany-isolation/manifest.json) | callmany-isolation | ✅ Yes |
| [h30](../evidence/2026-10-17/eval/h30/manifest.json) | h30 | ✅ Yes |
| [pending](../evidence/2026-10-18/eval-pending/pending/manifest.json) | pending | ✅ Yes |
| [raw-selector](../evidence/2026-10-17/eval/raw-selector/manifest.json) | raw-selector | ✅ Yes |
| [probes-prague](../evidence/2026-10-17/eval/probes-prague/manifest.json) | probes-prague | ✅ Yes |
| [probes-forks](../evidence/2026-10-17/eval/probes-forks/manifest.json) | probes-forks | ✅ Yes |
| [mined-probes](../evidence/2026-10-17/eval/mined-probes/manifest.json) | mined-probes | ⚠️ No |
| [reorg-safe](../evidence/2026-10-17/eval/reorg-safe/manifest.json) | reorg-safe | ⚠️ No |
| [pruned](../evidence/2026-10-17/eval/pruned/manifest.json) | pruned | ✅ Yes |
