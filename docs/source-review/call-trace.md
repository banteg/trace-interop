# Call-trace review (`trace` output family): H07, H08, H09, H10, H22, H24, H29 and frame fields

Scope: flat frames (`action` / `result` / `error` / `subtraces` / `traceAddress` / `type`) across all methods.
Sources: the pinned draft b979aefe (`src/schemas/trace.yaml`, `docs-api/docs/trace-profile.md`), Parity 55c90d40, Besu 07f0a4b2f8, Erigon 3b4861d1038, Nethermind ac02224f25, revm-inspectors 0.43.0,
revm-handler/inspector 43.0.3, alloy-rpc-types-trace 2.5.0 (cargo registry), go-ethereum `feat/trace` fork fa8ecb92, TrueBlocks
31897a4fa9. Evidence: I read every frame in `evidence/2026-09-24/current-matrix/*/observations.json.gz` and compared
fields for each frame, grouped by (case, envelope, txHash, traceAddress, type), across release builds plus the
geth draft.

Legend: **conf** = confidence; **sev** = severity: spec (would change the spec) / verdict (would change a
verdict) / cosmetic.

---

## Ranked summary

1. **The draft never defines the frame numbers (`action.gas`, `result.gasUsed`, `from`/`to` per callType, `value` for DELEGATECALL/STATICCALL).** All five implementations agree exactly with Parity on every frame in the matrix (1 Besu outlier). Writing the rule down costs nothing. The harness asserts none of these fields except on the REVERT fixtures. (A1: conf high, sev spec)
2. **The draft doesn't say whether CALL/CREATE that fail before execution emit a frame** (depth 1024, insufficient balance, CREATE collision). Clients split 3/3. geth and Erigon change their own behaviour for CREATE at Amsterdam. No fixture covers any of these cases. (A4: conf high on the source reading, sev spec)
3. **H09 failed-frame `result` is better justified than the ledger says, but the two halves need separating.** Erigon and Reth *already* emit `result` on failed frames: an object for REVERT, `null` otherwise. So the draft adopts majority practice, not a new invention. The truly new part is the failed-CREATE shape `{gasUsed, output}`. Reth and Erigon emit `{address, code, gasUsed}` there, with the would-be address, which pollutes `toAddress` filters (alloy `TraceFilterMatcher`). The `null` requirement for exceptional halts adds nothing and could be relaxed. (A2: conf high, sev spec)
4. **The error vocabulary is undefined, and only "Reverted" is universal.** Static-context write has 5 different labels. Precompile failure has 5 labels, 2 of them leaked library error strings that differ between geth and Erigon. Reth falls back to Rust `Debug` names. I propose a concrete canonical table. (A3: conf high, sev spec)
5. **Besu `trace_callMany` bug: net-gas-metering "original value" is not reset between calls.** Calls 2..n get 2×2800 = 5600 less gas on the fixture. None of the harness's assertions checks it. (C1: conf high, sev verdict)
6. **`creationMethod` is unspecified.** Parity, Erigon, Nethermind, Reth and geth emit it on every create. Besu computes it per *transaction*, not per frame. (A5/C2: conf high, sev spec)
7. **Harness: the filter oracles take `result.address` even for failed CREATE frames** (rules.py:267, coverage.py:156). This hides the Reth/Erigon would-be-address filter bug. It is latent because no fixture has a reverted nested CREATE. (B2: conf high, sev verdict when a fixture is added)
8. The draft's `revertReason` field has no defined meaning. Only Besu emits it, and Besu puts raw revert bytes there, while geth-style tracers use the decoded text. (A6: conf high, sev spec/cosmetic)

---

## A. Disagreements and underspecification in the draft/ledger

### A1. Frame numbers are unspecified, even though every client already agrees (conf high, sev spec)

The pinned `TraceCallAction`, `TraceCreateAction`, `TraceCallResult` and `TraceCreateResult` (trace.yaml:124-204) have
no descriptions. `grep -i 'gasUsed|intrinsic|stipend|63/64|refund'` finds nothing about frames in trace.yaml or
trace-profile.md. The one mention, "nested CALL stipend/refund gas accounting", is listed as *open*
(trace-profile.md:116), but it concerns vmTrace.

Parity's semantics:
- Root: `action.gas = tx.gas − intrinsic` (`init_gas`, ethcore/machine/src/executive.rs:858). Root
  `result.gasUsed = gas − gas_left` measured at call completion, *before* refunds and fee finalization
  (executive.rs:982-985; `finalize` applies refunds later, :1133ff). So root gasUsed ≠ receipt gasUsed.
- Nested CALL/CALLCODE with value > 0: `action.gas` = the forwarded gas after the EIP-150 63/64 cap **plus the 2300
  stipend** (interpreter/mod.rs:606-610). gasUsed is measured against that same amount (executive.rs:694-697).
- DELEGATECALL/CALLCODE: `from` = executing address, `to` = code address. CALL/STATICCALL: `from` = sender, `to` = target.
  `value` = `ActionValue::value()`, i.e. the apparent (inherited) value for DELEGATECALL and 0 for STATICCALL
  (ethcore/trace/src/types/trace.rs:225-245).

Evidence: I compared `action.gas` for every frame across Besu, Erigon, geth-draft, Nethermind and Reth. There is
exactly **one** divergence, a Besu CREATE inside callMany (see C1). `result.gasUsed` agrees everywhere except Besu
(C1, H13 raw paths, H27 filter paths). Examples:
- model-revert: root create `gas 0x3c44e` = 300000 − (21000+32000+136+2 initcode words). All five agree, and
  gasUsed 0x12 = 18 is opcode gas only.
- The calltree value call: `gas 0xf35c` = 60000 + 2300 stipend, `gasUsed 0x48`, identical in every client.
- EIP-7702 roots: `gas 0x25990`, identical, and it includes the per-authorization intrinsic.

Recommendation: write these rules into the schema descriptions. They are the de facto standard, and consumers
(TrueBlocks, Dune-style "internal tx" tables) depend on them. State explicitly:
- Root gasUsed excludes intrinsic gas, refunds and the EIP-7623 floor.
- CREATE gasUsed includes the code-deposit charge.
- Exceptional halt consumes `action.gas`.

Then add one assertion: for modelled roots, `action.gas == tx.gas − intrinsic` (vm_model.intrinsic already exists).
The "stipend" open item can then be closed for frames.

### A2. H09 failed-frame `result`: evaluation (conf high, sev spec)

What clients actually do today, counting frames in the evidence:

| client | failed CALL | failed CREATE (REVERT) | non-revert failure |
|---|---|---|---|
| Parity | `error` only (rpc/src/v1/types/trace.rs:528, 599) | `error` only | `error` only |
| Besu | `error` only (230 call / 120 create, no result) | `error` only; root also has `revertReason` | `error` only |
| Nethermind | `error` only (264 / 98) | `error` only | `error` only |
| Erigon | `result:{gasUsed,output}` (trace_adhoc.go:517-526) | `result:{address,code,gasUsed}`, address = would-be address (:412, :524-526) | `result:null` (:528-529) |
| Reth | `result:{gasUsed,output}` (revm-inspectors types.rs:338-349) | `result:{address,code,gasUsed}` (types.rs:351-367) | `result:null` (alloy `TransactionTrace.result` has no skip, parity.rs:575) |
| geth draft | `{gasUsed,output}` | `{gasUsed,output}` | `null` |

Consequences:
- The ledger (H09 background) frames the draft as "a richer contract than Parity's error-only failures". It
  omits that Erigon and Reth, the two most-used trace backends, have shipped `result` on REVERT frames for years.
  alloy deserializes both shapes: `result: Option<TraceOutput>` with `#[serde(default)]`, and a custom
  `TraceOutput` deserializer takes `{gasUsed,output}` as Call and `{address,code,gasUsed}` as Create (parity.rs:487-513).
  TrueBlocks' `Result *TraceResult` (types_trace.go:33) tolerates it as well. The real compatibility cost is
  therefore Besu + Nethermind adding REVERT results, plus Erigon + Reth renaming failed-CREATE `code`→`output` and
  dropping `address`. It is not a departure from "Parity & all clients".
- Failed-CREATE `address` is harmful, not just cosmetic. The alloy/Reth `TraceFilterMatcher::matches`
  (alloy filter.rs:176-183) matches `toAddress` against `result.address` whenever the result is a Create output. So
  on Reth a reverted CREATE matches a filter for an address where no contract exists. TrueBlocks'
  `uniq_appearances.go:115-118` records `Result.Address` as an appearance for any create with a result. The draft
  rule (Failed CREATE → no address/code) is justified. Using `output` rather than `code` for revert bytes is also
  justified: `code` means deployed runtime (H10).
- Requiring `result: null` for exceptional halts buys nothing. `error` already determines failure, and absence
  versus null carries the same information. It forces Besu and Nethermind to change for no consumer benefit. The
  stated rationale ("prevents callers from inferring success from result presence") is not served by an explicit
  null. Proposal: `result` is REQUIRED (object `{gasUsed, output}`) for REVERT; for exceptional halts it MAY be
  absent or null; `gasUsed` of a halted frame is implicitly `action.gas`. "When available" (ledger
  recommendation) is not testable. Replace it with this REVERT-versus-halt split.
- I considered an additive alternative (keep Parity's error-only shape and add a sibling `revertData`). It is
  worse: all four clients would have to add a new field, and Erigon/Reth would carry the data twice. Keep the
  draft's placement.

### A3. Error vocabulary: the "small stable set" is undefined and today's labels are accidental (conf high, sev spec)

Labels observed in the evidence (release builds and the geth draft), with the source of each:

| failure | Parity (error.rs:24-95) | Besu (ExceptionalHaltReason.java:106-130) | Erigon | geth draft | Nethermind (ParityLikeTxTracer.cs:95-107) | Reth (revm-inspectors utils.rs:21-72) |
|---|---|---|---|---|---|---|
| REVERT | Reverted | Reverted | Reverted | Reverted | Reverted | Reverted |
| out of gas | Out of gas | Out of gas | out of gas | out of gas | Out of gas | Out of gas |
| write in static context | Mutable Call In Static Context | Illegal state change | **out of gas: write protection** | **out of gas: write protection** | Static call violation | StateChangeDuringStaticCall |
| precompile failure (bn256 add, bad point) | Built-in failed | Precompile error | **invalid point: subgroup check failed** | **point is not on curve** | Out of gas | Built-in failed |
| opcode not active at fork (MCOPY at 55) | Bad instruction | Bad instruction | invalid opcode: MCOPY | invalid opcode: MCOPY | Bad instruction | **NotActivated** |
| stack overflow | Out of stack | Out of stack | Go error text | Go error text | Stack overflow | Out of stack |
| other (depth, collision, code size, 0xEF...) | n/a or "Out of gas" | description text | Go error text | Go error text | "Error" | Rust `Debug` name (`CallTooDeep`, `CreateCollision`, ...) |

Erigon and geth wrap gas-function errors in `ErrOutOfGas`, hence "out of gas: write protection" (Erigon
gas_table.go:128/214; geth core/vm/gas_table.go:100/187). Erigon and geth even disagree with each other on the
same precompile input. Only "Reverted" is universal. The harness correctly avoids comparing wording. The ledger's
"small stable set" needs an actual list, or H09 cannot close.

Proposal: normative Parity strings where Parity had one:
- Reverted
- Out of gas
- Bad instruction
- Bad jump destination
- Stack underflow
- Out of stack
- Mutable Call In Static Context
- Built-in failed
- Out of bounds

Plus a registered extension list for post-Parity failures:
- contract address collision
- code size limit
- invalid code prefix 0xEF
- nonce overflow
- depth or insufficient balance, but only if A4 retains those frames

Any other value is an extension. Consumers match exactly; human detail can go elsewhere.

### A4. Frames for CALL/CREATE that fail before execution are undefined (conf high, sev spec)

| case | Parity | Besu | Nethermind | Erigon | geth draft | Reth |
|---|---|---|---|---|---|---|
| CALL, depth ≥ 1024 or value > balance | no frame (interpreter/mod.rs:633-637) | no frame (FlatTraceGenerator.java:283-286) | no frame (EvmInstructions.Call.cs:209-240) | frame, error (evm.go:382-408) | frame, error (core/vm/evm.go:270-283) | frame, "CallTooDeep" / "Insufficient balance for transfer" (revm-handler frame.rs:176-192; inspector traits.rs:111-130) |
| CREATE, depth or balance | no frame (mod.rs:550-553) | unverified, see C3 | no frame (Create.cs:128-143) | frame pre-Amsterdam only (instructions.go:1054-1057; not after the Amsterdam precheck :1011) | frame pre-Amsterdam only (evm.go:538-547) | frame (frame.rs:292-304) |
| CREATE address collision | frame, **"Out of gas"** (check_eip684, executive.rs:311-316, called at :506 after prepare_trace_create) | unverified | no frame (Create.cs:195-205) | frame, "contract address collision" | frame, same | frame, "CreateCollision" |

This changes `subtraces`, later siblings' `traceAddress`, `trace_get` paths and `trace_filter` membership. It is
the same class of problem H29 addressed for precompiles, and the draft is silent on it. No fixture covers it. I
grepped the corpora and generators: there are no depth, nested insufficient-balance or collision probes.

Recommendation: follow Parity. A failed precheck creates no message call and forwards no gas, so it emits no
frame. Collision burns the forwarded gas and bumps the nonce, so it keeps a CREATE frame with an error. geth and
Erigon are already moving to "no frame" for CREATE prechecks at Amsterdam, so this is the forward-compatible
choice. Note that geth's callTracer (debug_*) emits these frames. If the group prefers debug_ parity, state that
instead. Either way, add three fixtures: a depth bomb, a nested value CALL beyond balance, and a CREATE2
collision.

**Update (2026-09-26):** H29 now takes the debug_ option. Geth chose to capture a call before its prechecks in
v1.14 after an explicit review debate, Erigon followed in v3.1.0, and the Geth, Erigon, Reth and Besu call tracers
all record the failed attempt; only Nethermind omits it in both APIs. A failed CALL keeps a frame with its error,
no result and no subtraces; a failed CREATE does the same before Amsterdam, where the precheck moves into the
creating opcode. See [H29](../../reports/decisions/H29.md).

### A5. `creationMethod` (conf high, sev spec)

- Parity emitted it (rpc/src/v1/types/trace.rs:217-229), skipping it only when None.
- Erigon (trace_adhoc.go:445), Nethermind (ParityLikeTxTracer.cs:427), Reth (types.rs parity_action) and the geth
  draft emit it on 100% of create frames in the evidence (908/908, 848/848, 1022/1022, 432/432). Besu emits it on
  116/586.
- alloy defaults it (parity.rs:381-384).

The draft's `TraceCreateAction` does not list it. Because additionalProperties is open, nothing is enforced.
Recommend making it REQUIRED with enum {create, create2}: CREATE2 changes address derivation and there is no
other way to tell them apart. H10's "decision needed" can then close.

### A6. `revertReason` (conf high, sev cosmetic→spec)

The draft adds `revertReason: string` to call and create frames (trace.yaml:239, :278) without semantics.

- Only Besu emits it: 140 frames, root only (FlatTraceGenerator.java:84-88), and the value is **raw hex revert
  bytes**, e.g. model-revert `"revertReason":"0x…2a"`.
- geth callTracer and revm-inspectors' geth builder use `revertReason` for the *decoded* Error(string) text
  (types.rs:466, `maybe_revert_reason`).

Once REVERT bytes live in `result.output`, either drop the field or define it as optional decoded Error(string)
text.

### A7. SELFDESTRUCT after Cancun (conf high, sev cosmetic)

All five clients emit a `suicide` frame for a non-deleting post-EIP-6780 SELFDESTRUCT (destroy-trace-56:
`[('call',[]),('suicide',[0], balance 0x64)]`, the same as block 55). The actions agree everywhere they are
emitted. The draft should say that `suicide` records the opcode and the value transferred, not account deletion.
It should also specify `balance` when the beneficiary is self. That case is not covered by any fixture.

Minor: the draft makes `result` optional on suicide and reward frames. Parity always emitted `"result": null`;
Nethermind omits the key. The schema is fine as is.

### A8. Brief checks where I found the stance correct

- **H29** (conf high): the draft rule matches Parity exactly: `depth != 0 && is_builtin && params.value.value()==0`
  (executive_tracer.rs:44), where value() is the apparent value. The builtin check is fork-aware
  (`machine.builtin(addr, block_number)`). Suggestion: state "precompile active at the executing block's fork". A
  zero-value call to 0x0a before Cancun, or to 0x100 before Osaka, must be retained. That is currently untested.
  revm-inspectors mod.rs:289-299 and Erigon trace_adhoc.go:399 use fork-active sets.
- **H22** (conf high): the ledger's Besu claim holds at current source. The root precompile path sets only
  `gasUsed` from `precompiledGasCost` (FlatTraceGenerator.java:114-121), and `handleReturn` never runs, so the
  output is empty.
- **H24** (conf high): the Besu claim holds. `hasRevertInSubCall` scans the whole transaction trace from index 0
  (FlatTraceGenerator.java:549-564) and is used for the root (:103) and nested frames (:308).
- **H10** (conf high): the Besu `output`-for-create claim holds (FlatTraceGenerator.java:351-363; 64 create frames in
  the evidence use `output`).
- **H07 / H08**: no call-trace-specific objection. The H07 check (rules.py:147) and the H08 checks (rules.py:148-155)
  correctly implement the draft.
- **EIP-7702**: every client reports the authority EOA as the root `to`, with identical gas (auth-set, auth-clear,
  auth-replace, auth-set-revert). No client reports the delegate target. Gap: no nested CALL or DELEGATECALL to a
  delegated EOA is tested. For DELEGATECALL, Parity's `to` = code address, and it should be the EOA
  (revm-inspectors mod.rs:661-666 uses `bytecode_address`).

---

## B. Harness bugs

### B1. Frame gas is almost never asserted (conf high, sev verdict)

rules.py and coverage.py check `gasUsed` only on the REVERT fixtures (rules.py:424-433, coverage.py:269-273), and
never check `action.gas`. As a result, several real divergences go unflagged:
- the Besu callMany gas bug (C1);
- Besu's degenerate `gasUsed 0x0` and missing `action.gas` in trace_rawTransaction and trace_filter-across-fork
  frames. H13/H27 flag these indirectly, but no gas assertion does.

Suggestion: a relational check that the same call in callMany entry *k* and in a standalone trace_call on the
matching post-state has identical frame gas, plus the A1 intrinsic check.

### B2. Filter oracles treat a failed CREATE's `result.address` as its recipient (conf high, sev verdict, latent)

- rules.py:267 `if kind=='create': to=mapping(frame.get('result')).get('address')`
- coverage.py:156, same logic

Both ignore `error`. Under the draft ("Failed CREATE … has no successful recipient address", trace-profile.md:84)
the expected set must exclude failed creates. Because the baseline is the client's own block trace, a Reth or
Erigon reverted CREATE, which carries the would-be `address`, would be expected to match `toAddress`. That makes
the check self-consistent with the bug. It stays latent only because no mined fixture has a reverted CREATE. Fix:
use `result.address` only when `'error' not in frame`, and add a mined reverted-CREATE transaction plus a
`toAddress` filter on its would-be address.

### B3. `anchored_reference` turns frame-field errors into silent "unassessed" (conf medium, sev verdict, latent)

oracles.py:70-80 validates calltree `callType`/`from`/`to`/`value`/`init` only as a *precondition*. A client that
reported the wrong `to` for DELEGATECALL, or a nonzero value for STATICCALL, makes the reference `None`. All the
dependent H02/H03/H04/H23/H27 checks then become "unassessed" rather than "change_needed". No direct assertion on
these calltree action fields exists. Today every client passes (no "did not establish" text appears in reports).
Suggestion: emit a failing check naming the mismatched field instead of returning `None`.

### B4. H09 Erigon/Reth verdicts are opaque (conf high, sev cosmetic)

The only H09 failures for Erigon and Reth come from model-revert (coverage.py:271), where revert bytes sit under
`result.code` with an `address`, and from schema shape validation. The client pages say "The linked case differs
from the proposed behavior". They should say: "failed CREATE result must be `{gasUsed, output}` with no
`address`/`code`".

### B5. The H16 accounting fallback ignores refunds (conf medium, sev cosmetic)

execution_models.py:245-251 uses `max(intrinsic + root.gasUsed, floor)` when no receipt exists. This is right
only when there are no refunds, because root gasUsed is pre-refund (A1). No current fixture has SSTORE clears,
so it is harmless. It needs a comment, or `− min(refund, used/5)` once a refund fixture exists.

---

## C. Missed issues (client behaviour not covered)

### C1. Besu trace_callMany does not reset the EIP-2200/3529 "original value" between calls (conf high, sev verdict)

initial/call-many-priced runs the same calltree call twice at 0x30.

| | root gasUsed | child [4] gasUsed | child [6] create gas |
|---|---|---|---|
| Erigon, geth, Nethermind, Reth: call 1 | 0x1fc63 | 0x2cd4 | 0x6d70b |
| Erigon, geth, Nethermind, Reth: call 2 | 0x1fc63 | 0x2cd4 | 0x6d70b |
| Besu: call 1 | 0x1fc63 | 0x2cd4 | 0x6d70b |
| Besu: call 2 | 0x1e683 | 0x16f4 | 0x6ec94 |

Both Besu gasUsed deltas are exactly 5600. The child [4] is a DELEGATECALL into `0x7dcd…df`, whose code is
`sstore(keccak(cd), sload(0)); sstore(0, sload(0)+1)`: two nonzero→nonzero SSTOREs. 5600 = 2 × (2900 − 100),
which means Besu prices both as already-dirty. Its "original" value is still the pre-callMany value, not the
value committed by call 1. Cold/warm carry-over cannot explain it: the root delta is also exactly 5600, and a
carried-over access list would give −4100 or −2500 steps. The create gas delta, 0x1589 = 5600·63/64, is the
knock-on effect.

The same bug would mis-state refunds. Each callMany entry is a separate transaction and must re-snapshot original
storage. No assertion catches this (B1).

### C2. Besu `creationMethod` is computed per transaction (conf high, sev verdict once A5 is adopted)

FlatTraceGenerator.java:651-666 labels *every* create frame "create2" if *any* trace frame in the transaction
executed CREATE2, and it is applied only on some paths (116/586 frames). A transaction with CREATE and CREATE2
mislabels one of them. repeat/call-mixed-create is exactly such a fixture, but Besu omits the field there, so the
mislabel does not show.

### C3. Besu: a CREATE that fails its precheck probably corrupts the flat tree (conf low-medium, sev verdict, needs fixture)

`handleCreateOperation` (FlatTraceGenerator.java:440-470, dispatched at :186-195) pushes a new context on every
non-halting CREATE opcode without checking that the next trace frame is deeper. `handleCall` does check this, at
:283. A CREATE that fails the depth or balance precheck (no child frame, no halt) leaves a dangling context. The
parent's next STOP/RETURN/REVERT would then close the phantom create frame instead of the parent. The A4 fixtures
would expose this.

### C4. Error labels drift even inside one codebase lineage (conf high, sev spec input)

This was covered in A3. Specifically:
- Reth's `format!("{status:?}")` fallback (utils.rs:68) exposes revm enum names, e.g. `NotActivated`,
  `StateChangeDuringStaticCall`, `CallTooDeep`, `CreateCollision`, `OutOfOffset`, `CreateContractSizeLimit`.
  These are unstable across revm versions.
- Erigon (trace_adhoc.go:529) and geth-draft use `err.Error()`, which leaks crypto-library messages.
- Nethermind maps every unknown case to "Error" (ParityLikeTxTracer.cs:106), and reports precompile failure as
  "Out of gas".

### C5. Erigon rewrites large `action.gas` (conf medium, sev cosmetic)

trace_adhoc.go:405-407: `if gas > 500000000 { gas = 500000001 - (0x8000000000000000 - gas) }`. This maps
geth-style "unlimited" (MaxUint64/2) roots to about 500M, an OpenEthereum-compatibility hack. Any explicit
`gas` between 500M and 2^63 under a large or zero `--rpc.gascap` wraps uint64 and reports roughly 9.2e18. The
draft says omitted gas "uses the client execution cap", so the root `action.gas` should be that cap minus
intrinsic. No fixture traces a call with gas omitted and `trace` selected (checked all corpora).

### C6. Coverage gaps worth one fixture each (conf high on absence)

1. Nested depth, nested insufficient balance, and CREATE/CREATE2 collision (A4).
2. SSTORE refund, to pin root gasUsed as pre-refund. Besu computes the root from post-refund remaining gas plus a
   compensation term (FlatTraceGenerator.java:584-605). Every other client is pre-refund by construction.
3. Nested CALL, and DELEGATECALL, to a 7702-delegated EOA (`to` = EOA; executed code = the delegate's).
4. A zero-value call to a precompile address before that precompile activates (retain it) or after (omit it).
5. A post-Cancun SELFDESTRUCT to self (`balance` semantics).
6. A reverted nested CREATE mined in a block, for the H23 filter check and B2.

---

## D. Ledger claims versus current source

- Verified as correct at current checkouts: H22 Besu (FlatTraceGenerator.java:114-121), H24 Besu (:549-564, used
  at :103 and :308), H29 Besu (:283-286 "don't log calls … precompiles"), H10 Besu (:351-363), H29 Parity
  (executive_tracer.rs:44), H09 Parity shape (rpc trace.rs:528, :599), Nethermind error-only failure branch
  (current ParityLikeTxTracer.cs:476; the writer link in the ledger is at an older pin).
- Incomplete or misleading: the H09 background presents a failed-frame `result` as a departure from Parity-style
  clients generally. It omits that Erigon (trace_adhoc.go:517-529) and Reth (revm-inspectors types.rs:338-367)
  already emit it, and that the only draft-specific novelty is the failed-CREATE shape. See A2.
- H29 "Decision needed … extend to more precompiles/forks": agreed. The rule is fork-dependent through the active
  precompile set (A8).
