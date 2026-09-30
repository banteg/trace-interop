# Hash selectors across trace methods

Checked 2026-09-30. Scope: all nine common Parity-style trace methods, EIP-1898's six state methods, and debug_traceCall. Acceptance and canonicality enforcement are separate properties. No specification changes made.

## Verdict

EIP-1898 standardizes the object selector and requireCanonical for eth_getBalance, eth_getStorageAt, eth_getTransactionCount, eth_getCode, eth_call and eth_getProof. It does not list any trace or debug methods. EIP-234 standardizes a separate blockHash member for log filters. Neither automatically extends trace_filter.

[H33's revised recommendation](../../reports/decisions/H33.md#softened-recommendation-2026-09-30)
specifies optional exact-block selection: a non-null member may be explicitly rejected, but an
accepted collection must belong to the requested block. Accurate orphan results are permitted
where supported, with no orphan-retention requirement. Null still means omission under H14.
This is a proposal for client review, not a claim that the implementations below support it.

The subsequent [draft update](https://github.com/banteg/execution-apis/commit/6a9a69b3)
adds this optional filter member. The [Geth fork follow-up](https://github.com/banteg/go-ethereum/commit/ec1cec0be8)
implements canonical, executed hash selection and preserves identity across a reorg during lookup;
it rejects noncanonical and unexecuted selections. Its regression and full repository checks passed.
The tables below retain the inspected revisions; this follow-up is not in the selected client captures.

The optional, orphan-permitting revision above was [reversed later on 2026-09-30](../../reports/decisions/H33.md#client-positions-and-reversal-2026-09-30):
on Nethermind's and Erigon's stated positions, H33 requires the member with canonical-only
selection, and H32 rejects hash range bounds again. The `requireCanonical` rule for optional
selectors on other methods stands.

For trace methods the selector shape is not uniform, even within one client. The following table describes acceptance of the EIP-1898 block-hash object, not proof that its canonicality flag is enforced.

| Method | Reth | Nethermind | Erigon | Besu | Anvil | Geth trace draft fork |
| --- | --- | --- | --- | --- | --- | --- |
| trace_call | Yes | Yes | Yes | No | Yes | No |
| trace_callMany | Yes | Yes | Yes | No | Yes | No |
| trace_rawTransaction optional block argument | Yes | No block argument | No block argument | No: numbers/tags | Yes | No block argument |
| trace_block | Yes | Yes | No | No | No | No |
| trace_replayBlockTransactions | Yes | Yes | Yes | No | No | No |
| trace_filter fromBlock/toBlock | No | Yes | Yes | No | No | No |
| trace_filter separate blockHash member | Rejected | No implementation | No implementation | Parsed but unused | Rejected | Rejected |
| trace_replayTransaction | Transaction hash; no block selector | Same | Same | Same | Same | Same |
| trace_transaction | Transaction hash; no block selector | Same | Same | Same | Same | Same |
| trace_get | Transaction hash and path; no block selector | Same | Same | Same | Same | Same |

Bare hash strings follow the same trace-method acceptance in these six implementations. Historical Parity is different: its BlockNumber parses hash objects, not bare hash strings, for call, callMany, rawTransaction, block, replayBlockTransactions and filter bounds. It drops requireCanonical when converting to internal BlockId. Its trace_block and filter resolve hashes to heights and then read the canonical trace database, so their accepted syntax does not establish identity preservation.

## Canonicality paths

- Nethermind's trace_call and callMany use SearchForHeader; block and replayBlockTransactions use SearchForBlock. These pass BlockParameter into the block finder and report a noncanonical-block error when requireCanonical is true. Filter bounds additionally require both endpoints to be on the main chain.
- Erigon's call, callMany and replayBlockTransactions use GetCanonicalBlockNumber. That helper passes true to its resolver independently of the supplied RequireCanonical flag. Consequently false does not enable orphan tracing. Its filter bounds also require canonical hashes.
- Reth accepts the object across all five block-selecting trace methods. Source inspection found paths that reduce BlockId to the underlying hash: recovered_block uses block_hash_for_id, while evm_env_at uses sealed_header_by_id. These helpers do not explicitly enforce requireCanonical. Other provider paths do inspect it. The live checks here do not establish behavior on a retained noncanonical block.
- Anvil's accepted simulation selectors go through ensure_block_number, which reads hash.block_hash and converts the block to a number without inspecting require_canonical. Its storage/reorg behavior constrains what blocks remain queryable.
- Historical Parity parses the flag but drops it in the trace methods.

## Other namespaces

All six EIP-1898 state methods have hash-capable parameter types in the inspected native Geth, Reth, Nethermind, Erigon and Besu sources. Besu uses a separate BlockParameterOrBlockHash for these methods, while its trace methods use numeric BlockParameter. Besu's shared state-method dispatcher checks requireCanonical. Geth's state backend also checks it. Erigon's state methods force canonical resolution, including when false was supplied. Syntax support alone is therefore not proof of the full EIP orphan-state contract.

debug_traceCall accepts the object in Geth, Reth, Nethermind, Erigon and the inspected Anvil snapshot. Besu's AbstractTraceCall/AbstractTraceByBlock takes numeric BlockParameter. Native Geth's debug TraceCall reads the hash and calls blockByHash without testing RequireCanonical; Erigon forces canonical resolution. This is another method-specific extension, not a uniform EIP-1898 contract.

## Live Reth controls

The user's node now reports reth/v2.7.0-3d592ec, replacing the screenshot's 2.6.0 build. [Raw responses](../../evidence/2026-09-30/hash-selectors/reth.json) record number, bare hash, hash object, requireCanonical true/false and unknown-hash controls.

- trace_call, callMany, block and replayBlockTransactions: every known block-1 selector succeeds and equals the numeric result.
- trace_rawTransaction: a real mainnet transaction from block 1,000,000 simulated on its parent's state succeeds with number, bare hash and objects with true/false, with identical results. An earlier first-transaction control hit an intrinsic-gas error and is retained in the evidence.
- All six EIP-1898 methods accept the selectors. Proofs at block 1 hit the configured maximum proof window; repeat controls at a pinned recent block succeed.
- debug_traceCall and eth_getBlockReceipts also accept the objects.
- Unknown block objects error with -32001 for trace_call, callMany, block and rawTransaction. replayBlockTransactions returns null. eth_getBlockReceipts returns null; debug_traceCall errors with -32000.
- trace_filter rejects blockHash with -32602. eth_getLogs accepts it and errors with -32001 for an unknown hash.
- Block 1's trace_block reward and its empty transaction replay are expected to differ: block replay has per-transaction envelopes, not a standalone PoW reward envelope.

These are canonical-block and unknown-block checks. No orphan or reorg behavior was induced, and other clients were checked from source rather than newly executed here.

## Source revisions and references

Local source inspected: Reth 0256b6a0; Nethermind ac02224f; Erigon 3b4861d1; Besu fc87cc71; Geth 74edc938; Geth trace draft fa8ecb92; historical Parity 55c90d40. Anvil uses the prior study's pinned f1a18255 snapshot, fetched read-only, because the local checkout is an older source layout lacking the ad-hoc trace methods. These are inspected revisions, not claims about today's remote heads.

- [EIP-1898](https://eips.ethereum.org/EIPS/eip-1898), [EIP-234](https://eips.ethereum.org/EIPS/eip-234).
- [Reth trace RPC signatures](https://github.com/paradigmxyz/reth/blob/0256b6a0c3760bb4dde109be53f71687defb872d/crates/rpc/rpc-api/src/trace.rs), [block hash conversion](https://github.com/paradigmxyz/reth/blob/0256b6a0c3760bb4dde109be53f71687defb872d/crates/storage/storage-api/src/block_id.rs), [provider selectors](https://github.com/paradigmxyz/reth/blob/0256b6a0c3760bb4dde109be53f71687defb872d/crates/storage/provider/src/providers/consistent.rs).
- [Nethermind trace interface](https://github.com/NethermindEth/nethermind/blob/ac02224f25fd4901116ebf2643d522ec4a0e60a1/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/ITraceRpcModule.cs), [implementation](https://github.com/NethermindEth/nethermind/blob/ac02224f25fd4901116ebf2643d522ec4a0e60a1/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs).
- [Erigon ad-hoc traces](https://github.com/erigontech/erigon/blob/3b4861d10387ca3e19f7b16d1b8c0ec1fcd616cd/rpc/jsonrpc/trace_adhoc.go), [block/filter methods](https://github.com/erigontech/erigon/blob/3b4861d10387ca3e19f7b16d1b8c0ec1fcd616cd/rpc/jsonrpc/trace_filtering.go), [canonical resolver](https://github.com/erigontech/erigon/blob/3b4861d10387ca3e19f7b16d1b8c0ec1fcd616cd/rpc/rpchelper/helper.go).
- [Besu trace block selector](https://github.com/besu-eth/besu/blob/fc87cc71c1871e578d9793dc1ff2433ef7b69783/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/AbstractTraceByBlock.java), [numeric BlockParameter](https://github.com/besu-eth/besu/blob/fc87cc71c1871e578d9793dc1ff2433ef7b69783/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/parameters/BlockParameter.java).
- [Anvil RPC selectors](https://github.com/foundry-rs/foundry/blob/f1a18255f69f6ed79bfc22e6868668a2d853e793/crates/anvil/src/eth/api.rs), [hash-to-number resolution](https://github.com/foundry-rs/foundry/blob/f1a18255f69f6ed79bfc22e6868668a2d853e793/crates/anvil/src/eth/backend/mem/mod.rs).
- [Geth draft selectors](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_namespace.go), [Parity trace selectors](https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/rpc/src/v1/impls/traces.rs).
- Existing cross-client blockHash filter measurements: [H33](../../reports/decisions/H33.md). Existing draft schemas: [trace-openrpc.json](../../spec/trace-openrpc.json); call and callMany permit bare hash strings but not EIP-1898 objects, block and replayBlockTransactions permit numbers/tags only, and rawTransaction has no block argument. The draft therefore differs from several implemented selectors.
