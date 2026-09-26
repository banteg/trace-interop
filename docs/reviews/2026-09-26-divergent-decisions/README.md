# Review of divergent decisions (2026-09-26)

Eleven decisions had most or all native clients differing from the draft: H04, H06, H08, H09, H14 (after its null rule), H15, H16, H20, H23, H30 and H32. This review asked, for each atomic rule, whether the clients already share an alternative (then the draft should adopt it, as it did for explicit null in H14) or whether the draft's rule is new behavior that it must justify or drop.

Each rule was re-derived from the `evidence/2026-09-26/anvil` matrix, client source at pinned commits, Parity `55c90d4` and the draft at `e437815d`, not from ledger prose. The Geth draft fork follows the draft by construction and is not counted as a vote. The per-decision reports below carry the behavior tables, source pins, verdicts and exact replacement text.

| Report | Decisions |
| --- | --- |
| [H06-H09.md](H06-H09.md) | Missing results, failed frames and labels |
| [H04-H23-H30-H32.md](H04-H23-H30-H32.md) | trace_filter address lists, special-action matching, omitted bounds, tags |
| [H14-H15-H16.md](H14-H15-H16.md) | Error codes, unsigned-call fees, stateDiff fee accounting |
| [H08-H20.md](H08-H20.md) | Execution envelope and vmTrace step contents |

## Verdicts

The draft mostly holds. Much of the apparent disagreement came from misattributed checks, stale ledger notes, or clients whose trace path is the outlier within their own codebase.

| Decision | Verdict | Change to the draft |
| --- | --- | --- |
| H04 empty and null address lists | Keep | None. Every native client except Nethermind, and Parity, treats `[]` as unrestricted; Nethermind's own `eth_getLogs` does too. |
| H06 missing transactions, blocks and paths | Keep | Rationale only: the -32001 code needs a corrected justification, or a switch to -32000 (decision 1). |
| H08 execution envelope | Keep | None. Every native development build conforms; Erigon's ⚠️ is an H15 environment difference. |
| H09 failed frames | Keep the core, change two labels | "Code size limit exceeded" → "Out of gas" and "Invalid code prefix 0xEF" → "Invalid code", both as Parity/OpenEthereum and EIP-170 report them; `revertReason` is no longer defined as decoded text. Reverted-CREATE shape is decision 3. |
| H14 error codes (remaining) | Keep -32602 and the -380xx codes, change the fallback | "Any other validation failure is -32602" matches no client. Proposed: -32602 only for call objects invalid regardless of state (taking precedence), -32003 for other rejections, as H13 uses. |
| H15 unsigned-call fees | Keep | None. Besu, Erigon and Nethermind already do this in their own `eth_call`; only their trace paths differ. Reth charges nothing in either path (decision 5). |
| H16 stateDiff fee accounting | Keep | Label `error.data.index` for a failed trace_callMany item as new behavior; only Erigon names the index, in message text. |
| H20 vmTrace step contents | Keep most, change two sub-rules | CALL-family `mem` may be the full output window (preferred) or exactly the copied bytes; the `cost` of a halted operation is implementation-defined; a failed precheck's `cost` still includes forwarded gas (clarification). |
| H23 special-action matching | Keep | Add the principle that a record matches only addresses it reports; the failed-CREATE rule is tied to H09 (decision 3). |
| H30 omitted bounds | Keep | None. Besu, Nethermind and Reth development already default to latest; Erigon is the outlier (decision 4). |
| H32 tags and `pending` | Keep the filter rules | `pending` for block methods and simulations, and block-hash bounds, need maintainer input (decision 6). |

Two premises in the request that started this review were wrong and are corrected above: Erigon is not the only client treating an empty list as unrestricted (Nethermind is the only one that does not), and Nethermind does not search history for omitted bounds.

## Decisions for the maintainer

1. **H06, unknown single block: -32001 or -32000.** Erigon, Nethermind, Besu and Parity return -32000; only Reth returns -32001, and the ledger's claim that -32001 "matches the eth/debug getters" is half wrong. The case for keeping -32001 is that every native client also uses -32000 for invalid-call errors in trace_call, so -32000 would not let a caller tell "unknown block" from "invalid call" without parsing the message. Recommended: keep -32001 with the corrected rationale.
2. **H06, pruned state.** Nethermind deliberately uses -32002 for missing state; the draft does not name a code. Only Reth has pruning coverage in the matrix, so this needs a Nethermind or Erigon pruned case before settling.
3. **H09 and H23 together, reverted CREATE.** The draft's `{gasUsed, output}` with no address is emitted by no native client: Erigon, Reth and Anvil emit `{address, code, gasUsed}` with the would-be address, as a side effect of reusing the success serializer, and Erigon, Nethermind and Reth then match that address in trace_filter. Keeping the draft keeps H23's "a failed CREATE has no created-address match"; adopting the client shape reverses both. Recommended: keep the draft (no contract exists at that address), with the rationale stated in both decisions.
4. **H30, Erigon's breaking change.** Erigon starts omitted bounds at genesis, a 2020 leftover that contradicts its own `eth_getLogs`. Its default `--rpc.blockrange.limit` of 1000 already makes such queries fail on real chains, so the change silently narrows results only for archive operators who set the limit to 0. It needs an Erigon breaking-change note and ideally an Erigon position.
5. **H15, Reth.** Reth's trace and `eth_call` paths charge no fees and check no funding, through a flag added for OP operator fees (#18634, reverted, re-added in #19073). Ask Reth whether that L1 behavior is intended; complying changes its `eth_call` too.
6. **H32 open items.**
   - `pending` for trace_block and trace_replayBlockTransactions: Reth traces a real pending block today; Nethermind traces the head (corrected 2026-09-27). There is no case yet.
   - `pending` for trace_call and trace_callMany: Besu and Nethermind accept it but evaluate at the head block, indistinguishable from latest. Proposed: accept `pending` only with a real pending environment (the next block number), otherwise -32602.
   - Block-hash filter bounds: Parity, Erigon and Nethermind accept them and the draft rejects them silently. Proposed: keep the rejection, state it, and add a case.

## Corrections to our own records

**Misattributed checks** (the harness assigns a topic from the case name or a coarse tag):
- Besu's H04 ⚠️ comes from `a/filter-from-empty-to-set`, whose only failure is the H23 SELFDESTRUCT-beneficiary miss (`trace_interop/rules.py:337`).
- Erigon's H08 ⚠️ is an output mismatch caused by its trace_call GASLIMIT of 2^256−1, an H15 environment difference (`trace_interop/coverage.py:274`).
- `a/call-gas7400` has no H20 assertions, so Nethermind shows agreement there while `repeat/call-gas7400` catches its 7400→9700 cost rewrite.

**Stale or wrong ledger and impact claims:**
- H14: "Besu has no -380xx codes" is false; Besu's `eth_simulateV1` maps -38010 to -38015, -38020, -38021, -38023 and -38026 (not -38025).
- H16: "All four clients already fail the whole request on an item error" is wrong; Besu nests an error in `result`, Nethermind streams earlier items and truncates, and only Erigon and Reth return one clean error.
- H15: the Geth draft already returns BASEFEE 0 for a zero-fee trace_call; the earlier-proposal note and snapshot table are historical.
- H23: Nethermind 2.1.0-preview matches rewards by author (8 of 8); fixtures now cover rewards and failed CREATE; `filter-selection.md` §5 wrongly says Erigon and Alloy/Reth give a failed CREATE no match.
- H30: Nethermind already defaults to latest (its ⚠️ is only the -32000 reversed-range code); the Reth development label should be `df7b7fdf`.
- H32: Erigon 3.7.0 no longer resolves `pending`; both builds reject it.
- H06: the captured Nethermind development build is `fca93966`, not `641592d2`.
- H08: Erigon does not return `trace: null`; several Geth "observed" strings in `impact.json` predate the fork's current behavior.
- The H20 source review's claim that Besu reverses multi-word `push` order is wrong (`probes-prague/vm-push-order`).

**Fix tracking:**
- Reth #27411 (omitted filter bounds default to latest, maintainer-merged) is missing from `fixes.json`.
- Erigon #24255 and Alloy #4257 also implement H04 and should list it.
- Nethermind #13857 (ours) codifies "an empty list matches no address" in its tests and docs; it must not count toward H04 and needs an amendment or a follow-up.
- Nethermind #13782 fixed the successful CREATE cost only; failed-precheck CREATE still reports 32002.
- revm-inspectors #504's MLOAD `mem` omission contradicts the kept H20 rule (its CALL clamp becomes acceptable).

## Missing coverage

- EIP-170 code size limit and EIP-3541 0xEF prefix frames (H09): both labels are unverified in every client.
- trace_replayBlockTransactions of an unknown block (H06): Erigon and Nethermind error, Besu and Reth return null (Reth locks it in an integration test).
- A `missing-block-filter` variant with `toBlock` just past the head, so Anvil's 300-block range cap cannot mask the bound check (H06).
- A blob-fee probe for the BLOBBASEFEE rule and a nonce probe (H15).
- `pending` on block methods and block-hash filter bounds (H32).
- A reward-leak case for Erigon, which emits rewards whenever the coinbase is in `toAddress`, ignoring `fromAddress` and mode (H23).

## Client work with no PR yet

- Nethermind: remove the 7400→9700 cost rewrite; CALL-family `mem`; keep halted operations with `ex: null`; forwarded gas in failed-precheck CREATE cost (H20). Treat `[]` as unrestricted (H04). Null for a missing transaction in trace_get (H06, after #13676).
- Erigon: `ex: null` and no `store` on execution-error halts; drop the implicit STOP; omit undefined opcodes (H20). Default omitted bounds to latest (H30).
- Besu: stipend and precompile and precheck `cost`, precheck `sub` (H20); SELFDESTRUCT beneficiary matching (H23); `safe` tag resolution (H32).
- revm-inspectors: MLOAD `mem`, no implicit STOP, precompile and empty-code `sub`, precheck `sub: null`, omit undefined opcodes (H20).
- Alloy: block tags for trace_filter bounds (H32), a typed-API change.
