# Besu VM trace fixes

Two Besu patches address incorrect `vmTrace` output reproduced through the real EVM
and HTTP service. Neither requires choosing between competing API contracts.

| Pull request | What goes wrong | Least surprising behavior |
| --- | --- | --- |
| [#11352: keep frame bookkeeping aligned when an opcode is omitted](https://github.com/besu-eth/besu/pull/11352) | A child that immediately executes `INVALID` absorbs its parent's subsequent instructions and loses its own bytecode. Separately, after enough failed calls in a loop, CALL gas is taken from an earlier iteration. | Parent instructions stay in the parent trace, child bytecode is retained, and each CALL uses its own resumption frame. |
| [#11353: suppress execution effects for root out-of-gas steps](https://github.com/besu-eth/besu/pull/11353) | With six execution gas, `PUSH1 1; PUSH1 2; ADD` reports a successful ADD push and **−3 remaining gas**, despite an out-of-gas error. | Use `ex: null`, as Besu already does for nested out-of-gas steps. |

## Why these are bugs

**Frame ownership and gas:** the parent successfully returns 42 after a failed CREATE,
but its RETURN is missing from the root VM trace and appears under the failed child.
A separate 64-call loop first misreports resumption gas on call 17: **918,572 instead
of 916,823**. Both arise because bookkeeping advances only for operations emitted in
`vmTrace`, even though call-resumption lookup walks the complete raw frame list.
Synthetic frames still need their existing depth treatment; they do not necessarily
have a corresponding child VM trace.

**Child bytecode:** an immediately failing `INVALID` or stack-underflowing `POP` reports
`code: "0xfe"` or `"0x50"` at the root, but `"0x"` as a child. Capturing bytecode when
opening the child subtrace retains the executed program even when its first opcode
is omitted. The root and child checks exercise the same bytecode through the real EVM.

The patch preserves Besu's existing choice to omit certain halted opcodes. Whether to
include those opcodes is a separate question. It also leaves precompile inclusion and
CALL gas-cost conventions alone.

**Root out of gas:** the execution already reports failure. A negative remaining-gas
value and a successful stack result cannot describe that failed step. Removing the
root-only exception makes the existing nested-frame behavior consistent at depth zero;
no new error wording or result format is needed.

Both fixes are in
[`VmTraceGenerator`](https://github.com/besu-eth/besu/blob/caab45ca02a3edf38d85a1d11842c8cc77e0d2b1/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/results/tracing/vm/VmTraceGenerator.java#L87).

## Validation

Both PRs target upstream `caab45ca` independently, without the earlier CALL-memory fix.
For #11352, the INVALID, stack-underflow and repeated-call regressions all fail before
its fix. The expanded child-halt tests also fail on missing bytecode before the
bytecode follow-up; afterward, 812 trace HTTP tests and 400 debug-trace HTTP tests pass.
For #11353, the out-of-gas regression fails before its fix while the sufficient-gas
control passes; afterward, 811 trace HTTP tests and 400 debug-trace HTTP tests pass.
The existing Forest trace suite remains skipped. No existing response fixtures changed.

[Reproducers and evidence](../evidence/2026-09-22/besu-next-fixes/README.md) include the
minimal bytecode and failing responses. Both PRs include formatted native tests and
changelog entries. Cross-client matrix verification remains outstanding.

## Existing work to validate

Avoid duplicating these upstream patches:

| Client | Existing patch | Useful follow-through |
| --- | --- | --- |
| Besu | [#10953: block pre-execution before tracing](https://github.com/besu-eth/besu/pull/10953) | Run our fork-context and system-contract cases against the patch. |
| Nethermind | [#13551: pair instruction completions with starts](https://github.com/NethermindEth/nethermind/pull/13551) | Retest VM traces around CALL/CREATE failure and resumption. |
| Nethermind | [#13622: terminal output for top-level action traces](https://github.com/NethermindEth/nethermind/pull/13622) | Retest direct and nested precompile output, returns and reverts. |
| Reth / revm-inspectors | [#511: executed bytecode](https://github.com/paradigmxyz/revm-inspectors/pull/511) | Retest constructor and delegated-code cases after dependency uptake. |

These checks could supply useful review evidence without another competing implementation.
