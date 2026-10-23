# Spec decision tables

[Back to the maintainer overview](README.md) · [Consistency laws](laws.md)

Each table encodes the clauses of the [pinned draft](https://github.com/banteg/execution-apis/tree/2f8ca20535d5797b21765dd75817453c5d0d108d) that decide one question, quoted verbatim, and enumerates every combination of the inputs they govern. A **conflict** is a cell whose clauses require different outcomes; a **gap** is a cell no clause decides. An **overlap** is a cell decided by several clauses that agree, where a sentence is implied by others. The encoding is a reading of the text, reviewed like any other assertion; its notes state the readings that shape the dimensions. Report generation fails when a quote no longer occurs in the pinned draft. [spec-tables.json](spec-tables.json) lists every clause and finding.

| Table | Topics | Cells | Conflicts | Gaps | Overlaps |
| --- | --- | --- | --- | --- | --- |
| [Frame emission](#frame-emission) | [H09](decisions/H09.md), [H29](decisions/H29.md) | 107 | 0 | 0 | 25 |
| [Address filtering](#address-filtering) | [H03](decisions/H03.md), [H04](decisions/H04.md), [H23](decisions/H23.md) | 144 | 0 | 0 | 8 |
| [Block selection](#block-selection) | [H06](decisions/H06.md), [H30](decisions/H30.md), [H31](decisions/H31.md), [H32](decisions/H32.md) | 70 | 0 | 0 | 0 |

## Frame emission

Does a call or create attempt produce a record, and does that record carry an error and a result?

**Dimensions:** position: root, nested; opcode: CALL, CALLCODE, DELEGATECALL, STATICCALL, CREATE, CREATE2; target: account, precompile; value: zero, transferred, inherited; outcome: success, revert, halt, collision, precheck depth, precheck balance, precheck nonce; fork: any fork, before Amsterdam, from Amsterdam.

**Readings:**

- “A precompile is an address in the precompile set active at the executing block's fork.” target is precompile exactly when the callee is in that set; a precompile cannot REVERT, so its failures are halts.
- “Retain root precompile calls regardless of value.” A root is the transaction itself: CALL or CREATE, whose prechecks are transaction validation, not frames.

| Finding | Outcome | Cells where | Cells | Clauses |
| --- | --- | --- | --- | --- |
| Overlap | emitted | nested · CALL · precompile · transferred · precheck depth · any fork<br>nested · CALL · precompile · transferred · precheck balance · any fork<br>nested · CALLCODE · precompile · transferred · precheck depth · any fork<br>nested · CALLCODE · precompile · transferred · precheck balance · any fork<br>nested · DELEGATECALL · precompile · inherited · precheck depth · any fork | 5 | agreeing: nested-value-precompile, call-precheck |
| Overlap | result | outcome: halt | 20 | agreeing: halt-result, halt |

<details><summary>Clauses</summary>

| Clause | Quote |
| --- | --- |
| baseline | “The transaction and every CALL-family or CREATE-family operation that targets an account outside the precompile set emit a frame, whether they succeed, revert or halt.” |
| root-precompile | “Retain root precompile calls regardless of value.” |
| nested-zero-precompile | “Omit nested precompile frames with zero value, including one whose call fails its precheck” |
| nested-value-precompile | “retain nested frames with nonzero transferred or inherited value, whether successful or failed” |
| call-precheck | “Any other CALL-family call that fails its precheck (call depth limit or insufficient balance) emits a frame with its action and error, a null result and no subtraces” |
| create-precheck | “A CREATE or CREATE2 that fails its precheck (call depth limit, insufficient balance or nonce overflow) emits the same kind of frame before Amsterdam” |
| create-precheck-amsterdam | “from Amsterdam the check runs in the creating opcode and no frame is emitted” |
| collision | “A CREATE whose address collides emits a create frame with error "Contract address collision" that consumes its gas.” |
| halt-result | “Exceptional halt, including an address collision; result is null.” |
| halt | “An exceptional halt consumes the frame's action gas; its result is null.” |
| revert | “A REVERT frame has error "Reverted" and a required result {gasUsed, output} carrying its revert bytes” |
| success | “Successful frame; result is required and error must be absent.” |
| error-alone | “error alone determines failure.” |

</details>

## Address filtering

Does trace_filter select a record, given how each address list relates to the record’s sides and the mode?

**Dimensions:** record: call, failed call, create, failed create, suicide, reward; from: unrestricted, match, miss; to: unrestricted, match, miss; mode: omitted, intersection, union.

**Readings:**

- “Match CALL sender/recipient, CREATE creator/created address and SELFDESTRUCT executing (self-destructing) account/beneficiary” from and to describe the list against the record’s side: unrestricted, containing that side’s address (match) or not (miss).
- “A record matches only addresses it reports; a failed CREATE reports no created address, so it has no created-address match.” A failed create’s to side never matches.
- “A reward matches toAddress by author and has no from side” A reward’s from side never matches.
- “Missing, null or empty lists are unrestricted.” unrestricted covers an omitted, null or empty list.

| Finding | Outcome | Cells where | Cells | Clauses |
| --- | --- | --- | --- | --- |
| Overlap | selected | reward · miss · unrestricted · omitted<br>reward · miss · unrestricted · intersection<br>reward · miss · match · omitted<br>reward · miss · match · intersection<br>reward · miss · miss · omitted<br>reward · miss · miss · intersection | 6 | agreeing: intersection, reward-intersection |
| Overlap | selected | reward · unrestricted · match · union<br>reward · miss · match · union | 2 | agreeing: union, reward-union |

<details><summary>Clauses</summary>

| Clause | Quote |
| --- | --- |
| intersection | “OR within each address list; AND between lists by default” |
| union | “mode union matches either populated list” |
| unrestricted | “Missing, null or empty lists are unrestricted.” |
| reward-intersection | “in intersection mode it is excluded whenever fromAddress is populated” |
| reward-union | “while in union mode a toAddress match suffices” |

</details>

## Block selection

What does a request return for each way of naming its block, when the block’s state is available or pruned?

**Dimensions:** method: trace_call, trace_callMany, trace_block, trace_replayBlockTransactions, trace_filter; selector: omitted, number, number beyond head, hash, unknown hash, non-canonical hash, latest, earliest, safe, finalized, unresolvable safe, pending; history: available, pruned.

**Readings:**

- “Resolve tags once per request.” trace_filter is read with both bounds naming the same block.
- “If the `safe` or `finalized` tag cannot be resolved to a block, the method responds as it does for an unknown block.” unresolvable safe stands for either tag before the chain has one.
- “pending, block-hash strings and block-hash objects are rejected (-32602 recommended); numeric bounds fit uint64” This names no response; the schema, which omits pending and hashes from trace_filter bounds, decides it.

Every cell is decided by exactly one clause.

<details><summary>Clauses</summary>

| Clause | Quote |
| --- | --- |
| schema | “Invalid params” |
| call-default | “Optional block, latest when omitted or null” |
| call-state | “Execution runs against the state at the end of the selected block, under its fork rules and block environment” |
| many-state | “The first item runs against the same state and environment as `trace_call` at the selected block” |
| call-unknown | “an unknown selected block returns an error (-32001, Resource not found), and a known block whose required state is pruned returns an error (4444 recommended)” |
| call-noncanonical | “A block hash, as a string or an object, selects that block even when it is not canonical, as in eth_call; with requireCanonical true a noncanonical hash returns an error (-32001).” |
| many-resolution | “Execution runs against the state at the end of the selected block, under its fork rules and block environment; in trace_callMany the first item runs against that state.” |
| call-pending | “is accepted only when the client has such a pending environment; a client without one rejects it (-32602 recommended) rather than substitute another block” |
| block-state | “Each block is traced from its parent's post-block state with its own pre-transaction system operations applied, under its own fork rules” |
| block-unknown | “An unknown selected block returns an error (-32001, Resource not found); a known block whose required state is pruned returns an error (4444 recommended)” |
| block-pending | “Block accepts pending only when the client has a pending block (the next block number with its pending transactions); otherwise pending is rejected (-32602 recommended).” |
| filter-default | “defaults omitted fromBlock and toBlock to the same latest head” |
| filter-range | “If either bound resolves beyond the current head block, or fromBlock resolves above toBlock, return an error (-32602 recommended)” |
| filter-records | “Indexed retrieval and replay must yield the same fork-correct per-block records, each block traced from its parent's post-block state.” |
| filter-finality-unavailable | “Unresolvable safe or finalized tags return an error” |
| filter-pruned | “return an error (4444 recommended) if required history is unavailable” |

</details>
