# Zero-value precompile call at the depth limit — 2026-10-18

A recapture of `probes-forks` with the [2026-10-18 eval](../eval/README.md) builds, made after the corpus gained
`depth-limit-precompile`. That case measures the frame-emission conflict the draft settled in
[execution-apis 28a58240](https://github.com/banteg/execution-apis/commit/28a5824023fbd76ef4e1dec9564b94be5883fbc1).
Its recursion reaches depth 1024 at a Homestead block. The deepest frame's self-call fails the depth check, and it
then calls the identity precompile with zero value, which fails the same check. Nested zero-value precompile frames
are omitted, so only the failed self-call may appear.

The run uses the eval's [clients.lock.json](../eval/clients.lock.json) from a clean clone at harness commit
`7d57e254` on Fedora. It is complete, every build is eligible, and it captured 657 responses.
[reports.lock.json](../../../reports.lock.json) selects it in place of the eval's `probes-forks`; every other case is
the same request as in the eval.

| Build | Under the deepest frame |
| --- | --- |
| Geth draft, Erigon (both), Nethermind (both), Reth (both) | the failed self-call only; the precompile call is omitted |
| Besu (both) | nothing; Besu emits no frame for a failed precheck (H29) |

Every build that emits precheck frames already omits the zero-value precompile call, so the draft's choice matches
current behavior.
