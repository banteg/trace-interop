# Outstanding trace API harmonization decisions

Updated September 15, 2026. **Recommendations are proposals for discussion, not an adopted standard or a vote-based correctness claim.** Results apply to the pinned builds and generated fixtures; this adversarial sample is not a client-wide compatibility score.

The initial matrix used Reth 2.5.2+5a6940e3, Erigon 3.7.0-dev-c5a056d2, Nethermind 1.40.0-unstable+9cfa9cf5 and Besu 26.8.1 on one 48-block Prague chain. It contained 60 trace probes and six controls; eight trace probes were exact matches across all four. The extended pass uses the same four builds plus Reth nightly 2.5.2+95823365. The nightly predates the merged inspector fix and is not a fifth independent client vote.

## What the additional coverage changes

- **Query contracts now have stronger discriminators:** positive nested lookup, null/one-sided filters, CREATE/SELFDESTRUCT matching, pagination and fork-boundary completeness.
- **New reporting defects:** Besu leaks a sibling's revert status; Nethermind rewrites a 7,400-gas opcode cost and emits malformed JSON for several rejected raw transactions; pre-Cancun deletion is incompletely reported by Reth. Nonempty stateDiff-only output and authorization replacement/clearing extend earlier findings.
- **Useful agreement:** dependent storage writes survive between callMany entries, a reverting write rolls back, independent simulations remain isolated, pagination is consistent on a fixed range, MCOPY activation follows Cancun, and withdrawal balances agree.
- **Context matters:** Besu range traces diverge at several fork boundaries; Erigon exposes the following block's beacon-root update in historical queries. These should be investigated separately from cosmetic schema differences.

## Suggested meeting order

1. Agree the supported-method profile and query semantics (H01–H06, H23).
2. Settle output/error conventions and signed-versus-unsigned simulation rules (H07–H17, H25).
3. Route reporting defects and historical-context discrepancies to focused client work (H18–H28).

**Recommended starting position:** singular tree-path lookup; OR within address arrays and AND between them; empty filters mean unconstrained; null means not found; explicit errors mean unavailable history. Preserve actual execution bytes/state and apply the selected block's fork rules. These are proposed meanings, not majority-vote verdicts.

[Complete case index](../evidence/2026-09-15/case-index.md) · [Machine-readable ledger](ledger.json)

## Decisions and recommendations

<a id="h01"></a>
### H01 — Method coverage

**Disposition:** Scope decision

**Observed:** Besu returns -32601 for trace_replayTransaction. Erigon, Nethermind and Reth implement it. Besu supports block replay, so individual and block replay coverage differ.

**Recommendation:** Specify each method independently; make the implemented subset discoverable or explicitly declared. An unsupported method should return -32601, never a fabricated empty result. Add individual replay to Besu when practical rather than removing it from the common API.

**Why:** A caller should be able to distinguish an unsupported operation from a valid query with no trace.

**Next:** Agree the optional-method/conformance model at the meeting; no assumption of adopted optional status or Geth support.

**Reproducers:** [replay-7702-stateDiff](../evidence/2026-09-15/cases/replay-7702-stateDiff.json), [replay-7702-trace](../evidence/2026-09-15/cases/replay-7702-trace.json), [replay-7702-vmTrace](../evidence/2026-09-15/cases/replay-7702-vmTrace.json), [replay-block-tree](../evidence/2026-09-15/cases/replay-block-tree.json), [replay-missing](../evidence/2026-09-15/cases/replay-missing.json), [replay-revert-stateDiff](../evidence/2026-09-15/cases/replay-revert-stateDiff.json), [replay-revert-trace](../evidence/2026-09-15/cases/replay-revert-trace.json), [replay-revert-vmTrace](../evidence/2026-09-15/cases/replay-revert-vmTrace.json), [replay-transfer-stateDiff](../evidence/2026-09-15/cases/replay-transfer-stateDiff.json), [replay-transfer-trace](../evidence/2026-09-15/cases/replay-transfer-trace.json), [replay-transfer-vmTrace](../evidence/2026-09-15/cases/replay-transfer-vmTrace.json), [replay-tree-stateDiff](../evidence/2026-09-15/cases/replay-tree-stateDiff.json), [replay-tree-trace](../evidence/2026-09-15/cases/replay-tree-trace.json), [replay-tree-vmTrace](../evidence/2026-09-15/cases/replay-tree-vmTrace.json).

<a id="h02"></a>
### H02 — trace_get selector and return shape

**Disposition:** Spec decision

**Observed:** For a simple transfer, [] returns the root object in Erigon/Besu, null in Reth and [] in Nethermind. On the call tree, ["0x0"] returns the first child in Erigon/Besu and the root in Reth. Nethermind returns arrays; ["0x0","0x0"] returns two records rather than a nested-path lookup. A positive ["0x6","0x0"] probe selects the actual nested SELFDESTRUCT in Erigon/Besu. Reth returns null; Nethermind returns two unrelated records at [6] and [0].

**Recommendation:** Treat the argument as one traceAddress path: [] is root, [0] first child, [6,0] a nested child. Return one trace object, or null when the transaction/path does not exist. Specify the wire encoding of indices explicitly (prefer hex quantities for compatibility with these requests).

**Why:** The lookup argument should identify the same path that traceAddress describes, with a singular result matching the method name.

**Next:** Choose the tree-path contract and align Reth/Nethermind; the positive nested discriminator is now available.

**Reproducers:** [get-missing](../evidence/2026-09-15/cases/get-missing.json), [get-missing-tx](../evidence/2026-09-15/cases/get-missing-tx.json), [get-nested](../evidence/2026-09-15/cases/get-nested.json), [get-one](../evidence/2026-09-15/cases/get-one.json), [get-root](../evidence/2026-09-15/cases/get-root.json), [get-transfer-root](../evidence/2026-09-15/cases/get-transfer-root.json), [get-zero](../evidence/2026-09-15/cases/get-zero.json), [semantic-01--get-nested-positive](../evidence/2026-09-15/cases/semantic-01--get-nested-positive.json), [semantic-01--get-nested-parent](../evidence/2026-09-15/cases/semantic-01--get-nested-parent.json).

<a id="h03"></a>
### H03 — Filter composition and mode

**Disposition:** Spec decision

**Observed:** Both address lists produce six records in Erigon/Reth and one in Nethermind/Besu: the default splits OR versus AND. Explicit intersection produces the same one-record result in Erigon/Nethermind/Reth; Besu rejects the extra mode parameter. The union request does not make Nethermind join Erigon/Reth. With intersection and only one nonempty side, Erigon returns zero while Reth/Nethermind return matching records; Besu rejects mode. Unknown mode is rejected by Reth/Besu but silently behaves like the default in Erigon/Nethermind.

**Recommendation:** Use OR within each address list and AND between fromAddress and toAddress. One unconstrained side should not suppress matches. If union is retained, expose it explicitly as an optional extension and reject unsupported mode values rather than silently ignoring their meaning.

**Why:** Supplying a second filter normally narrows a search; combining two sets of alternatives should be explicit.

**Next:** Settle boolean composition and extension validation together; one-sided and unknown-mode fixtures are available.

**Reproducers:** [filter-both](../evidence/2026-09-15/cases/filter-both.json), [filter-from](../evidence/2026-09-15/cases/filter-from.json), [filter-intersection](../evidence/2026-09-15/cases/filter-intersection.json), [filter-to](../evidence/2026-09-15/cases/filter-to.json), [filter-union](../evidence/2026-09-15/cases/filter-union.json), [semantic-01--filter-from-only-intersection](../evidence/2026-09-15/cases/semantic-01--filter-from-only-intersection.json), [semantic-01--filter-to-only-intersection](../evidence/2026-09-15/cases/semantic-01--filter-to-only-intersection.json), [semantic-01--filter-both-unknown-mode](../evidence/2026-09-15/cases/semantic-01--filter-both-unknown-mode.json).

<a id="h04"></a>
### H04 — Empty address lists

**Disposition:** Spec decision

**Observed:** Explicit fromAddress:[] and toAddress:[] preserve each client’s unfiltered result in Erigon/Reth/Besu; Nethermind returns zero. Unfiltered lists themselves differ because of reward records and trace fields. The one-empty-side probes confirm Nethermind still returns zero. Null lists are accepted as unrestricted by Erigon/Nethermind/Besu and rejected as invalid params by Reth.

**Recommendation:** Treat an omitted list or [] as no restriction. If null is accepted, give it the same meaning; document whether null is accepted at all. A supplied nonempty list restricts that side.

**Why:** Programmatically adding an empty optional filter should not erase all results.

**Next:** Agree whether null is legal; distinguish that schema choice from empty-array matching and special-action membership.

**Reproducers:** [filter-all](../evidence/2026-09-15/cases/filter-all.json), [filter-empty](../evidence/2026-09-15/cases/filter-empty.json), [semantic-01--filter-both-null](../evidence/2026-09-15/cases/semantic-01--filter-both-null.json), [semantic-01--filter-from-empty-to-set](../evidence/2026-09-15/cases/semantic-01--filter-from-empty-to-set.json), [semantic-01--filter-to-empty-from-set](../evidence/2026-09-15/cases/semantic-01--filter-to-empty-from-set.json).

<a id="h05"></a>
### H05 — Post-merge reward records

**Disposition:** Spec decision

**Observed:** Besu/Nethermind append a zero-value rewardType:block record on this PoS chain; Erigon/Reth omit it. Nethermind omits several inapplicable fields where Besu emits null. This changes trace_block and unfiltered trace_filter counts. The 72-block fork chain now covers real PoW rewards and the Merge boundary. All four show a 100 Gwei withdrawal balance increase at block 52, but none returns a trace_filter match for that withdrawal recipient. This is not evidence that trace_filter enumerates every balance change.

**Recommendation:** Do not emit a synthetic PoW block reward on a PoS block. Represent real protocol balance changes only under explicitly defined semantics; keep transaction tips in transaction accounting. Define nullable localization fields separately for non-transaction records.

**Why:** A reward trace should correspond to a real protocol operation, not a zero-value placeholder that changes pagination.

**Next:** Specify which protocol operations belong in this namespace. Keep withdrawals and system transitions separate from transaction call traces unless explicitly included.

**Reproducers:** [block-transfer](../evidence/2026-09-15/cases/block-transfer.json), [block-tree](../evidence/2026-09-15/cases/block-tree.json), [filter-all](../evidence/2026-09-15/cases/filter-all.json), [filter-empty](../evidence/2026-09-15/cases/filter-empty.json), [fork-followup-01--withdrawal-balance-51](../evidence/2026-09-15/cases/fork-followup-01--withdrawal-balance-51.json), [fork-followup-01--withdrawal-balance-52](../evidence/2026-09-15/cases/fork-followup-01--withdrawal-balance-52.json), [fork-followup-01--withdrawal-filter-52](../evidence/2026-09-15/cases/fork-followup-01--withdrawal-filter-52.json), [fork-followup-01--withdrawal-block-52](../evidence/2026-09-15/cases/fork-followup-01--withdrawal-block-52.json).

<a id="h06"></a>
### H06 — Missing transactions and paths

**Disposition:** Spec decision / client exception

**Observed:** trace_transaction for an unknown hash returns null in Erigon/Reth, [] in Besu, and -32000 in Nethermind. Individual replay returns null in Erigon, -32000 in Nethermind, -32001 in Reth; Besu lacks the method. Nethermind trace_get on an unknown hash exposes an ArgumentNullException as -32602. In an explicitly pruned Reth fixture, old headers and receipts remain available and a latest-state call succeeds, while trace_transaction, trace_replayTransaction, trace_block and trace_filter for the old range return -32603 with a state-is-pruned message. Offline pruning removed 706 entries before the test; unknown-block probes are kept separate.

**Recommendation:** Return null for a well-formed lookup of an unknown transaction or trace path, consistently across these methods. Reserve [] for a successfully evaluated collection with no elements. Preserve -32601 for unsupported methods and use errors for unavailable/pruned state instead of pretending data is absent.

**Why:** Not found, empty, unsupported and unavailable are different states that callers need to distinguish.

**Next:** Choose an unavailable-history error contract. Extend the retention fixture to Erigon, Nethermind and Besu; the current pruning result is Reth-only.

**Reproducers:** [get-missing](../evidence/2026-09-15/cases/get-missing.json), [get-missing-tx](../evidence/2026-09-15/cases/get-missing-tx.json), [get-nested](../evidence/2026-09-15/cases/get-nested.json), [replay-missing](../evidence/2026-09-15/cases/replay-missing.json), [transaction-missing](../evidence/2026-09-15/cases/transaction-missing.json), [pruned-02--old-header](../evidence/2026-09-15/cases/pruned-02--old-header.json), [pruned-02--old-receipt](../evidence/2026-09-15/cases/pruned-02--old-receipt.json), [pruned-02--latest-call](../evidence/2026-09-15/cases/pruned-02--latest-call.json), [pruned-02--old-transaction](../evidence/2026-09-15/cases/pruned-02--old-transaction.json), [pruned-02--old-replay](../evidence/2026-09-15/cases/pruned-02--old-replay.json), [pruned-02--old-block](../evidence/2026-09-15/cases/pruned-02--old-block.json), [pruned-02--old-filter](../evidence/2026-09-15/cases/pruned-02--old-filter.json).

<a id="h07"></a>
### H07 — Replay transactionHash field

**Disposition:** Spec decision

**Observed:** Erigon/Nethermind include transactionHash in individual replay envelopes; Reth omits it. For the simple transfer’s trace-only replay this is the only Erigon–Reth difference. Block replay already agrees on the transfer block.

**Recommendation:** Include transactionHash in both individual and per-transaction block-replay envelopes. Do not require it for unsigned trace_call or trace_callMany simulations.

**Why:** A replay object should keep its identity when stored or moved out of its original request context.

**Next:** Confirm the envelope schema and add one serialization test; treat missing support in Besu separately under H01.

**Reproducers:** [replay-7702-stateDiff](../evidence/2026-09-15/cases/replay-7702-stateDiff.json), [replay-7702-trace](../evidence/2026-09-15/cases/replay-7702-trace.json), [replay-7702-vmTrace](../evidence/2026-09-15/cases/replay-7702-vmTrace.json), [replay-block-tree](../evidence/2026-09-15/cases/replay-block-tree.json), [replay-missing](../evidence/2026-09-15/cases/replay-missing.json), [replay-revert-stateDiff](../evidence/2026-09-15/cases/replay-revert-stateDiff.json), [replay-revert-trace](../evidence/2026-09-15/cases/replay-revert-trace.json), [replay-revert-vmTrace](../evidence/2026-09-15/cases/replay-revert-vmTrace.json), [replay-transfer-stateDiff](../evidence/2026-09-15/cases/replay-transfer-stateDiff.json), [replay-transfer-trace](../evidence/2026-09-15/cases/replay-transfer-trace.json), [replay-transfer-vmTrace](../evidence/2026-09-15/cases/replay-transfer-vmTrace.json), [replay-tree-stateDiff](../evidence/2026-09-15/cases/replay-tree-stateDiff.json), [replay-tree-trace](../evidence/2026-09-15/cases/replay-tree-trace.json), [replay-tree-vmTrace](../evidence/2026-09-15/cases/replay-tree-vmTrace.json).

<a id="h08"></a>
### H08 — Empty output and unrequested components

**Disposition:** Spec decision / likely reporting fix

**Observed:** Nethermind emits output:null in stateDiff-only cases where the executed return bytes are empty; the other successful clients emit "0x". The transfer’s trace and vmTrace-only calls agree across all four, so this depends on trace selection. A contract returning the nonempty word 42 confirms Nethermind output:null under ["stateDiff"], while all other builds return the bytes. Under ["vmTrace"], all return the nonempty output.

**Recommendation:** Keep a stable envelope: output is the execution return bytes ("0x" when empty); trace is [] when not requested; stateDiff and vmTrace are null when not requested. Requesting a different tracer must not change or erase the returned execution output.

**Why:** Empty bytes and an unavailable value are different, and selecting an auxiliary view should not change the primary call result.

**Next:** Preserve the execution return bytes independently of which optional trace components are requested.

**Reproducers:** [call-transfer-stateDiff](../evidence/2026-09-15/cases/call-transfer-stateDiff.json), [replay-7702-stateDiff](../evidence/2026-09-15/cases/replay-7702-stateDiff.json), [replay-revert-stateDiff](../evidence/2026-09-15/cases/replay-revert-stateDiff.json), [replay-transfer-stateDiff](../evidence/2026-09-15/cases/replay-transfer-stateDiff.json), [replay-tree-stateDiff](../evidence/2026-09-15/cases/replay-tree-stateDiff.json), [repeat-01--state-only-nonempty-output](../evidence/2026-09-15/cases/repeat-01--state-only-nonempty-output.json).

<a id="h09"></a>
### H09 — Failed frame results and error labels

**Disposition:** Spec decision

**Observed:** Erigon/Reth retain REVERT output and gasUsed in result; Besu/Nethermind omit that result in the replayed tree. Static-write failure labels differ across all four. Besu also supplies revertReason on a top-level revert. Omitted result versus result:null occurs on exceptional frames.

**Recommendation:** Always mark failure explicitly, preserve REVERT return bytes and measured gasUsed when available, and define a small stable set of failure kinds. Human-readable explanations or decoded revertReason may be optional. Use null for an inapplicable result; never manufacture a successful result for an exceptional halt.

**Why:** Consumers need the raw revert data and failure identity without parsing implementation-specific English or mistaking a failure for success.

**Next:** Agree exact field placement and stable failure kinds. Separate REVERT, exceptional halt and SELFDESTRUCT/no-result cases in fixtures; do not require identical free-text descriptions.

**Reproducers:** [block-tree](../evidence/2026-09-15/cases/block-tree.json), [call-many](../evidence/2026-09-15/cases/call-many.json), [call-many-priced](../evidence/2026-09-15/cases/call-many-priced.json), [call-many-transfers](../evidence/2026-09-15/cases/call-many-transfers.json), [call-tree-trace](../evidence/2026-09-15/cases/call-tree-trace.json), [call-tree-trace-priced](../evidence/2026-09-15/cases/call-tree-trace-priced.json), [filter-all](../evidence/2026-09-15/cases/filter-all.json), [filter-from](../evidence/2026-09-15/cases/filter-from.json), [filter-to](../evidence/2026-09-15/cases/filter-to.json), [filter-union](../evidence/2026-09-15/cases/filter-union.json), [replay-revert-trace](../evidence/2026-09-15/cases/replay-revert-trace.json), [replay-tree-trace](../evidence/2026-09-15/cases/replay-tree-trace.json), [transaction-revert](../evidence/2026-09-15/cases/transaction-revert.json), [transaction-tree](../evidence/2026-09-15/cases/transaction-tree.json).

<a id="h10"></a>
### H10 — Creation result field names

**Disposition:** Spec decision / likely schema fix

**Observed:** Besu’s CREATE record in the call-tree result uses result.output:"0x" where Erigon uses result.code:"0x". This is separate from vmTrace.code, which should describe executing bytecode. In the mixed CREATE/CREATE2 simulation, all clients produce the same two contract addresses and runtime code. Besu omits creationMethod on both Parity frames; its debug callTracer correctly distinguishes CREATE and CREATE2. This probe does not establish the earlier source-only claim that both would be mislabeled CREATE2.

**Recommendation:** Use result.address, result.code and result.gasUsed for successful creation. result.code is deployed runtime bytecode, including "0x" for an empty deployment. Use result.output for CALL results; vmTrace.code for executing initcode.

**Why:** Creation has two different bytecodes—initcode and deployed code—and their field meanings should remain distinct.

**Next:** Specify creationMethod if it is required; retain the successful mixed-creation probe and investigate historical-method metadata separately.

**Reproducers:** [block-tree](../evidence/2026-09-15/cases/block-tree.json), [call-constructor](../evidence/2026-09-15/cases/call-constructor.json), [call-constructor-priced](../evidence/2026-09-15/cases/call-constructor-priced.json), [call-tree-trace-priced](../evidence/2026-09-15/cases/call-tree-trace-priced.json), [replay-block-tree](../evidence/2026-09-15/cases/replay-block-tree.json), [transaction-tree](../evidence/2026-09-15/cases/transaction-tree.json), [repeat-01--call-mixed-create](../evidence/2026-09-15/cases/repeat-01--call-mixed-create.json), [repeat-01--debug-mixed-create](../evidence/2026-09-15/cases/repeat-01--debug-mixed-create.json).

<a id="h11"></a>
### H11 — Empty trace-type selection

**Disposition:** Likely client bug

**Observed:** With a valid nonzero fee and traceTypes:[], Erigon/Reth/Besu return the same output envelope. Nethermind returns -32603 with “Sequence contains no elements”.

**Recommendation:** Accept an empty selection, execute the call and return its output with empty/unrequested components. Never leak a collection-reduction exception.

**Why:** An empty list of auxiliary views is a natural request for just the execution output, and already works identically in three clients.

**Next:** A focused Nethermind fix and regression fixture can proceed independently of the broader API design.

**Reproducers:** [call-empty-types](../evidence/2026-09-15/cases/call-empty-types.json), [call-empty-types-priced](../evidence/2026-09-15/cases/call-empty-types-priced.json).

<a id="h12"></a>
### H12 — Raw-transaction block argument

**Disposition:** Spec / extension decision

**Observed:** Reth accepts a third block argument; Erigon/Nethermind/Besu reject that three-argument request with -32602. A nonce-correct two-argument request executes on all four.

**Recommendation:** Standardize the existing two-argument baseline with an explicit default of latest state. Treat an optional third block selector as a separately negotiated extension until clients adopt it; reject unsupported extra arguments consistently.

**Why:** The baseline should be usable on all four today without silently changing which state is traced.

**Next:** Decide whether to add the block selector later. Keep its acceptance test separate from raw transaction execution fidelity.

**Reproducers:** [raw-valid](../evidence/2026-09-15/cases/raw-valid.json).

<a id="h13"></a>
### H13 — Signed transaction nonce validation

**Disposition:** Spec decision / likely client fix

**Observed:** For a signed nonce-0 transaction against state nonce 133, Reth returns nonce-too-low; the other three produce results. Besu’s invalid-nonce result loses stateDiff and the action gas field. With signed nonce 133, all four execute and Besu restores those fields. Further signed-transaction probes cover high nonce, wrong chain, insufficient funds, intrinsic gas too low and fee cap below base fee. Reth rejects all five invalid cases. Erigon/Nethermind accept the high-nonce case; Erigon also simulates the unfunded sender. Besu returns result-shaped partial outcomes for the invalid cases. Nethermind produces malformed JSON for four rejection cases (H25).

**Recommendation:** For trace_rawTransaction, honor the signed transaction’s nonce and validity rules at the selected state. Reject nonce mismatch with a stable transaction-validation error. Use unsigned trace_call for hypothetical execution that deliberately relaxes admission rules.

**Why:** A signed transaction is a concrete transaction, so tracing should not silently rewrite its nonce or return a partial-looking success.

**Next:** Agree admission semantics for signed raw transactions; fix malformed responses independently of that policy choice.

**Reproducers:** [raw-valid-current-nonce](../evidence/2026-09-15/cases/raw-valid-current-nonce.json), [raw-valid-default-block](../evidence/2026-09-15/cases/raw-valid-default-block.json), [repeat-01--raw-nonce-high](../evidence/2026-09-15/cases/repeat-01--raw-nonce-high.json), [repeat-01--raw-wrong-chain](../evidence/2026-09-15/cases/repeat-01--raw-wrong-chain.json), [repeat-01--raw-insufficient-funds](../evidence/2026-09-15/cases/repeat-01--raw-insufficient-funds.json), [repeat-01--raw-low-gas](../evidence/2026-09-15/cases/repeat-01--raw-low-gas.json), [repeat-01--raw-below-basefee](../evidence/2026-09-15/cases/repeat-01--raw-below-basefee.json).

<a id="h14"></a>
### H14 — Invalid-parameter error codes

**Disposition:** Spec decision

**Observed:** Malformed raw bytes return -32602 in Reth/Besu but -32000 in Erigon/Nethermind. Excess positional arguments consistently use -32602, with different messages. Nethermind also misclassifies an unknown transaction as invalid params in trace_get. All but Besu reject a scalar fromAddress; Besu accepts it as a singleton filter. Negative count is rejected by Erigon/Reth and returns [] in Nethermind/Besu. Unknown filter keys are rejected by Reth/Besu and ignored by Erigon/Nethermind.

**Recommendation:** Use -32602 for malformed encodings, wrong types and unsupported argument shapes. Use a documented execution/validation error for a well-formed but invalid transaction. Keep messages implementation-specific; omit internal stack traces.

**Why:** Callers should distinguish a malformed request from a valid request that cannot execute, without text matching.

**Next:** Specify accepted types, bounds and unknown-field handling, then align parameter validation; do not conflate validation with EVM errors.

**Reproducers:** [get-missing-tx](../evidence/2026-09-15/cases/get-missing-tx.json), [raw-invalid](../evidence/2026-09-15/cases/raw-invalid.json), [raw-valid](../evidence/2026-09-15/cases/raw-valid.json), [semantic-01--filter-wrong-address-type](../evidence/2026-09-15/cases/semantic-01--filter-wrong-address-type.json), [semantic-01--filter-negative-count](../evidence/2026-09-15/cases/semantic-01--filter-negative-count.json), [semantic-01--filter-unknown-field](../evidence/2026-09-15/cases/semantic-01--filter-unknown-field.json).

<a id="h15"></a>
### H15 — Unsigned simulation fees and block environment

**Disposition:** Spec decision / likely environment bug

**Observed:** For explicit gasPrice:0, Reth/Nethermind execute; Erigon rejects below-base-fee and Besu’s single call returns an internal error. The embedded callenv contract reads BASEFEE as zero in Reth and the actual block value 0x199876 in Nethermind. With a sufficient fee, all four expose 0x199876.

**Recommendation:** Allow explicit zero-fee unsigned simulations without changing the selected block’s BASEFEE or other block fields. With nonzero supplied fees, use those fees consistently in opcode context and simulated accounting. Apply the same policy to trace_call and trace_callMany; keep strict signed validation separate.

**Why:** Relaxing transaction admission for a hypothetical call should not silently rewrite the block the caller selected.

**Next:** Agree the fee-free simulation rule, then fix the block-environment discrepancy. The source contract confirms BASEFEE is returned as word 3; this is more than an error-message difference.

**Reproducers:** [call-constructor](../evidence/2026-09-15/cases/call-constructor.json), [call-constructor-priced](../evidence/2026-09-15/cases/call-constructor-priced.json), [call-many](../evidence/2026-09-15/cases/call-many.json), [call-many-priced](../evidence/2026-09-15/cases/call-many-priced.json), [call-many-transfers](../evidence/2026-09-15/cases/call-many-transfers.json), [call-tree-stateDiff](../evidence/2026-09-15/cases/call-tree-stateDiff.json), [call-tree-stateDiff-priced](../evidence/2026-09-15/cases/call-tree-stateDiff-priced.json), [call-tree-trace](../evidence/2026-09-15/cases/call-tree-trace.json), [call-tree-trace-priced](../evidence/2026-09-15/cases/call-tree-trace-priced.json), [call-tree-vmTrace](../evidence/2026-09-15/cases/call-tree-vmTrace.json), [call-tree-vmTrace-priced](../evidence/2026-09-15/cases/call-tree-vmTrace-priced.json).

<a id="h16"></a>
### H16 — Fee accounting and sequential state diffs

**Disposition:** Spec decision / likely accounting bug

**Observed:** In nonce-correct raw tracing, Nethermind/Besu/Reth debit sender value plus gas; Erigon debits only the transferred value while still crediting the fee recipient. Unsigned Reth transfer simulation debits value only and omits the recipient fee credit. All four callMany transfer probes carry the recipient balance 0→1→2 and nonce 133→134→135; their fee diffs still disagree. A dependent storage write(42), reverting write(43), read sequence returns 42 after the revert in every client. Sender nonce advances for each call, and an independent subsequent simulation reads the original zero. Thus the observed accounting differences do not demonstrate broken storage carry-over or rollback.

**Recommendation:** For signed/raw and mined replay, report the complete actual transition: sender pays value plus gas, fee recipient gets the tip, base fee is burned. For unsigned calls use H15’s documented policy consistently. Each callMany result should describe its own transition from the preceding call’s post-state, not a cumulative diff from the original state.

**Why:** A state diff should be internally coherent and reconstructible; an ordered multi-call simulation should have one predictable state timeline.

**Next:** Resolve fee and environment rules while preserving the now-tested storage carry-over, revert rollback and simulation isolation. Broader warm-access/refund behavior remains to test.

**Reproducers:** [call-many](../evidence/2026-09-15/cases/call-many.json), [call-many-priced](../evidence/2026-09-15/cases/call-many-priced.json), [call-many-transfers](../evidence/2026-09-15/cases/call-many-transfers.json), [call-transfer-stateDiff](../evidence/2026-09-15/cases/call-transfer-stateDiff.json), [call-tree-stateDiff](../evidence/2026-09-15/cases/call-tree-stateDiff.json), [call-tree-stateDiff-priced](../evidence/2026-09-15/cases/call-tree-stateDiff-priced.json), [raw-valid-current-nonce](../evidence/2026-09-15/cases/raw-valid-current-nonce.json), [raw-valid-default-block](../evidence/2026-09-15/cases/raw-valid-default-block.json), [replay-block-tree](../evidence/2026-09-15/cases/replay-block-tree.json), [replay-tree-stateDiff](../evidence/2026-09-15/cases/replay-tree-stateDiff.json), [semantic-01--many-storage-write-read](../evidence/2026-09-15/cases/semantic-01--many-storage-write-read.json), [semantic-01--many-storage-write-revert-read](../evidence/2026-09-15/cases/semantic-01--many-storage-write-revert-read.json), [semantic-01--control-storage-after-many](../evidence/2026-09-15/cases/semantic-01--control-storage-after-many.json).

<a id="h17"></a>
### H17 — New-account stateDiff encoding

**Disposition:** Spec decision / likely serializer fix

**Observed:** For the previously absent transfer recipient, Erigon/Besu use + tags for balance/code/nonce, Nethermind uses + for balance/nonce but code:"=", and Reth uses a * balance change from zero with unchanged code/nonce markers.

**Recommendation:** Make account existence explicit: + for fields of a newly created account (including empty code and nonce zero), - for deletion, * for a changed existing value, = for unchanged existing fields. If an address already existed with empty code, do not mark it as newly created.

**Why:** Absent and existing-but-empty are different states; consumers should be able to reconstruct the change without guessing.

**Next:** Confirm the historical delta model and add pre-funded empty account and deletion fixtures. Current evidence isolates a previously absent recipient.

**Reproducers:** [call-constructor](../evidence/2026-09-15/cases/call-constructor.json), [call-constructor-priced](../evidence/2026-09-15/cases/call-constructor-priced.json), [call-many-transfers](../evidence/2026-09-15/cases/call-many-transfers.json), [call-transfer-stateDiff](../evidence/2026-09-15/cases/call-transfer-stateDiff.json), [raw-valid](../evidence/2026-09-15/cases/raw-valid.json), [raw-valid-current-nonce](../evidence/2026-09-15/cases/raw-valid-current-nonce.json), [raw-valid-default-block](../evidence/2026-09-15/cases/raw-valid-default-block.json), [replay-block-tree](../evidence/2026-09-15/cases/replay-block-tree.json), [replay-tree-stateDiff](../evidence/2026-09-15/cases/replay-tree-stateDiff.json).

<a id="h18"></a>
### H18 — EIP-7702 code changes in stateDiff

**Disposition:** Likely client bug

**Observed:** The mined authorization replay changes the authority nonce in all three implementing clients. Erigon/Nethermind also report empty code→delegation indicator; Reth reports code:"=". This extends the earlier simulation reproduction to mined replay on the shared chain. Signed type-4 simulations now cover delegation set, replacement, clearing and setting followed by a reverted call. Erigon/Nethermind/Besu report the actual authorization code changes, including changes surviving execution revert; both tested Reth binary images continue to report code:"=". The diagnostic source build with the merged inspector fix also retains code:"=" for authorization clearing and authorization followed by revert.

**Recommendation:** Report every actual delegation-code transition, including set, replace and clear, independently of account-creation flags. Preserve authorization changes when later execution reverts, according to execution semantics.

**Why:** stateDiff must include code that changed, even if the account already existed.

**Next:** Fix account code-change reporting separately; these cases persist after the VM-delta fix.

**Reproducers:** [replay-7702-stateDiff](../evidence/2026-09-15/cases/replay-7702-stateDiff.json), [replay-block-tree](../evidence/2026-09-15/cases/replay-block-tree.json), [semantic-01--auth-set](../evidence/2026-09-15/cases/semantic-01--auth-set.json), [semantic-01--auth-replace](../evidence/2026-09-15/cases/semantic-01--auth-replace.json), [semantic-01--auth-clear](../evidence/2026-09-15/cases/semantic-01--auth-clear.json), [semantic-01--auth-set-revert](../evidence/2026-09-15/cases/semantic-01--auth-set-revert.json), [fixed-01--auth-clear](../evidence/2026-09-15/cases/fixed-01--auth-clear.json), [fixed-01--auth-set-revert](../evidence/2026-09-15/cases/fixed-01--auth-set-revert.json).

<a id="h19"></a>
### H19 — vmTrace executing bytecode

**Disposition:** Likely client bug

**Observed:** All clients execute the constructor and return runtime 0x01. Erigon/Nethermind/Besu report initcode 0x60016000526001601ff3; Reth reports vmTrace.code:"0x" with nonempty operations. Earlier simulations also reproduced stale/missing delegated bytecode. On delegation set, the two Reth images emit vmTrace.code:0x despite executing the return42 target. On replacement they report the old delegation indicator instead of the newly executed reverting bytecode. Other clients provide the executed target code. The source build with the merged inspector fix still returns empty constructor code and empty/stale delegation code in the retained examples. The VM-delta fix does not resolve bytecode identity.

**Recommendation:** Record the bytecode actually executed in each frame: initcode for creation, resolved implementation code for delegation, and the relevant code source for delegatecall/callcode. Do not populate it from an address-only pre-state lookup after tracing.

**Why:** The operations must be decodable against the bytes in their own frame.

**Next:** Fix bytecode population separately from the already-retested instruction deltas.

**Reproducers:** [call-constructor](../evidence/2026-09-15/cases/call-constructor.json), [call-constructor-priced](../evidence/2026-09-15/cases/call-constructor-priced.json), [call-tree-vmTrace](../evidence/2026-09-15/cases/call-tree-vmTrace.json), [call-tree-vmTrace-priced](../evidence/2026-09-15/cases/call-tree-vmTrace-priced.json), [replay-block-tree](../evidence/2026-09-15/cases/replay-block-tree.json), [replay-tree-vmTrace](../evidence/2026-09-15/cases/replay-tree-vmTrace.json), [semantic-01--auth-set](../evidence/2026-09-15/cases/semantic-01--auth-set.json), [semantic-01--auth-replace](../evidence/2026-09-15/cases/semantic-01--auth-replace.json), [fixed-01--constructor](../evidence/2026-09-15/cases/fixed-01--constructor.json), [fixed-01--auth-clear](../evidence/2026-09-15/cases/fixed-01--auth-clear.json), [fixed-01--auth-set-revert](../evidence/2026-09-15/cases/fixed-01--auth-set-revert.json).

<a id="h20"></a>
### H20 — vmTrace step timing and deltas

**Disposition:** Implementation alignment / release retest

**Observed:** In the constructor, the first PUSH costs 3: Erigon/Nethermind/Besu report ex.used=46847, Reth 46850. MSTORE at pc 4 has its write at that step in the other three; Reth reports an empty write, then repeats the data at later steps with off=32. More complex VM differences remain in the raw captures. A dedicated CALLDATACOPY at pc 8 has a gas cost of 7,400 in all four debug opcode traces. Nethermind vmTrace alone reports 9,700; all call-frame totals remain 7,409. The minimal code is 0x6174e060006101803700 and the discrepancy repeated. An interpreter-based diagnostic Reth build at 8194fcedefcfa1cbfe11d57f30cae45a21fe136f, with revm-inspectors pinned to merged commit 19746b981132035fdfb7ca89c3faab6258104a18, confirms post-step ex.used, same-step MSTORE/MCOPY deltas, and CALL success/output writes in the focused fixtures. A CALL forwarding 60,000 gas records gross cost 62,603 and post-return remaining gas 576,370; the other clients agree on those gas numbers. This is a source-override diagnostic build, not released adoption.

**Recommendation:** Define ex.used as post-operation gas remaining, and mem/store/push as effects of that same operation. Use null for no memory write, with actual offset and bytes for a write. Specify call/return gas boundaries using dedicated nested-call fixtures before choosing detailed gas formulas.

**Why:** A consumer applying deltas in order should reconstruct the state after every opcode without shifting effects to neighboring steps.

**Next:** Retain the fixed regression cases. Nested warm-access, stipend, refund and output-memory edge cases still require broader coverage.

**Reproducers:** [call-constructor](../evidence/2026-09-15/cases/call-constructor.json), [call-constructor-priced](../evidence/2026-09-15/cases/call-constructor-priced.json), [call-tree-vmTrace](../evidence/2026-09-15/cases/call-tree-vmTrace.json), [call-tree-vmTrace-priced](../evidence/2026-09-15/cases/call-tree-vmTrace-priced.json), [replay-block-tree](../evidence/2026-09-15/cases/replay-block-tree.json), [replay-revert-vmTrace](../evidence/2026-09-15/cases/replay-revert-vmTrace.json), [replay-tree-vmTrace](../evidence/2026-09-15/cases/replay-tree-vmTrace.json), [repeat-01--call-gas7400](../evidence/2026-09-15/cases/repeat-01--call-gas7400.json), [repeat-01--debug-gas7400-opcodes](../evidence/2026-09-15/cases/repeat-01--debug-gas7400-opcodes.json), [repeat-01--constructor](../evidence/2026-09-15/cases/repeat-01--constructor.json), [repeat-01--call-mcopy](../evidence/2026-09-15/cases/repeat-01--call-mcopy.json), [fixed-01--constructor](../evidence/2026-09-15/cases/fixed-01--constructor.json), [fixed-01--call-return42](../evidence/2026-09-15/cases/fixed-01--call-return42.json), [fixed-01--call-mcopy](../evidence/2026-09-15/cases/fixed-01--call-mcopy.json), [fixed-01--call-siblings-revert-ok](../evidence/2026-09-15/cases/fixed-01--call-siblings-revert-ok.json).

<a id="h21"></a>
### H21 — vmTrace numeric and optional metadata encoding

**Disposition:** Spec decision

**Observed:** Nethermind push values use byte-oriented forms such as 0x01 and 0x00 where the other three use 0x1 and 0x0. Erigon supplies op and idx; Reth supplies op; Besu/Nethermind omit both. These differences alone prevent exact JSON equality.

**Recommendation:** Encode stack words as minimal hex quantities (zero is 0x0), memory/code as even-length byte strings. Make op/idx optional metadata; require consumers to accept their absence and validate consistency when present. Keep required execution fields independent of these annotations.

**Why:** Numeric values and byte arrays have different formatting needs; optional convenience labels should not determine whether a trace can be consumed.

**Next:** Agree schema types and extension policy. A diagnostic comparison may show a separate typed-semantic projection, but must retain the exact wire differences.

**Reproducers:** [call-constructor](../evidence/2026-09-15/cases/call-constructor.json), [call-constructor-priced](../evidence/2026-09-15/cases/call-constructor-priced.json), [call-tree-vmTrace](../evidence/2026-09-15/cases/call-tree-vmTrace.json), [call-tree-vmTrace-priced](../evidence/2026-09-15/cases/call-tree-vmTrace-priced.json), [replay-block-tree](../evidence/2026-09-15/cases/replay-block-tree.json), [replay-revert-vmTrace](../evidence/2026-09-15/cases/replay-revert-vmTrace.json), [replay-tree-vmTrace](../evidence/2026-09-15/cases/replay-tree-vmTrace.json).

<a id="h22"></a>
### H22 — Precompile return bytes

**Disposition:** Likely client bug

**Observed:** All four return top-level output 0x11223344 from the identity precompile. Erigon/Nethermind/Reth repeat those bytes in trace[0].result.output; Besu returns 0x there.

**Recommendation:** Report the actual return bytes in both the execution envelope and the corresponding successful call-frame result, including precompiles with no EVM bytecode.

**Why:** Two views of the same successful call should not disagree about its return value.

**Next:** A focused Besu reporting fix and regression fixture can proceed without waiting on broad API policy.

**Reproducers:** [call-identity](../evidence/2026-09-15/cases/call-identity.json).

<a id="h23"></a>
### H23 — Special-action address matching

**Disposition:** Spec decision / client discrepancy

**Observed:** Erigon, Nethermind and Reth match a CREATE by its created address and a SELFDESTRUCT by its source/refund beneficiary. Besu misses the CREATE and SELFDESTRUCT records under those filters, even though they exist in the unfiltered transaction tree.

**Recommendation:** Define from/to equivalents per action: creator/created address for CREATE, destroyed account/refund beneficiary for SELFDESTRUCT. Include these records when the corresponding address matches.

**Why:** Address-based history should not silently omit a transfer or creation because its action uses different field names.

**Next:** Agree the action mapping and add the discriminating filter fixtures.

**Reproducers:** [semantic-01--filter-created-to](../evidence/2026-09-15/cases/semantic-01--filter-created-to.json), [semantic-01--filter-suicide-from](../evidence/2026-09-15/cases/semantic-01--filter-suicide-from.json), [semantic-01--filter-suicide-beneficiary](../evidence/2026-09-15/cases/semantic-01--filter-suicide-beneficiary.json), [semantic-01--transaction-tree](../evidence/2026-09-15/cases/semantic-01--transaction-tree.json).

<a id="h24"></a>
### H24 — Sibling failure isolation

**Disposition:** Reproduced reporting defect

**Observed:** For CALL(revert) followed by CALL(return42), Besu marks the successful second sibling Reverted and omits its result. Reversing sibling order avoids the error. All other Parity traces and every debug callTracer, including Besu, identify the second call as successful with return word 42. The failing order was repeated.

**Recommendation:** Attach error and result data to the actual call frame. A sibling failure must not change another frame's status.

**Why:** A successful caller can handle a failed subcall and continue; frame results must preserve that distinction.

**Next:** Prepare a focused Besu regression and fix without waiting for broad schema policy.

**Reproducers:** [repeat-01--call-siblings-revert-ok](../evidence/2026-09-15/cases/repeat-01--call-siblings-revert-ok.json), [repeat-01--debug-siblings-revert-ok](../evidence/2026-09-15/cases/repeat-01--debug-siblings-revert-ok.json).

<a id="h25"></a>
### H25 — Well-formed errors for rejected raw transactions

**Disposition:** Reproduced response serialization defect

**Observed:** Nethermind returns malformed JSON for wrong-chain, unfunded, intrinsic-gas-too-low and below-basefee signed raw probes. All-component and trace-only/stateDiff-only/vmTrace-only repeats reproduce it. One captured body starts {"jsonrpc":"2.0","result":{"vmTrace":"output":null,...; this is not a JSON-RPC error object.

**Recommendation:** Return one complete valid JSON-RPC error response on validation failure. Do not begin serializing a result before validation has succeeded.

**Why:** Clients must be able to parse failures and associate them with a request, regardless of the chosen signed-transaction admission policy.

**Next:** Fix the serializer/error path; retain raw malformed response text in regression evidence.

**Reproducers:** [repeat-01--raw-below-basefee](../evidence/2026-09-15/cases/repeat-01--raw-below-basefee.json), [repeat-01--raw-below-basefee-trace](../evidence/2026-09-15/cases/repeat-01--raw-below-basefee-trace.json), [repeat-01--raw-below-basefee-stateDiff](../evidence/2026-09-15/cases/repeat-01--raw-below-basefee-stateDiff.json), [repeat-01--raw-below-basefee-vmTrace](../evidence/2026-09-15/cases/repeat-01--raw-below-basefee-vmTrace.json).

<a id="h26"></a>
### H26 — Account deletion across Cancun

**Disposition:** Reproduced stateDiff discrepancy

**Observed:** For an existing contract self-destructing before Cancun, Erigon/Besu use deletion markers for balance/code/nonce; Nethermind uses changes whose destination is null, and Reth reports balance going to zero but code/nonce unchanged. After Cancun, all correctly retain the existing contract code and report the balance transfer. The before/after Parity cases repeated.

**Recommendation:** Represent genuine account deletion with the deletion marker, including code, nonce and storage. After EIP-6780, an existing account survives SELFDESTRUCT; do not report code deletion.

**Why:** Deletion and a zero balance with retained code are observably different states. Apply the rules of the selected block.

**Next:** Align deletion encoding and fix missing Reth deletion data. The separate Besu prestateTracer probe had no complete response and is not used as an execution oracle.

**Reproducers:** [fork-followup-01--destroy-trace-55](../evidence/2026-09-15/cases/fork-followup-01--destroy-trace-55.json), [fork-followup-01--destroy-trace-56](../evidence/2026-09-15/cases/fork-followup-01--destroy-trace-56.json).

<a id="h27"></a>
### H27 — Filter execution across fork boundaries

**Disposition:** Reproduced cross-method discrepancy

**Observed:** In Besu, concatenating trace_block for blocks 35 and 36 gives 16 records, but trace_filter over the same London boundary gives 8. Across Cancun and Prague, range filtering also changes gas/output/error fields compared with the individual blocks. Erigon, Nethermind and both Reth builds match per-block concatenation at all five tested boundaries. A separate ten-probe Besu-only repeat matches every earlier response exactly, including the London omission and Cancun/Prague field changes.

**Recommendation:** Execute each block with its own fork rules and state, then filter and paginate the resulting ordered records. A range query should agree with the corresponding per-block queries.

**Why:** The same block must not trace differently depending on the other blocks included in a query.

**Next:** The repeated fixtures are ready for a focused processor-context investigation and regression.

**Reproducers:** [forks-01--block-35](../evidence/2026-09-15/cases/forks-01--block-35.json), [forks-01--block-36](../evidence/2026-09-15/cases/forks-01--block-36.json), [forks-01--filter-across-36](../evidence/2026-09-15/cases/forks-01--filter-across-36.json), [forks-01--filter-across-56](../evidence/2026-09-15/cases/forks-01--filter-across-56.json), [forks-01--filter-across-60](../evidence/2026-09-15/cases/forks-01--filter-across-60.json), [boundary-repeat-01--block-35](../evidence/2026-09-15/cases/boundary-repeat-01--block-35.json), [boundary-repeat-01--block-36](../evidence/2026-09-15/cases/boundary-repeat-01--block-36.json), [boundary-repeat-01--filter-across-36](../evidence/2026-09-15/cases/boundary-repeat-01--filter-across-36.json), [boundary-repeat-01--filter-across-56](../evidence/2026-09-15/cases/boundary-repeat-01--filter-across-56.json), [boundary-repeat-01--filter-across-60](../evidence/2026-09-15/cases/boundary-repeat-01--filter-across-60.json).

<a id="h28"></a>
### H28 — Historical state at system-operation boundaries

**Disposition:** Reproduced historical-state discrepancy; cause unresolved

**Observed:** All clients import the same fork-chain head and boundary headers. At block 55, before the first Cancun system update at 56, Erigon already exposes timestamp 560 and its beacon root in EIP-4788 storage; the other clients return zero. A trace_call querying timestamp 560 also succeeds in Erigon at 55 and reverts elsewhere. At 56 all return the root. Both storage and call observations repeated in a separate run.

**Recommendation:** Historical state at block N should include that block's changes, including system operations, but none from N+1. Replay should start from the appropriate parent state and apply each system transition once.

**Why:** A future system write must not appear in an earlier block's state. This is an execution-context issue, not a cosmetic trace encoding choice.

**Next:** Minimize the historical-state boundary discrepancy and investigate Erigon history indexing separately from the Parity schema.

**Reproducers:** [fork-followup-01--system-beacon-55-560](../evidence/2026-09-15/cases/fork-followup-01--system-beacon-55-560.json), [fork-followup-01--system-beacon-56-560](../evidence/2026-09-15/cases/fork-followup-01--system-beacon-56-560.json), [fork-followup-01--system-beacon-55-8751](../evidence/2026-09-15/cases/fork-followup-01--system-beacon-55-8751.json), [fork-followup-01--beacon-call-55](../evidence/2026-09-15/cases/fork-followup-01--beacon-call-55.json), [fork-followup-01--beacon-call-56](../evidence/2026-09-15/cases/fork-followup-01--beacon-call-56.json).

## Coverage and limits

The extended semantic run contains 86 cases per build; the focused repeat has 41. A 72-block chain crosses London (36), Merge (48), Shanghai (52), Cancun (56) and Prague (60), with 62 probes plus an 18-case focused followup. All five builds passed exact head/state/transaction-root/receipt-root identity checks; the fork-boundary headers also match. Capture placeholders intentionally fail Hive assertions: those failure counts are not conformance scores. The ledger records malformed and incomplete responses separately.

A branch replacement at blocks 40–48 and restoration succeeded in Reth, Nethermind and Besu. Trace filters and receipts followed the new canonical branch and returned to their original values on restoration. Erigon rejected forkchoice after accepting the alternative payloads, including a repeat with safe/finalized markers held on the common prefix. This is an unresolved Engine/setup gate, not a proven stale-trace bug. Each reorg run captured 65 of 75 planned probe exchanges; the missing ten belong to Erigon's post-switch phases.

The separate ten-case Besu boundary repeat reproduces the initial outcomes exactly. A 41-case diagnostic Reth source-build pass pins the merged inspector fix; the source commit, dependency commit, binary hash and build options are in the ledger. It disables optional default features, including JIT, and enables jemalloc and the portable interpreter; it is not a release build.

The separate ten-case pruned-state fixture is Reth-only. Headers and receipts remain available, the latest state works, and historical trace queries explicitly fail after verified pruning. The initial retention configuration was rejected and pruned nothing; only the successful explicit cutoff run is evidence of unavailable history.

Mixed CREATE/CREATE2 execution and addresses agree. The source-only theory that Besu would label both creations CREATE2 was not reproduced by the simulation; its Parity output omitted creationMethod while its debug tracer labeled both correctly. The Besu debug prestateTracer before-Cancun deletion probe returned no complete response; the repeated Parity deletion observations are recorded separately.

Remaining work: retention fixtures for the other three clients; resolve Erigon's reorg gate; transaction-order and system-operation variations; exhaustive nested VM gas, warm-access, stipend and refund combinations; invalid EIP-7702 authorization tuples and broader fork/history ranges. These are explicit limits, not claims that the namespace is now exhaustively covered.

## Evidence and existing work

The extended passes captured 1,226 probe exchanges across nine successful or partially completed runs: 20 malformed JSON responses and one incomplete response are retained explicitly. The two reorg attempts each lack ten post-switch Erigon exchanges. Failed setup attempts are excluded from this exchange count.

Every local case capsule contains its exact request and captured replies; the ledger records versions, chain identity and capture hashes. Original capture files are preserved. Public request examples target generated chains, not mainnet, and require the associated genesis and block data. Runnable inputs, client image digests and raw Hive logs are retained for contribution. The extended run's requests use only public test keys and were never broadcast.

- [revm-inspectors #504](https://github.com/paradigmxyz/revm-inspectors/pull/504): merged September 14; binary adoption must be verified separately.
- [Reth #27213](https://github.com/paradigmxyz/reth/pull/27213): open at the earlier September 15 check; concerns block-replay bytecode population.
- [Besu #11286](https://github.com/besu-eth/besu/pull/11286): open at the earlier September 15 check; existing MCOPY work remains separate from other trace defects.
- [Pinned Hive revision](https://github.com/ethereum/hive/tree/43ea47bef5761351e3da7b726050ea80ab362c52): basis for the generated-chain fixtures.

These findings are discussion material. No specification PR is opened by this update.
