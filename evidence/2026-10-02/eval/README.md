# Eval: published client matrix — 2026-10-02

The nineteen-corpus suite captured **19,562 RPC exchanges** against eleven immutable builds. Its [live freshness preflight](preflight.json) passed at **2026-10-02T14:41:05.957366+00:00**; no development build predates its stable release, so `lagging_development` is empty. [clients.lock.json](clients.lock.json) records exact image digests, image identities and Geth build provenance.

All captures ran on Fedora from clean harness commit `61f51bf5060af516ab873aaaca5b96e38bd7e4cf`, with output in the clone's ignored `runs/` directory. Every manifest records `source_dirty: false` ([source audit](source-audit.json)). The previous comparison is the [October 1 eval](../../2026-10-01/eval/README.md). The reports assess both matrices with the same code and ledger.

The capture was taken for Besu, which merged #11401 (11:59 UTC) and #11404 (13:33 UTC) today. Before capturing, the `hyperledger/besu:develop` image was checked: its `org.opencontainers.image.revision` label is `711f8142eb12750a1777ef366e0e0eeeca69513d`, which is #11404's merge commit and identical to Besu `main` per the GitHub compare API, and #11401's merge commit `7545fa05` is three commits behind it. Every other development build moved too, and three stable releases are new:

- **Besu** develop `711f8142` (26.10-develop) includes #11401 (H25) and #11404 (H15, H16). 26.9.0 is unchanged.
- **Anvil**: Foundry 1.8.4 · `50af4efe` replaces 1.8.3 and the nightly moves to `328811cb`. Both ship revm-inspectors 0.44.1 (#17226) and foundry #17106, so the stable release now carries everything the October 1 nightly did, plus the stateDiff account markers.
- **Nethermind**: 2.1.0 · `b3e7e84c` replaces 2.0.0, and master moves to `3370d566`. 2.1.0 carries #13667 and #13668 but none of the fixes merged after them, including #13666. The development build adds #14158 (by a Nethermind maintainer): trace_call and trace_callMany answer fee, funding and intrinsic-gas rejections with the eth_simulateV1 codes (-38012, -38014, -38013) instead of -32000.
- **Erigon**: 3.7.1 · `8c1e3893` replaces 3.7.0, and main moves to `6da806cb`. Both return byte-identical responses to their predecessors.
- **Reth** nightly `078d0262`; 2.7.0 is unchanged. Apart from version strings both Reth builds differ from the previous eval in one response only: `reorg-safe/after/tail-receipt` is null again, the timing flip noted on October 1.
- **Geth draft** `67f41dea` is unchanged and returns byte-identical responses.

Uptake is recorded in the generated [fix catalog](../../../docs/client-fixes.md).

## Measured changes

Eighteen verdicts change, all improvements, and none regresses. No case verdict regresses for any build: the 36 Besu development cases that move from blocked to differs are failures that the wrapped error envelope hid until now (see below). The headline rises from 83 to **85 of 132** native development decisions in agreement, through Besu's H11 and H25.

**Besu development (2 verdicts).** H25 agrees: a rejected trace_callMany bundle is one top-level JSON-RPC error, so no response nests an error envelope inside `result`. H11 agrees: with #11404 the zero-fee empty-selection call executes and returns its output; the empty selection needed no separate fix. H15 and H16 still differ, now on the failures listed in the next section. With the bundles executing, 258 previously blocked H16 checks resolve, and checks in H08 (+121 cases), H10 (+62), H14, H17, H19, H20 and H21 (+59) that were blocked or not run now pass.

**Anvil stable (9 verdicts, not in the headline).** Foundry 1.8.4 agrees on H03, H08, H30 and H31 (#17078) and moves H09, H17, H18, H19 and H20 from differs to partially assessed, with only the blocked mined-probes cases left. The Anvil release law note on L09 (an empty trace-type list in trace_call against trace_callMany) is removed because 1.8.4 no longer violates it.

**Anvil development (2 verdicts).** The nightly with #17106 moves H17 and H26 from differs to partially assessed: accounts absent before the call are marked `+` for transfers and creations alike, and an account created and destroyed in one transaction is omitted.

**Nethermind stable (5 verdicts).** 2.1.0 agrees on H08, H11, H16, H17 and H26. It still truncates rejected streamed traces (H25) because it lacks #13666, and keeps 2.0.0's trace_call BASEFEE (H15).

**Nethermind development.** No verdict changes. #14158 changes 308 error responses from -32000 to the eth_simulateV1 codes; the codes are recommended, so these cases already agreed.

## Besu: failures exposed by #11401 and #11404

Before this build, every unpriced Besu trace_callMany failed and the failure came back as an error envelope inside `result`. That blocked 258 H16 checks and parts of H08, H11, H14, H17, H19, H20 and H21. The list below is what Besu `711f8142` now shows, compared with the Geth draft and the Erigon, Nethermind and Reth development builds, which agree with one another on every item. It is the work list for the next Besu fixes.

### H16: no transaction boundary between trace_callMany calls

Each call still sees the pre-bundle original value of a slot an earlier call wrote, so SSTORE is priced as a dirty write. Transient storage, warm sets and SELFDESTRUCT scope already reset per call: `many-transient`, `many-warm` and `many-selfdestruct` agree. The fix is #11365 (open).

| Case | Besu | Expected (every other build) | Difference |
| --- | --- | --- | --- |
| `initial/call-many`, `initial/call-many-priced`, call 2 | root gasUsed 0x1e683 (124,547) | 0x1fc63 (130,147), equal to call 1 | 5,600 gas less: two SSTOREs at 2,800 each. The unpriced bundle shows it too, now that it runs |
| `probes-prague/many-original-value`, call 2 | measured SSTORE gas 0x8a0 (2,208), root gasUsed 0x8b7 | 0x1390 (5,008) for a clean, cold slot, root gasUsed 0x13a7 | 2,800 gas less. The only H16 check failing on call gas |
| `a/many-storage-write-revert-read` (also `repeat/` and `callmany-isolation/`), call 2, the reverted write | sender debited 23,535 gas at 2 gwei | 26,335 gas | 2,800 gas less (5.6e12 wei less sender debit and coinbase tip). Root gasUsed is hidden because Besu reports a REVERT frame's `result` as null (H09). The H16 checks pass within the refund bound and H15 marks the refund as not independently derived, so only the debit shows it |
| `probes-prague/field-gas-omitted-allowance-many` | -32603 Internal error | -38014 insufficient funds for the defaulted gas budget | A rejected item does not name its violation (H15 below) |

`initial/raw-valid-default-block` and the `mined-probes/replay-block-2` fee settlement still differ, as before; neither involves trace_callMany.

### H15: trace calls now follow eth_call; rejections and blob pricing remain

#11404 fixed the fee environment. Every unpriced trace_call and trace_callMany family in `fee-policy` and `fee-compat` (zero, omitted, tip-only zero, free-exact funding, mixed free/priced/free bundles, refunds, reverts, out-of-gas) and every priced call agree. Their eth_call parity checks, which were blocked on internal errors, now pass. What remains:

1. **trace_callMany answers every rejected item with `-32603 Internal error`.** There are 152 checks (19 families × 8 trace selections). The fix is to return the item's own reason, with the eth_simulateV1 code recommended and `error.data.index` for the failing call:

   | Families | Reference code |
   | --- | --- |
   | `legacy-one`, `legacy-below-base`, `typed-one`, `typed-below-base`, `typed-below-base-positive-tip`, `mixed-{legacy,typed}-invalid-then-free` (index 0), `mixed-{legacy,typed}-free-then-invalid` (index 1) | -38012 fee cap below base fee |
   | `funding-free-short`, `funding-legacy-short`, `funding-typed-short`, `funding-typed-free-short`, `funding-typed-effective-only`, `empty-sender-priced`, `sequential-funding` (index 1) | -38014 insufficient funds |
   | `typed-tip-over-cap`, `typed-zero-cap-positive-tip`, `defaults-tip-only-positive` | -32602 priority fee above fee cap |
   | `probes-prague/field-gas-zero-many` (explicit `gas: 0`) | -38013 intrinsic gas |

   Besu's trace_call already names each of these: -32009 below the base fee, -32004 insufficient funds, -32003 intrinsic gas, and -32000 for a tip above a positive cap. Its trace_call checks pass, because the codes are only recommended.
2. **A positive tip over a zero or omitted fee cap is reported as below the base fee.** `fee-policy/typed-zero-cap-positive-tip/call` and `defaults-tip-only-positive/call`, with their `fee-compat` trace_call twins, fail 32 checks. Besu returns -32009 “Gas price below current base fee” where the priority-above-cap rejection takes precedence (-32602; Geth and Erigon). `typed-tip-over-cap`, whose cap is positive, is already classified correctly.
3. **Blob calls run at the head's BLOBBASEFEE.** In `probes-prague/blob-fee-defaulted` and `blob-fee-zero` the probe reads BLOBBASEFEE as 1 where 0 is expected. Gas is identical, and the explicit zero is now accepted (26.9.0 returns -32603).
4. **A supplied nonce below the state nonce is rejected.** `probes-prague/field-nonce-below` returns -32001 “Nonce too low”; the expected behavior is to ignore the nonce and return the result (26.9.0 returns -32603).

Also visible now, but owned by other decisions, with the same behavior as Besu's trace_call and replays: reverted frames have `result: null` and a static-context write is labelled “Illegal state change” (H09, for example `initial/call-many`); `call-tree-trace` lacks `creationMethod` (H10); and the `call-tree-vmTrace` steps differ (H20). `probes-prague/field-chain-id-mismatch` still executes a call for another chain (H14), and `field-authorization`, legacy-priced with an authorization list (policy open), returns -32603 with a Java `NoSuchElementException` stack trace in the message.

## Report registration

[reports.lock.json](../../../reports.lock.json) selects this matrix's nineteen runs and compares them with the October 1 eval. It selects no focused capture.

## Capture completeness

| Corpus | Complete | Exchanges | Setup failures |
| --- | --- | --- | --- |
| [initial](initial/summary.json) | Yes | 836 | — |
| [a](a/summary.json) | Yes | 1,034 | — |
| [repeat](repeat/summary.json) | Yes | 484 | — |
| [forks](forks/summary.json) | Yes | 828 | — |
| [fork-followup](fork-followup/summary.json) | Yes | 216 | — |
| [precompiles](precompiles/summary.json) | Yes | 209 | — |
| [precompile-values](precompile-values/summary.json) | Yes | 165 | — |
| [raw-validation](raw-validation/summary.json) | Yes | 781 | — |
| [coverage](coverage/summary.json) | Yes | 264 | — |
| [fee-policy](fee-policy/summary.json) | Yes | 8,316 | — |
| [fee-compat](fee-compat/summary.json) | Yes | 3,300 | — |
| [callmany-isolation](callmany-isolation/summary.json) | Yes | 110 | — |
| [h30](h30/summary.json) | Yes | 495 | — |
| [raw-selector](raw-selector/summary.json) | Yes | 176 | — |
| [probes-prague](probes-prague/summary.json) | Yes | 836 | — |
| [probes-forks](probes-forks/summary.json) | Yes | 315 | — |
| [mined-probes](mined-probes/summary.json) | No | 979 | anvil_development, anvil_release |
| [reorg-safe](reorg-safe/summary.json) | No | 188 | erigon_development, erigon_release |
| [pruned](pruned/summary.json) | Yes | 30 | — |

**17 of 19 corpora completed.** The two incomplete scenarios retain their full evidence and remain blocked, for the same reasons as in the previous eval. Both Anvil builds replay mined-probes block `0x2` with different gas used and receipts root (the fixture uses a parent beacon root that this replica cannot set). Both Erigon builds, including 3.7.1, reject the reorg branch switch with “Invalid forkchoice state” (open [erigon#24032](https://github.com/erigontech/erigon/pull/24032)).

## Reproduction and validation

On Linux with Docker, from capture source commit `61f51bf5`:

```sh
uv run python scripts/run_matrix.py --reproduce-lock evidence/2026-10-02/eval/clients.lock.json --output runs/reproduction
```

Rebuild the recorded clean Geth source image if the local image is absent, following [the usage guide](../../../docs/usage.md). The matrix command exits nonzero for the two retained incomplete scenarios; this does not turn captured observation placeholders into conformance verdicts.

[validation.json](validation.json) records checks against the selected evidence and generated assessment.

[Cleanup verification](cleanup.json) records what was removed:

- The task clone, its launcher, its log and its done marker.
- The five superseded development images whose tags this run's pulls moved.
- One dangling `rpc-compat` simulator build from this run; the simulator tag kept its cached image.

The runner had already removed the seven replaced Hive adapter images, and the rebuilt adapter tags remain. No test containers, new anonymous volumes or new dangling images remained, and unrelated Docker services were unchanged. Published base images remain available for reproduction. These include the previous Erigon 3.7.0, Nethermind 2.0.0 and Foundry 1.8.3 releases, and every `trace-interop/*` image.
