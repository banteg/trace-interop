# Amsterdam gas in trace output: source reading

Read on 2026-10-28; nothing was built from these trees. Each section names the commit read.

## EIP-8037 quantities

From [EIP-8037](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-8037.md) (Last Call, deadline 2026-11-01):

- `gas_left = min(TX_MAX_GAS_LIMIT − intrinsic, tx.gas − intrinsic)` with `TX_MAX_GAS_LIMIT = 2^24`;
  the rest of `tx.gas − intrinsic` is the `state_gas_reservoir`. Below 2^24 the reservoir is 0.
- Execution charges come from `gas_left`. State charges (new slot 64×1530 = 97,920; new account
  120×1530 = 183,600; code deposit L×1530) come from the reservoir first and spill into `gas_left`,
  counted per frame in `state_gas_from_gas_left`.
- Refills (a slot set and cleared in one transaction, a failed CALL/CREATE, a rolled-back frame)
  credit `gas_left` first, up to the frame's outstanding spill, then the reservoir. `gas_left` can
  rise during an SSTORE, and the EIP warns that two `GAS` reads can differ by a negative amount.
- The reservoir passes to a child in full; the 63/64 rule applies to `gas_left` only. A successful
  child returns its spill counter and reservoir; the parent then moves `min(reservoir, spill)` from
  the reservoir back to `gas_left`. A reverted or halted child restores its reservoir to its entry
  value; a halted child's `gas_left` is consumed.
- `tx_gas_used_before_refund = tx.gas − gas_left − state_gas_reservoir`; the block counts
  `evm_state_gas_used` (net state gas) and execution gas separately.
- Pre-frame charges (EIP-2780 runtime charges: a creation transaction's new account, EIP-7702
  authorizations) come out of the pools before the root frame is entered. The creation charge is
  inside the root frame's rollback scope; authorization charges are committed.

## Geth: go-ethereum#35970 (head bdf52bd7, open)

- Hooks `OnEnterV2(gas Gas)`, `OnExitV2(gasLeft Gas)`, `OnOpcodeV2(gas Gas, cost OpCost)` with
  `Gas{Execution, State}` (State is the reservoir) and `OpCost{Execution uint64, State int64}`
  (signed net state charge, CREATE's account charge looked ahead).
- callTracer: `gas = gas.Execution`, `gasUsed = gas − gasLeft.Execution` (clamped at 0), and
  `stateGasReservoir` = entry reservoir on every frame from Amsterdam. Root keeps `gas = tx.gas`.
- Struct logger: `gas`/`gasCost` execution, `stateGasCost` signed and `stateGasReservoir` before
  the step, both omitted when zero.
- The changelog notes `gas.Execution − cost.Execution` is not the next step's gas when a state
  charge spills; the sum of both dimensions is conserved.

## Erigon main (8a5bf399, 2026-10-28)

- `mdgas.MdGasUsage{Execution, State int64, StateSpill}`. At frame end
  `Execution = inputTotal − remainingTotal − State`: execution gas only, spill excluded.
- trace_*: `action.gas` = execution `gas_left` at entry (`rpc/jsonrpc/trace_adhoc.go` L501, L527);
  `result.gasUsed = gasUsed.Execution` (L583, L597-600); `result.stateGasUsed` = signed net state gas
  of the frame and its descendants (trace_types.go L232-277, trace_adhoc.go L603-609), Amsterdam
  only, `"0x0"` when zero, absent with a null result, 0 for a reverted frame. Create actions (not
  calls) carry `stateGasReservoir`. Root excludes pre-frame state charges.
- vmTrace: `cost` = execution charge (forwarded gas included for CALL/CREATE), `stateGasCost`
  signed, omitted when 0; `ex.used` = `gas_left` after the op, spill and refill applied;
  `ex.stateUsed` = reservoir after, omitted when 0 (trace_adhoc.go L143-157, L749-762).
- trace_call and trace_callMany set `SkipExecutionGasCap` (#24520): the whole limit is execution gas
  and the reservoir is 0. Replays and trace_rawTransaction use the real split.
- Introduced in erigon#24240 (part 4 of the V2-hook series for issue #20086); #24370 made the opcode
  state cost signed.
- callTracer: `stateGasReservoir` (omitempty), child `stateGasUsed` signed, root `regularGasUsed`,
  `stateGasUsed`, `gasRefund`. Struct logger: `stateGasCost`, `stateGasReservoir`, root `stateGasUsed`.

## Reth main (f1cc50e4) and v2.8.1

- Reth main dropped revm on 2026-10-23 (reth#28098) for `evm2`/`evm2-inspectors` (DaniPopes fork,
  4a53ec08); v2.8.1 uses revm 43.0.3 and revm-inspectors 0.44.3. The gas model and Parity builder
  match, except when a CALL step closes.
- `GasTracker{remaining, gas_limit, reservoir, state_gas_spent i64, state_gas_spilled, refunded}`.
  Parity `action.gas = gas_limit` (the frame's execution gas), `gasUsed = gas_limit − remaining`:
  spill included, refills credited to `remaining` subtracted, reservoir never included.
- vmTrace `cost` = saturating drop in `remaining` (spill included; a refill gives 0), `used` =
  remaining after. In evm2 the CALL/CREATE step closes after the child returns, so `cost` is the net
  drop across the call; revm-inspectors closes it before the child runs.
- No Parity state-gas members. callTracer root: `executionGasUsed`/`regularGasUsed`,
  `stateGasUsed`, `gasRefund`; no per-frame reservoir. Struct logger: `stateGasCost`,
  `stateGasReservoir` per step, top-level `executionGasUsed`, `stateGasUsed`, `gasRefund`.
- trace_call keeps the 2^24 execution cap under Amsterdam (reth#27633); the excess becomes the reservoir.

## Nethermind master (415be627, 2026-10-28)

- `EthereumGasPolicy{Value, StateReservoir, StateGasUsed, StateGasSpill, ...}`; every tracer hook
  receives `Value` (`gas_left`) only.
- Parity `action.gas` = `gas_left` at entry; `gasUsed = action.gas − gas_left` at exit (spill
  included, reservoir excluded). Root `action.gas` is after spilled pre-frame state charges. CREATE
  `gasUsed` includes the spilled part of the code deposit only.
- vmTrace `cost = gas_left before − gas_left after` as `ulong`: a refill larger than the execution
  cost wraps to about 2^64 (likely bug, `ParityLikeTxTracer.cs` L386-397). `used` = `gas_left` after.
- No Parity state-gas members. callTracer root `regularGasUsed`/`stateGasUsed`/`gasRefund`
  (nethermind#12628) and a `stateGasTracer`; per-step state fields deliberately left out.
- trace_call keeps the 2^24 cap; the excess goes to the reservoir.

## Besu main (af0dbfab, 2026-10-28)

- EIP-8037 implemented: `TxValues.stateGasReservoir` (shared by all frames),
  `MessageFrame.stateGasSpilled`, LIFO refill.
- Flat traces read `getRemainingGas()` (`gas_left`): root `action.gas` = capped `gas_left` after
  pre-frame charges; nested CALL `gasUsed` includes spill and refills. Root `gasUsed` uses the
  refunded remainder, which includes leftover reservoir, so its branch depends on the reservoir.
  Nested CREATE `action.gas` is computed as `(remaining − cost) × 63/64` and leaves out the
  account charge (overstated by up to 183,600 × 63/64); the code deposit is still hardcoded at
  200 gas per byte (`FlatTraceGenerator.java` L362, L608-619).
- vmTrace `cost` = execution charge only (SSTORE's state charge excluded); `ex.used =
  gasRemaining − cost`, which overstates `gas_left` by any spill. CALL/CREATE `ex.used` is read
  after the child returns.
- No state-gas members anywhere. trace_call keeps the 2^24 cap.
