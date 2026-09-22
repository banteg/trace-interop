# Harness assertion audit

The September 23 audit reproduced nine ways an incomplete or invalid observation could
receive a successful assessment. The regression tests mutate copies of captured responses;
they do not claim that a client produced those mutations.

| Finding | Check now enforced |
| --- | --- |
| An imported numbered header did not prove it was the canonical head | Wait for RPC readiness, capture `latest`, and verify its hash, number and roots against the frozen head |
| Invalid control envelopes could establish setup | Require a successfully parsed, correlated result for every independent control; pruning requires a valid RPC error |
| Reference and target could omit the same traces | Anchor comparisons to frozen transaction roots, required call-tree actions and emitted tree structure before comparing |
| REVERT bytes and gas were only type checked | Compare exact fixture bytes and gas; check the hand-derived constants against the frozen bytecode |
| Requested raw-transaction products could be absent | Require state changes and the executing bytecode/opcode sequence, including marker storage and creation code; OOG cannot commit the marker write |
| A retained precompile child could have the wrong identity or value | Check call-site address, target, call type, input, value and execution outcome |
| Missing responses disappeared from topic coverage | Emit unassessed checks for every declared case, including missing observations and failed setup |
| Different builds could collectively satisfy a harmonization badge | Select the most recently captured immutable build per client/channel and require all declared cases on it |
| Nonstandard JSON numbers were accepted | Reject `NaN`, `Infinity` and `-Infinity` while preserving the exact raw response |

Tests cover the counterexamples, unmodified positive controls, joint reference/target
omission, malformed control payloads, missing build provenance and superseding an older
build. Missing independent reference inventory remains unassessed. The fixture anchors
are deliberately limited to the named properties; they do not claim general EVM correctness
or complete method conformance.

Fresh captures are selected in [the report inventory](../reports.lock.json). They use the
same locked native images and Geth fork image as the preceding comparison. Original
captures remain unchanged, including their historical completeness flags. Current reports
recompute eligibility rather than trusting those flags. Every imported capture is verified
against its retained checksums before assessment.

The batch runs on the Fedora devbox against disposable Hive chains. After the first run,
`source_dirty` records the preceding untracked evidence directories; the tracked capture
source remains at `caf32ff` throughout. These flags are retained, and the manifests record
the exact runner hash. The current assessment source hashes are recorded separately in
[assessment.json](../reports/assessment.json).

The refresh contains **3,652 exchanges across 18 runs**. Seventeen runs completed;
the native reorg run is partial. Erigon development rejected the switch with
`Invalid forkchoice state`. Both Reth builds accepted restoration as `VALID`, but the
canonical RPC head did not return to the expected hash within 30 seconds. Their reorg
observations stay ineligible. Geth, both Besu builds, both Nethermind builds and Erigon
release completed the reorg scenario. The report includes all 20 missing exchanges as
unassessed records rather than dropping them.

Validation: 84 unit/regression tests, the frozen-input/inventory verifier, all nine method
schemas and recursive negative schema vectors pass. Report generation is deterministic.
The original nine counterexamples are rejected by the new assertions; unmodified positive
controls remain accepted for the properties those tests exercise.

## Second review pass

Five additional gaps are covered by `tests/test_second_audit.py`:

- Malformed reference envelopes remain recorded failures; dependent comparisons become
  unassessed instead of aborting report generation.
- Empty trace selections must preserve the fixture's exact return bytes (`0xffee`
  for the call tree and word 42 for `return42`).
- Multi-call storage probes check per-call sender nonce progression, the initial slot
  write and absence of storage transitions from reverted writes or subsequent reads.
  These checks accept both zero-slot addition and zero-to-value modification encoding;
  they do not impose a fee-accounting policy.
- Pre-Cancun deletion checks compare actual old code and nonce with the frozen fixture,
  and require its empty storage map. Nonempty storage deletion needs a separate fixture.
- [The ordered isolation scenario](scenarios.md#multi-call-simulation-isolation) uses
  independent `eth_getStorageAt` calls after each simulation. The older
  `control-storage-after-many` observation is retained but cannot prove isolation.

The mutation tests use copies of observations. They demonstrate weaknesses in the old
assertions, not additional client defects. Reassessing the preceding 18 runs with the
stricter value checks identifies no new failing client cases.

The ordered scenario captured **90 responses** on the same eight native builds and
Geth fork image. All nine builds pass its ten H16 assertions: two envelope checks,
two output-sequence checks, two nonce checks, two storage-transition checks and two
canonical-storage isolation checks. This establishes the named storage/nonce
properties, not agreement on the unresolved fee policy. Existing schema differences
in reverted trace results remain visible separately.

Captures use source `f2c76c0`; tracked source stayed clean. Their `source_dirty` flags
reflect preceding untracked evidence directories. Two earlier attempts failed before
simulator startup with a Docker/containerd shim protocol error; both are retained
outside the report inventory. The generated Hive adapter passes its Go tests, and
captured request-order regressions verify phase order for every client. Validation
now passes **95 Python tests**, the frozen-input/inventory verifier and the method
schema checks. The report inventory contains 20 runs and 3,762 assessment records.
