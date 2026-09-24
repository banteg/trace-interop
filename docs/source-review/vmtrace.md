# vmTrace review: H19, H20, H21, nested `sub`

Scope: the `vmTrace` output family. Sources checked: Parity 55c90d4 (ethcore/evm interpreter, ethcore/trace executive_tracer,
machine/executive, rpc types), Erigon main 3b4861d1 (`rpc/jsonrpc/trace_adhoc.go`, `execution/vm/evm.go`), Nethermind master
ac02224f (`Nethermind.Blockchain/Tracing/ParityStyle/*`, `Nethermind.Evm/*`), Besu main 07f0a4b2 (`VmTraceGenerator.java`,
`AbstractDebugOperationTracer.java`), revm-inspectors 0.43.0 (the version Reth locks, from ~/.cargo/registry) and revm-inspectors main
aac3544 (unreleased after 0.43.0), revm-context(-interface) 43.0.x, the Geth draft fork fa8ecb92 (`eth/tracers/trace_capture.go`),
the pinned spec b979aefe (src/schemas/trace.yaml `TraceVm`, lines 535-613), and harness `vm_model.py`, `coverage.py`, `rules.py`,
`execution_models.py`. Evidence: `evidence/2026-09-24/h15-call-compat` (the active report set). Other evidence was used only where it adds builds.

Reproduce trace dumps with `uv run python scripts/compare_responses.py show <run dir> <case> --family vmTrace`.

---

## 0. What Parity actually did (baseline, verified in source)

| Field | Parity semantics | Source |
|---|---|---|
| `pc` | Byte offset of the opcode (`reader.position - 1`) | interpreter/mod.rs:355 |
| op recorded? | `trace_prepare_execute` runs only after `verify_instruction` and `requirements()` succeed. Invalid opcode, stack under/overflow and gas-calc overflow produce **no op**. Running past the end of code produces **no synthetic STOP** (mod.rs:430). | mod.rs:336-356, 430-432 |
| `cost` | `requirements.gas_cost`: static + dynamic + memory expansion. For CALL-family and CREATE/CREATE2 (`Request::GasMemProvide`) this **includes the gas made available to the child** (EIP-150 capped). It **excludes the 2300 stipend**, which is added only to the child's gas (mod.rs:606-609). | gasometer.rs:201-257, 289-298 |
| `ex.used` | Remaining gas **after** the op, including unused gas the child returns (`UnusedGas`). The internal name `gas_used` is misleading. | mod.rs:391-399; executive_tracer.rs:257-274 |
| `ex.push` | `stack.peek_top(info.ret)`: the top `ret` words after execution, **deepest first, top last**. `DUPn` has ret=n+1 and `SWAPn` has ret=n+1 (instructions.rs:552-583). A CALL/CREATE pushes 1 item after resume. | mod.rs:396-399; stack.rs:89-92 |
| `ex.mem` | `mem_written` is computed **before** execution from stack operands: MSTORE/**MLOAD** (32), MSTORE8, CALLDATACOPY/CODECOPY/RETURNDATACOPY dest, EXTCODECOPY dest, and the **full CALL-family output window**. A zero-size range gives None (`is_valid_range`, memory.rs:46-49). The tracer then slices the **post-op memory** over that range. So `mem` is a post-operation snapshot of a stack-designated range, not "bytes written". RETURN, REVERT, LOG, KECCAK and CREATE: none. | mod.rs:472-491; executive_tracer.rs:257-266 |
| `ex.store` | SSTORE only, taken from the pre-execution operands `(key, value)`. It is reported whether or not the value changes. Transient storage did not exist yet. | mod.rs:493-501 |
| failing op | If the op fails after prepare (OOG in `verify_gas`, or an exec error such as a static-context write): **op present, `ex: null`** (`trace_failed` pops the pending data and never sets `executed`). An invalid JUMP target is detected **after** `trace_executed`, so that op keeps its `ex`. | mod.rs:357-360, 373-377, 396-415 |
| `sub` | Every CALL/CREATE that traps into a child gets `prepare_subtrace(code)`. That includes **precompiles and empty-code accounts**, which get `{code:"0x", ops:[]}`. CALLs that fail the balance or depth precondition do not trap, so they get no `sub` (mod.rs:633-636). The sub attaches to the op at `parent_step`. The root is always an object, including `{code:"0x",ops:[]}` for an EOA target (executive.rs:963-964). | executive.rs:728-729, 748, 963-964; rpc types trace.rs |
| `code` | The bytes passed to `prepare_subtrace`: initcode for CREATE, `params.code` for calls (the code address's code for DELEGATECALL/CALLCODE). | executive.rs:729, 748 |

Hand check of the gas rule against captured data (replay-tree root, CALL at pc=71: value=1, gas arg 60000, cold target, memory
expanding 1→9 words). cost = 2600 + 9000 + 24 + 60000 = **71624**. The child starts with 62300 = 60000 + 2300 (first child op: used 62298 + cost 2).
The parent's `used` after the call is 578967 − 71624 + 62228 (child leftover) = **569571**. Erigon, Nethermind and the Geth draft all emit exactly that.

---

## A. Disagreements with the current recommendation / draft

### A1. H20 `mem` narrowing (MLOAD and CALL window) departs from Parity and from every established client. Severity: would change the spec and the verdicts. Confidence: high.

The draft says (trace.yaml:607-610) "mem is null for no byte write, including MLOAD ... CALL output excludes untouched bytes past the
returned data". What each implementation actually emits (source + evidence):

| Op | Parity | Erigon (both) | Nethermind (both) | Besu (both) | Reth 0.43 (shipped) | revm-inspectors main | Geth draft |
|---|---|---|---|---|---|---|---|
| MLOAD | 32-byte post-op snapshot | same (trace_adhoc.go:595, 653-657) | same (Storage.cs:268-272) | same (VmTraceGenerator.java:235) | whole-memory garbage | null | null |
| CALL out window, short return | full window | full window (trace_adhoc.go:620-626) | **never emits CALL mem** (observed null, pc=71) | returned bytes, or a **fabricated** value (see C4) | garbage | returned bytes (mod.rs:607) | returned bytes (trace_capture.go:351) |
| CALL with empty return | window snapshot | window | null | fabricated or null | garbage | null | null |
| CALLDATACOPY/CODECOPY/RETURNDATACOPY/EXTCODECOPY | dest range, zero padded | same | same | same | garbage | same | same |
| MCOPY (post-Parity) | n/a | dest (dev e26d9bd4; 3.6.1 misses it) | dest (Storage.cs:326-329; last report wins) | **missing** (known) | garbage | dest | dest |
| zero length | null | null | null | null | `{off,data:"0x"}` | null | null |

- For MLOAD the draft departs from Parity and from **all three** established implementations. Only our own Geth fork and unreleased revm main
  follow the draft. On the dedicated model cases, the MLOAD policy is the **only** H20 disagreement for Erigon e26d9bd4 and Nethermind 641592d2.
  I re-ran `differences()` against the h15-call-compat coverage observations. Erigon dev and Nethermind dev pass return42, mcopy, mcopy-overlap,
  mcopy-zero, empty-runtime and revert exactly. They "differ" only at `step N (MLOAD) mem`. Besu additionally differs on MCOPY.
  So the rendered ⚠️ for these builds is manufactured by the draft's choice, not by a client defect.
- For the CALL window there is **no majority**: Parity and Erigon use the window; the Geth draft, revm main and (partly) Besu use returned bytes; Nethermind emits nothing.
- The narrowing buys nothing that consumers can observe. Parity's value is always the **true post-op contents** of the designated range.
  A consumer that applies `mem` as a write reconstructs memory exactly under either rule. That holds for MLOAD with expansion (zeros are the true
  post-state) and for a short CALL return (the tail keeps its prior bytes). The draft's objection ("a short return must not claim the
  untouched tail") only applies if `mem` is *defined* as "bytes written", which is a definitional choice, not a correctness issue.
  The length of the returned data is already observable through RETURNDATASIZE.
- **Proposal:** define `mem` as "post-operation contents of the memory range designated by the opcode's operands". The ranges are:
  MSTORE/MLOAD [off,32), MSTORE8 [off,1), *COPY/MCOPY destination, and the CALL-family output window. It is null when that range is empty
  or the op has no designated range. This is a single stack-derived rule, needs no return-data dependency, is Parity-exact, and makes Erigon
  fully conformant. It needs changes only in Besu (MCOPY, C4), Nethermind (CALL window), Geth draft, revm main, and Reth.
  If the draft keeps the "written bytes" rule anyway, the ledger should say plainly that it overturns every established client for MLOAD, and the
  rendered "differs" rows should say "policy departure" rather than implying a bug.

### A2. Call/return gas boundary: a concrete majority rule already exists, and it makes nested gas checkable. Severity: would change the spec, Geth draft and Nethermind. Confidence: high.

Observed in replay-tree-vmTrace and call-tree-vmTrace-priced (my check script is in the report log below):

- **CALL-family `cost`** = static + access + value transfer + new account + memory expansion + forwarded gas (63/64 capped). It **excludes the stipend**.
  Agreeing: Parity, Erigon, Nethermind, Geth draft, Reth, revm main. **Besu** adds the stipend on value calls (73924 vs 71624,
  VmTraceGenerator.java:171). For precompiles Besu uses the precompile execution cost instead of forwarded gas (118 vs 60100, :191-192).
- **CREATE/CREATE2 `cost`** = 32000 (+ EIP-3860 initcode words, + CREATE2 hashing) + memory + forwarded gas (all but 1/64).
  Agreeing: Parity (GasMemProvide), Erigon (trace_adhoc.go:391-394), Besu (480269), Reth (466193). **Geth draft (32002) and Nethermind
  (32002) exclude the forwarded gas.** Nethermind's own base tracer intends to include it ("another Parity quirkiness",
  ParityLikeTxTracer.cs:429-432). The streaming tracer used by the RPC never sets `_currentOperation` (StreamingParityLikeTxTracer.cs:285-303),
  so the add is lost (see C3).
- **`used`** on a call/create op = caller gas after the child's unused gas (including unused stipend) is returned. Every client except Reth 0.43 agrees.
- Resulting invariant, which I verified on the evidence. For an op with a non-empty `sub`:
  `used_op = used_prev − cost_op + leftover`, where `leftover` = `used` of the child's last op if that op ended normally
  (STOP, RETURN or REVERT), else 0. With this rule:
  - It holds for every CALL in Erigon, Nethermind and Geth, and for CREATE in Erigon and Besu.
  - It fails for CREATE in Geth draft and Nethermind, and for Besu's value CALL.
  - It fails in Erigon and Nethermind for the STATICCALL whose child failed on SSTORE. Their failed op carries a non-null `ex` (A3),
    so the child's apparent leftover is wrong. Geth passes because its failed op has `ex: null`; Besu passes because it writes used = 0.
- **Proposal:** replace "remain provisional" (trace.yaml:612) with: *"`cost` is the total gas deducted from the caller when the operation starts,
  including gas made available to a child frame and excluding the CALL value stipend. `used` is the caller's gas after any unused child gas is returned."*
  Also add the invariant above to `local_invariants` instead of excluding call/create ops entirely (vm_model.py:232). The Geth draft must add forwarded gas to CREATE cost.

### A3. Failing-op convention: adopt Parity's "op present, `ex: null`, `sub: null`". Severity: would change the spec and verdicts. Confidence: high.

Current behaviour, shown by the SSTORE in the STATICCALL child at pc=14 (replay-tree / call-tree):
- Parity: `ex` null. Geth draft: `ex` null (trace_capture.go:292, 365-377). revm main: `ex` None for halts (parity.rs:367-368).
- Erigon: `ex` kept with `used = gas − cost`. It even reports `store` for the **failed** static write (trace_adhoc.go:687-690; only `Used<0` nulls `ex`, :692).
- Nethermind: the **op is deleted** except for InvalidJumpDestination and NotEnoughBalance (ParityLikeTxTracer.cs:292-299).
- Besu: most halts are dropped (`mustIgnore`, VmTraceGenerator.java:103-114). ILLEGAL_STATE_CHANGE keeps `ex` with cost = all remaining gas and used = 0. OOG gets `ex` null only at depth > 0 (:118-126).
- Reth 0.43: always `ex`, with pre-op gas.

A null `ex` is the only convention that makes the nested-gas invariant (A2) computable without opcode knowledge: a halted child returns 0.
It also avoids claiming writes that did not happen, like Erigon's store. Specify: an op that began execution and halted exceptionally is
present with its pre-execution `cost`, `ex: null`, `sub: null`. Also decide whether ops rejected before execution (undefined opcode, stack
underflow) appear. Parity omits them; that is the simplest rule to match.

### A4. `push` needs explicit arity and order. Severity: would change the spec. Confidence: high.

"replacement stack suffix words" (trace.yaml:607-608) implies Parity's rule but does not state it. State it: "the top `k` stack words after execution,
deepest first, where k is the number of words the opcode leaves in place of its inputs (DUPn: n+1, SWAPn: n+1, CALL/CREATE: 1 after resume)".
Two clients violate this (C1, C6).

### A5. Requested `vmTrace` is never null, and every entered child frame gets a `sub` object. Severity: would change the spec. Confidence: high.

- EOA target with vmTrace requested (`call-transfer-vmTrace`, `replay-transfer-vmTrace`): Besu, Erigon, Nethermind and Reth (all builds) and
  Parity return `{"code":"0x","ops":[]}`. **Only the Geth draft returns `null`**, because its root VM is created lazily on the first opcode
  (trace_capture.go:270-283, 212-213).
- Precompile or empty-code callee: Parity, Erigon, Nethermind and Besu give an empty `sub`. The Geth draft (same lazy creation) and revm main give null.
- The schema allows null (trace.yaml:629-631), and the harness explicitly tolerates it (B2).
- Proposal: "When vmTrace is selected it is an object. An operation that entered a child frame (including precompile, empty-code and
  EIP-7702-to-precompile targets) has `sub` = that frame's trace, `{code:"0x",ops:[]}` if no instruction ran. An operation that did not enter
  a frame (failed balance or depth precondition, halted) has `sub: null`."

### A6. `store` wording. Severity: would change the spec (clarification). Confidence: high.

"store records the storage write" is ambiguous in two cases:
- An SSTORE of the unchanged value: Parity reports it, from operands.
- Transient storage: TSTORE is reported by no client. I verified Erigon's SSTORE-only case, Nethermind's separate `SetOperationTransientStorage`,
  and Besu's SStoreOperation.java:155 as the only `storageWasUpdated`.

Specify: "SSTORE only, operands `(key, value)` as quantities, reported whenever SSTORE completes, even if the value is unchanged. TSTORE and SLOAD never populate `store`." This matters for revm main (C8).

### Checked and agreed with the current stance

- **H19 recommendation:** correct. All clients except Reth use executing bytes, 7702-resolved (e.g. Erigon uses `ResolveCode`, evm.go:371-383).
  The EIP-7702 one-hop and precompile-target controls in "Decision needed" match the EIP.
- **H20 `ex.used` = post-op remaining gas:** correct per mod.rs:391-399.
- **H21 minimal quantities for push and store, integers for pc/cost/used/off, optional op/idx:** matches Parity's rpc types (trace.rs:48-110).
  For `idx`, Erigon numbers from "1-…" in replay and from "…" in trace_call, so the "explicitly defined numbering convention" caveat is needed.
- **PUSH0, BLOBHASH, BLOBBASEFEE, TLOAD:** single-word push in every client (Erigon lists them explicitly, trace_adhoc.go:582-588). No issue.

---

## B. Harness bugs

### B1. The H21 check covers `push` only, so the ledger's "Nethermind 641592d2 ✅" is wrong for `store`. Would change a verdict. Confidence: high.

`rules.py:234-251` and `coverage.py:211-227` validate only `ex.push`. In replay-block-tree, Nethermind (**both builds**, including 641592d2) emits:
- `store.key` as a 32-byte padded word: `"0x0000…0000"`.
- `store.val` as non-minimal bytes: `"0x00"`, `"0x01"`.

Cause: TraceSstore uses `ToBigEndianWord()` for the key (EvmInstructions.Storage.cs:653-660), and the streaming writer uses `skipLeadingZeros: false` (StreamingParityLikeTxTracer.cs:538-546, 640-641).
The schema requires `vmQuantity` for key/val (trace.yaml:589-596). Besu, Erigon and Geth emit `"0x0"`/`"0x1"`.

Fix: extend the H21 walk to `store.key`/`store.val` (quantity), `mem.data` and `code` (even-length lowercase data), and `mem.off` (integer).

### B2. `vmTrace: null` for empty code is accepted as a pass. False negative. Confidence: high.

- `execution_models.py:196`: `... or code=='0x' and vm is None`.
- `coverage.py:213-216, 231-232`: `empty_execution_indexes`.

This hides the Geth draft's `null` against a unanimous `{code:"0x",ops:[]}` from four clients and Parity (A5). Remove the special case once A5 is adopted.

### B3. No assertion ever exercises DUP/SWAP `push`. False negative for real bugs. Confidence: high.

- `vm_model.execute` models DUP/SWAP correctly (vm_model.py:71-78, Parity arity and order), but no model fixture contains DUP or SWAP.
- `local_invariants` checks only PUSH values (vm_model.py:234-240).
- The replay roots that contain DUP (the calltree) are rejected by the model because they contain CALL.

As a result, Nethermind's DUPn arity bug (C1, visible in the captured evidence) and Besu's reversed order (C6) are never detected.

Add a model fixture such as `PUSH1 1 PUSH1 2 PUSH1 3 DUP3 SWAP2 POP POP POP POP PUSH1 0 DUP1 RETURN`, with distinct values so that order is observable.

### B4. `local_invariants` hard-codes the contested MLOAD rule and ignores `sub` placement. Confidence: high.

- vm_model.py:241-243 flags any MLOAD `mem`. If A1 is adopted this becomes a false positive for Erigon, Besu and Nethermind across all H20 cases.
  Whatever the decision, keep the MLOAD check in one policy flag, not in the "local invariants" that are described as mandatory.
- There is no check that `sub` appears only on CALL/CALLCODE/DELEGATECALL/STATICCALL/CREATE/CREATE2, and none that
  `sub.code` matches the callee's code (from the matching `trace` frame action/result). That misses two defects:
  - Erigon's spurious SELFDESTRUCT sub (C7). An empty `code` with empty `ops` passes vm_model.py:214.
  - Reth 0.43's sub shifted onto the precompile CALL (C8). This is only caught incidentally, through mnemonics.

### B5. Gas relation excludes all call/create ops. Confidence: high.

vm_model.py:232 skips every call/create op, so the CREATE-cost split (A2: Geth draft and Nethermind vs Parity, Erigon, Besu, Reth) and Besu's
stipend-in-cost produce no verdict. Adopt the invariant in A2, with leftover taken from the child's last op when it ended normally, else 0.

### B6. Implicit STOP is silently tolerated. Spec gap, not a false verdict today. Confidence: high.

- Erigon, the Geth draft and Reth (every build) emit a synthetic `STOP` at `pc == len(code)` when code runs off its end. Evidence: the DELEGATECALL child in
  call-tree-vmTrace-priced ends with LOG2 at pc=34; those three add `pc=35 STOP`.
- Parity (mod.rs:430-432), Nethermind and Besu do not.
- `local_invariants` accepts both (vm_model.py:222-225), and `execute()` never emits one. Model fixtures all end in RETURN/REVERT, so the split is invisible.
  Any future model fixture that falls off the end would fail three clients on op count.

The spec must pick one. Parity's "no synthetic op" keeps every `pc` inside `code`.

### vm_model.py correctness (validated)

I recomputed by hand and re-ran the model against captured traces:
- mload-existing: 300000 − (21000 + 32000 + 2 + 4·4 + 10·16) = 246822; MSTORE 6; MLOAD 3.
- mload-expansion: MLOAD at 0x40 on empty memory: 3 + 3·3 = 12.
- mcopy-overlap: 3 + 3·1 + expansion 1→2 words (3) = 9; source read before write (memmove).
- CALLDATALOAD/SHR/SUB operand order, JUMP 8 / JUMPI 10 / JUMPDEST 1, GAS pushes post-deduction, intrinsic with EIP-3860 and 7702 25000 per authorization.

Costs, used, push and memory match Geth, Erigon, Nethermind and Besu exactly on every model case except the policy/MCOPY rows above.
The model has no SSTORE, CALL or access-list modelling (it fails closed), so it cannot be wrong on EIP-2200/3529, stipend or 63/64.

Latent issues, none affecting current fixtures:
- (a) SLOAD warmth ignores the tx access list (`_warm_slots` starts empty, vm_model.py:103). I checked that no fixture tx with an access list targets the modelled revert contract 0x…d3.
- (b) No synthetic STOP (B6).
- (c) `execution_code`/`prestate` apply every authorization without validity checks (execution_models.py:92-104). Fine for the current valid-auth fixtures; this belongs to H18.

---

## C. Missed issues (real client divergences not covered)

- **C1. Nethermind DUPn pushes n words instead of n+1.** High confidence, observed; would change a verdict once tested.
  `EvmStack.Dup` calls `Trace(depth)` **before** `head++` and before the copy (EvmStack.cs:2090-2098). It reports the pre-op top n words and omits the new top.
  Evidence (replay-tree, both builds):
  - DUP1 → `["0x0"]` (Parity, Erigon, Geth and Reth: `["0x0","0x0"]`).
  - DUP3 → 3 items instead of 4.
  SWAP is correct (the trace runs after the swap).
- **C2. Nethermind `ex.store` appears only when `stateDiff` is also selected.** High confidence, observed.
  - The RPC wraps tracers in `CancellationTxTracer` (TraceRpcModule.cs:176, 484, 538, 660, 671). That wrapper forwards the VM `ReportStorageChange(key,value)` only if `IsTracingStorage` (CancellationTxTracer.cs:328-334).
  - ParityLikeTxTracer sets `IsTracingStorage` only for StateDiff (ParityLikeTxTracer.cs:49-53).
  - Evidence: replay-tree-vmTrace (`["vmTrace"]`) has **zero** stores for both Nethermind builds. replay-block-tree (`[trace,stateDiff,vmTrace]`) has 3.

  vmTrace content must not depend on other selections. This also fits the "trace type independence" theme of H08.
- **C3. Nethermind CREATE `cost` omits forwarded gas (32002) on the RPC path.** High confidence on the observation, medium on the cause.
  The base tracer adds it (ParityLikeTxTracer.cs:429-432). The streaming tracer handles StartOperation itself and never sets the private
  `_currentOperation` (StreamingParityLikeTxTracer.cs:285-303), so the add is skipped.
- **C4. Besu fabricates CALL/DELEGATECALL `mem` from the calling frame's final RETURN.** High confidence, observed.
  `findReturnInCall` scans forward for a RETURN **at the caller's depth** and sets `mem = {data: that RETURN's output, off: 0}` (VmTraceGenerator.java:145-149, 314-324).
  In call-tree-vmTrace-priced, the reverted CALL at pc=112, the DELEGATECALL at pc=219 and the identity CALL at pc=308 all carry `{"0xffee", off 0}`.
  That is the root transaction's own return value, not anything those calls wrote.
- **C5. Besu gas at boundaries** (see A2): the value-CALL cost includes the stipend; a precompile CALL cost excludes forwarded gas; a failed op gets cost = all remaining gas and used = 0.
- **C6. Besu multi-word `push` order is top-first (reversed).** Medium-high confidence, from source only; no captured case has a non-palindromic DUP/SWAP.
  `captureStack` builds the array bottom→top (AbstractDebugOperationTracer.java:127-130). `generateTracingPush` then emits `stack[len-1-i]` for i=0.. (VmTraceGenerator.java:252-262).
  This affects DUPn (n≥3) and every SWAPn.
- **C7. Erigon extra `sub`s.** High confidence for SELFDESTRUCT (observed), medium for the balance/depth case (source only).
  - SELFDESTRUCT receives `{code:"0x",ops:[]}` because `captureStartOrEnter` attaches a sub for every OnEnter, including the SELFDESTRUCT pseudo-call (trace_adhoc.go:381-386). Observed at CREATE child pc=13.
  - CALLs that fail the depth or balance precondition also get a sub, because `captureBegin` runs before those checks (evm.go:383 vs 392-407).
  - Parity, Nethermind (ParityLikeTxTracer.cs:198, `action.Type != "suicide"`) and Geth give no sub in either case.
  - Also in Erigon: the failed static SSTORE carries `store` (A3).
- **C8. Reth / revm-inspectors.**
  - **0.43.0 (shipped):**
    - `store` is **always null**, because `from_parity_config` never enables state-diff recording (0.43.0 config.rs:174-182). Observed: zero stores in every Reth capture.
    - When a precompile call is excluded from the node list, later children shift. In replay-tree, the CREATE's child ops (JUMPDEST…SELFDESTRUCT) sit under the identity CALL at pc=308, and the CREATE has no `sub`.
    - Also: `used` is pre-op gas (parity.rs:391), and `mem` is `{off: memory.len(), data: whole memory}` (:385-388).
  - **main (unreleased)** fixes these, but introduces two new store bugs:
    - (i) A **cold SLOAD reports `store`**. `fill_step_on_step_end` records `storage_change` for SLOAD on `StorageWarmed` (mod.rs:662-690), and `make_instruction` maps any `storage_change` into `store` without checking the reason (parity.rs:361-364).
    - (ii) A **warm SSTORE of the unchanged value reports `store: null`**. revm journals only when `present != new` (revm-context-interface 43.0.2 account.rs:259-268), so the journal length does not change.

    Both need a vmTrace SSTORE fixture (warm no-op write, cold read), which the corpus lacks.
- **C9.** The implicit-STOP split (B6) and the precompile/EOA `sub` split (A5) are live 3-vs-3 or 4-vs-2 divergences with no spec text.

---

## D. Ledger or rendered claims that are wrong against current source or evidence

- **D1.** The H21 rows for Nethermind 641592d2 ("✅ Checked cases agree", "emits minimal quantities") ignore `store`. That build emits a padded key and `"0x00"`/`"0x01"` values (B1).
- **D2.** The H20 page says Erigon "3.6.1 · 0c4d9c91 ⚠️ / 3.8.0-dev · e26d9bd4 ⚠️: The `MCOPY` step omits its memory write".
  This is true only for 3.6.1. e26d9bd4 reports MCOPY at off 32 (a/call-mcopy, marked ✅ on that case page) and at off 1 in model-mcopy-overlap.
  Current source handles MCOPY (trace_adhoc.go:595, 663-666). The dev build's remaining H20 "differs" rows are the MLOAD policy (A1).
  The H20 background sentence that "Erigon VM tracer should classify MCOPY's destination" is stale.
- **D3.** The H20 background says Parity's region "included MLOAD and the entire requested CALL output window. Those were post-step snapshots, not exclusively writes."
  That is accurate. But the ledger never records that Erigon, Nethermind and Besu **all still do this for MLOAD**, which is the key compatibility fact for A1.

---

## Report log (how the evidence was obtained)

- Dumps: `uv run python scripts/compare_responses.py show evidence/2026-09-24/h15-call-compat/<corpus> <case> --family vmTrace [--builds ...]`.
  Cases used: initial/replay-tree-vmTrace, call-tree-vmTrace-priced, replay-block-tree, call-transfer-vmTrace, replay-transfer-vmTrace;
  coverage/model-*; a/call-mcopy; a/auth-set.
- Nested-gas invariant check: inline script (A2). The result per client was:
  - Erigon: all CALLs and CREATE ok, except the STATICCALL whose child failed (non-null failed `ex`).
  - Geth: all CALLs ok, CREATE fails.
  - Nethermind: CALLs ok except the failed-child STATICCALL, CREATE fails.
  - Besu: CREATE ok, value CALL fails.
  - Reth 0.43: every call fails.
- The model re-run against coverage evidence used `.venv/bin/python` with `vm_model.execute`/`differences`.
