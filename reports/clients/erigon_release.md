# erigon_release: proposed changes

Fresh builds: not run.

Matches mean only the linked assertions matched. They do not certify a whole decision or method. Historical change descriptions require review against fresh results.

| Decision | Fresh assertion results | Historical candidate change / review task |
| --- | --- | --- |
| [H01 — Method coverage](../decisions/H01.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H02 — trace_get selector and return shape](../decisions/H02.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H03 — Filter composition and mode](../decisions/H03.md) | Not asserted / needs review | Change default union to intersection and avoid suppressing one-sided intersection queries. |
| [H04 — Empty address lists](../decisions/H04.md) | Not asserted / needs review | The draft rejects null filters; historically accepted null, so stricter validation is a compatibility change. |
| [H05 — Post-merge reward records](../decisions/H05.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H06 — Missing transactions and paths](../decisions/H06.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H07 — Replay transactionHash field](../decisions/H07.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H08 — Empty output and unrequested components](../decisions/H08.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H09 — Failed frame results and error labels](../decisions/H09.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H10 — Creation result field names](../decisions/H10.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H11 — Empty trace-type selection](../decisions/H11.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H12 — Raw-transaction block argument](../decisions/H12.md) | Not asserted / needs review | Keep the two-argument baseline; document any block-selector extension. |
| [H13 — Signed transaction nonce validation](../decisions/H13.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H14 — Invalid-parameter error codes](../decisions/H14.md) | Not asserted / needs review | Normalize malformed input to -32602 and separate it from valid-but-rejected transactions; code changes affect consumers. |
| [H15 — Unsigned simulation fees and block environment](../decisions/H15.md) | Not asserted / needs review | Review zero-fee unsigned calls without changing BASEFEE; fee admission and opcode context need separate checks. |
| [H16 — Fee accounting and sequential state diffs](../decisions/H16.md) | Not asserted / needs review | Confirm actual fee accounting and per-entry callMany diffs; storage sequencing alone does not prove the entire rule. |
| [H17 — New-account stateDiff encoding](../decisions/H17.md) | Not asserted / needs review | Review new-account + markers for empty code and zero nonce, independently of prefunded existing accounts. |
| [H18 — EIP-7702 code changes in stateDiff](../decisions/H18.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H19 — vmTrace executing bytecode](../decisions/H19.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H20 — vmTrace step timing and deltas](../decisions/H20.md) | Not asserted / needs review | Refresh after the merged MCOPY fix; retain nested gas timing as an open semantic question. |
| [H21 — vmTrace numeric and optional metadata encoding](../decisions/H21.md) | Not asserted / needs review | Review stack word canonicalization; optional op/idx must not become mandatory for consumers. |
| [H22 — Precompile return bytes](../decisions/H22.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H23 — Special-action address matching](../decisions/H23.md) | Not asserted / needs review | Verify CREATE and SELFDESTRUCT matching against explicit from/to equivalents; do not infer behavior from ordinary CALL filters. |
| [H24 — Sibling failure isolation](../decisions/H24.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H25 — Well-formed errors for rejected raw transactions](../decisions/H25.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H26 — Account deletion across Cancun](../decisions/H26.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H27 — Filter execution across fork boundaries](../decisions/H27.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H28 — Historical state at system-operation boundaries](../decisions/H28.md) | Not asserted / needs review | Investigate historical queries exposing the next block beacon-root update; block N must exclude N+1 changes. |
