# Related pull requests

Related client, specification and test-suite PRs. Status checked **2026-09-24**.

Reports show 🛠️ Fix submitted instead of ⚠️ or 🟡 for a build when a PR tagged with its client and decision is open, was merged after the build’s commit, or awaits uptake of the merged library change. A PR marked partial is linked but leaves ⚠️ or 🟡 in place, since part of the measured difference has no submitted fix. Generated from [fixes.json](../decisions/fixes.json); refresh PR states with `uv run python scripts/refresh_fixes.py`.

## Open

| PR | Change | Decisions |
| --- | --- | --- |
| [Alloy EVM #411](https://github.com/alloy-rs/evm/pull/411) | Preserve fatal system call error sources | [H06](../reports/decisions/H06.md) (partial) |
| [Besu #10953](https://github.com/besu-eth/besu/pull/10953) | Replay block pre-execution before tracing transactions | [H27](../reports/decisions/H27.md), [H28](../reports/decisions/H28.md) |
| [Besu #11286](https://github.com/besu-eth/besu/pull/11286) | Include MCOPY memory updates in vmTrace | [H20](../reports/decisions/H20.md) (partial) |
| [Besu #11345](https://github.com/besu-eth/besu/pull/11345) | Keep Parity trace failures local to their call frame | [H24](../reports/decisions/H24.md) |
| [Besu #11346](https://github.com/besu-eth/besu/pull/11346) | Retain precompile output in Parity call frames | [H22](../reports/decisions/H22.md) |
| [Besu #11347](https://github.com/besu-eth/besu/pull/11347) | Retain root precompile halt reasons | [H09](../reports/decisions/H09.md) (partial) |
| [Besu #11350](https://github.com/besu-eth/besu/pull/11350) | Avoid attributing parent return memory to calls | [H20](../reports/decisions/H20.md) (partial) |
| [Besu #11352](https://github.com/besu-eth/besu/pull/11352) | Retain VM frame positions across omitted opcodes | [H20](../reports/decisions/H20.md) (partial) |
| [Besu #11353](https://github.com/besu-eth/besu/pull/11353) | Omit root out-of-gas execution effects | [H20](../reports/decisions/H20.md) (partial) |
| [Besu #11360](https://github.com/besu-eth/besu/pull/11360) | Retain nonzero-value precompile trace frames | [H29](../reports/decisions/H29.md) |
| [Besu #11362](https://github.com/besu-eth/besu/pull/11362) | Report empty code for self-destructing creations | [H10](../reports/decisions/H10.md) (partial) |
| [Besu #11365](https://github.com/besu-eth/besu/pull/11365) | Start each trace_callMany call at a transaction boundary | [H16](../reports/decisions/H16.md) (partial) |
| [Erigon #24255](https://github.com/erigontech/erigon/pull/24255) | Default trace_filter address lists to intersection | [H03](../reports/decisions/H03.md) |
| [Erigon #24290](https://github.com/erigontech/erigon/pull/24290) | Read trace_call calldata from `input` | — |
| [Erigon #24291](https://github.com/erigontech/erigon/pull/24291) | No vmTrace sub for SELFDESTRUCT or for calls that fail their precheck | [H20](../reports/decisions/H20.md) (partial) |
| [execution-apis #895](https://github.com/ethereum/execution-apis/pull/895) (draft) | Parity trace methods and output schemas | — |
| [Geth #35791](https://github.com/ethereum/go-ethereum/pull/35791) (draft) | Add Parity trace RPC namespace; implements the nine Parity trace methods and all three output families; remains a draft while client harmonization and specification work continue | — |
| [Nethermind #13551](https://github.com/NethermindEth/nethermind/pull/13551) | Pair instruction trace completions with starts | — |
| [Nethermind #13622](https://github.com/NethermindEth/nethermind/pull/13622) | Report terminal output for top-level action traces | — |
| [Nethermind #13666](https://github.com/NethermindEth/nethermind/pull/13666) | Preserve error responses for streamed traces | [H15](../reports/decisions/H15.md) (partial), [H25](../reports/decisions/H25.md) |
| [Nethermind #13779](https://github.com/NethermindEth/nethermind/pull/13779) | Report vmTrace store without stateDiff | [H20](../reports/decisions/H20.md) (partial) |
| [Nethermind #13780](https://github.com/NethermindEth/nethermind/pull/13780) | Serialize vmTrace store key and value as quantities | [H21](../reports/decisions/H21.md) |
| [Nethermind #13781](https://github.com/NethermindEth/nethermind/pull/13781) | Report DUPn vmTrace push as n + 1 words | [H20](../reports/decisions/H20.md) (partial) |
| [Nethermind #13782](https://github.com/NethermindEth/nethermind/pull/13782) | Include forwarded gas in streamed vmTrace create cost | [H20](../reports/decisions/H20.md) (partial) |
| [Nethermind #13783](https://github.com/NethermindEth/nethermind/pull/13783) | Return no traces for the genesis block in trace_block | [H05](../reports/decisions/H05.md) (partial) |
| [Reth #27213](https://github.com/paradigmxyz/reth/pull/27213) | Populate VM bytecode in block replay traces | [H19](../reports/decisions/H19.md) |
| [Reth #27217](https://github.com/paradigmxyz/reth/pull/27217) | Correct Otterscan block and transaction responses | — |
| [Reth #27378](https://github.com/paradigmxyz/reth/pull/27378) | Preserve pruned history errors through execution wrappers | [H06](../reports/decisions/H06.md) (partial) |
| [revm-inspectors #528](https://github.com/paradigmxyz/revm-inspectors/pull/528) | Report vmTrace store from SSTORE operands | [H20](../reports/decisions/H20.md) (partial) |
| [Silkworm #2885](https://github.com/erigontech/silkworm/pull/2885) (draft) | Capture missing vmTrace opcode effects | [H20](../reports/decisions/H20.md) |

## Merged

| PR | Change | Decisions | Merged (UTC) |
| --- | --- | --- | --- |
| [Alloy #4216](https://github.com/alloy-rs/alloy/pull/4216) | Default address filters to intersection | [H03](../reports/decisions/H03.md) | 2026-09-22 |
| [Alloy #4218](https://github.com/alloy-rs/alloy/pull/4218) | Serialize absent transaction fields as null | [H05](../reports/decisions/H05.md) | 2026-09-22 |
| [Erigon #23952](https://github.com/erigontech/erigon/pull/23952) | Include MCOPY memory writes in vmTrace | [H20](../reports/decisions/H20.md) (partial) | 2026-09-14 |
| [Erigon #24056](https://github.com/erigontech/erigon/pull/24056) | Read account state at the end of the requested block | [H28](../reports/decisions/H28.md) | 2026-09-18 |
| [Nethermind #13667](https://github.com/NethermindEth/nethermind/pull/13667) | Accept empty Parity trace selections | [H08](../reports/decisions/H08.md) (partial), [H11](../reports/decisions/H11.md) | 2026-09-24 |
| [Nethermind #13668](https://github.com/NethermindEth/nethermind/pull/13668) | Serialize deleted account fields with deletion markers; verified in development build 9d6e8b8d | [H17](../reports/decisions/H17.md), [H26](../reports/decisions/H26.md) | 2026-09-24 |
| [Nethermind #13676](https://github.com/NethermindEth/nethermind/pull/13676) | Preserve trace_get errors and bound positions | [H06](../reports/decisions/H06.md) (partial) | 2026-09-24 |
| [Nethermind #13677](https://github.com/NethermindEth/nethermind/pull/13677) | Reject trace filters with unavailable history | [H06](../reports/decisions/H06.md) (partial) | 2026-09-24 |
| [Nethermind #13750](https://github.com/NethermindEth/nethermind/pull/13750) | Serialize Parity VM stack values as quantities | [H21](../reports/decisions/H21.md) | 2026-09-24 |
| [Reth #27364](https://github.com/paradigmxyz/reth/pull/27364) | Return null for missing transaction replays | [H06](../reports/decisions/H06.md) (partial) | 2026-09-22 |
| [Reth #27365](https://github.com/paradigmxyz/reth/pull/27365) | Include transaction hash in individual replays | [H07](../reports/decisions/H07.md) | 2026-09-22 |
| [Reth #27366](https://github.com/paradigmxyz/reth/pull/27366) | Select trace_get results by tree path | [H02](../reports/decisions/H02.md) | 2026-09-22 |
| [Reth #27367](https://github.com/paradigmxyz/reth/pull/27367) | Classify pruned changeset errors as unavailable history | [H06](../reports/decisions/H06.md) (partial) | 2026-09-22 |
| [Reth #27423](https://github.com/paradigmxyz/reth/pull/27423) | Omit genesis block reward traces | [H05](../reports/decisions/H05.md) | 2026-09-24 |
| [revm-inspectors #504](https://github.com/paradigmxyz/revm-inspectors/pull/504) | Record complete Parity VM execution deltas | [H20](../reports/decisions/H20.md) (partial) | 2026-09-14 |
| [revm-inspectors #509](https://github.com/paradigmxyz/revm-inspectors/pull/509) | Report EIP-7702 code changes in state diffs | [H18](../reports/decisions/H18.md) | 2026-09-15 |
| [revm-inspectors #510](https://github.com/paradigmxyz/revm-inspectors/pull/510) | Report selfdestructed account deletions | [H26](../reports/decisions/H26.md) | 2026-09-15 |
| [revm-inspectors #511](https://github.com/paradigmxyz/revm-inspectors/pull/511) | Record executed bytecode in VM traces | [H19](../reports/decisions/H19.md) | 2026-09-22 |
| [revm-inspectors #526](https://github.com/paradigmxyz/revm-inspectors/pull/526) | Preserve account existence in state diffs | [H17](../reports/decisions/H17.md) | 2026-09-24 |
| [rpc-tests #604](https://github.com/erigontech/rpc-tests/pull/604) | Make trace filter union fixtures explicit | [H03](../reports/decisions/H03.md) | 2026-09-23 |

## Closed

| PR | Change | Decisions |
| --- | --- | --- |
| [Nethermind #13665](https://github.com/NethermindEth/nethermind/pull/13665) | Retain output in state-only Parity traces | [H08](../reports/decisions/H08.md) |
