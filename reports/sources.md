# Client source guide

Entry points for reviewing the proposed changes. Links are pinned to the tested development revisions (or the experimental Geth fork), so line numbers remain stable. They identify relevant code, not necessarily the full fix.

## Besu

| Area | Source | Revision |
| --- | --- | --- |
| Lookup | [Trace lookup](https://github.com/besu-eth/besu/blob/f9572aa82a2dadb3dd1b218d3ca97101540faf97/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceGet.java#L37) | `f9572aa82a2d` |
| Filter | [Filter execution pipeline](https://github.com/besu-eth/besu/blob/f9572aa82a2dadb3dd1b218d3ca97101540faf97/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceFilter.java#L135) | `f9572aa82a2d` |
| Call | [Call simulation](https://github.com/besu-eth/besu/blob/f9572aa82a2dadb3dd1b218d3ca97101540faf97/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/AbstractTraceCall.java#L40) | `f9572aa82a2d` |
| Raw | [Signed transaction replay](https://github.com/besu-eth/besu/blob/f9572aa82a2dadb3dd1b218d3ca97101540faf97/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceRawTransaction.java#L46) | `f9572aa82a2d` |
| Replay | [Block replay](https://github.com/besu-eth/besu/blob/f9572aa82a2dadb3dd1b218d3ca97101540faf97/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceReplayBlockTransactions.java#L58) | `f9572aa82a2d` |
| Frames | [Call-frame inclusion](https://github.com/besu-eth/besu/blob/f9572aa82a2dadb3dd1b218d3ca97101540faf97/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/results/tracing/flat/FlatTraceGenerator.java#L284) | `f9572aa82a2d` |
| Vm | [VM memory deltas](https://github.com/besu-eth/besu/blob/f9572aa82a2dadb3dd1b218d3ca97101540faf97/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/results/tracing/vm/VmTraceGenerator.java#L230) | `f9572aa82a2d` |
| Bounds | [Filter range defaults](https://github.com/besu-eth/besu/blob/f9572aa82a2dadb3dd1b218d3ca97101540faf97/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/parameters/FilterParameter.java#L66) | `f9572aa82a2d` |
| Many | [Batched call argument count](https://github.com/besu-eth/besu/blob/f9572aa82a2dadb3dd1b218d3ca97101540faf97/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceCallMany.java#L92) | `f9572aa82a2d` |
| Tags | [Filter block-tag resolver](https://github.com/besu-eth/besu/blob/f9572aa82a2dadb3dd1b218d3ca97101540faf97/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceFilter.java#L275) | `f9572aa82a2d` |
| State | [State differences](https://github.com/besu-eth/besu/blob/f9572aa82a2dadb3dd1b218d3ca97101540faf97/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/results/tracing/diff/StateTraceGenerator.java#L148) | `f9572aa82a2d` |

## Erigon

| Area | Source | Revision |
| --- | --- | --- |
| Lookup | [Trace lookup](https://github.com/erigontech/erigon/blob/e26d9bd4056586e004488c31b561fb2663d46019/rpc/jsonrpc/trace_filtering.go#L135) | `e26d9bd40565` |
| Filter | [Address filtering](https://github.com/erigontech/erigon/blob/e26d9bd4056586e004488c31b561fb2663d46019/rpc/jsonrpc/trace_filtering.go#L311) | `e26d9bd40565` |
| Call | [Call simulation](https://github.com/erigontech/erigon/blob/e26d9bd4056586e004488c31b561fb2663d46019/rpc/jsonrpc/trace_adhoc.go#L1096) | `e26d9bd40565` |
| Raw | [Signed transaction replay](https://github.com/erigontech/erigon/blob/e26d9bd4056586e004488c31b561fb2663d46019/rpc/jsonrpc/trace_adhoc.go#L1695) | `e26d9bd40565` |
| Replay | [Replay results](https://github.com/erigontech/erigon/blob/e26d9bd4056586e004488c31b561fb2663d46019/rpc/jsonrpc/trace_adhoc.go#L920) | `e26d9bd40565` |
| Frames | [Call frames and precompiles](https://github.com/erigontech/erigon/blob/e26d9bd4056586e004488c31b561fb2663d46019/rpc/jsonrpc/trace_adhoc.go#L378) | `e26d9bd40565` |
| Vm | [VM execution deltas](https://github.com/erigontech/erigon/blob/e26d9bd4056586e004488c31b561fb2663d46019/rpc/jsonrpc/trace_adhoc.go#L577) | `e26d9bd40565` |
| State | [State differences](https://github.com/erigontech/erigon/blob/e26d9bd4056586e004488c31b561fb2663d46019/rpc/jsonrpc/trace_adhoc.go#L781) | `e26d9bd40565` |
| Bounds | [Filter range defaults](https://github.com/erigontech/erigon/blob/e26d9bd4056586e004488c31b561fb2663d46019/rpc/jsonrpc/trace_filtering.go#L335) | `e26d9bd40565` |
| Many | [Batched call block default](https://github.com/erigontech/erigon/blob/e26d9bd4056586e004488c31b561fb2663d46019/rpc/jsonrpc/trace_adhoc.go#L1325) | `e26d9bd40565` |
| Tags | [Filter pending-tag check](https://github.com/erigontech/erigon/blob/e26d9bd4056586e004488c31b561fb2663d46019/rpc/jsonrpc/trace_filtering.go#L312) | `e26d9bd40565` |

## Geth draft fork

| Area | Source | Revision |
| --- | --- | --- |
| Lookup | [Trace lookup](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_namespace.go#L154) | `fa8ecb9242dd` |
| Filter | [Address filtering](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_namespace.go#L187) | `fa8ecb9242dd` |
| Call | [Call simulation](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_namespace.go#L53) | `fa8ecb9242dd` |
| Raw | [Signed transaction replay](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_namespace.go#L98) | `fa8ecb9242dd` |
| Replay | [Replay results](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_namespace.go#L123) | `fa8ecb9242dd` |
| Frames | [Call frames and precompiles](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_capture.go#L123) | `fa8ecb9242dd` |
| Vm | [VM execution deltas](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_capture.go#L264) | `fa8ecb9242dd` |
| State | [State differences](https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_capture.go#L233) | `fa8ecb9242dd` |

## Nethermind

| Area | Source | Revision |
| --- | --- | --- |
| Lookup | [Trace lookup](https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L433) | `2a3b2531b4dc` |
| Filter | [Address matching](https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TxTraceFilter.cs#L56) | `2a3b2531b4dc` |
| Call | [Call simulation](https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L78) | `2a3b2531b4dc` |
| Raw | [Signed transaction replay](https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L150) | `2a3b2531b4dc` |
| Replay | [Replay serialization](https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/ParityReplayEnvelopeWriter.cs#L24) | `2a3b2531b4dc` |
| Frames | [Call frames and precompiles](https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.Blockchain/Tracing/ParityStyle/ParityLikeTxTracer.cs#L419) | `2a3b2531b4dc` |
| Vm | [VM step serialization](https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.Blockchain/Tracing/ParityStyle/ParityVmOperationTraceConverter.cs#L17) | `2a3b2531b4dc` |
| State | [Code and nonce state changes](https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.Blockchain/Tracing/ParityStyle/ParityLikeTxTracer.cs#L362) | `2a3b2531b4dc` |
| Bounds | [Filter range defaults](https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L294) | `2a3b2531b4dc` |
| Many | [Batched call block default](https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L95) | `2a3b2531b4dc` |
| Tags | [Filter tag lookup](https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L287) | `2a3b2531b4dc` |

## Reth

| Area | Source | Revision |
| --- | --- | --- |
| Lookup | [Trace lookup](https://github.com/paradigmxyz/reth/blob/58a51b3ee3f6714ded9207b244a273c8afb592fd/crates/rpc/rpc/src/trace.rs#L218) | `58a51b3ee3f6` |
| Filter | [Address filtering](https://github.com/paradigmxyz/reth/blob/58a51b3ee3f6714ded9207b244a273c8afb592fd/crates/rpc/rpc/src/trace.rs#L370) | `58a51b3ee3f6` |
| Call | [Call simulation](https://github.com/paradigmxyz/reth/blob/58a51b3ee3f6714ded9207b244a273c8afb592fd/crates/rpc/rpc/src/trace.rs#L97) | `58a51b3ee3f6` |
| Raw | [Signed transaction replay](https://github.com/paradigmxyz/reth/blob/58a51b3ee3f6714ded9207b244a273c8afb592fd/crates/rpc/rpc/src/trace.rs#L121) | `58a51b3ee3f6` |
| Replay | [Replay results](https://github.com/paradigmxyz/reth/blob/58a51b3ee3f6714ded9207b244a273c8afb592fd/crates/rpc/rpc/src/trace.rs#L195) | `58a51b3ee3f6` |
| Vm | [VM trace builder (revm-inspectors 0.43.0)](https://github.com/paradigmxyz/revm-inspectors/blob/453c67d7ccdf51327c9e7687ac6ba0b8651e7f87/src/tracing/builder/parity.rs#L317) | `453c67d7ccdf` |
| State | [State-diff builder (revm-inspectors 0.43.0)](https://github.com/paradigmxyz/revm-inspectors/blob/453c67d7ccdf51327c9e7687ac6ba0b8651e7f87/src/tracing/builder/parity.rs#L509) | `453c67d7ccdf` |
| Frames | [Precompile frame selection (revm-inspectors 0.43.0)](https://github.com/paradigmxyz/revm-inspectors/blob/453c67d7ccdf51327c9e7687ac6ba0b8651e7f87/src/tracing/mod.rs#L289) | `453c67d7ccdf` |
| Bounds | [Filter range defaults](https://github.com/paradigmxyz/reth/blob/58a51b3ee3f6714ded9207b244a273c8afb592fd/crates/rpc/rpc/src/trace.rs#L377) | `58a51b3ee3f6` |
| Many | [Batched call block default](https://github.com/paradigmxyz/reth/blob/58a51b3ee3f6714ded9207b244a273c8afb592fd/crates/rpc/rpc/src/trace.rs#L155) | `58a51b3ee3f6` |
| Tags | [Filter block-selector type](https://github.com/paradigmxyz/reth/blob/58a51b3ee3f6714ded9207b244a273c8afb592fd/crates/rpc/rpc/src/trace.rs#L372) | `58a51b3ee3f6` |

Reth’s inspector links point into its locked `revm-inspectors` 0.43.0 dependency. File hashes and anchor text are retained in [the source catalog](../decisions/sources.json).
