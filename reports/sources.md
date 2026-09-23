# Client source guide

Entry points for reviewing the proposed changes. Links are pinned to the tested development revisions (or the experimental Geth fork), so line numbers remain stable. They identify relevant code, not necessarily the full fix.

## Besu

| Area | Source | Revision |
| --- | --- | --- |
| Lookup | [Trace lookup](https://github.com/besu-eth/besu/blob/d997aad7b3be6333464c0687d3761c568ee63524/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceGet.java#L37) | `d997aad7b3be` |
| Filter | [Filter execution pipeline](https://github.com/besu-eth/besu/blob/d997aad7b3be6333464c0687d3761c568ee63524/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceFilter.java#L135) | `d997aad7b3be` |
| Call | [Call simulation](https://github.com/besu-eth/besu/blob/d997aad7b3be6333464c0687d3761c568ee63524/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/AbstractTraceCall.java#L40) | `d997aad7b3be` |
| Raw | [Signed transaction replay](https://github.com/besu-eth/besu/blob/d997aad7b3be6333464c0687d3761c568ee63524/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceRawTransaction.java#L46) | `d997aad7b3be` |
| Replay | [Block replay](https://github.com/besu-eth/besu/blob/d997aad7b3be6333464c0687d3761c568ee63524/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceReplayBlockTransactions.java#L58) | `d997aad7b3be` |
| Frames | [Call-frame inclusion](https://github.com/besu-eth/besu/blob/d997aad7b3be6333464c0687d3761c568ee63524/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/results/tracing/flat/FlatTraceGenerator.java#L284) | `d997aad7b3be` |
| Vm | [VM memory deltas](https://github.com/besu-eth/besu/blob/d997aad7b3be6333464c0687d3761c568ee63524/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/results/tracing/vm/VmTraceGenerator.java#L230) | `d997aad7b3be` |
| Bounds | [Filter range defaults](https://github.com/besu-eth/besu/blob/d997aad7b3be6333464c0687d3761c568ee63524/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/parameters/FilterParameter.java#L66) | `d997aad7b3be` |
| Many | [Batched call argument count](https://github.com/besu-eth/besu/blob/d997aad7b3be6333464c0687d3761c568ee63524/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceCallMany.java#L92) | `d997aad7b3be` |
| Tags | [Filter block-tag resolver](https://github.com/besu-eth/besu/blob/d997aad7b3be6333464c0687d3761c568ee63524/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/methods/TraceFilter.java#L275) | `d997aad7b3be` |

## Erigon

| Area | Source | Revision |
| --- | --- | --- |
| Lookup | [Trace lookup](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_filtering.go#L135) | `c25b8e47dc1a` |
| Filter | [Address filtering](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_filtering.go#L311) | `c25b8e47dc1a` |
| Call | [Call simulation](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1056) | `c25b8e47dc1a` |
| Raw | [Signed transaction replay](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1656) | `c25b8e47dc1a` |
| Replay | [Replay results](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L880) | `c25b8e47dc1a` |
| Frames | [Call frames and precompiles](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L357) | `c25b8e47dc1a` |
| Vm | [VM execution deltas](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L545) | `c25b8e47dc1a` |
| State | [State differences](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L741) | `c25b8e47dc1a` |
| Bounds | [Filter range defaults](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_filtering.go#L335) | `c25b8e47dc1a` |
| Many | [Batched call block default](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_adhoc.go#L1287) | `c25b8e47dc1a` |
| Tags | [Filter pending-tag check](https://github.com/erigontech/erigon/blob/c25b8e47dc1a77ecdbd15d38ba3beae1d29530ec/rpc/jsonrpc/trace_filtering.go#L312) | `c25b8e47dc1a` |

## Geth draft fork

| Area | Source | Revision |
| --- | --- | --- |
| Lookup | [Trace lookup](https://github.com/banteg/go-ethereum/blob/40eecf3647f26546df9dbf72ce48f372df469ef2/eth/tracers/trace_namespace.go#L153) | `40eecf3647f2` |
| Filter | [Address filtering](https://github.com/banteg/go-ethereum/blob/40eecf3647f26546df9dbf72ce48f372df469ef2/eth/tracers/trace_namespace.go#L186) | `40eecf3647f2` |
| Call | [Call simulation](https://github.com/banteg/go-ethereum/blob/40eecf3647f26546df9dbf72ce48f372df469ef2/eth/tracers/trace_namespace.go#L52) | `40eecf3647f2` |
| Raw | [Signed transaction replay](https://github.com/banteg/go-ethereum/blob/40eecf3647f26546df9dbf72ce48f372df469ef2/eth/tracers/trace_namespace.go#L97) | `40eecf3647f2` |
| Replay | [Replay results](https://github.com/banteg/go-ethereum/blob/40eecf3647f26546df9dbf72ce48f372df469ef2/eth/tracers/trace_namespace.go#L122) | `40eecf3647f2` |
| Frames | [Call frames and precompiles](https://github.com/banteg/go-ethereum/blob/40eecf3647f26546df9dbf72ce48f372df469ef2/eth/tracers/trace_capture.go#L123) | `40eecf3647f2` |
| Vm | [VM execution deltas](https://github.com/banteg/go-ethereum/blob/40eecf3647f26546df9dbf72ce48f372df469ef2/eth/tracers/trace_capture.go#L264) | `40eecf3647f2` |
| State | [State differences](https://github.com/banteg/go-ethereum/blob/40eecf3647f26546df9dbf72ce48f372df469ef2/eth/tracers/trace_capture.go#L233) | `40eecf3647f2` |

## Nethermind

| Area | Source | Revision |
| --- | --- | --- |
| Lookup | [Trace lookup](https://github.com/NethermindEth/nethermind/blob/a404c4f06a67aee52cc448216b8d37a77062f106/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L402) | `a404c4f06a67` |
| Filter | [Address matching](https://github.com/NethermindEth/nethermind/blob/a404c4f06a67aee52cc448216b8d37a77062f106/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TxTraceFilter.cs#L56) | `a404c4f06a67` |
| Call | [Call simulation](https://github.com/NethermindEth/nethermind/blob/a404c4f06a67aee52cc448216b8d37a77062f106/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L69) | `a404c4f06a67` |
| Raw | [Signed transaction replay](https://github.com/NethermindEth/nethermind/blob/a404c4f06a67aee52cc448216b8d37a77062f106/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L141) | `a404c4f06a67` |
| Replay | [Replay serialization](https://github.com/NethermindEth/nethermind/blob/a404c4f06a67aee52cc448216b8d37a77062f106/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/ParityReplayEnvelopeWriter.cs#L24) | `a404c4f06a67` |
| Frames | [Call frames and precompiles](https://github.com/NethermindEth/nethermind/blob/a404c4f06a67aee52cc448216b8d37a77062f106/src/Nethermind/Nethermind.Blockchain/Tracing/ParityStyle/ParityLikeTxTracer.cs#L413) | `a404c4f06a67` |
| Vm | [VM step serialization](https://github.com/NethermindEth/nethermind/blob/a404c4f06a67aee52cc448216b8d37a77062f106/src/Nethermind/Nethermind.Blockchain/Tracing/ParityStyle/ParityVmOperationTraceConverter.cs#L17) | `a404c4f06a67` |
| State | [Code and nonce state changes](https://github.com/NethermindEth/nethermind/blob/a404c4f06a67aee52cc448216b8d37a77062f106/src/Nethermind/Nethermind.Blockchain/Tracing/ParityStyle/ParityLikeTxTracer.cs#L356) | `a404c4f06a67` |
| Bounds | [Filter range defaults](https://github.com/NethermindEth/nethermind/blob/a404c4f06a67aee52cc448216b8d37a77062f106/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L280) | `a404c4f06a67` |
| Many | [Batched call block default](https://github.com/NethermindEth/nethermind/blob/a404c4f06a67aee52cc448216b8d37a77062f106/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L90) | `a404c4f06a67` |
| Tags | [Filter tag lookup](https://github.com/NethermindEth/nethermind/blob/a404c4f06a67aee52cc448216b8d37a77062f106/src/Nethermind/Nethermind.JsonRpc/Modules/Trace/TraceRpcModule.cs#L278) | `a404c4f06a67` |

## Reth

| Area | Source | Revision |
| --- | --- | --- |
| Lookup | [Trace lookup](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L220) | `03cb186c1d36` |
| Filter | [Address filtering](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L363) | `03cb186c1d36` |
| Call | [Call simulation](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L97) | `03cb186c1d36` |
| Raw | [Signed transaction replay](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L121) | `03cb186c1d36` |
| Replay | [Replay results](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L195) | `03cb186c1d36` |
| Vm | [VM trace builder (revm-inspectors 0.43.0)](https://github.com/paradigmxyz/revm-inspectors/blob/453c67d7ccdf51327c9e7687ac6ba0b8651e7f87/src/tracing/builder/parity.rs#L317) | `453c67d7ccdf` |
| State | [State-diff builder (revm-inspectors 0.43.0)](https://github.com/paradigmxyz/revm-inspectors/blob/453c67d7ccdf51327c9e7687ac6ba0b8651e7f87/src/tracing/builder/parity.rs#L509) | `453c67d7ccdf` |
| Frames | [Precompile frame selection (revm-inspectors 0.43.0)](https://github.com/paradigmxyz/revm-inspectors/blob/453c67d7ccdf51327c9e7687ac6ba0b8651e7f87/src/tracing/mod.rs#L289) | `453c67d7ccdf` |
| Bounds | [Filter range defaults](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L370) | `03cb186c1d36` |
| Many | [Batched call block default](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L155) | `03cb186c1d36` |
| Tags | [Filter block-selector type](https://github.com/paradigmxyz/reth/blob/03cb186c1d36eebbacc7bda08f36e25711d0804e/crates/rpc/rpc/src/trace.rs#L365) | `03cb186c1d36` |

Reth’s inspector links point into its locked `revm-inspectors` 0.43.0 dependency. File hashes and anchor text are retained in [the source catalog](../decisions/sources.json).
