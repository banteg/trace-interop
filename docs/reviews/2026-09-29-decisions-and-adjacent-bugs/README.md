# Decision review and adjacent client bugs — 2026-09-29

The 33 recommendations are mostly coherent. I would correct H15's gas-default rule and reconsider
H26's prohibition on accurate deleted-slot entries under the grandfathering policy. H06 and H13
also depart from Parity, but they are explicit compatibility choices rather than nonsensical rules.
Four additional client findings are below: Reth can raise an omitted-gas call above its RPC cap;
Nethermind and Besu reduce signed gas; Besu replaces the signature before validating it; and Besu
can turn an invalid type-4 transaction into type 2.

This is a review. No recommendation, specification, assertion, client source or generated report
was changed. The new requests are review artifacts, not registered corpus cases.

## Evidence and scope

Reviewed the current [ledger](../../../decisions/ledger.json), [pinned OpenRPC
schema](../../../spec/trace-openrpc.json), [current captures](../../../reports.lock.json), the
[adopted source review](../../source-review/README.md), the [September 26 decision
review](../2026-09-26-divergent-decisions/README.md), and the existing
[fix inventory](../../../decisions/fixes.json). The starting harness commit is `ad67ebfc`.
Historical findings were checked against the current wording before treating them as outstanding.

Client source was read at the development revisions in the current capture. Local checkouts do
not all contain these revisions, so missing files were read from the exact public Git commit
without changing a checkout. For the four adjacent findings, affected paths were then rechecked
at today's upstream heads. This is a trace-namespace source review, not a repository-wide audit.

| Source | Captured/source pin | Additional upstream check |
| --- | --- | --- |
| Parity v2.7.2 | [55c90d40](https://github.com/openethereum/parity-ethereum/tree/55c90d4016505317034e3e98f699af07f5404b63) | Historical reference |
| Besu | [c197ac57](https://github.com/besu-eth/besu/tree/c197ac57d1c4c132f68a9e3c3e056f360b417a93) | [3cbf077c](https://github.com/besu-eth/besu/tree/3cbf077c5d71acfcdc02a1292c9bba9416b40672) |
| Erigon | [a2a19253](https://github.com/erigontech/erigon/tree/a2a192535bb96246af6d537ea846e2350e484678) | No additional new finding claimed |
| Nethermind | [287f54f0](https://github.com/NethermindEth/nethermind/tree/287f54f00b29d38935b33c7e7a3d7317d6aa884a) | [4aae97e6](https://github.com/NethermindEth/nethermind/tree/4aae97e671e54f70938f5924f2222663a766d166) |
| Reth | [60aeb532](https://github.com/paradigmxyz/reth/tree/60aeb53225c2ed80410c01bcfd922791480a31d2) | [098ca328](https://github.com/paradigmxyz/reth/tree/098ca328fee57ac866503e15a6dee332b7ef2257) |
| revm-inspectors 0.44.0 | [25203b21](https://github.com/paradigmxyz/revm-inspectors/tree/25203b21dd367ac357251f1172314371eb3d959b) | Tag resolved to commit |
| Anvil | [00989695](https://github.com/foundry-rs/foundry/tree/009896955c0e5a49fbf76a1976ce522795f41183) | No additional new finding claimed |
| Geth trace draft | [e26833e3](https://github.com/banteg/go-ethereum/tree/e26833e3322f918c365f74be6971061c41736fc5) | A draft implementation, not an independent vote |
| Execution-apis trace draft | [afcbc676](https://github.com/banteg/execution-apis/tree/afcbc676aa2d11cc5a3afcc73555b99a8f69ac33) | H33 remains a proposal outside this pin |

[sources.json](sources.json) retains source revisions and file hashes. The initial local RPC proof
comes from the archive node reporting **Reth v2.6.0, 73a3a00**. After the Fedora upgrade, the same
controls were repeated directly through SSH against **Reth v2.7.0, 3d592ec**, and still reproduced
the gas-cap bug. The implicated Reth helper is byte-identical between the captured development pin
and today's head. Besu and Nethermind findings are source-verified; their new requests have not
been executed against those clients.

## Recommendations to revisit

### D1. H15's omitted-gas rule contradicts its eth_call compatibility goal

**High confidence; change the wording/defaulting contract.** H15 says omitted gas runs at the
server's execution cap, “as eth_call does.” That is not the common eth_call contract:

- Reth first sets the RPC cap, then for a priced call with omitted gas replaces it with
  `min(sender allowance, block gas limit)`. Both trace_call and eth_call use this helper.
  [Reth call.rs L856–919](https://github.com/paradigmxyz/reth/blob/098ca328fee57ac866503e15a6dee332b7ef2257/crates/rpc/rpc-eth-api/src/helpers/call.rs#L856-L919)
- Besu uses `min(rpcGasCap, blockGasLimit)` when gas is omitted, rather than the RPC cap alone.
  [TransactionSimulator.java L522–547](https://github.com/besu-eth/besu/blob/3cbf077c5d71acfcdc02a1292c9bba9416b40672/ethereum/core/src/main/java/org/hyperledger/besu/ethereum/transaction/TransactionSimulator.java#L522-L547)

The read-only probe at mainnet block **23,000,000** gives the caller balance for exactly 100,000
gas at the supplied price. With gas omitted, both Reth methods execute with 100,000 gas and return
the same GAS word as explicit gas 100,000. Explicit gas 1,000,000 produces a different word.
The server cap is 50,000,000. Requiring that exact cap for the omitted priced call would therefore
change the execution, or turn it into a funding rejection when H15's funding rule is enforced.
The previous [simulation review](../../source-review/simulation.md)
already noted different defaults; the current recommendation still overstates their agreement.

**Suggested rule:** omitted gas follows the client's eth_call defaulting at the selected state,
subject to the server execution cap. All unsigned trace methods share that policy. Supplied gas
above the cap is reduced to the cap. Consumers needing a portable gas budget should supply gas;
even the server cap is already implementation/configuration dependent.

Keep H15's zero-fee compatibility and positive-price accounting requirements. A sender allowance
must be a further bound, never a way to raise a previously applied server cap; C1 is a separate bug.

### D2. H26 rejects coherent Parity deletion details

**High confidence on source; a compatibility recommendation, not an execution bug.** Requiring
`storage: {}` as the ordinary deletion result is reasonable. Requiring that *no* deleted slot may
be listed is stronger than needed and discards accurate historical information.

The full Parity path matters here:

1. Each callMany item clones the current dirty state before execution. Items share the state and
   there is no intervening commit.
   [client.rs L1225–1234](https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/ethcore/src/client/client.rs#L1225-L1234),
   [L1518–1538](https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/ethcore/src/client/client.rs#L1518-L1538)
2. The clone retains dirty storage changes. After deletion, to_pod_diff can still recover keys
   dirtied by an earlier item from that pre-state clone, despite the post-state account being absent.
   [state.rs L868–926](https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/ethcore/account-state/src/state.rs#L868-L926),
   [L1142–1150](https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/ethcore/account-state/src/state.rs#L1142-L1150),
   [account.rs L573–576](https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/ethcore/account-state/src/account.rs#L573-L576)
3. The deletion helper emits `-` entries for those known pre-state slots.
   [pod/account.rs L114–118](https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/ethcore/pod/src/account.rs#L114-L118)

For example, before Cancun, item 0 writes slot 0 to 42 and item 1 deletes that account. Parity's
second diff can include slot 0 as `{"-": <32-byte 42>}`. This correctly describes item 1's pre-state.
A standalone deletion normally reports `{}` because its clean pre-state clone has no dirty keys.
It would be wrong to infer from the generic helper that every standalone Parity deletion listed
storage. The ledger and earlier source review already explain this distinction; the new objection
is to forbidding the valid sequential-call exception.

**Suggested rule:** keep `{}` as the default and require consumers to treat account deletion as
wiping all storage. Permit correctly valued `-` entries for known pre-state slots; do not require
enumeration or interpret an omitted slot as surviving. Continue rejecting `*` to zero for a deleted
account, incorrect pre-values, and deletion markers for an account surviving EIP-6780.
This is a source-derived compatibility witness; no Parity RPC runtime was launched.

### Departures that should remain explicit

**H06:** an unknown trace_block returning null was coherent Parity behavior and survives in Besu;
it was not an extremely bad original decision. Requiring an error is a harmonization preference.
The current ledger correctly says this. Keep ordinary established absence separate from pruned or
inconclusive history, and do not sell the error choice as necessary to stop fabricated empty arrays.
The latter are a different problem. Unknown simulation blocks already error in Parity.

**H13:** strict execution validity is the largest departure from Parity's diagnostic raw simulation.
Rejecting rather than silently replacing nonce/balance makes an exact signed-execution contract
defensible, especially for CREATE. But permissive pre-broadcast and queued-transaction diagnostics
are legitimate workflows. The [current H13 guide](../../h13-validation.md) and ledger acknowledge
this; retain it as an explicit design/migration decision. Nethermind's relaxed nonce path is a
known open policy question, not a newly discovered incidental bug. Chain identity, lost transaction
type, and silently rewritten signed gas should be discussed separately from that nonce choice.

## Additional client findings

### C1. Reth's omitted-gas allowance can raise the RPC cap

**P2; runtime reproduced and source verified at today's head.** Reth sets call gas to the server
cap and then overwrites it for priced omitted-gas calls with `min(allowance, block gas limit)`.
The allowance helper divides available balance by gas price without applying the transaction's
existing gas limit. Consequently this step can raise, rather than lower, the cap.
The block gas-limit check is disabled in the same call path.
[Reth call.rs L856–919](https://github.com/paradigmxyz/reth/blob/098ca328fee57ac866503e15a6dee332b7ef2257/crates/rpc/rpc-eth-api/src/helpers/call.rs#L856-L919),
[alloy-evm 0.39.0 call.rs L36–57](https://github.com/alloy-rs/alloy-evm/blob/ba6f83b80aba8cf005175f4d776d8b90796c72d9/crates/evm/src/call.rs#L36-L57)

At mainnet block **26,085,139**, hash
`0x895a5a4ffcdf78157afeefe5ed6d8b4b22c30d2eeeae9b6aadd66db46895b15c`, with a
60,000,000 block gas limit, temporary state overrides install `GAS; MSTORE; RETURN` and give the
caller ample balance. No transaction is submitted and no persistent state changes.

| Omitted-gas request | eth_call budget | trace_call budget |
| --- | ---: | ---: |
| gasPrice 0 | 50,000,000 | 50,000,000 |
| gasPrice 1,000,000,000,000 wei | 60,000,000 | 60,000,000 |

The returned GAS words are 49,978,998 and 59,978,998 respectively: adding intrinsic gas 21,000
and the first GAS opcode's cost 2 gives those budgets. The trace root action.gas independently
agrees. This establishes extra executable budget without burning the whole budget in a loop.
[Requests and raw responses](local-reth-probes.json)

**Rechecked after the Fedora upgrade:** Reth **v2.7.0, 3d592ec** still reproduces it at block
**26,085,329**, hash
`0x708e1d3aa8a5805260f544c531bea83530dfbdfa69eb6c8445e62c70cdb0e00e`, whose gas limit is
59,999,886. Both methods give the zero-price omitted-gas control 50,000,000 gas and the positive-price
control 59,999,886 gas. Returned GAS words are 49,978,998 and 59,978,884; the trace roots independently
report action.gas 49,979,000 and 59,978,886. The historical low-allowance defaulting and high-s rejection
controls also retain their earlier results. [Updated requests and raw responses](updated-reth-probes.json)

**Fix direction:** take the minimum of the already normalized transaction gas limit, the caller
allowance and any intended block-limit default. Apply the correction in the shared helper so
eth_call and trace_call retain identical execution. This is distinct from the already tracked
Reth fee-charging/funding issue.

### C2. Nethermind and Besu reduce a signed raw transaction's gas limit

**P2; source verified at today's heads, runtime capture outstanding.** Nethermind decodes the raw
transaction and calls `tx.CapGasLimit(jsonRpcConfig.GasCap)`, whose implementation assigns
`min(tx.GasLimit, gasCap)`. It then traces that altered transaction.
[TraceRpcModule.cs L219–227](https://github.com/NethermindEth/nethermind/blob/4aae97e671e54f70938f5924f2222663a766d166/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L219-L227),
[TransactionExtensions.cs L76–81](https://github.com/NethermindEth/nethermind/blob/4aae97e671e54f70938f5924f2222663a766d166/src/Nethermind/Nethermind.Core/TransactionExtensions.cs#L76-L81)

Besu's raw method converts the signed transaction to call parameters. The shared simulator caps
the supplied gas and builds a replacement transaction using that capped limit.
[TraceRawTransaction.java L95–111](https://github.com/besu-eth/besu/blob/3cbf077c5d71acfcdc02a1292c9bba9416b40672/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceRawTransaction.java#L95-L111),
[TransactionSimulator.java L522–578](https://github.com/besu-eth/besu/blob/3cbf077c5d71acfcdc02a1292c9bba9416b40672/ethereum/core/src/main/java/org/hyperledger/besu/ethereum/transaction/TransactionSimulator.java#L522-L578)

A small configured cap isolates this from the selected block's consensus gas limit: use the
existing valid frozen transaction signed with gas 100,000 and configure RPC gas cap 30,000.
H13 requires a server-limit rejection. Instead these paths execute with 30,000 gas, potentially
turning a successful transaction into an EVM out-of-gas trace. The decoded signature authenticates
the original limit, not this replacement. This concrete mutation was not separately recorded in
the fix inventory, although the H13 recommendation already prohibits it.

**Fix direction:** reject raw gas above the server cap before execution; retain clamping for
unsigned calls. The [candidate requests](raw-transaction-candidates.json) specify the configuration.

### C3. Besu validates a replacement signature, losing the original high-s violation

**P2; source verified, Besu RPC capture outstanding.** Decoding a legacy transaction permits
`s < curve order`, which is necessary for historical Frontier transactions. The Homestead low-s
rule is enforced later by the transaction validator. But trace_rawTransaction calls
`CallParameter.fromTransaction`, which retains the recovered sender and drops the signature;
the simulator supplies `FAKE_SIGNATURE` to its replacement transaction. The original signature
therefore never reaches that fork validation.
[FrontierTransactionDecoder.java L76–83](https://github.com/besu-eth/besu/blob/c197ac57d1c4c132f68a9e3c3e056f360b417a93/ethereum/core/src/main/java/org/hyperledger/besu/ethereum/core/encoding/FrontierTransactionDecoder.java#L76-L83),
[SECPSignature.java L75–97](https://github.com/besu-eth/besu/blob/c197ac57d1c4c132f68a9e3c3e056f360b417a93/crypto/algorithms/src/main/java/org/hyperledger/besu/crypto/SECPSignature.java#L75-L97),
[CallParameter.java L124–145](https://github.com/besu-eth/besu/blob/3cbf077c5d71acfcdc02a1292c9bba9416b40672/ethereum/core/src/main/java/org/hyperledger/besu/ethereum/transaction/CallParameter.java#L124-L145),
[TransactionSimulator.java L398–411](https://github.com/besu-eth/besu/blob/3cbf077c5d71acfcdc02a1292c9bba9416b40672/ethereum/core/src/main/java/org/hyperledger/besu/ethereum/transaction/TransactionSimulator.java#L398-L411),
[validator L386–403](https://github.com/besu-eth/besu/blob/c197ac57d1c4c132f68a9e3c3e056f360b417a93/ethereum/core/src/main/java/org/hyperledger/besu/ethereum/mainnet/MainnetTransactionValidator.java#L386-L403)

The reproducer takes the valid frozen legacy transaction, changes `s` to `n-s`, and flips recovery
parity while preserving its chain ID. Both signatures were independently recovered to the same
sender. The high-s form is invalid after Homestead under [EIP-2](https://eips.ethereum.org/EIPS/eip-2).
The local Reth control rejects it with `-32602: invalid transaction signature`; the low-s fixture
control reaches the separate wrong-chain rejection on mainnet. This verifies the signature mutant,
not Besu's runtime response. Arbitrary malformed r/s values are still rejected by Besu's decoder;
the finding is specifically the lost fork-dependent signature check.

**Fix direction:** validate the original decoded signature under the selected fork and execute
the original transaction, with resource-limit handling kept separate. Add a low-s valid control
beside the high-s request; malformed-RLP tests cannot cover this.

### C4. Besu silently downgrades an invalid type-4 transaction

**P2; source verified at today's head, runtime capture outstanding.** Besu's type-4 decoder
preserves an explicitly present authorization list even if empty. The transaction constructor
requires the list's presence but does not reject emptiness. `CallParameter.fromTransaction` copies
each list element rather than preserving the original type or list presence. With no elements,
the simulator never sets code delegations and `guessType()` selects EIP-1559 from the fee fields.
[CodeDelegationTransactionDecoder.java L45–80](https://github.com/besu-eth/besu/blob/3cbf077c5d71acfcdc02a1292c9bba9416b40672/ethereum/core/src/main/java/org/hyperledger/besu/ethereum/core/encoding/CodeDelegationTransactionDecoder.java#L45-L80),
[Transaction.java L258–264](https://github.com/besu-eth/besu/blob/3cbf077c5d71acfcdc02a1292c9bba9416b40672/ethereum/core/src/main/java/org/hyperledger/besu/ethereum/core/Transaction.java#L258-L264),
[CallParameter.java L139–145](https://github.com/besu-eth/besu/blob/3cbf077c5d71acfcdc02a1292c9bba9416b40672/ethereum/core/src/main/java/org/hyperledger/besu/ethereum/transaction/CallParameter.java#L139-L145),
[simulator L633–652](https://github.com/besu-eth/besu/blob/3cbf077c5d71acfcdc02a1292c9bba9416b40672/ethereum/core/src/main/java/org/hyperledger/besu/ethereum/transaction/TransactionSimulator.java#L633-L652),
[type inference L1490–1500](https://github.com/besu-eth/besu/blob/3cbf077c5d71acfcdc02a1292c9bba9416b40672/ethereum/core/src/main/java/org/hyperledger/besu/ethereum/core/Transaction.java#L1490-L1500)

[EIP-7702](https://eips.ethereum.org/EIPS/eip-7702) requires a nonempty authorization list for
type 4. Revalidating the inferred type-2 replacement cannot detect that original violation.
The loss can also hide type-4 fork activation rules on a pre-Prague block. The retained candidate
is a correctly signed type-4 request using the frozen sender, nonce, recipient and fee cap, with
an empty list; its cryptographic signature was checked locally. The older source review already
identified missing raw type-4 coverage, but did not identify this downgrade mechanism.

**Fix direction:** preserve and validate the original transaction type and authorization-list
presence; do not infer a different type from a lossy unsigned-call representation.
These findings concern RPC fidelity. They do not establish acceptance of invalid transactions
in blocks or the transaction pool.

## Disposition of all 33 decisions

“Keep” means the recommendation has a coherent contract and a defensible compatibility basis;
it does not claim client convergence or exhaustive runtime coverage.

| Decision | Verdict | Reason |
| --- | --- | --- |
| H01 Method coverage | Keep | A complete portable profile is coherent; unserved methods must remain -32601. Do not confuse absence of a method with an empty answer. |
| H02 trace_get path | Keep | Parity's one path and singular result are coherent. Hex request indices versus integer output indices are an inherited wart worth keeping. |
| H03 Filter composition/mode | Keep | OR within lists and AND between lists preserve Parity; explicit union is an additive compatibility option. |
| H04 Empty address lists | Keep | Empty/null/omitted means unrestricted, consistent with the inherited matcher and optional-field convention. |
| H05 Rewards/system operations | Keep | PoS/genesis must not invent PoW rewards; transaction traces do not include block-level operations. Replay still applies their state effects. |
| H06 Missing lookups/history | Explicit choice | Null for established missing transactions/paths and errors for unavailable history are sound. Unknown-block null-to-error is a harmonization departure, not proof of bad Parity semantics. |
| H07 Replay hashes | Keep | Hashes identify replay envelopes and are an additive field; the draft fork is not independent evidence of consensus. |
| H08 Envelope/output | Keep | Stable unrequested components and selection-independent output preserve useful behavior. |
| H09 Failure results/labels | Keep | REVERT bytes add diagnostics without changing error-defined failure. Old labels, including code-deposit Out of gas, are deliberately grandfathered. |
| H10 Creation fields/addresses | Keep | Runtime code and per-frame creationMethod avoid conflating initcode, deployed code and CREATE2; caller/code-address roles are correct. |
| H11 Empty selection | Keep | Execution with no selected tracer is useful; a collection-reduction crash is incidental. |
| H12 Raw third argument | Keep | Two-argument latest baseline plus an observed selector extension avoids pretending the clients agree on the extension. Parity had the extension. |
| H13 Signed validation | Explicit choice | Exact signed execution justifies strictness, but this changes Parity's diagnostic contract. Keep the legitimate relaxed-workflow and migration question explicit. |
| H14 Parameters/errors | Keep | Null-as-omission, honor-or-reject defined fields, and reason-correct errors have a coherent shared basis. Recommended codes avoid unnecessary compatibility changes. |
| H15 Unsigned simulation | Revise gas defaults | Fee/default/environment rules are coherent. The exact omitted-gas-cap claim conflicts with eth_call and should be bounded client defaulting, D1. |
| H16 Accounting/callMany | Keep | Each item is a transaction with its own lifecycle and state delta. Whole-request admission failure follows Parity; error.data.index is an explicitly new diagnostic. |
| H17 Account/storage markers | Keep | Endpoint trie existence, net changes and surviving-slot from/to words preserve the meaningful Parity model. Omitting net-zero born-slot noise is sensible. |
| H18 EIP-7702 stateDiff | Keep | Durable authorization effects and net delegation-code changes are protocol requirements, including on later revert. |
| H19 Executing vmTrace code | Keep | Actual executed code is the only reliable answer for initcode, delegatecall and delegation. |
| H20 VM step effects | Keep | Operand-designated memory, Parity gas timing and empty child subtraces are coherent. Permitting both full CALL windows and exact copied bytes avoids gratuitous breakage. |
| H21 VM encoding/metadata | Keep | Quantities versus byte strings remain distinct; optional annotations should not determine execution semantics. |
| H22 Precompile output | Keep | Real successful return bytes are required; empty bytecode does not imply empty output. |
| H23 Special-action filtering | Keep | Match only reported addresses, with H03 composition. Failed CREATE has no recipient; rewards have no sender. |
| H24 Failure isolation | Keep | Local child outcome and committed state are different facts; ancestor rollback must not relabel successful siblings/children. |
| H25 Complete errors | Keep | A replaceable complete error before output commitment and transport abort after commitment prevent false success. |
| H26 Deletion | Reconsider storage ban | Account markers and EIP-6780 rules are sound. Allow accurate known-slot deletion details rather than declaring the valid Parity exception wrong, D2. |
| H27 Fork-boundary filtering | Keep | Each block uses its own rules and parent state; pagination must preserve per-block trace order. |
| H28 Historical/system state | Keep | Post-state at N, pre-block operations for replay and no N+1 leakage follow block execution order. |
| H29 Precompile/precheck frames | Keep | Keep Parity's odd zero-value nested-precompile omission. The deliberate attempted-action extension supplies useful precheck failures; numbering is over emitted records. |
| H30 Filter defaults | Keep | Latest/latest preserves Parity. Changing Erigon's historical lower-bound default still needs migration notice; no silent truncation is permitted. |
| H31 callMany default block | Keep | Optional latest preserves Parity and aligns the simulation methods. |
| H32 Tags/pending | Keep | Actual pending execution or rejection is honest. Removing hash range bounds is justified because the old number resolution did not pin identity. Earliest follows the shared range type. |
| H33 Filter blockHash | Keep as proposal | Identity-preserving selection solves the empty-result/reorg ambiguity. Canonical-only is an explicit narrowing of EIP-234, not its full orphan contract. |

## Remaining proof gaps and follow-ups

1. Capture C2–C4 on the frozen raw-validation chain, with valid controls and the small cap
   configuration for C2. [raw-transaction-candidates.json](raw-transaction-candidates.json) contains
   the exact requests. Source predictions must not be counted as observed RPC results.
2. Add an omitted-gas priced probe with a funded allowance below the cap, and one with a block
   limit above the cap. Current GAS-field coverage is unpriced and cannot expose C1 or D1.
3. A pre-Cancun deletion with nonzero storage and a write-then-delete bundle would discriminate
   D2. The existing deletion probe is not proof that all deleted-slot encodings have been exercised.
4. Previously recognized gaps remain: unprotected legacy signed transactions, raw blob encodings,
   Osaka signed gas validity, pending blocks with transactions, and earliest on genuinely pruned
   history. Their presence is not a newly established client bug. Nethermind's shared raw/unsigned
   path also warrants a signed zero-fee control distinct from its existing positive-below-base probe.

I would address C1 and correct D1 first. C2–C4 should get focused native captures before upstream
patches. D2 needs a policy decision before changing a serializer or reversing the already tracked
deleted-storage recommendation.
