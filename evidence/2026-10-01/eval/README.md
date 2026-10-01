# Eval: published client matrix — 2026-10-01

The nineteen-corpus suite captured **19,562 RPC exchanges** against eleven immutable builds. Its [live freshness preflight](preflight.json) passed at **2026-10-01T11:19:31.990714+00:00**; no development build predates its stable release, so `lagging_development` is empty. [clients.lock.json](clients.lock.json) records exact image digests, image identities and Geth build provenance. Stable releases remain Reth 2.7.0, Erigon 3.7.0, Nethermind 2.0.0, Besu 26.9.0 and Foundry 1.8.3.

All captures ran on Fedora from clean harness commit `01b69812ff87408f2caec4a3ae8ebdf0d6cbe4ab`, with output in the clone's ignored `runs/` directory. Every manifest records `source_dirty: false` ([source audit](source-audit.json)). The previous comparison is the [September 30 eval](../../2026-09-30/eval/README.md). The reports assess both matrices with the same code and ledger, including the policy revisions made since that eval: H15 adopts Erigon's blob rule (a blob call with an omitted or zero `maxFeePerBlobGas` runs at BLOBBASEFEE 0) and treats an explicit `gas: 0` as a zero limit, and the pinned draft carries the matching TraceCall blob wording.

Every development build moved: the Reth nightly to `5b686303` (the merge commit of reth#27586, main on 2026-09-30), Erigon to `50e2cc4f`, Nethermind to `759efed7`, Besu to `28edf391` (now `26.10-develop`), the Foundry nightly to `df92604b`, and the Geth draft fork to `67f41dea`. The stable builds keep their previous images. Uptake is recorded in the generated [fix catalog](../../../docs/client-fixes.md):

- **Nethermind** `759efed7` (2026-10-01 09:50 UTC) carries all four trace fixes merged on October 1: #14089 (reject disagreeing `data` and `input`, H14), #14091 (validate trace_rawTransaction as block inclusion does, H13), #14111 (the trace_filter `blockHash` member and rejected hash bounds, H33 and H32), and #14092 (blob calls without a positive cap at BLOBBASEFEE 0, H15). The build also carries the TraceStore fixes #14093, #14115 and #14122, which no corpus exercises because the harness does not enable the TraceStore plugin; #14123 merged after the build.
- **Reth** nightly `5b686303` is #27586's merge commit, which keeps an omitted-gas call within the RPC gas cap. It still pins revm-inspectors 0.44.0, so the 0.44.1 fixes (#530, #532, #533) are not in it.
- **Anvil** nightly `df92604b` is the first with revm-inspectors 0.44.1 (foundry#17226), which brings #530 (H26), #532 (H20) and #533 (H09, H23). foundry#17106 (H17 and H26 stateDiff markers) merged after this nightly was built and is not in it.
- **Geth draft** `67f41dea` adds four follow-ups to `ec1cec0b`, including 26f398b9 (keep a `blockHash` selection canonical through replay); the frozen corpora do not exercise their paths.

## Measured changes

Seven verdicts change, all improvements, and none regresses. No case verdict regresses for any build. The headline rises from 81 to **83 of 132** native development decisions in agreement, through Nethermind's H32 and H33.

**Nethermind development (5 verdicts).** H32 and H33 now agree: `759efed7` rejects block-hash filter bounds, as a string or an EIP-1898 object, with -32602, and selects exactly the hashed canonical block. It answers every hash case with block 2's records (the genesis hash and a page past the end with `[]`), rejects a hash with non-null bounds and a malformed hash with -32602, and returns -32000 (“header not found”) for an unknown hash, also with `count: 0`. In reorg-safe, A's hash after the switch and B's after the restore return -32000 (“block is not canonical”); -32001 is recommended but not required. H13 moves to partially assessed: every invalid raw-validation probe is rejected for its own violation, except a code sender, which is rejected with -32000 “sender has deployed code”, a message the checks do not yet recognize as a validation failure, so those four cases are blocked. The raw transaction sent at the default block is now rejected for its stale nonce. H14 moves to policy open: disagreeing `data` and `input` are rejected with -32602, and only the open legacy-priced authorization-list case remains. H15 moves to partially assessed: `blob-fee-defaulted` and `blob-fee-zero` now execute at BLOBBASEFEE 0, and the remaining cases are blocked where the default gas budget exceeds the sender's funds or a refund is not independently derived. No checked case of the development build differs.

**Anvil development (2 verdicts, not in the headline).** With revm-inspectors 0.44.1 the nightly changes 81 responses. H09 and H20 move from differs to partially assessed, with only the blocked mined-probes cases left: a reverted CREATE reports `{gasUsed, output}` without an address or code, a static-context write is labelled “Mutable Call In Static Context”, MLOAD reports its memory, code that runs off its end has no synthetic STOP, and a call that fails its precheck has no `sub`. The failed-CREATE filter matching from #533 (H23) changes only in mined-probes, which the replica cannot verify, and no fixture deletes an account with storage, so #530 (H26) has no measured effect. H17 and H26 still differ until a nightly carries #17106.

**Reth development.** No verdict changes. #27586 caps the omitted-gas budget at the 50,000,000 RPC gas cap instead of about 100,000,000, so the three `field-gas-omitted-funded` probes (trace_call, trace_callMany and the eth_call control) now agree; H15 still differs on other cases. Both Reth builds also returned block 0x2a's receipt for the replaced branch's tail transaction after the reorg switch (`reorg-safe/after/tail-receipt`), where the September 30 eval returned null. The release image is unchanged, so this is timing; the case is not assessed.

Apart from their client-version strings, the Erigon, Besu and Geth draft development builds return byte-identical responses to the previous eval.

## Report registration

[reports.lock.json](../../../reports.lock.json) selects this matrix's nineteen runs and compares them with the September 30 eval. It selects no focused capture. The new matrix captures every default corpus, `probes-prague` included, and that corpus now carries the explicit zero and null gas cases, so the focused [gas-zero](../gas-zero/README.md) recapture, which the lock previously selected in place of the September 30 `probes-prague`, is superseded by this matrix's `probes-prague` and remains retained as history only.

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

**17 of 19 corpora completed.** The two incomplete scenarios retain their full evidence and remain blocked, for the same reasons as in the previous eval. Both Anvil builds replay mined-probes block `0x2` with different gas used and receipts root (the fixture uses a parent beacon root that this replica cannot set). Both Erigon builds reject the reorg branch switch with “Invalid forkchoice state” (open [erigon#24032](https://github.com/erigontech/erigon/pull/24032)). `probes-prague` has 44 more exchanges than in the previous eval: the four gas cases for each of the eleven builds.

## Reproduction and validation

On Linux with Docker, from capture source commit `01b69812`:

```sh
uv run python scripts/run_matrix.py --reproduce-lock evidence/2026-10-01/eval/clients.lock.json --output runs/reproduction
```

Rebuild the recorded clean Geth source image if the local image is absent, following [the usage guide](../../../docs/usage.md). The matrix command exits nonzero for the two retained incomplete scenarios; this does not turn captured observation placeholders into conformance verdicts.

[validation.json](validation.json) records checks against the selected evidence and generated assessment.

[Cleanup verification](cleanup.json): removed the task clone, its log and its done marker, the five superseded development images whose tags this run's pulls moved, and the `rpc-compat` simulator image this run's rebuild replaced. The runner had already removed the replaced Hive adapter images, and the rebuilt adapter and simulator tags remain. No test containers or new anonymous volumes remained, and unrelated Docker services were unchanged. Published base images and every `trace-interop/*` image, including the new source-built Geth image, remain available for reproduction.
