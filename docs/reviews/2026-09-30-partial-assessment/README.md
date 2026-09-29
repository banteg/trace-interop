# Partial assessment review

The selected September 29 matrix had 1,176 partially assessed trace observations
across 597 corpus/case pairs. Of those observations, 1,090 already had a
`change_needed` assertion. The other 86 comprised 48 unsupported Besu replay
requests and 38 accounting proof gaps. Every incomplete assertion in these
partial observations was `blocked`; none was `unassessed` because of a missing
assertion registration.

This review starts from `e5b50e4f8efebe70d85f22dd5adaf64148bb4755` and
[the selected matrix](../../../evidence/2026-09-29/refresh/matrix.json).
Counts are observation counts, including both release and development builds,
multiple trace selections, and repeated isolation captures. They are not counts
of distinct client bugs. Each row below assigns an observation to its first
applicable blocker, in table order, so the rows sum to 1,176.

| Main blocker | Observations | Attribution and action |
| --- | ---: | --- |
| Malformed JSON or an error envelope inside `result` | 839 | Client protocol defects: 325 Nethermind release responses and 257 responses from each Besu build. Keep H25 as the defect owner; downstream execution checks cannot read a valid result. |
| Opaque paired outcome | 180 | Generic/internal RPC failures, invalid output, or an unrecognized execution halt prevent the H15 comparison. An internal error does not establish a fee rejection. The Reth halt subset exposed a harness issue described below. |
| Unsupported methods | 48 | Besu does not implement `trace_replayTransaction`. H01 records unsupported; replay metadata/execution assertions cannot run. Method coverage is a profile decision, not evidence of malformed replay behavior. |
| Accounting proof gap | 48 | Refund uncertainty or a missing gas witness prevents an exact fee check. Eight zero-fee observations were unnecessarily blocked by the harness. Priced legacy nested calls and storage bundles need independent refund/state models. |
| Dependent property | 35 | Address-list semantics or another owned defect prevents isolating failure-frame/special-action selection. Resolve the upstream assertion before calling this a second bug. |
| Client rejection | 14 | The call returned an RPC error, leaving no execution result to inspect. The admission assertion can differ while execution properties stay blocked. |
| Missing frame or requested field | 12 | Failed prechecks/depth attempts and missing state-diff objects leave no independently identifiable target for the secondary assertion. Inspect the frame-inventory/response defect first. |

The wire evidence establishes that the largest category is not a JSON parser
bug. For example, Nethermind's `repeat/raw-wrong-chain` wire response contains
`"vmTrace":"output":null`, which is invalid JSON. Besu's `initial/call-many`
returns a second JSON-RPC envelope, with `error`, inside the outer `result`.
The collector preserves those bytes and correctly classifies them. Nethermind's
streamed-error fix is already tracked as
[Nethermind #13666](https://github.com/NethermindEth/nethermind/pull/13666);
the release capture predates its inclusion. The refreshed matrix will establish
current development behavior separately.

## Harness corrections

At zero effective fees, the beneficiary tip and base-fee burn are both zero.
Every gas/refund value in the allowed interval therefore gives the same balance
obligations. Requiring an exact refund before checking those obligations was
unnecessary. The correction still rejects an unexpected debit or beneficiary
payment and retains the unresolved refund check for priced calls.

The Reth fee-compatibility captures reveal a separate response-representation
issue. For the two fee-free, underfunded creation families, `eth_call` returns
`EVM error: OutOfFunds`; `trace_call` returns a root CREATE frame with
`Insufficient balance for transfer`. Both describe a funds execution halt.
The comparison now recognizes that witnessed correspondence. It does not
equate an EVM halt with a pre-execution validation rejection, or turn an empty
output into proof of success. When the root trace was not requested, the
comparison remains blocked. Unknown root failures also remain blocked; a
failed child does not make an independently successful root a failed call.
The separate admission-policy assertion still differs for these captures.

Reassessing the same immutable evidence with these corrections moves 24
observations from partial to assessed: eight zero-fee accounting observations
and sixteen root-witnessed halt comparisons. It leaves 1,152 partial
observations, of which 1,072 already differ and 80 contain only support/evidence
gaps. No wire response, request, client build or policy decision was changed.
“Assessed” continues to describe coverage, including assessed failures.

## Remaining evidence work

The 80 partial observations without a differing assertion are the 48 unsupported
Besu replay requests and 32 priced accounting observations: six nested
`initial/call-tree-stateDiff-priced` observations and 26 storage-bundle
observations in `a` and `callmany-isolation`. The bundles already check write/read
carry-over, reverted writes, and sender nonce transitions under H16. Their
additional H15 fee-accounting checks lack independently reconstructed
transaction-start storage/refunds. This is a bounded-model limitation, not a
demonstrated client bug or a reason to weaken the rule.

The useful next oracle is exact transaction-start storage and gas/refund
execution for those bundles, including a fresh transaction boundary per item
and rollback of reverted writes. The nested calltree needs its own execution
model. A client's state-diff balances cannot supply the expected refund: doing
that would make the accounting check circular. Generic/internal failures need
client repros or fixes before the secondary properties can be evaluated.

The report coverage explanation now distinguishes partial observations with an
existing differing assertion from those with only support/evidence gaps.
Regression tests use retained Reth captures and mutations that alter balance
settlement, halt/success classification, admission versus execution failure, and
root versus child failure ownership.

Validation: all 342 unit tests passed, the nine method schemas and recursive
negative vectors passed, and inventory verification checked 72 frozen inputs
and 33 decisions. The published reports were regenerated against the existing
matrix; its selection lock and wire evidence remain unchanged.
