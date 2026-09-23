# Related pull requests

Related client, specification and test-suite PRs. Status checked **2026-09-24**.

## Open

| PR | Change |
| --- | --- |
| [Alloy EVM #411](https://github.com/alloy-rs/evm/pull/411) | Preserve fatal system call error sources |
| [Besu #10953](https://github.com/besu-eth/besu/pull/10953) | Replay block pre-execution before tracing transactions |
| [Besu #11286](https://github.com/besu-eth/besu/pull/11286) | Include MCOPY memory updates in vmTrace |
| [Besu #11345](https://github.com/besu-eth/besu/pull/11345) | Keep Parity trace failures local to their call frame |
| [Besu #11346](https://github.com/besu-eth/besu/pull/11346) | Retain precompile output in Parity call frames |
| [Besu #11347](https://github.com/besu-eth/besu/pull/11347) | Retain root precompile halt reasons |
| [Besu #11350](https://github.com/besu-eth/besu/pull/11350) | Avoid attributing parent return memory to calls |
| [Besu #11352](https://github.com/besu-eth/besu/pull/11352) | Retain VM frame positions across omitted opcodes |
| [Besu #11353](https://github.com/besu-eth/besu/pull/11353) | Omit root out-of-gas execution effects |
| [Erigon #24255](https://github.com/erigontech/erigon/pull/24255) | Default trace filters to intersection |
| [execution-apis #895](https://github.com/ethereum/execution-apis/pull/895) (draft) | Parity trace methods and output schemas |
| [Nethermind #13551](https://github.com/NethermindEth/nethermind/pull/13551) (draft) | Pair instruction trace completions with starts |
| [Nethermind #13622](https://github.com/NethermindEth/nethermind/pull/13622) (draft) | Report terminal output for top-level action traces |
| [Nethermind #13665](https://github.com/NethermindEth/nethermind/pull/13665) | Retain output in state-only Parity traces |
| [Nethermind #13666](https://github.com/NethermindEth/nethermind/pull/13666) | Preserve error responses for streamed traces |
| [Nethermind #13667](https://github.com/NethermindEth/nethermind/pull/13667) | Accept empty Parity trace selections |
| [Nethermind #13668](https://github.com/NethermindEth/nethermind/pull/13668) | Serialize deleted account fields with deletion markers |
| [Nethermind #13676](https://github.com/NethermindEth/nethermind/pull/13676) | Preserve trace_get errors and bound positions |
| [Nethermind #13677](https://github.com/NethermindEth/nethermind/pull/13677) | Reject trace filters with unavailable history |
| [Reth #27213](https://github.com/paradigmxyz/reth/pull/27213) | Populate VM bytecode in block replay traces |
| [Reth #27217](https://github.com/paradigmxyz/reth/pull/27217) | Correct Otterscan block and transaction responses |
| [Reth #27378](https://github.com/paradigmxyz/reth/pull/27378) | Preserve pruned history errors through execution wrappers |
| [rpc-tests #604](https://github.com/erigontech/rpc-tests/pull/604) | Make trace filter union fixtures explicit |
| [Silkworm #2885](https://github.com/erigontech/silkworm/pull/2885) (draft) | Capture missing vmTrace opcode effects |

## Merged

| PR | Change |
| --- | --- |
| [Alloy #4216](https://github.com/alloy-rs/alloy/pull/4216) | Default address filters to intersection |
| [Alloy #4218](https://github.com/alloy-rs/alloy/pull/4218) | Serialize absent transaction fields as null |
| [Erigon #23952](https://github.com/erigontech/erigon/pull/23952) | Include MCOPY memory writes in vmTrace |
| [Reth #27364](https://github.com/paradigmxyz/reth/pull/27364) | Return null for missing transaction replays |
| [Reth #27365](https://github.com/paradigmxyz/reth/pull/27365) | Include transaction hash in individual replays |
| [Reth #27366](https://github.com/paradigmxyz/reth/pull/27366) | Select trace_get results by tree path |
| [Reth #27367](https://github.com/paradigmxyz/reth/pull/27367) | Classify pruned changeset errors as unavailable history |
| [revm-inspectors #504](https://github.com/paradigmxyz/revm-inspectors/pull/504) | Record complete Parity VM execution deltas |
| [revm-inspectors #509](https://github.com/paradigmxyz/revm-inspectors/pull/509) | Report EIP-7702 code changes in state diffs |
| [revm-inspectors #510](https://github.com/paradigmxyz/revm-inspectors/pull/510) | Report selfdestructed account deletions |
| [revm-inspectors #511](https://github.com/paradigmxyz/revm-inspectors/pull/511) | Record executed bytecode in VM traces |
