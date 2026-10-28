# Amsterdam gas in trace_* output (2026-10-28)

How each client reports gas in Parity `trace_*` output when execution follows EIP-8037
(two-dimensional gas), and a proposed rule for the trace specification. The specification
currently leaves Amsterdam gas accounting unspecified. Gary Rong asked on
[go-ethereum#35791](https://github.com/ethereum/go-ethereum/pull/35791) that the Geth
implementation support EIP-8037 from the start, building on his tracer model in
[go-ethereum#35970](https://github.com/ethereum/go-ethereum/pull/35970). This capture picks the
rule from what the clients emit, read against the EIP and #35970.

- [Source notes](source-notes.md): the EIP-8037 quantities, #35970's hooks and tracers, and where
  each client computes every number below.
- [`capture/`](capture): the Hive run (820 responses, all five builds eligible).
- [`corpus.json`](corpus.json), built by [`build_corpus.py`](build_corpus.py);
  [`analyze.py`](analyze.py) tabulates frames, vmTrace ops and native tracers;
  [`conservation.py`](conservation.py) checks the vmTrace gas law.

## Builds

| Build | Version | Source |
|---|---|---|
| `besu_development` | besu/v26.10-develop-af0dbfa | `hyperledger/besu:develop`, 2026-10-28 |
| `erigon_development` | 3.9.0-dev-8a5bf399 | `erigontech/erigon:main-latest`, 2026-10-28 |
| `nethermind_development` | 2.3.0-preview+4848636c | `nethermindeth/nethermind:master`, 2026-10-28 |
| `reth_development` | Reth 2.8.1+f1cc50e4 | `ghcr.io/paradigmxyz/reth:nightly`, 2026-10-28 (evm2, after reth#28098) |
| `go-ethereum_trace` | Geth v1.17.9-unstable-a15b96ff | go-ethereum#35791 as in the 2026-10-23 eval, without #35970 |

All five imported the chain and passed the head controls.

## Method

The chain is the execution-apis rpc-compat chain from `tests/` at 2f8ca205: genesis gas limit
100M, Amsterdam from timestamp 570 (blocks 0x39–0x3c), head 0x3c. Every probe executes on the head
state:

- **Root probes:** a call that touches no state, a value transfer to an address with no account,
  and a call to the chain's storage contract 0x7dcd…27df, which writes a new slot.
- **Initcode programs:** nine programs, each run as the root creation and in a CREATE2 frame under
  a root call to the deployment proxy 0x4e59…956c. They create a slot; create and clear it in one
  frame; create it and have a DELEGATECALL child clear it (the refill lands in another frame);
  have a CALL child create a slot; have that child revert; CREATE a 6-byte runtime; send 1 wei to a
  new account; give a child 50,000 gas for a slot (state charge above its `gas_left`); give a looping
  child 30,000 gas.
- **Two gas limits:** 1,000,000, where the reservoir is 0 and every state charge spills into
  `gas_left`, and 30,000,000, above the 2^24 cap, which seeds a 13.2M reservoir.
- **Two methods:** `trace_call` and `trace_rawTransaction` of the same transaction, signed with
  testgen's key for 0x0c2c…7508.
- **Native tracers:** `debug_traceCall` with callTracer for every factory probe, and the struct
  logger for four of them.
- **Mined:** `trace_replayTransaction`, callTracer and `trace_block` for all 15 Amsterdam
  transactions, with receipts as controls.

The capture ran from a fresh clone at ef5ec006 whose only change was one `CHAINS` entry mapping
the corpus to the copied chain, so the manifest records `source_dirty: true`. To reproduce on
Linux, copy `build_corpus.py`'s chain and corpus outputs into `fixtures/`, add
`'amsterdam-gas': 'amsterdam'` to `CHAINS` in `trace_interop/cli.py`, and run
`uv run trace-interop run --lock <lock> --corpus amsterdam-gas --output <dir>`.

## What the clients emit

Numbers are decimal. "Low" is the 1M limit, "high" the 30M limit, both from `trace_rawTransaction`.

### Frame `action.gas`

All five agree: it is the execution gas (`gas_left`) the frame starts with. The reservoir is not
included.

- Root: `min(tx.gas, 2^24) − intrinsic`, less any pre-execution state charge drawn from `gas_left`.
  For example, a 1M value transfer to a new account has 795,400 = 1,000,000 − 21,000 − 183,600.
- Nested frames: the 63/64-capped forwarded `gas_left`.

There are two exceptions:

- **trace_call skips the cap.** Erigon (since erigon#24520) and the Geth draft run trace_call
  without the 2^24 split, so the whole limit is execution gas and the reservoir is 0. A 30M plain
  call has root `action.gas` 29,985,000 there, against 16,762,216 in Besu, Nethermind and Reth and
  in every client's `trace_rawTransaction`.
- **Besu overstates nested CREATE `action.gas`.** It computes `(remaining − cost) × 63/64` without
  the 183,600 account charge, so with an empty reservoir the frame shows 957,472 where the child
  received 776,740.

### Frame `result.gasUsed`

The clients split two ways.

- **Erigon** reports the frame's **execution gas** only, and adds `result.stateGasUsed`: the
  signed net state gas of the frame and its descendants.
- **Besu, Nethermind, Reth and the Geth draft** report the **drop in `gas_left`**. That includes
  whatever state gas spilled into `gas_left`, so the value depends on the reservoir.

| Probe | Frame | Erigon gasUsed / stateGasUsed | Others, low | Others, high |
|---|---|---|---|---|
| root call writes a slot | root | 25,776 / 97,920 | 123,696 | 25,776 |
| CALL child writes a slot | [0,1] | 12,106 / 97,920 | 110,026 | 12,106 |
| same, its CREATE2 parent | [0] | 24,273 / 290,700 | 314,973 | 24,273 |
| same, root | root | 36,382 / 474,300 | 510,682 | 36,382 |
| DELEGATECALL child clears the parent's slot | [0,1] | 106 / −97,920 | 106 | 106 |
| child given 50,000 gas writes a slot (high) | [0,1] | 12,106 / 97,920 | out of gas (low) | 12,106 |

Across the 48 successful frames of the signed probes:

- In Erigon, the same execution reports the same `gasUsed` and `stateGasUsed` at both limits. The
  exceptions are the three frames of oog-state-child, whose outcome changes: with 1M gas the child
  runs out of gas, and with 30M the reservoir pays for its slot.
- The four `gas_left` clients change `gasUsed` in 40 of the 48 frames.

At the root, `intrinsic + pre-execution charges + gasUsed + stateGasUsed` equals the receipt's gas
before refunds. For mined block 0x39 transaction 0 that is 23,740 + 101,576 + 783,360 = 908,676.

Smaller frame differences:

- **Erigon** emits `stateGasReservoir` on create actions only, as a hex quantity, and
  `stateGasUsed` as signed hex (`"-0x17e80"`), `"0x0"` for a reverted frame.
- **Nethermind** reports a reverted child's `gasUsed` before the rollback returns its spill: 110,032
  where the others report 12,112.
- **Besu** reports a nested CREATE's code deposit at the pre-Amsterdam 200 gas per byte: 1,218
  where the others report 24 for a 6-byte runtime. Its CREATE `gasUsed` also carries the
  overstated `action.gas`.
- **Failed pre-execution charges.** A mined creation whose 183,600 account charge exceeds its gas
  (blocks 0x39 and 0x3c) is a failed `create` frame with `Out of gas` in Erigon, Nethermind and
  the Geth draft. Reth emits a placeholder zero-address `call` frame with gas 0 and no error. Besu
  reports a successful create with a would-be address and no `gas`. Besu's develop build has no
  `trace_replayTransaction`, so its mined evidence comes from `trace_block`.

### vmTrace `cost` and `ex.used`

| Op | Erigon | Geth draft | Besu | Nethermind | Reth |
|---|---|---|---|---|---|
| SSTORE writes a slot (low): cost | 12,100, `stateGasCost` 97,920 | 12,100 | 12,100 | 110,020 | 110,020 |
| same: ex.used | 682,220 | 682,220 | 780,140 (spill missing) | 682,220 | 682,220 |
| SSTORE clears it (low): cost | 100, `stateGasCost` −97,920 | 100 | 100 | 18446744073709453796 | 0 |
| same: ex.used | 780,034 | 780,034 | 682,114 (refill missing) | 780,034 | 780,034 |
| CALL with 1 wei to a new account (low): cost | 599,212, `stateGasCost` 183,600 | 599,212 | 601,512 (stipend) | 782,812 | 195,600 (net, evm2) |

The split for `cost`:

- **Execution charge only:** Erigon, the Geth draft and Besu. Erigon adds `stateGasCost` (signed,
  omitted when 0) on the op and `ex.stateUsed` (the reservoir after the op, omitted when 0).
- **Drop in `gas_left`:** Nethermind and Reth. That needs a negative value for a refill:
  Nethermind wraps its unsigned cost to 2^64 − 97,820, in its struct logger too, and Reth
  saturates at 0.

`ex.used` is `gas_left` after the op everywhere except Besu, which computes it as the gas before the
op minus `cost`.

[`conservation.py`](conservation.py) checks
`used[i] + stateUsed[i] = used[i−1] + stateUsed[i−1] − cost[i] − stateGasCost[i]`
for ops that enter no frame:

- It holds on all 62,838 Erigon ops.
- The other clients have no state members, so it reduces to the one-dimensional law
  `used[i] = used[i−1] − cost[i]`. That breaks on 52 Geth draft ops, 26 Besu ops, and 4 each in
  Nethermind and Reth, the refills.

Reth main's CALL and CREATE ops report the net drop across the call instead of including the
forwarded gas. This came in with evm2 (reth#28098), not with EIP-8037.

### Native tracers

These are not part of the specification, but they show where the clients are heading.

**callTracer root.** Every client reports root `gas` = `tx.gas` and root `gasUsed` = receipt gas.
Erigon and Nethermind add `regularGasUsed`, `stateGasUsed` and `gasRefund` at the root; Reth adds
`executionGasUsed`, `stateGasUsed` and `gasRefund`. For example, 52,030 + 474,300 = 526,330.

**callTracer children.** Erigon reports execution-gas `gasUsed` and signed `stateGasUsed`. The
other four report the drop in `gas_left`.

**Struct logger.** Erigon and Reth add a signed `stateGasCost`. Reth also adds
`stateGasReservoir` on every step and puts the spill in `gasCost`; Erigon leaves the spill out.

**#35970's callTracer** reports execution-dimension `gas`, `gasUsed = gas − gasLeft.Execution`
(the drop in `gas_left`) and `stateGasReservoir` on every frame.

## Proposed rule

From Amsterdam, gas has an execution dimension (`gas_left`) and a state dimension (the reservoir,
plus the state charges that spill into `gas_left`). Trace output reports each dimension
separately, and no value depends on which pool paid a state charge.

**Call frames**

- `action.gas` is the execution gas the frame starts with.
  - Root: the transaction gas minus intrinsic gas, capped at EIP-7825's `TX_MAX_GAS_LIMIT` minus
    intrinsic gas, less any pre-execution state charge drawn from `gas_left`.
  - Nested CALL family: the forwarded gas after the 63/64 cap, plus the 2300 stipend for a value
    transfer.
  - Nested CREATE family: all but 1/64 of the caller's remaining `gas_left`, after the account
    charge.
- `action.stateGasReservoir` (new, hex quantity) is the reservoir the frame starts with. It is
  present on every frame from Amsterdam and absent before.
- `result.gasUsed` is the execution gas the frame and its descendants consumed. It excludes state
  gas, whichever pool paid it. CREATE `gasUsed` includes the code deposit's hash cost but not its
  per-byte state cost.
- `result.stateGasUsed` (new, signed hex quantity) is the net state gas the frame and its
  descendants charged: positive for charges, negative when refills exceed them. It is present
  whenever `result` is present from Amsterdam. A reverted frame reports `0x0`, because its state
  changes are rolled back.
- **Root totals:** the root's two members exclude intrinsic gas and pre-execution charges (a
  creation's or value transfer's new account, authorizations). The receipt's gas before refunds
  is intrinsic gas + pre-execution charges + root `gasUsed` + root `stateGasUsed`.
- **Exceptional halt:** the frame still consumes `action.gas` and has `result: null`. The
  reservoir returns to its entry value. A pre-execution charge that fails reports the root frame
  with that charge's `action.gas`, `Out of gas` and `result: null`.
- **trace_call** applies the EIP-8037 split as a transaction would, so `trace_call` and
  `trace_rawTransaction` of the same transaction report the same frames.

**vmTrace**

- `cost` keeps its meaning and covers execution gas only: the execution gas the op charges,
  including gas made available to a child frame.
- `stateGasCost` (new, signed integer, omitted when 0) is the net state gas the op charges or
  refills before any child frame is entered:
  - SSTORE: its slot charge or refill;
  - CALL family: the new-account charge;
  - CREATE family: the account charge.
- `ex.used` stays `gas_left` after the op, now with spills and refills applied.
- `ex.stateUsed` (new, integer, omitted when 0) is the reservoir after the op.
- For an op that enters no frame, `used + stateUsed` falls by exactly `cost + stateGasCost`.

### Why

1. **Gas used describes the execution, not the funding.** Below the 2^24 cap the reservoir is
   empty and every state charge spills into `gas_left`. Above it, the same charges come from the
   reservoir. Reporting the drop in `gas_left` makes one SSTORE cost 123,696 at a 1M limit and
   25,776 at 30M. That happened in 40 of 48 frames for four clients and in none for Erigon. It
   would also make `trace_call` disagree with `trace_rawTransaction` whenever a client skips the
   cap, as Erigon and the Geth draft do.
2. **State usage can be negative.** A DELEGATECALL child that clears a slot its caller created
   has net state gas −97,920 and execution gas 106. A single combined total would be negative, so
   it cannot be the unsigned `gasUsed`. Splitting the dimensions keeps `gasUsed` unsigned and
   bounded by `action.gas`, and gives the sign only to the member that needs it. #35970's changelog
   makes the same point about `OnExitV2`.
3. **Nothing is lost, and receipts reconcile.** The two members sum to all gas the frame consumed
   from both pools, and the root reconciles with the receipt. The drop in `gas_left` cannot be
   decomposed without the pool history.
4. **The protocol already counts the two dimensions separately.** Blocks count execution and
   state gas apart. Erigon, Nethermind and Reth already report the split at the callTracer root,
   and Erigon in every Parity and callTracer frame. The member names follow Erigon, the only
   client that emits Parity state members today.
5. **The halt rule stays true.** "An exceptional halt consumes `action.gas`" still holds in the
   execution dimension. The state dimension is restored, as the EIP specifies.
6. **vmTrace stays self-checking.** The two-dimensional law holds on every Erigon op. The
   one-dimensional `cost` used today needs a negative value for a refill, which comes out as
   2^64 − 97,820 in Nethermind and 0 in Reth.
7. **It matches #35970's quantities.**
   - `action.gas` and `stateGasReservoir` are callTracer's `gas` and `stateGasReservoir`.
   - vmTrace `cost` and `stateGasCost` are `OpCost{Execution, State}`.
   - `ex.used` and `ex.stateUsed` are the next step's `Gas{Execution, State}`.

   The one difference is frame usage. #35970's callTracer `gasUsed` is the drop in `gas_left`;
   this rule needs the frame's net state gas, which Geth's EVM tracks as `UsedStateGas`. The Geth
   implementation would take it from an exit hook that carries it, as Erigon's
   `OnExitV2(MdGasUsage)` does, or accumulate `OpCost.State`, successful children and the code
   deposit in the tracer.

**Alternatives considered:**

- **Drop in `gas_left`, the status quo for four clients.** It matches pre-Amsterdam numbers for
  the usual sub-2^24 transaction, but it depends on the reservoir and cannot be split into the two
  dimensions.
- **One combined total.** It can be negative.
- **`action.gas` including the reservoir.** Every child receives the whole reservoir, so the
  budget would be counted again at each depth, and the 63/64 relation and the halt rule would
  break.

### Main disagreements and what changes

1. **Frame `gasUsed`.** Erigon reports execution gas; Besu, Nethermind, Reth and the Geth draft,
   like #35970's callTracer, report the drop in `gas_left`. Under the rule, Erigon keeps its
   numbers and the other four change whenever state gas is charged.
2. **The trace_call cap.** Erigon (erigon#24520) and the Geth draft skip the 2^24 split;
   Besu, Nethermind and Reth keep it. Under the rule only root `action.gas` and the reservoir
   depend on this, but the two methods should still agree.
3. **vmTrace `cost`.** It is execution only in Erigon, the Geth draft and Besu, and the drop in
   `gas_left` in Nethermind and Reth.
4. **New members.** Only Erigon emits any, and its reservoir appears on create actions only.

Per client:

- **Erigon:** add `stateGasReservoir` to call actions, and apply the split in `trace_call` and
  `trace_callMany`.
- **Reth and Nethermind:** split `gasUsed` and vmTrace `cost`, and add the four members.
  - Nethermind also needs to fix the reverted-child `gasUsed` and the unsigned cost wrap.
  - Reth also needs a proper root frame for a failed pre-execution charge. Its evm2 CALL/CREATE
    `cost` regression is a separate issue.
- **Besu:** fix nested CREATE `action.gas`, code-deposit gas, `ex.used` after state charges and
  failed creation frames, and add the members. It also has two existing gaps: op mnemonics and
  the stipend in CALL `cost`.
- **Geth (#35791):** adopt #35970's hooks and derive per-frame state usage.

### Open points

- **Encoding.** The signed hex quantity for `stateGasUsed` is Erigon's choice
  (`hexutil.Int64`). No other JSON-RPC quantity is signed. A decimal JSON integer, as vmTrace
  uses, is the alternative.
- **Omit-when-zero vs always present.** Hive compares exactly, and both forms are deterministic.
  Erigon omits zero in vmTrace and always emits `stateGasUsed` on frames.
- **A reverted root creation.** It also refills its pre-execution account charge (the EIP's
  baseline sits before it). This capture has no such case; the rule reports `0x0` for the
  reverted frame and leaves the refill outside the trace, like the charge.
- **EIP-7702 authorization charges and `SELFDESTRUCT` to a new account** are not probed here.
