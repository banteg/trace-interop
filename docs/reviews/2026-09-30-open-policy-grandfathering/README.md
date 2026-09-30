# Remaining trace policy decisions and existing client behavior

The strongest changes are to make H16's structured batch index optional, separate H15's blob simulation policy from ordinary execution fees, and preserve correct existing selector and override extensions. H14, H16's execution contract, and H33's optional exact-block contract are close to a defensible recommendation. This is a review of H14, H15, H16, H32 and H33, using grandfathering and consistency with sibling methods as the decision criteria. The research snapshot did not change the ledger, pinned specification, assertions, or recorded client positions; subsequent approved uptake is recorded below.

## Recommendation uptake

On September 30 the user approved applying the proposed softenings: H16's index is recommended, H15's ordinary fees follow eth_call with zero/default blob normalization separately unresolved, override forms are optional extensions, and H32 permits correct canonical hash range endpoints. The ledger, draft and assessment rules were aligned. The H32 hash-endpoint grandfathering and H33's optional, orphan-permitting contract were [reversed later that day](../../../reports/decisions/H33.md#client-positions-and-reversal-2026-09-30) on Nethermind's and Erigon's stated positions, which ask for rejected hash bounds and a required, canonical-only `blockHash` member; the other uptake stands. Retained captures were not rewritten, and client policy review remains open; earlier Erigon agreement is labelled as concerning the previous proposal. The evidence and disposition below preserve the research snapshot and its remaining proof gaps.

## Evidence and decision criteria

Current public source heads were resolved on September 30, 2026. The [source manifest](sources.json) records 64 retrieved source files, their immutable URLs and checksums; the load-bearing passages are preserved in [source excerpts](source-excerpts.json). Existing RPC evidence comes from the September 30 refresh selected by reports.lock.json; [selected observations](selected-observations.json) retain the exact responses for 16 relevant cases. Source at a newer head is not a newly executed build. The fresh runtime work here is limited to the user's Reth archive node: [requests and responses](reth-probes.json), [reproduction script](reth-probe.py).

| Implementation | Current source inspected | Role |
| --- | --- | --- |
| Besu | `045e0079` | Native trace implementation and eth_call comparison |
| Erigon | `85e1ca92` | Native trace implementation and eth_call comparison |
| Nethermind | `83fae5b6` | Native trace implementation and eth_call comparison; newer than the selected preview capture |
| Reth | `43a93dbc` | Native trace implementation; live node is released 2.7.0, `3d592ec` |
| Geth | `5dcdd051` | Native eth_call, eth_getLogs and eth_simulateV1 comparison; no native Parity namespace |
| Anvil | `ccc793cc` | Tooling compatibility; separate from the four-client harmonization count |
| Geth trace draft | `e26833e3` | Experimental implementation, not an independent policy vote |
| Specification draft | `b9febf5e` | Proposed contract at source inspection |

These revisions identify the sources inspected for this review. Before publication, repository commit `b7ce46a1` synced the subsequent specification draft `6a9a69b3` and recorded Geth fork follow-up `ec1cec0be8`. That follow-up implements canonical, executed hash selection; neither it nor the newer specification is part of the retained source manifest or selected client captures. The H33 specification-alignment step is therefore complete, while explicit client review remains outstanding.

Historical Parity/OpenEthereum behavior is taken from the previously pinned source studies and the separately preserved OpenEthereum runtime witness, not a new Parity execution here.

Grandfather a coherent behavior or a useful optional extension, rather than forcing every client to add or remove it. Where trace methods disagree, prefer their shared behavior and then the corresponding eth_* contract. An ignored selector, fabricated success, internal failure, malformed completed response or silently truncated answer is not a useful behavior to grandfather. Count independent native implementations separately from stable/development channels, Anvil and our Geth fork. Maintainer willingness to adopt a behavior is also separate from implementation evidence.

## H14 parameters and error responses

**Keep the substance and seek a policy conclusion soon.** The September 29 relaxation already removed the largest unnecessary compatibility cost: most exact codes are recommended, while the required rejection and its reason remain observable.

| Rule | Existing behavior and sibling precedent | Recommendation |
| --- | --- | --- |
| Optional null means omission | The retained cross-client eth_call, eth_estimateGas, eth_getLogs and eth_simulateV1 controls support this convention. Trace enum decoders and some list decoders still differ. | Keep. Preserve null's explicit schema meaning, such as contract creation through `to`. |
| Defined fields take effect or cause rejection | Current Erigon converts its trace call object through its eth_call arguments. Nethermind now validates chain identity and uses the shared transaction conversion. Besu and Reth apply modern call fields, with specific remaining discrepancies. | Keep the requirement; do not infer support from successful decoding. H15's explicitly ignored nonce remains its documented exception. |
| Conflicting data and input are rejected | Besu, Erigon and Reth reject the disagreement in their trace paths. Nethermind's current shared alias still lets the last non-null member win. Native Geth's eth_call prefers input, although its transaction defaulting path rejects a mismatch. | Keep the native trace majority. The eth_* analogy does not justify weakening an already useful trace contract. |
| Closed filter objects | Current Nethermind has merged the Disallow annotation and unsigned after/count types. Besu and Reth already reject ordinary unknown filter fields; Erigon's Go struct still ignores them. Besu's declared but unused blockHash is a separate H33 hazard. | Keep. Retest Nethermind instead of carrying its old captured unknown-field behavior forward as current source behavior. |
| Reason-correct errors, flexible codes | Trace methods currently use several -32000/-32003/-32602 mappings. The borrowed eth_simulateV1 mappings exist but are not uniformly used by trace paths. | Keep recommended codes. A server failure is not evidence that a required validation rejection occurred. |

Sources: [Erigon call conversion][E-call], [Nethermind call validation][N-trace], [Nethermind filter type][N-filter], [Nethermind calldata alias][N-legacy], [Geth call defaults][G-args]. [Erigon's stated H14 agreement](https://github.com/ethereum/execution-apis/issues/890#issuecomment-5857403064) supports the direction, but does not establish unanimous approval of every later amendment.

There is no need to reopen H14 around one universal numeric code table. Remaining decoder and serialization fixes can proceed independently of a policy conclusion.

## H15 ordinary fees and blob simulation

**Keep ordinary execution fees. Revise the claim of universal alignment with eth_simulateV1, and separate the blob rule before settling the whole decision.**

| Implementation | Ordinary execution fees | Blob simulation |
| --- | --- | --- |
| Besu | eth_call uses relaxed zero-fee handling; its trace path still uses stricter simulator parameters. Retained trace captures reprice omitted fees and turn zero-fee rejection into an internal error. Positive-priced calls are charged. | Current eth_call's relaxed simulator uses MIN_BLOB_GASPRICE, 1, and normalizes the transaction's blob cap to match. Retained trace captures reject explicit zero with an internal error and preserve the real blob price when the cap is omitted. |
| Erigon | Current trace_call and callMany use eth_call fee conversion, zero the unpriced BASEFEE, preserve GASLIMIT and charge priced calls. | Both call and trace paths explicitly zero the blob base fee for named blob fields with omitted or zero blob pricing. |
| Nethermind | Current main adds UnpricedCallTraceAdapter: all-zero execution caps clear the header base fee for each transaction and restore it afterwards. This is newer than the selected preview's H15 capture. Priced calls retain normal accounting. | The inspected eth/trace paths have no equivalent zero-blob adapter. Retained trace captures reject explicit zero and fail the omitted-cap request. The nullable cap flows into transaction processing; this is not evidence of a successful omitted-cap contract. |
| Reth | Both methods zero BASEFEE at zero effective gas price, but prepare_call_env still disables fee charging for priced calls. | Fresh live comparisons show both methods preserve the selected BLOBBASEFEE with an omitted cap, reject an explicit zero cap, and accept a covering positive cap. |
| Native Geth | eth_call zeros BASEFEE at zero price and retains priced gas accounting. | CallDefaults supplies a zero cap when blob hashes are present and applyMessage zeros BlobBaseFee for a zero cap. |
| Anvil | Retained captures keep the selected BASEFEE even for free calls; priced accounting is applied. | Retained trace captures preserve BLOBBASEFEE for omitted pricing and reject explicit zero. Current code passes blob pricing into its shared backend. |

Sources: [Besu eth_call predicate][B-call-params], [Besu simulator][B-simulator], [Besu trace validation][B-trace], [Erigon blob normalization][E-args], [Nethermind fee adapter][N-free], [Nethermind factory][N-factory], [Nethermind blob conversion][N-blob], [Reth call environment][R-call], [Geth call execution][G-call], [Anvil call dispatch][A-api]. Blob trace responses are retained in selected-observations.json.

The fresh Reth block is 26,086,872, hash `0x44a144fc4c697c78064d5b0983f7c9bf3698b51e9a0062a6ace9cd2a17cfa790`. Its BLOBBASEFEE is 6,736,426 wei. Identical eth_call and trace_call inputs return that value for an omitted blob cap under both free and priced execution fees. Both reject an explicit zero blob cap with -32003. A covering positive cap succeeds and preserves the same value. Temporary overrides supply a small opcode observer and sender funding; nothing is submitted or persisted.

The older review's inference that Besu's balance-relaxation predicate establishes BLOBBASEFEE 0 was too strong. The actual current simulator supplies 1. The predicate only selects a relaxed validation/pricing path. This review corrects that evidence claim.

Ordinary fees have a strong cross-method basis: free calls use zero execution price and BASEFEE; priced calls enforce funding and apply upfront debit, refund, burn and tip settlement. Reth's no-charge setting is the remaining deliberate implementation question. Its maintainer [suggested disabling fee charge only at price zero](https://github.com/paradigmxyz/reth/issues/27476#issuecomment-5853260678), which supports the proposed direction but is not a merged correction. Besu still needs trace/eth alignment. Nethermind's new source needs a capture before it can change report verdicts.

Blob normalization has no comparable common contract. A universal zero rule would change behavior that currently agrees with the same client's eth_call. I recommend moving zero/default blob pricing into a separately unresolved clause and grandfathering the documented existing normalization policies while that clause is reviewed. The provisional assessment should record those policies and check same-client trace/eth consistency, without treating one universal zero policy as already agreed. Explicit positive blob pricing, actual blob hashes and fee effects must remain observable; malformed/internal errors or ignored fields are not acceptable alternatives. This is not a claim that preserving the real blob price is an agreed universal replacement for zero.

Suggested core wording:

> Ordinary execution-fee defaults and pricing follow eth_call. Omitted execution fees default to zero; a zero effective execution price exposes GASPRICE and BASEFEE zero and has no execution-gas fee effects. Priced calls enforce funding and apply gas payment and settlement. Blob simulation defaults, fee-cap validation and opcode-visible BLOBBASEFEE are specified separately. Existing documented blob normalization policies remain distinguishable during that review.

Also replace the blanket statement that fees follow eth_call and eth_simulateV1. [Geth's simulator][G-sim] builds simulated next blocks, and with validation disabled it sets an unoverridden base fee to zero at block construction. That is not eth_call's per-call zero-price rule. Borrow its field schemas and recommended errors where appropriate, without implying identical execution environments.

## H15 override extensions

**Soften the unconditional positional reservation.** Reth accepts state overrides fourth and block overrides fifth in trace_call. Nethermind accepts state overrides fourth. Erigon accepts a configuration wrapper fourth in trace_call and third in callMany; its configuration carries override members. Besu's trace baseline has no override support. The two positional state-map implementations are useful precedent, but not a universal existing contract, and callMany has an existing wrapper collision in the newly reserved third position.

Sources: [Reth trace signatures][R-signatures], [Nethermind trace signatures][N-signatures], [Erigon trace methods][E-call], [Erigon configuration][E-config].

Keep the baseline call arity portable and mark the positional state/block forms as preferred optional extensions. Grandfather existing recognized configuration wrappers where they actually apply their contents. A client must reject an unsupported override shape rather than accept it as a configuration with every field ignored. In particular, an address-keyed state map must not silently become an empty Erigon configuration. Conversely, a valid existing Erigon wrapper should not become nonconformant merely because it is not the preferred map. The override's actual state/environment effects need discriminating probes before adoption.

## H16 transaction boundaries and accounting

**The core can be settled soon. Make error.data.index recommended rather than mandatory.**

Replay fee accounting is already shared in the retained cases: signed/mined execution includes sender gas and blob payments, beneficiary tips and burns, while transaction diffs exclude block-level system operations, withdrawals and rewards. Each callMany item has a fresh transaction lifecycle, carries the preceding state forward and uses one shared block environment. The retained original-storage discriminator identifies Besu as the exception; its current callMany still commits nested updaters without an explicit transaction boundary. Reth constructs a fresh execution for each item, Erigon finalizes each item, and Nethermind processes them as separate transactions.

Sources: [retained H16 accounting review](../2026-09-26-divergent-decisions/H14-H15-H16.md#h16-which-fee-payments-a-transactions-statediff-reports), [Besu callMany][B-many], [Reth callMany][R-trace], [Erigon callMany][E-call], [Nethermind callMany][N-trace].

Keep one error and no successful partial result when a decoded item fails validation. Erigon and Reth implement that behavior, and it preserves Parity. Besu's nested error envelope and the older Nethermind streamed truncation are protocol defects, not competing useful batch contracts. The existing H25 distinction still applies after output commitment: a server may have to abort transport instead of fabricating a completed success or pretending it can replace already-written output.

No native client returns the proposed structured index. Erigon identifies the item in message text; the other implementations do not supply error.data.index. Making that field mandatory adds a new wire requirement to every implementation for diagnostics, not execution portability.

Suggested replacement:

> If a decoded item fails validation, return one error and no successful partial results. A client SHOULD include the failing item's zero-based index in error.data.index. If present, the index MUST identify the failing item. Malformed parameters need not include an item index.

Retain exact refund and original-storage proof work. The [partial assessment review](../2026-09-30-partial-assessment/README.md) identifies independent priced-accounting gaps; a client's own stateDiff cannot be the expected refund oracle. Those gaps block complete verification, not the choice of transaction semantics.

## H32 pending tags and range selectors

**Keep pending execution or rejection, but reconsider the mandatory removal of existing canonical hash range bounds.**

| Implementation | Pending simulation | Hash range bounds |
| --- | --- | --- |
| Besu | Current common block dispatcher substitutes latest; retained trace calls execute at the head. Its eth_call dispatcher follows the same fallback. | Numeric/tag parameters; no hash bounds. |
| Erigon | Current trace methods and eth_call reject pending. | Existing hash strings/objects resolve through a canonical resolver inside the read transaction. |
| Nethermind | Current trace methods explicitly reject pending because it has no pending block for RPC. Its older eth_call/header path resolves pending to the head. | Existing block selectors are accepted; SearchForBlocksOnMainChain rejects noncanonical endpoints. |
| Reth | Fresh eth_call and trace_call comparisons use NUMBER head+1. The trace block path can use its pending block. | The quantity-based filter type rejects hashes and also misses useful explicit tag support. |
| Native Geth | eth_call uses the backend's pending environment when available. | eth_getLogs range bounds use numbers/tags, with a separate exact blockHash selector. |
| Anvil | Retained simulation cases and current dispatch use a pending request; block tracing can still resolve pending through the generic number conversion to the head. | Hash bounds are rejected by the shared filter type. |

Sources: [Besu block dispatcher][B-block-param], [Erigon pending rejection][E-pending], [Erigon eth_call][E-eth-call], [Erigon range resolver][E-filter], [Nethermind trace rejection][N-trace], [Nethermind canonical endpoint check][N-range], [Reth trace execution][R-trace], [Anvil dispatch][A-api], [Anvil number conversion][A-mem].

A silent pending-to-latest substitution is not the current native trace majority: Erigon and Nethermind reject, while Reth supplies next-block semantics. Keep the requirement that accepted pending requests use an actual pending environment, otherwise reject. Do not claim mempool inclusion or complete pending block localization from an empty frozen-chain result. A pending block with transactions remains useful coverage.

For bounds, portable numbers/tags remain the right baseline and match eth_getLogs. But Erigon and Nethermind already offer a meaningful canonical hash-to-height extension. It does not solve H33's exact identity problem, and should not be advertised as doing so. Its existence also does not require every client to implement it.

I would grandfather that extension: a client may accept a documented canonical hash range endpoint, resolving it within a coherent canonical view, or reject the unsupported selector. Noncanonical/unknown/unexecuted endpoints must not be silently replaced. Reorg consistency needs a discriminating runtime probe; the source inspection is not proof of every concurrent-reorg path. This softening preserves the common baseline while avoiding an unnecessary removal. Erigon has [explicitly agreed to the stricter no-hash baseline](https://github.com/ethereum/execution-apis/issues/890#issuecomment-5889999591), so retaining the extension is a proposal for review, not an assertion that Erigon objects to removal. Nethermind's position is not recorded. The cited numeric-versus-hash error-code difference alone is a weaker removal argument now that exact codes are recommendations.

Clarify unavailable safe/finalized bounds now: return an error if the tag cannot be resolved, never an internal failure, head substitution or successful empty collection. Exact codes remain recommendations. Native Geth's eth_getLogs errors on an unavailable safe/finalized header, and Nethermind's range search also propagates the lookup failure.

Keep the shared earliest definition, but retain the pruning proof gap. Geth's eth_getLogs resolves earliest using its history-pruning cutoff; Erigon's generic earliest quantity is zero and Anvil uses its configured genesis. Header retention, receipt retention and executable state retention are different. Do not claim every client's trace earliest is already verified to select a successfully traceable retention boundary.

## H33 optional exact block selection

**Keep the September 30 softened recommendation and seek agreement soon.** The mandatory-implementation and canonical-only requirements were already removed. That makes this a precise optional capability, not a request for every client to retain and trace orphan state.

No build in the selected capture implements the member. Besu, Erigon and the captured Nethermind preview silently ignored it; Reth, Anvil and the Geth draft rejected it. Current Nethermind's closed filter type now rejects it as well, although that newer source still needs a capture. Ignoring a hash and returning another block's records, including an empty collection, cannot be grandfathered as hash-selection support.

Keep optional exact selection or explicit rejection; keep unknown/unexecuted/unavailable selection as an error; keep accurate retained-orphan answers permitted without a retention requirement. EIP-234 supplies the selector shape and the exact-block motivation, while EIP-1898 only names six eth state methods and does not automatically impose one syntax on trace methods. Existing correct optional hash-string/object selectors on other trace methods should survive. Accepting requireCanonical true must enforce it or reject the request; syntactic acceptance on canonical blocks does not establish that property on an orphan.

Sources: [EIP-234](https://eips.ethereum.org/EIPS/eip-234), [EIP-1898](https://eips.ethereum.org/EIPS/eip-1898), [all-method hash review](../2026-09-30-hash-selectors-all-methods.md), [current H33 recommendation](../../../reports/decisions/H33.md), [Nethermind closed filter][N-filter].

One follow-up remains before claiming client agreement: the public thread still describes the earlier mandatory, canonical-only proposal. The softened recommendation should be explicitly reviewed in that thread. Erigon's statement that either answer works is not approval of the newer optional-orphan wording. No message or comment was sent as part of this review.

## Proposed disposition and remaining validation

| Decision | Proposed disposition | What prevents claiming complete settlement |
| --- | --- | --- |
| H14 | Keep; ready for a policy conclusion on substance. | Record client review of the relaxed code policy; remaining defined-field/decoder behavior still needs fixes and captures. |
| H15 ordinary execution fees | Keep; close to a policy conclusion. | Reth fee-charging change, Besu trace/eth alignment, recapture Nethermind's new adapter. |
| H15 blobs and overrides | Revise or split into separate optional-extension clauses. | Paired blob/override probes across all native clients, explicit agreement on any portable normalization rule. |
| H16 | Keep execution semantics; recommend the structured index. | Client review of softened diagnostics; independent priced refunds and Besu transaction-boundary verification. |
| H32 | Keep pending/tag behavior; grandfather correct canonical hash endpoints as an optional extension. | Nethermind response on bounds, unavailable-finality and pruning cases, concurrent-reorg endpoint validation. |
| H33 | Keep optional exact-block-or-error and optional orphan serving. | Explicit review of the softened proposal; the pinned specification was subsequently aligned in `b7ce46a1`. |

This order avoids holding established transaction semantics behind new diagnostics or extension uniformity. It also avoids counting source uptake, a proposed relaxation or an unmeasured response as harmonization. The research snapshot changed no policy status or conformance total. Subsequent approved uptake regenerates assessments against the relaxed recommendation without treating unresolved blob normalization as agreement.

[E-call]: https://github.com/erigontech/erigon/blob/85e1ca92dd1bd471d748f13878d22e4ed18863f0/rpc/jsonrpc/trace_adhoc.go#L186
[E-args]: https://github.com/erigontech/erigon/blob/85e1ca92dd1bd471d748f13878d22e4ed18863f0/rpc/ethapi/api.go#L201
[E-config]: https://github.com/erigontech/erigon/blob/85e1ca92dd1bd471d748f13878d22e4ed18863f0/execution/tracing/tracers/config/api.go#L32
[E-filter]: https://github.com/erigontech/erigon/blob/85e1ca92dd1bd471d748f13878d22e4ed18863f0/rpc/jsonrpc/trace_filtering.go#L307
[E-pending]: https://github.com/erigontech/erigon/blob/85e1ca92dd1bd471d748f13878d22e4ed18863f0/rpc/jsonrpc/tracing.go#L44
[E-eth-call]: https://github.com/erigontech/erigon/blob/85e1ca92dd1bd471d748f13878d22e4ed18863f0/rpc/jsonrpc/eth_call.go#L63
[N-trace]: https://github.com/NethermindEth/nethermind/blob/83fae5b6a3cf482692e4a5a086bec0e90edb66c7/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L89
[N-filter]: https://github.com/NethermindEth/nethermind/blob/83fae5b6a3cf482692e4a5a086bec0e90edb66c7/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceFilterForRpc.cs#L11
[N-legacy]: https://github.com/NethermindEth/nethermind/blob/83fae5b6a3cf482692e4a5a086bec0e90edb66c7/src/Nethermind/Nethermind.Facade/Eth/RpcTransaction/LegacyTransactionForRpc.cs#L39
[N-free]: https://github.com/NethermindEth/nethermind/blob/83fae5b6a3cf482692e4a5a086bec0e90edb66c7/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/UnpricedCallTraceAdapter.cs#L20
[N-factory]: https://github.com/NethermindEth/nethermind/blob/83fae5b6a3cf482692e4a5a086bec0e90edb66c7/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceModuleFactory.cs#L45
[N-blob]: https://github.com/NethermindEth/nethermind/blob/83fae5b6a3cf482692e4a5a086bec0e90edb66c7/src/Nethermind/Nethermind.Facade/Eth/RpcTransaction/BlobTransactionForRpc.cs#L58
[N-signatures]: https://github.com/NethermindEth/nethermind/blob/83fae5b6a3cf482692e4a5a086bec0e90edb66c7/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/ITraceRpcModule.cs#L20
[N-range]: https://github.com/NethermindEth/nethermind/blob/83fae5b6a3cf482692e4a5a086bec0e90edb66c7/src/Nethermind/Nethermind.JsonRpc/Modules/BlockFinderExtensions.cs#L106
[B-call-params]: https://github.com/besu-eth/besu/blob/045e00792b89f1ed97f212cbfb300f4c0979cb17/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/CallParameterUtil.java#L60
[B-simulator]: https://github.com/besu-eth/besu/blob/045e00792b89f1ed97f212cbfb300f4c0979cb17/ethereum/core/src/main/java/org/hyperledger/besu/ethereum/transaction/TransactionSimulator.java#L377
[B-trace]: https://github.com/besu-eth/besu/blob/045e00792b89f1ed97f212cbfb300f4c0979cb17/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/AbstractTraceByBlock.java#L120
[B-many]: https://github.com/besu-eth/besu/blob/045e00792b89f1ed97f212cbfb300f4c0979cb17/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceCallMany.java#L120
[B-block-param]: https://github.com/besu-eth/besu/blob/045e00792b89f1ed97f212cbfb300f4c0979cb17/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/AbstractBlockParameterMethod.java#L52
[R-call]: https://github.com/paradigmxyz/reth/blob/43a93dbcffd5d5cd41664ad6d29fc58291a22c13/crates/rpc/rpc-eth-api/src/helpers/call.rs#L873
[R-trace]: https://github.com/paradigmxyz/reth/blob/43a93dbcffd5d5cd41664ad6d29fc58291a22c13/crates/rpc/rpc/src/trace.rs#L152
[R-signatures]: https://github.com/paradigmxyz/reth/blob/43a93dbcffd5d5cd41664ad6d29fc58291a22c13/crates/rpc/rpc-api/src/trace.rs#L16
[G-args]: https://github.com/ethereum/go-ethereum/blob/5dcdd05159ac162239e6c4ba2e7de03fc40b6581/internal/ethapi/transaction_args.go#L84
[G-call]: https://github.com/ethereum/go-ethereum/blob/5dcdd05159ac162239e6c4ba2e7de03fc40b6581/internal/ethapi/api.go#L793
[G-sim]: https://github.com/ethereum/go-ethereum/blob/5dcdd05159ac162239e6c4ba2e7de03fc40b6581/internal/ethapi/simulate.go#L258
[A-api]: https://github.com/foundry-rs/foundry/blob/ccc793cc1f66aa7d7f71f6cd7af6fbc7d21a2054/crates/anvil/src/eth/api.rs#L1515
[A-mem]: https://github.com/foundry-rs/foundry/blob/ccc793cc1f66aa7d7f71f6cd7af6fbc7d21a2054/crates/anvil/src/eth/backend/mem/mod.rs#L2110
