# Eval: published client matrix — 2026-11-25

The twenty-corpus suite captured **20,576 RPC exchanges** against eleven immutable builds. Its [live freshness preflight](preflight.json) passed at **2026-11-25T15:07:31Z**. Every lock entry matched its published image, and the Geth draft matched its branch head.

All captures ran on Fedora from harness commit `8e9f0c8f`, which adds seven positional override probes to `probes-prague`. The matrix wrote its output under the clone's ignored `runs/` folder, so every manifest records `source_dirty: false`.

## Builds

Four stable releases are new:

- **Foundry 1.10.0** · `083e2299` replaces 1.9.0. It replaces revm and revm-inspectors with evm2 and takes Alloy 2.6.1, which carries the null trace_filter address list fix (Alloy #4257) and the trace_filter `blockHash` member (Alloy #4274).
- **Besu 26.11.2** · `09b9e94d` replaces 26.11.0. It carries trace_replayTransaction (#11406), #11439, #11441, local failure frames (#11345), precompile output (#11346), nonzero-value precompile frames (#11360), empty code for self-destructing creations (#11362), raw transaction validation (#11395) and creationMethod on every create frame (#11435).
- **Erigon 3.8.2** · `8a3f3b2c` replaces 3.8.1.
- **Reth 2.11.0** · `b9abbcc1` replaces 2.10.1. It takes evm2 past #744 but does not pin Alloy 2.6.

Nethermind 2.2.2 is unchanged. The Geth draft moved to `edbd5f17`: the #35791 rework rebased on #35970, reporting Amsterdam execution and state gas through the EIP-8037 hooks. The development builds moved:

- **Besu** develop `f58f40e2` adds root precompile halt reasons (#11347) and rejects extra trace_call parameters.
- **Reth** nightly `7f5e740c` pins Alloy 2.6.0 (#4257, #4274).
- **Anvil** nightly `50d75f19` runs evm2, as 1.10.0 does.
- **Erigon** main `e91aca7f` carries #26090. **Nethermind** master `e2f069a6` is 2.4.0-preview.

Uptake is recorded in the generated [fix catalog](../../../docs/client-fixes.md), and every build's source revision in [locks/source-revisions.json](../../../locks/source-revisions.json).

## Capture completeness

All 20 corpora are complete.

## New probes

`probes-prague` gains positional overrides (H15): a state override map as `trace_call`'s fourth parameter (code, balance and a stateDiff slot) and as `trace_callMany`'s third, applied to both items, and a block override of NUMBER as the fifth and fourth. The draft lets a server reject either form, so each probe passes when the override takes effect or the request is rejected, and fails when it is ignored. `override-state-exclusive` sends an account override with both `state` and `stateDiff`, which must be rejected (H14).

| Build | trace_call | trace_callMany | state and stateDiff |
| --- | --- | --- | --- |
| Geth draft | applied | applied | rejected |
| Reth 2.11.0, nightly | applied | ignored | rejected |
| Nethermind master | state applied, block rejected | rejected | rejected |
| Nethermind 2.2.2 | state applied, block rejected | rejected | accepted |
| Erigon 3.8.2, main | state ignored, block rejected | state ignored, block rejected | accepted |
| Besu develop | rejected | rejected | rejected |
| Besu 26.11.2 | ignored | rejected | accepted |
| Foundry 1.10.0, nightly | rejected | rejected | rejected |

Erigon decodes the positional map into an empty configuration; #26785, by lupin012, applies it. Reth's `trace_callMany` takes two parameters and drops the trailing ones without an error, as Besu 26.11.2 does for `trace_call`.

## Measured changes

36 verdicts change for five clients ([changes since the previous matrix](../../../reports/changes.md)). Across the five development builds, **141 of 165** decisions agree, up from 133. 3 more have a submitted fix, 19 differ with no fix yet, and 2 are not fully measured.

**Besu 26.11.2 goes from 8 to 19 agreements, and develop from 15 to 20.**
- The release gains what develop had: H01, and with it the replay cases of H07, H08, H18 and H19, plus H32.
- Both builds gain H10 (#11362, #11435), H22 (#11346), H24 (#11345) and H26 (#11362). Develop's H17 is now fully assessed and agrees.
- H13 moves from differs to partially assessed on both builds.
- The release ignores trailing trace_call parameters. Its H15 now differs, and its H14 still differs, now only because it accepts the override with both state forms.

**Foundry 1.10.0 and the nightly go from 28 to 30.**
- evm2 reports the post-Cancun self-destruct-to-self payload, so H23 and H26 agree without revm #3833.
- Alloy 2.6.1 omits a null trace_filter address list, so H04 agrees.
- H20 now differs: evm2's vmTrace CREATE in `call-tree-vmTrace` costs 32,002 where Erigon, Nethermind and the Geth draft report 480,269, as on Reth (evm2 #876).
- Alloy 2.6.1 parses the trace_filter `blockHash` member, but Anvil ignores it and answers the head block (H33).

**Reth's nightly goes from 25 to 28.** Alloy 2.6.0 makes H04 and H33 agree, and H23 is fully assessed and agrees. 2.11.0 stays at 25. Both ignore trace_callMany overrides (H15), which already differed.

**Erigon goes from 32 to 31 on main, and the release from 29 to 31.** Both differ on H15 for the ignored state override map. 3.8.2 gains H05, H06 and H21.

**Nethermind master goes from 33 to 32.** It runs a trace_call whose `data` and `input` disagree, executing `input`, which #14089 had rejected (H14). 2.2.2 stays at 27.

The Geth draft agrees on all 33 decisions.

| Release | Agrees on | Previous release |
| --- | --- | --- |
| Erigon 3.8.2 | 31 | 29 |
| Foundry 1.10.0 | 30 | 28 |
| Nethermind 2.2.2 | 27 | 27 |
| Reth 2.11.0 | 25 | 25 |
| Besu 26.11.2 | 19 | 8 |

## Reproduction and validation

On Linux with Docker, from capture source commit `8e9f0c8f`:

```sh
uv run python scripts/run_matrix.py --reproduce-lock evidence/2026-11-25/eval/clients.lock.json --output runs/reproduction
```

If the local Geth image is missing, rebuild it from its recorded clean source following [the usage guide](../../../docs/usage.md).

The assessment also includes a rule change made after the capture: a `trace_callMany` probe that allows rejection no longer requires one execution envelope per call when the request is rejected.

[validation.json](validation.json) records the checks run against the selected evidence and the generated assessment. [Cleanup verification](cleanup.json) records what was removed:
- the task clone and its log;
- the dangling images, including the November 9 eval's superseded images;
- build cache older than a day.

Tagged `trace-interop/*` source builds were kept.
