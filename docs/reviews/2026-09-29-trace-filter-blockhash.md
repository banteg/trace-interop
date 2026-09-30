# A single blockHash selector for trace_filter

Study, 2026-09-29. **Recommendation, not an adopted decision.** No specification, ledger,
client implementation or conformance verdict is changed by this note.

H33's [September 30 softening](../../reports/decisions/H33.md#softened-recommendation-2026-09-30)
made support optional and allowed accurate orphan replies. It was
[reversed the same day](../../reports/decisions/H33.md#client-positions-and-reversal-2026-09-30) on Nethermind's and Erigon's stated positions: the mandatory,
canonical-only recommendation below is the converged decision, and serving side-chain blocks is
left to a possible later extension.

Add a separate `blockHash` selector and continue rejecting hashes in `fromBlock`/`toBlock`.
Require support in the eventual trace profile, while making use of the field optional for callers.
The useful contract is **exact requested block or error**, including for empty results and pages.
For an initial canonical-only profile, explicitly reject noncanonical hashes. Serving retained
orphan blocks should be a separately agreed expansion, not an accidental consequence of reusing
a generic selector type. This is alignment with the log-filter interface and its identity guarantee,
not full adoption of EIP-234's noncanonical-block semantics.

## What the concern gets right

Suppose an indexer observes block A at height N, then requests traces at N filtered to address X.
Between the calls, B replaces A. If B has no matching traces, the response is `[]`, with no
`blockHash` to inspect. The indexer cannot conclude that A had no matches. Nonempty results carry
localization, so checking their hashes can detect the mismatch; the empty result cannot.

Reading the header before and after is not a complete solution: A → B → A between those reads
can conceal the replacement. A load-balanced endpoint can also answer different requests from
different views. A JSON-RPC batch does not establish a shared chain snapshot. The existing draft's
one-snapshot-per-filter rule prevents inconsistencies *inside that request*, but does not pin it
to the block seen by an earlier request. Numeric pagination across separate calls has the same
problem even when each call is internally coherent.

[EIP-234](https://github.com/ethereum/EIPs/blob/05f291880623d064fd76abd089298b278dafe94a/EIPS/eip-234.md)
(Final) motivates a log-filter hash selector using this empty-result ambiguity: "if they get a
result set, it is for the block in question". It also intends queries of noncanonical blocks
("whether those blocks were in the current main chain or not"), makes `blockHash` mutually exclusive
with `fromBlock`/`toBlock`, and gives -32000 "Block not found." for an unknown hash. The
execution-apis conformance test `tests/eth_getLogs/filter-error-invalid-blockHash-and-range.io`
expects -32602 for a hash combined with a range; no test covers unknown or noncanonical hashes.
[EIP-1898](https://eips.ethereum.org/EIPS/eip-1898) generalizes hash selection to state methods and
separately provides `requireCanonical`. Neither EIP automatically specifies `trace_filter`.

## What clients do today

Source revisions: Geth `f8f9bc57`, Geth draft `e26833e3`, Erigon `48d3a168`, Nethermind `83c8d6ce`,
Reth `1cb086ad` (Alloy `4388f757`), Besu `d4ad1359`, Foundry `f1a18255`, Parity `55c90d40`,
execution-apis `5bcdc34a`. **Measured** cells cite the 2026-09-29 refresh
([evidence](../../evidence/2026-09-29/refresh/README.md): Anvil 1.8.3/1.8.4, Besu
26.9.0/26.9-develop, Erigon 3.7.0/3.8.0, Geth draft 1.17.7-unstable-e26833e3, Nethermind
2.0.0/2.2.0-preview, Reth 2.7.0 release and development; both builds agree in every cell) or the
Reth 2.6.0 probe below. **Source** cells come from the linked code and were not executed.

### `trace_filter` with a `blockHash` member

No client implements the member. Three silently answer for **latest** instead: exactly the
misattribution the member is meant to prevent, happening today without any reorg.

No refresh case sends a top-level `blockHash`. The measured part of the Erigon, Nethermind, Besu,
Geth draft and Anvil cells is `a/filter-unknown-field` (`{fromBlock: 0x2, toBlock: 0x2,
unknownDiagnosticFlag: true}`): Erigon and Nethermind answer it with records, every other client
rejects it with -32602.

| Client | `{blockHash: H}` | `{blockHash: H, fromBlock, toBlock}` | Basis |
| --- | --- | --- | --- |
| Nethermind | **Ignored: traces latest..latest** | Hash ignored; the range is used | Source: [`TraceFilterForRpc`](https://github.com/NethermindEth/nethermind/blob/83c8d6cec184fbe82b23b09c1c1f76da7e953a6f/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceFilterForRpc.cs#L10-L26) has no such member; null bounds default to latest ([TraceRpcModule](https://github.com/NethermindEth/nethermind/blob/83c8d6cec184fbe82b23b09c1c1f76da7e953a6f/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L376-L377)). Measured: unknown members are accepted |
| Erigon | **Ignored: traces latest..latest** | Hash ignored; the range is used | Source: [`TraceFilterRequest`](https://github.com/erigontech/erigon/blob/48d3a168fbbf3ccf28b0361a7472bca4c8d92376/rpc/jsonrpc/trace_filtering.go#L1080-L1088) has no such member; nil bounds become the latest executed block ([L330-L336](https://github.com/erigontech/erigon/blob/48d3a168fbbf3ccf28b0361a7472bca4c8d92376/rpc/jsonrpc/trace_filtering.go#L330-L336)). Measured: unknown members are accepted |
| Besu | **Parsed, then ignored: traces latest..latest** | Hash ignored; the range is used, although `isValid()` would be false | Source: [`FilterParameter`](https://github.com/besu-eth/besu/blob/d4ad1359b3c04b0f72cf216283a4c0dd1562424b/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/parameters/FilterParameter.java#L49-L76) declares it (shared with `eth_getLogs`); [`TraceFilter`](https://github.com/besu-eth/besu/blob/d4ad1359b3c04b0f72cf216283a4c0dd1562424b/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceFilter.java#L96-L109) never reads it or calls `isValid()`. Measured: a truly unknown member is rejected (-32602), so the declared member is the loophole |
| Reth | Rejected, -32602 | Rejected, -32602 | Measured on 2.6.0 (below). Source: Alloy [`TraceFilter`](https://github.com/alloy-rs/alloy/blob/4388f757c79e5f2d6f9b47498473e560d93e3956/crates/rpc-types-trace/src/filter.rs#L11-L36) is `deny_unknown_fields` |
| Anvil | Rejected, -32602 | Rejected, -32602 | Source: same Alloy type ([api.rs](https://github.com/foundry-rs/foundry/blob/f1a18255f69f6ed79bfc22e6868668a2d853e793/crates/anvil/src/eth/api.rs#L1571-L1576)). Measured: unknown members are rejected |
| Geth draft | Rejected, -32602 | Rejected, -32602 | Source: `DisallowUnknownFields` after dropping null members ([trace_types.go](https://github.com/banteg/go-ethereum/blob/e26833e3322f918c365f74be6971061c41736fc5/eth/tracers/trace_types.go#L169-L224)). Measured: unknown members are rejected |
| Parity | Rejected | Rejected | Source: `deny_unknown_fields`, no member ([trace_filter.rs](https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/rpc/src/v1/types/trace_filter.rs#L26-L43)); the OpenEthereum `main` copy is the same |

The draft's H14 rule (filters reject unknown members) already requires Nethermind and Erigon to
reject the member, and Besu to reject a member it declares, even if the draft adds nothing.

### `trace_filter` with hash range bounds

Measured in the refresh (`h30/filter-hash-bounds`, `h30/filter-hash-object-bounds`: fixture chain a,
block 2, `count: 3`; the Anvil replica substitutes its own hash). Nobody chose either behavior; each
follows how the parameter is typed. The noncanonical and unknown columns are from source.

| Client | Hash string bounds | `{blockHash}` object bounds | Noncanonical hash | Unknown hash |
| --- | --- | --- | --- | --- |
| Nethermind | Measured: accepted, 3 records from block 2 | Measured: accepted, same | Source: -32000 "block is not canonical" ([BlockFinderExtensions.cs L92-L113](https://github.com/NethermindEth/nethermind/blob/83c8d6cec184fbe82b23b09c1c1f76da7e953a6f/src/Nethermind/Nethermind.JsonRpc/Modules/BlockFinderExtensions.cs#L92-L113)) | Source: -32000 "header not found", or 4444 below the served floor ([L55-L90](https://github.com/NethermindEth/nethermind/blob/83c8d6cec184fbe82b23b09c1c1f76da7e953a6f/src/Nethermind/Nethermind.JsonRpc/Modules/BlockFinderExtensions.cs#L55-L90)) |
| Erigon | Measured: accepted, 3 records from block 2 | Measured: accepted, same | Source: rejected; `GetCanonicalBlockNumber` always requires canonical ([helper.go L80-L89](https://github.com/erigontech/erigon/blob/48d3a168fbbf3ccf28b0361a7472bca4c8d92376/rpc/rpchelper/helper.go#L80-L89), [L131-L146](https://github.com/erigontech/erigon/blob/48d3a168fbbf3ccf28b0361a7472bca4c8d92376/rpc/rpchelper/helper.go#L131-L146)) | Source: **`[]`**, "waiting for spec" ([trace_filtering.go L337-L353](https://github.com/erigontech/erigon/blob/48d3a168fbbf3ccf28b0361a7472bca4c8d92376/rpc/jsonrpc/trace_filtering.go#L337-L353)); open #24357 makes it an error |
| Reth | Measured: -32602 | Measured: -32602 | — | — |
| Besu | Measured: -32602 "Invalid filter params" | Measured: -32602 | — | — |
| Geth draft | Measured: -32602 "hex number > 64 bits" | Measured: -32602 | — | — |
| Anvil | Measured: -32602 | Measured: -32602 | — | — |
| Parity | Source: rejected; hex strings parse as numbers | Source: accepted ([block_number.rs L114-L160](https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/rpc/src/v1/types/block_number.rs#L114-L160)) | Source: **not pinned** (below) | Source: `null`; `filter_traces` returns `None` |

Erigon's `[]` for an unknown hash bound is the empty-result ambiguity in its purest form. The open
[erigontech/erigon#24357](https://github.com/erigontech/erigon/pull/24357) removes that branch, so an
unknown hash bound returns the existing block-not-found error instead.

Parity accepted the EIP-1898 object but rejected a bare hash string, and its hash bounds **never
pinned a block**: `block_number(hash)` read any known header, then scanned the canonical,
number-indexed trace database ([client.rs](https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/ethcore/src/client/client.rs#L2052-L2073)),
so a side-chain hash returned the canonical block's traces at that height. The Parity baseline has
no pinned, address-filtered trace query at all; `blockHash` is new relative to Parity, but it is
EIP-234 (Final, implemented by every client's `eth_getLogs`), not an invented feature.

### `eth_getLogs` with `blockHash` (the alignment target)

| Client | Combined with bounds | Unknown hash | Noncanonical (side-chain) hash |
| --- | --- | --- | --- |
| Geth | -32602 ([api.go](https://github.com/ethereum/go-ethereum/blob/f8f9bc574459a1afefac7b63163739910ee0fe62/eth/filters/api.go#L637-L641)) | -32000 "unknown block" | **Served**: any stored header ([api_backend.go](https://github.com/ethereum/go-ethereum/blob/f8f9bc574459a1afefac7b63163739910ee0fe62/eth/api_backend.go#L143-L145)) |
| Besu | -32602 ([EthGetLogs](https://github.com/besu-eth/besu/blob/d4ad1359b3c04b0f72cf216283a4c0dd1562424b/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/EthGetLogs.java#L65-L86)) | -32000 "Block not found" | **Served, with `removed: true`** ([BlockchainQueries](https://github.com/besu-eth/besu/blob/d4ad1359b3c04b0f72cf216283a4c0dd1562424b/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/query/BlockchainQueries.java#L1305-L1311)) |
| Erigon | -32602 ([eth_receipts.go](https://github.com/erigontech/erigon/blob/48d3a168fbbf3ccf28b0361a7472bca4c8d92376/rpc/jsonrpc/eth_receipts.go#L224-L226)) | -32000 "block not found" | **Rejected** as not found ([L118-L150](https://github.com/erigontech/erigon/blob/48d3a168fbbf3ccf28b0361a7472bca4c8d92376/rpc/jsonrpc/eth_receipts.go#L118-L150)) |
| Reth | -32602 (Alloy [filter.rs](https://github.com/alloy-rs/alloy/blob/4388f757c79e5f2d6f9b47498473e560d93e3956/crates/rpc-types-eth/src/filter.rs#L1070-L1076)) | -32001 (measured below) | **Rejected** in practice: canonical-only provider ([eth/filter.rs](https://github.com/paradigmxyz/reth/blob/1cb086adcbf6d9c18627ce03dd2fc9ec550f9c11/crates/rpc/rpc/src/eth/filter.rs#L496-L512)) |
| Anvil | -32602 (Alloy) | -32000 "unknown block" | Unknown: a reorg deletes the old blocks ([storage.rs](https://github.com/foundry-rs/foundry/blob/f1a18255f69f6ed79bfc22e6868668a2d853e793/crates/anvil/src/eth/backend/mem/storage.rs#L389-L403)) |
| Nethermind | -32602 ([Filter.cs](https://github.com/NethermindEth/nethermind/blob/83c8d6cec184fbe82b23b09c1c1f76da7e953a6f/src/Nethermind/Nethermind.JsonRpc/Modules/Eth/Filter.cs#L43-L65)); also rejects an explicit `fromBlock: null` | -32000 "header not found" | **Apparently the wrong block** (source only): resolves the side-chain header by hash, then scans by number through canonical lookups ([LogFinder.cs](https://github.com/NethermindEth/nethermind/blob/83c8d6cec184fbe82b23b09c1c1f76da7e953a6f/src/Nethermind/Nethermind.Facade/Find/LogFinder.cs#L344-L355)), returning the replacement block's logs |
| Parity | -32602 | -32000 with the hash in `data` | **Served** by walking parent links ([client.rs](https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/ethcore/src/client/client.rs#L1956-L2013)) |

All cells are from source except Reth's unknown hash, measured on 2.6.0. Unknown-hash sources:
Geth [filter.go L83-L97](https://github.com/ethereum/go-ethereum/blob/f8f9bc574459a1afefac7b63163739910ee0fe62/eth/filters/filter.go#L83-L97),
Besu [RpcErrorType.java L225](https://github.com/besu-eth/besu/blob/d4ad1359b3c04b0f72cf216283a4c0dd1562424b/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/response/RpcErrorType.java#L225),
Erigon [eth_receipts.go L124-L131](https://github.com/erigontech/erigon/blob/48d3a168fbbf3ccf28b0361a7472bca4c8d92376/rpc/jsonrpc/eth_receipts.go#L124-L131),
Anvil [mem/mod.rs L5468-L5480](https://github.com/foundry-rs/foundry/blob/f1a18255f69f6ed79bfc22e6868668a2d853e793/crates/anvil/src/eth/backend/mem/mod.rs#L5468-L5480)
(forwarded upstream in fork mode), Nethermind
[BlockFinderExtensions.cs L50-L52](https://github.com/NethermindEth/nethermind/blob/83c8d6cec184fbe82b23b09c1c1f76da7e953a6f/src/Nethermind/Nethermind.JsonRpc/Modules/BlockFinderExtensions.cs#L50-L52)
(its `ResourceNotFound` is -32000), Parity
[errors.rs L559-L570](https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/rpc/src/v1/helpers/errors.rs#L559-L570).
Nethermind's side-chain path: the hash becomes `BlockParameter(hash)` with `RequireCanonical = false`
([Filter.cs L47-L56](https://github.com/NethermindEth/nethermind/blob/83c8d6cec184fbe82b23b09c1c1f76da7e953a6f/src/Nethermind/Nethermind.JsonRpc/Modules/Eth/Filter.cs#L47-L56)),
and the scan walks block numbers ([LogFinder.cs L188-L198](https://github.com/NethermindEth/nethermind/blob/83c8d6cec184fbe82b23b09c1c1f76da7e953a6f/src/Nethermind/Nethermind.Facade/Find/LogFinder.cs#L188-L198)).
Erigon's resolver documents the hazard Nethermind appears to have: "a side-chain hash must not
resolve to the canonical block at that height".

Everyone agrees on mutual exclusivity. On side-chain hashes the live clients split: Geth and Besu
serve them; Erigon, Reth and Anvil do not; Nethermind appears to answer for a different block. So
"same as `eth_getLogs`" does not settle canonicality. The execution-apis Filter schema encodes the
exclusivity as a `oneOf` ([filter.yaml](https://github.com/ethereum/execution-apis/blob/5bcdc34a477b10af278c079525374e6a4046f291/src/schemas/filter.yaml#L13-L59))
and tests hash-plus-range as -32602, but specifies neither unknown nor noncanonical hashes.

### `trace_block` and `trace_replayBlockTransactions` by hash

| Client | `trace_block(hash)` | `trace_block({blockHash})` | Canonicality | Replay by hash |
| --- | --- | --- | --- | --- |
| Nethermind | Source: accepted ([ITraceRpcModule.cs L54-L56](https://github.com/NethermindEth/nethermind/blob/83c8d6cec184fbe82b23b09c1c1f76da7e953a6f/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/ITraceRpcModule.cs#L54-L56)) | Source: accepted; `requireCanonical: true` enforced | Source: a bare hash is not canonical-only, so a retained side-chain block is traced ([BlockParameter.cs](https://github.com/NethermindEth/nethermind/blob/83c8d6cec184fbe82b23b09c1c1f76da7e953a6f/src/Nethermind/Nethermind.Blockchain/Find/BlockParameter.cs#L55-L62), [TraceRpcModule.cs L479-L492](https://github.com/NethermindEth/nethermind/blob/83c8d6cec184fbe82b23b09c1c1f76da7e953a6f/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L479-L492)) | Source: accepted, same selector ([L312-L325](https://github.com/NethermindEth/nethermind/blob/83c8d6cec184fbe82b23b09c1c1f76da7e953a6f/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L312-L325)) |
| Reth | Measured on 2.6.0: accepted; unknown hash -32001 | Measured on 2.6.0: accepted | Source: canonical in practice; provider and cache ([trace.rs L520-L526](https://github.com/paradigmxyz/reth/blob/1cb086adcbf6d9c18627ce03dd2fc9ec550f9c11/crates/rpc/rpc/src/trace.rs#L520-L526)) | Measured on 2.6.0: accepted |
| Erigon | Source: rejected; `rpc.BlockNumber` ([L183](https://github.com/erigontech/erigon/blob/48d3a168fbbf3ccf28b0361a7472bca4c8d92376/rpc/jsonrpc/trace_filtering.go#L183), [types.go L109-L154](https://github.com/erigontech/erigon/blob/48d3a168fbbf3ccf28b0361a7472bca4c8d92376/rpc/types.go#L109-L154)) | Source: rejected | — | Source: accepted, canonical only ([trace_adhoc.go](https://github.com/erigontech/erigon/blob/48d3a168fbbf3ccf28b0361a7472bca4c8d92376/rpc/jsonrpc/trace_adhoc.go#L1105-L1125)) |
| Besu | Source: rejected; `BlockParameter` uses `Long.decode` ([TraceBlock.java L87](https://github.com/besu-eth/besu/blob/d4ad1359b3c04b0f72cf216283a4c0dd1562424b/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceBlock.java#L87), [BlockParameter.java L71](https://github.com/besu-eth/besu/blob/d4ad1359b3c04b0f72cf216283a4c0dd1562424b/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/parameters/BlockParameter.java#L71)) | Source: rejected | — | Source: rejected ([TraceReplayBlockTransactions.java L90](https://github.com/besu-eth/besu/blob/d4ad1359b3c04b0f72cf216283a4c0dd1562424b/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceReplayBlockTransactions.java#L90)) |
| Geth draft | Source: rejected; `rpc.BlockNumber` ([trace_namespace.go L187](https://github.com/banteg/go-ethereum/blob/e26833e3322f918c365f74be6971061c41736fc5/eth/tracers/trace_namespace.go#L187)) | Source: rejected | — | Source: rejected ([L141](https://github.com/banteg/go-ethereum/blob/e26833e3322f918c365f74be6971061c41736fc5/eth/tracers/trace_namespace.go#L141)) |
| Anvil | Source: rejected; `BlockNumber` ([api.rs L1563](https://github.com/foundry-rs/foundry/blob/f1a18255f69f6ed79bfc22e6868668a2d853e793/crates/anvil/src/eth/api.rs#L1563)) | Source: rejected | — | Source: rejected ([L1594-L1597](https://github.com/foundry-rs/foundry/blob/f1a18255f69f6ed79bfc22e6868668a2d853e793/crates/anvil/src/eth/api.rs#L1594-L1597)) |
| Parity | Source: rejected | Source: accepted ([traces.rs L72-L80](https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/rpc/src/v1/impls/traces.rs#L72-L80)) | Source: **not pinned**; resolved to a number and read from the canonical trace db ([client.rs L2100-L2107](https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/ethcore/src/client/client.rs#L2100-L2107)) | Source: object accepted; replays the named block's own body on its parent state ([traces.rs L177-L190](https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/rpc/src/v1/impls/traces.rs#L177-L190), [client.rs L1647-L1650](https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/ethcore/src/client/client.rs#L1647-L1650)) |
| Draft | Rejected: both methods take `BlockNumberOrTag` ([methods.yaml L313-L317](https://github.com/banteg/execution-apis/blob/afcbc676aa2d11cc5a3afcc73555b99a8f69ac33/src/trace/methods.yaml#L313-L317)) | Rejected | — | Rejected |

## The alternatives are more nuanced than the message suggests

The pinned draft is [afcbc676](https://github.com/banteg/execution-apis/blob/afcbc676aa2d11cc5a3afcc73555b99a8f69ac33/src/trace/methods.yaml).
It specifies number/tag selectors for **both** `trace_block` and `trace_replayBlockTransactions`.
Its `TraceFilter` has no `blockHash`, rejects additional fields, and excludes hashes from bounds.
Thus the portable gap in this draft is real. But implementation support differs:

| Interface | Hash pinning | Address filters / mode / pagination | Record consequences |
| --- | --- | --- | --- |
| Draft `trace_filter` | No | Yes | Localized frames and historical PoW rewards |
| Draft `trace_block` | No | No | Same record family as the filter |
| Reth / Nethermind `trace_block` | Yes (Reth measured on 2.6.0; Nethermind from source, not canonical-only) | No | Can filter and paginate locally after receiving the block |
| Erigon / Besu / Geth draft / Anvil `trace_block` | No: number/tag only | No | Would need a draft change and four client changes |
| Reth / Erigon / Nethermind block replay | Hash-capable implementation selectors (Erigon canonical-only) | No | Per-transaction envelopes; no standalone protocol reward records |

Reth's current [implementation](https://github.com/paradigmxyz/reth/blob/1cb086adcbf6d9c18627ce03dd2fc9ec550f9c11/crates/rpc/rpc/src/trace.rs#L519-L555)
takes `BlockId`, obtains the selected block and passes it into tracing. Nethermind's
[block method](https://github.com/NethermindEth/nethermind/blob/83c8d6cec184fbe82b23b09c1c1f76da7e953a6f/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L479-L526)
uses `BlockParameter` and `SearchForBlock`; that selector has a hash and canonicality flag.
Erigon's [block method](https://github.com/erigontech/erigon/blob/48d3a168fbbf3ccf28b0361a7472bca4c8d92376/rpc/jsonrpc/trace_filtering.go#L183)
still takes `rpc.BlockNumber`. Besu resolves the selector to a number and calls
[`getBlockByNumber`](https://github.com/besu-eth/besu/blob/d4ad1359b3c04b0f72cf216283a4c0dd1562424b/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceBlock.java#L85-L106).

On the user's archive Reth node, `reth/v2.6.0-73a3a00`, mainnet block 1 gave:

| Request | Observed result |
| --- | --- |
| `trace_block(1)` | One PoW reward record |
| `trace_block(hash-of-1)` | Identical reward record and requested block hash |
| `trace_block({blockHash: hash-of-1, requireCanonical: true})` | Identical reward record |
| `trace_block(unknown-hash)` | Error, -32001 |
| Numeric `trace_filter` over block 1, selecting its reward author | One matching reward |
| `trace_filter({blockHash: hash-of-1, ...})` | Error, -32602, unknown field |
| `trace_replayBlockTransactions(hash-of-1, ["trace"])` | `[]`: this block has no transactions |
| `eth_getLogs({blockHash: hash-of-1})` | `[]` |
| `eth_getLogs({blockHash: unknown-hash})` | Error, -32001 |

This proves canonical hash acceptance and shows that replay is not a drop-in substitute even
after flattening: it omits the reward. It does **not** prove behavior during a reorg or access to
orphan state. Raw observations and a bounded repeatable probe are in
[the evidence directory](../../evidence/2026-09-29/blockhash-study/reth.json).

Adding hash selection to `trace_block` is therefore a credible alternative if minimizing the
filter API is the priority. It preserves identity and localized records, but shifts filtering,
pagination and full-block response costs to callers. Adding it to `trace_filter` directly serves
the proposed use case and can reuse the existing matcher and ordering rules. Neither choice
guarantees cheap execution: replay-based implementations may still execute the entire block.

## Identity and canonicality are separate choices

| Policy | A is canonical in the request's selected view | A is known but noncanonical |
| --- | --- | --- |
| Canonical-only hash selector | Return matching records from A, or an availability error | Error |
| EIP-234-style exact-block selector | Return matching records from A, or an availability error | Return A's records when required data/state is available; otherwise error |

Both prevent B's empty result from being attributed to A. Only the second promises to serve
retained orphan history. A hash does not prove finality, nor that the selected block remains
canonical after the response. The caller must still follow fork choice and roll back its index.

The broader policy costs more for traces than merely retaining logs: replay needs the selected
block's body, its parent's state and the correct branch environment. An address index over the
canonical chain cannot answer an orphan query by resolving its hash to a height. Historical
canonical state retention is not proof of orphan-state retention.

This distinction is already visible in Erigon. Its current
[`eth_getLogs` hash resolver](https://github.com/erigontech/erigon/blob/48d3a168fbbf3ccf28b0361a7472bca4c8d92376/rpc/jsonrpc/eth_receipts.go#L118-L148)
checks that the requested hash equals the canonical hash at that height and rejects a side-chain
hash. Its trace bound resolver likewise uses
[`GetCanonicalBlockNumber`](https://github.com/erigontech/erigon/blob/48d3a168fbbf3ccf28b0361a7472bca4c8d92376/rpc/jsonrpc/eth_api.go#L277-L297)
in a committed database view. Therefore “same as eth_getLogs” alone does not settle orphan policy:
the EIP's intent and this client's implementation differ.

My preference is to require the canonical-only facility in the first profile and describe that
limit explicitly. It fixes the motivating correctness gap without requiring a new orphan tracing
capability. If maintainers want full EIP-234 semantics, choose and test that deliberately, and
revise the draft's statement that non-pending localized records carry canonical hashes.

## Proposed contract to discuss

1. `blockHash` is an optional 32-byte hash member that every conforming client must implement:
   optional to send, not optional to support. A pin callers cannot rely on is not a pin, and the
   minimum any client must do anyway (reject the unknown member) gives callers nothing.
2. A non-null `blockHash` is mutually exclusive with non-null `fromBlock` and `toBlock`.
   Normalize null as omitted, consistently with the existing trace-filter member rule, before
   selecting hash mode or applying default bounds. Explicitly document this null policy.
3. Resolve the hash, check canonicality and execution availability, and obtain traces using one
   coherent view. Never resolve H to N and then query N against a newer view. Retaining the selected
   block and the appropriate state, or erroring when that view cannot be retained, are valid strategies.
4. Unknown, noncanonical or not-yet-executed selected blocks produce an error (-32001 recommended,
   as for an unknown single block under H06; 4444 recommended for pruned history). Pruned required
   history and resource limits also produce errors. No fallback to latest, another block at the
   same height, an empty result or a partial result. Validate selector identity before a `count: 0`
   shortcut; an invalid selector must not look supported because no results were requested.
5. Apply existing address matching and mode to that block's records, including reward matching;
   then skip `after` and take `count`. Preserve localization and original `traceAddress` values.
   An empty page means no records remain after these operations **for H**, not necessarily that
   the block contains no traces or no matching addresses.
6. No hash range bounds and no implicit ancestry traversal. Queries across multiple blocks keep
   the current range contract. Hash pinning stabilizes pages for one block; it does not give
   separate numeric-range calls a shared snapshot.

The specific numeric error codes can remain recommendations under the current draft policy.
The [-32602 versus -32000 review comment](https://github.com/erigontech/erigon/pull/24357#discussion_r4118373485)
is useful evidence of resolver complexity, but is not itself the reason to add this feature.
That PR is open at `3f6d9a583e9b7ed3f63ce09f70954db2b4b0f8dc` at review time; its body explicitly
documents the remaining transient overlay-only hash case. Neither it nor its review establishes
agreement on a new `blockHash` field.

## Suggested draft wording

`TraceFilter` schema, new property:

```yaml
blockHash:
  anyOf:
  - $ref: '#/components/schemas/hash32'
  - type: 'null'
  description: Selects exactly one block by hash, as eth_getLogs does (EIP-234). A non-null blockHash
    is mutually exclusive with non-null fromBlock and toBlock (-32602 recommended); null is the same as omitted.
```

Addition to the `trace_filter` description:

> A non-null blockHash selects exactly the block with that hash; the result, including [], is for
> that block. The block must be in the request's canonical chain view and executed: an unknown,
> noncanonical or not yet executed hash returns an error (-32001, Resource not found, recommended),
> never another block's records or []; a block whose required history is pruned returns an error
> (4444 recommended). Address matching, mode, ordering and after/count then apply as for a
> single-block range, and records carry the requested hash. Resolve the hash and trace the block in
> one chain view. Unlike EIP-234, trace_filter does not serve noncanonical blocks (H32).

The profile bullet in `docs-api/docs/trace-profile.md` that ends "select a single block by number"
becomes:

> … but `eth_getLogs` range bounds do not. As in `eth_getLogs` (EIP-234), a separate `blockHash`
> member selects one block by hash, so an empty result cannot be mistaken for the result of a block
> that replaced it. The draft narrows EIP-234 to canonical blocks: a hash that is not canonical in
> the request's view is an error (-32001 recommended), and serving noncanonical blocks is left to a
> later decision.

`trace_filter` also lists -32001 among its errors.

This also separates the two errors raised in the Erigon #24357 review: a range bound past the
head is the range rule's error (-32602 recommended), and a hash not in the view is the not-found
rule's error (-32001 recommended).

Estimated client cost is a thin mapping everywhere (check the hash is canonical, then trace it as
`fromBlock = toBlock = number` within one view): about 10 lines in Nethermind, whose
`SearchForBlocksOnMainChain` already rejects side-chain blocks and traces resolved `Block`
objects; about 20 in Erigon, reusing its `eth_getLogs` hash resolver inside the existing read
transaction; about 15 in Besu, which already parses the member; a new Alloy `TraceFilter` field
for Reth and Anvil (alongside the tag change H32 already needs); and about 15 in the Geth draft.
Three of those changes also remove today's silent answer for latest.

## Migration and discriminating tests

Do not infer support from a successful response. Besu's
[`FilterParameter`](https://github.com/besu-eth/besu/blob/d4ad1359b3c04b0f72cf216283a4c0dd1562424b/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/parameters/FilterParameter.java#L49-L75)
already parses `blockHash`, but its current
[`TraceFilter`](https://github.com/besu-eth/besu/blob/d4ad1359b3c04b0f72cf216283a4c0dd1562424b/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceFilter.java#L96-L129)
uses defaulted range bounds and never reads that hash or calls `isValid()`. A hash-only request
therefore selects latest/latest in the inspected source. Reth explicitly rejects the field in
the live probe. Erigon and Nethermind also answer for latest: their request types have no hash
member, and the refresh's `a/filter-unknown-field` case shows both accept unknown members
(see [What clients do today](#what-clients-do-today)).

Use a tested client/profile version or a discriminating capability check, not a generic success
or error alone. A known non-head block with known matches should return those hashes; an unknown
hash should error. Unknown-hash rejection alone is insufficient because a client that rejects
every use of the field also passes it. `count: 0` alone proves nothing about selection.

Before adopting the feature, add these cases to the harness:

- A known canonical non-head block with matching and nonmatching addresses; compare with the
  same numeric single-block filter, including union/intersection and rewards.
- Unknown hash, malformed hash, conflicting bounds, explicit nulls, and unknown hash with count 0.
- Hash selection with pagination: first page, later page, past-end page and count 0. Keep the same
  hash across calls while advancing or reorganizing the head.
- Reorg A → B at the same height where A matches X and B does not. Query H(A) after the switch:
  canonical-only must error; a future orphan-capable profile may return A's matches, never B's `[]`.
- The reverse empty/nonempty arrangement, and the A → B → A sequence. Re-establishing A should
  restore successful hash queries once A is available in the selected execution view.
- A reorg between internal hash resolution and trace lookup, using a controlled client test hook:
  return the selected block's result or error, never the replacement's result.
- Known header ahead of execution, pruned required state and retention-boundary cases. Header
  existence alone does not authorize a successful empty trace answer.

### Concrete h30 cases

On fixture chain a (block 2 is `0xf5de2a84…`; the Anvil replica substitutes its own hashes, as
`filter-hash-bounds` already does), each hash case is compared with its numeric equivalent, so the
comparison proves the block was actually selected:

| Case | Request | Expected |
| --- | --- | --- |
| `filter-blockhash` | `{blockHash: H2, count: 3}` | The records of `{fromBlock: 0x2, toBlock: 0x2, count: 3}`, each localized with H2. **The Besu, Erigon and Nethermind check:** today they would answer with head block 48 |
| `filter-blockhash-address` | `{blockHash: H2, fromAddress: [X]}`, and a `toAddress` variant | The numeric equivalents, including a reward matched by author |
| `filter-blockhash-union` | `{blockHash: H2, fromAddress, toAddress, mode: union}` | The numeric equivalent |
| `filter-blockhash-page` | `{blockHash: H2, after: 1, count: 1}`, and `after` past the end | The numeric pages; `[]` past the end |
| `filter-blockhash-empty` | A known non-head block with no matching records | `[]`, not an error |
| `filter-blockhash-genesis` | The genesis hash | `[]` |
| `filter-blockhash-and-range` | `{blockHash: H2, fromBlock: 0x2}` | -32602 recommended |
| `filter-blockhash-null-bounds` | `{blockHash: H2, fromBlock: null, toBlock: null}` | As `filter-blockhash` |
| `filter-blockhash-null` | `{blockHash: null, fromBlock: 0x2, toBlock: 0x2}` | As the numeric range |
| `filter-blockhash-unknown` | An absent hash, alone and with `count: 0` | Error, -32001 recommended |
| `filter-blockhash-malformed` | A short hash, and an EIP-1898 object as the value | -32602 recommended |
| `filter-hash-bounds`, `filter-hash-object-bounds` | Unchanged | -32602 recommended |

The reorg cases above belong in the `reorg` and `reorg-safe` Hive scenarios, one `blockHash` query
per before, after and restored phase; the adapter needs a per-branch hash substitution.

The current `reorg-safe` corpus already switches and restores branches, but its trace requests
select numbers, not hashes. It is a useful base, not evidence that the proposed guarantee holds.
No new client reorg run was performed for this study. Cross-client results above are source
inspection except for the explicitly labeled Reth probes and the cited refresh cases. Exact source revisions and content
digests are recorded in [sources.json](../../evidence/2026-09-29/blockhash-study/sources.json).

## Suggested reply to Paolo

Not posted; for the maintainer to adapt.

> Agreed, and thanks for pushing on it. Proposal: trace_filter gains `blockHash`, as eth_getLogs has
> since EIP-234. It is mutually exclusive with fromBlock/toBlock (-32602), and an explicit null counts
> as omitted. It selects exactly that block: records carry that hash, and after/count/mode and
> rewards work as for a single-block range. One narrowing against EIP-234: canonical only. An unknown,
> noncanonical or not-yet-executed hash is an error (-32001 recommended, as for trace_block's unknown
> block), never `[]` or another block's records, and the hash is resolved and traced in one view.
> Hash range bounds stay rejected, so `{fromBlock: H, toBlock: H}` becomes `{blockHash: H}`. For
> Erigon this should be a small mapping onto `resolveLogsBlockHash`/`resolveCommittedBlockNumber`
> inside the existing transaction. It also settles the #24357 split: a bound past the head is -32602
> under the range rule, and a hash outside the view is -32001 under the not-found rule. Serving
> noncanonical blocks would be a separate, later decision. Does that work for you?
