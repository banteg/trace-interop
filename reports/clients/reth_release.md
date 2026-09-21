# reth_release: proposed changes

Fresh builds: not run.

Matches mean only the linked assertions matched. They do not certify a whole decision or method. Historical change descriptions require review against fresh results.

| Decision | Fresh assertion results | Historical candidate change / review task |
| --- | --- | --- |
| [H01 — Method coverage](../decisions/H01.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H02 — trace_get selector and return shape](../decisions/H02.md) | Not asserted / needs review | Replace flat/offset selection with one traceAddress path; [] must select root. Existing callers may depend on old indexing. |
| [H03 — Filter composition and mode](../decisions/H03.md) | Not asserted / needs review | Change the default from union to intersection between address lists; explicit union would remain an extension. |
| [H04 — Empty address lists](../decisions/H04.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H05 — Post-merge reward records](../decisions/H05.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H06 — Missing transactions and paths](../decisions/H06.md) | Not asserted / needs review | Return null for unknown individual replay rather than a missing-transaction error. |
| [H07 — Replay transactionHash field](../decisions/H07.md) | Not asserted / needs review | Add transactionHash to individual replay envelopes. |
| [H08 — Empty output and unrequested components](../decisions/H08.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H09 — Failed frame results and error labels](../decisions/H09.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H10 — Creation result field names](../decisions/H10.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H11 — Empty trace-type selection](../decisions/H11.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H12 — Raw-transaction block argument](../decisions/H12.md) | Not asserted / needs review | The baseline rejects a third block argument; preserve existing extension only under a separate profile. |
| [H13 — Signed transaction nonce validation](../decisions/H13.md) | Not asserted / needs review | Review signed nonce validation; ensure simulation does not replace the signed nonce. |
| [H14 — Invalid-parameter error codes](../decisions/H14.md) | Not asserted / needs review | Normalize malformed input to -32602 and separate it from valid-but-rejected transactions; code changes affect consumers. |
| [H15 — Unsigned simulation fees and block environment](../decisions/H15.md) | Not asserted / needs review | Review zero-fee unsigned calls without changing BASEFEE; fee admission and opcode context need separate checks. |
| [H16 — Fee accounting and sequential state diffs](../decisions/H16.md) | Not asserted / needs review | Confirm actual fee accounting and per-entry callMany diffs; storage sequencing alone does not prove the entire rule. |
| [H17 — New-account stateDiff encoding](../decisions/H17.md) | Not asserted / needs review | Review new-account + markers for empty code and zero nonce, independently of prefunded existing accounts. |
| [H18 — EIP-7702 code changes in stateDiff](../decisions/H18.md) | Not asserted / needs review | Capture EIP-7702 code set/replace/clear changes even when the account already exists; preserve authorization changes across execution revert. |
| [H19 — vmTrace executing bytecode](../decisions/H19.md) | Not asserted / needs review | Capture actually executing constructor and delegated code rather than relying on pre-state address lookup. |
| [H20 — vmTrace step timing and deltas](../decisions/H20.md) | Not asserted / needs review | Refresh after the merged inspector fix; old gas/memory/call-return findings may now be resolved. |
| [H21 — vmTrace numeric and optional metadata encoding](../decisions/H21.md) | Not asserted / needs review | Review stack word canonicalization; optional op/idx must not become mandatory for consumers. |
| [H22 — Precompile return bytes](../decisions/H22.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H23 — Special-action address matching](../decisions/H23.md) | Not asserted / needs review | Verify CREATE and SELFDESTRUCT matching against explicit from/to equivalents; do not infer behavior from ordinary CALL filters. |
| [H24 — Sibling failure isolation](../decisions/H24.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H25 — Well-formed errors for rejected raw transactions](../decisions/H25.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H26 — Account deletion across Cancun](../decisions/H26.md) | Not asserted / needs review | Report real pre-Cancun deletion of account fields; preserve existing accounts after EIP-6780. |
| [H27 — Filter execution across fork boundaries](../decisions/H27.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H28 — Historical state at system-operation boundaries](../decisions/H28.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
