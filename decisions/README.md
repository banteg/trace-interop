# Trace API decisions

[Client reports](../reports/README.md) · [Tested builds and coverage](../reports/technical.md) · [Source guide](../reports/sources.md)

The target is a useful, precise contract. Historical implementations explain compatibility costs, but do not decide the recommendation. Intentional departures need a concrete benefit and an explicit migration cost; observed agreement alone does not establish correctness.

| Decision | Status | Positions | Question | Stable | Dev |
| --- | --- | --- | --- | --- | --- |
| [H01](../reports/decisions/H01.md) | ⚪ Under review | ···· | **Method coverage**<br>Which trace_* methods must a client implement, and how does it signal the ones it does not? | ⛔✅✅✅— | ⛔✅✅✅✅ |
| [H02](../reports/decisions/H02.md) | 🤝 Converged | ···👍 | **trace_get selector and return shape**<br>What does trace_get's path argument select, and does it return one trace or a list? | ✅✅⚠️🛠️— | ✅✅⚠️✅✅ |
| [H03](../reports/decisions/H03.md) | 🤝 Converged | ·👍·👍 | **Filter composition and mode**<br>How do fromAddress and toAddress combine in trace_filter, and what does `mode` change? | ⚠️🛠️⚠️🛠️— | ⚠️✅⚠️✅✅ |
| [H04](../reports/decisions/H04.md) | ⚪ Under review | ···· | **Empty address lists**<br>Does an empty address list in trace_filter match every record or none? | ⚠️✅⚠️⚠️— | ⚠️✅⚠️⚠️✅ |
| [H05](../reports/decisions/H05.md) | ⚪ Under review | ···👍 | **Post-merge reward records**<br>Which reward records does a block produce after the Merge and at genesis, and do system operations or withdrawals produce any? | ⚠️🛠️⚠️🛠️— | ⚠️🛠️⚠️✅✅ |
| [H06](../reports/decisions/H06.md) | ⚪ Under review | ···· | **Missing transactions and paths**<br>When a transaction, block or trace path does not exist, does a method return null, [] or an error? | ⚠️⚠️⚠️⚠️— | ⚠️⚠️⚠️⚠️✅ |
| [H07](../reports/decisions/H07.md) | 🤝 Converged | ···👍 | **Replay transactionHash field**<br>Which replay results carry `transactionHash`? | 🟡✅✅🛠️— | 🟡✅✅✅✅ |
| [H08](../reports/decisions/H08.md) | ⚪ Under review | ···· | **Empty output and unrequested components**<br>What do `output`, `trace`, `stateDiff` and `vmTrace` hold when they are empty or not requested? | 🟡⚠️⚠️✅— | 🟡⚠️⚠️✅✅ |
| [H09](../reports/decisions/H09.md) | ⚪ Under review | ···· | **Failed frame results and error labels**<br>How does a failed frame report its failure: which `result` fields remain, and which `error` labels are allowed? | ⚠️⚠️⚠️⚠️— | ⚠️⚠️⚠️⚠️✅ |
| [H10](../reports/decisions/H10.md) | ⚪ Under review | ···· | **Creation result field names**<br>Which fields and values describe a creation result and a call action? | ⚠️✅✅✅— | ⚠️✅✅✅✅ |
| [H11](../reports/decisions/H11.md) | ⚪ Under review | ··👍· | **Empty trace-type selection**<br>What happens when the trace-type list is empty? | ⚠️⚠️🛠️✅— | ⚠️⚠️✅✅✅ |
| [H12](../reports/decisions/H12.md) | ⚪ Under review | ···· | **Raw-transaction block argument**<br>Does trace_rawTransaction take a block argument, and which state does it run against? | ❔❔❔❔— | ❔❔❔❔❔ |
| [H13](../reports/decisions/H13.md) | 🤝 Converged | ·👍·· | **Signed transaction execution validity**<br>Which validity checks does trace_rawTransaction apply to a signed transaction before tracing it? | ⚠️⚠️⚠️⚠️— | ⚠️⚠️⚠️⚠️✅ |
| [H14](../reports/decisions/H14.md) | ⚪ Under review | ···· | **Invalid-parameter error codes**<br>Which error codes do malformed parameters and rejected unsigned calls return? | ⚠️⚠️⚠️⚠️— | ⚠️⚠️⚠️⚠️❔ |
| [H15](../reports/decisions/H15.md) | ⚪ Under review | ···· | **Unsigned simulation fees and block environment**<br>Which fee defaults and block environment do unsigned trace_call and trace_callMany use? | ⚠️⚠️⚠️⚠️— | ⚠️⚠️⚠️⚠️✅ |
| [H16](../reports/decisions/H16.md) | ⚪ Under review | ···· | **Fee accounting and sequential state diffs**<br>Which fee payments does a transaction's stateDiff report, and where do block-level balance changes go? | ⚠️⚠️⚠️⚠️— | ⚠️⚠️🟡⚠️🟡 |
| [H17](../reports/decisions/H17.md) | ⚪ Under review | ··👍👍 | **New-account stateDiff encoding**<br>How does stateDiff mark an account that is created or deleted? | 🟡🟡🛠️🛠️— | 🟡🟡✅🛠️✅ |
| [H18](../reports/decisions/H18.md) | 🤝 Converged | ···👍 | **EIP-7702 code changes in stateDiff**<br>How does stateDiff report EIP-7702 delegation code changes? | 🟡✅✅🛠️— | 🟡✅✅🛠️✅ |
| [H19](../reports/decisions/H19.md) | ⚪ Under review | ···👍 | **vmTrace executing bytecode**<br>Which bytecode does a vmTrace frame's `code` hold? | 🟡🟡✅🛠️— | 🟡🟡✅🛠️✅ |
| [H20](../reports/decisions/H20.md) | ⚪ Under review | ···· | **vmTrace step timing and deltas**<br>What do a vmTrace step's `mem`, `cost` and `used` contain, and at which point are they measured? | ⚠️⚠️⚠️⚠️— | ⚠️⚠️⚠️⚠️✅ |
| [H21](../reports/decisions/H21.md) | ⚪ Under review | ··👍· | **vmTrace numeric and optional metadata encoding**<br>How are vmTrace numbers encoded, and which step fields are optional? | 🟡🟡🛠️✅— | 🟡🟡✅✅✅ |
| [H22](../reports/decisions/H22.md) | ⚪ Under review | ···· | **Precompile return bytes**<br>What output does a successful precompile call frame report? | 🛠️✅✅✅— | 🛠️✅✅✅✅ |
| [H23](../reports/decisions/H23.md) | ⚪ Under review | ···· | **Special-action address matching**<br>Which addresses of a CREATE, SELFDESTRUCT or reward record do trace_filter address lists match? | ⚠️⚠️⚠️⚠️— | ⚠️⚠️⚠️⚠️✅ |
| [H24](../reports/decisions/H24.md) | ⚪ Under review | ···· | **Sibling failure isolation**<br>Can a failure in one call frame change another frame's reported status? | 🛠️✅✅✅— | 🛠️✅✅✅✅ |
| [H25](../reports/decisions/H25.md) | ⚪ Under review | ···· | **Well-formed errors for rejected raw transactions**<br>How does a trace method report a validation or execution failure found while producing its response? | ⚠️✅🛠️✅— | ⚠️✅🛠️✅✅ |
| [H26](../reports/decisions/H26.md) | 🤝 Converged | ··👍· | **Account deletion across Cancun**<br>How does stateDiff report a deleted account, before and after EIP-6780? | 🛠️✅🛠️⚠️— | 🛠️✅✅⚠️✅ |
| [H27](../reports/decisions/H27.md) | ⚪ Under review | ···· | **Filter execution across fork boundaries**<br>When trace_filter spans a fork boundary, does each block run under its own fork rules and state? | 🛠️✅✅🟡— | 🛠️✅✅🟡✅ |
| [H28](../reports/decisions/H28.md) | 🤝 Converged | ·👍·· | **Historical state at system-operation boundaries**<br>Which state does a historical trace at block N run against, relative to the system operations of blocks N and N+1? | 🛠️🛠️✅✅— | 🛠️🛠️✅✅✅ |
| [H29](../reports/decisions/H29.md) | ⚪ Under review | ···· | **Precompile call-frame inclusion**<br>Which precompile calls appear as call frames? | ⚠️⚠️⚠️⚠️— | ⚠️⚠️⚠️⚠️✅ |
| [H30](../reports/decisions/H30.md) | ⚪ Under review | ···· | **Omitted trace_filter range bounds**<br>Which range does trace_filter use when fromBlock or toBlock is omitted? | ✅⚠️⚠️⚠️— | ✅⚠️⚠️✅✅ |
| [H31](../reports/decisions/H31.md) | ⚪ Under review | ···· | **Omitted trace_callMany block**<br>Is trace_callMany's block argument optional, and what is its default? | ⚠️✅✅⚠️— | ⚠️✅✅✅✅ |
| [H32](../reports/decisions/H32.md) | ⚪ Under review | ···· | **Trace block tags and pending state**<br>Which block tags do the trace methods accept, and how is `pending` handled? | ⚠️⚠️⚠️⚠️— | ⚠️⚠️⚠️⚠️❔ |

## Status key

### Client checks

**Client order:** [Besu](../reports/clients/besu.md) → [Erigon](../reports/clients/erigon.md) → [Nethermind](../reports/clients/nethermind.md) → [Reth](../reports/clients/reth.md) → [Geth draft fork](../reports/clients/geth.md). Geth is the experimental draft fork, dev only; — marks its absent stable build.

Stable/dev symbols describe captured checks: ✅ agree · ⚠️ differ · 🛠️ fix submitted · ⛔ unavailable · 🟡 partial · ⚪ unassessed · 🚧 blocked · ❔ policy open · 🔎 control/N/A. 🛠️ replaces ⚠️ or 🟡 while [related PRs](../docs/client-fixes.md) for that client and decision cover the measured difference and are not yet in the build; partial fixes leave ⚠️ or 🟡 in place. The captured checks are unchanged. [Outcome details](../reports/technical.md#test-status-key).

### Policy status

- ⚪ **Under review:** no recorded policy conclusion.
- 🔀 **Diverging:** competing policy positions.
- 🤝 **Converged:** direction aligned, implementation work or verification remains; not unanimous formal approval.
- 🧪 **Harmonized · dev:** converged and all declared cases pass on the captured development builds of Besu, Erigon, Nethermind and Reth.
- ✅ **Harmonized · stable:** the same is also verified on their captured releases.

Missing cases, ineligible runs, unsupported methods, unchecked assertions and invalid result schemas prevent harmonization. Each client/channel uses its most recently captured immutable build; evidence from different builds is never combined. These are milestones for the declared cases at the linked revisions, not full conformance or a claim about the latest builds. The experimental Geth fork is reported separately and is not a policy vote.

### Client positions

**Client order:** Besu → Erigon → Nethermind → Reth. 👍 agrees · ✋ agrees on conditions · 👎 objects · `·` no response. A position is a client team’s stated view of the recommendation, or a maintainer-merged fix that implements it (a complete, non-partial PR in [client fixes](../docs/client-fixes.md)). Positions are separate from the policy status and from the captured checks.

Decision pages link directly relevant upstream issues and PRs as context. A filed issue, proposed patch or merged change does not establish cross-client agreement or change the captured checks for the pinned builds; 🛠️ only marks a difference with a submitted fix, and [client fixes](../docs/client-fixes.md) tracks implementation and retesting.
