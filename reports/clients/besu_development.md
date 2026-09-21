# besu_development: proposed changes

Fresh builds: `besu/v26.9-develop-d997aad/linux-x86_64/openjdk-java-25`.

Matches mean only the linked assertions matched. They do not certify a whole decision or method. Historical change descriptions require review against fresh results.

| Decision | Fresh assertion results | Historical candidate change / review task |
| --- | --- | --- |
| [H01 — Method coverage](../decisions/H01.md) | 13 unsupported | Decide whether to add trace_replayTransaction or declare it unsupported in the agreed profile. |
| [H02 — trace_get selector and return shape](../decisions/H02.md) | 4 matches | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H03 — Filter composition and mode](../decisions/H03.md) | 1 change needed, 3 matches | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H04 — Empty address lists](../decisions/H04.md) | 1 matches | The draft rejects null filters; historically accepted null, so stricter validation is a compatibility change. |
| [H05 — Post-merge reward records](../decisions/H05.md) | 2 change needed | Remove synthetic zero PoW reward records on PoS blocks; pagination counts will change. |
| [H06 — Missing transactions and paths](../decisions/H06.md) | 1 change needed, 3 matches | Return null rather than [] for unknown transaction lookup. |
| [H07 — Replay transactionHash field](../decisions/H07.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H08 — Empty output and unrequested components](../decisions/H08.md) | 27 matches | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H09 — Failed frame results and error labels](../decisions/H09.md) | 4 change needed | Retain revert bytes and gas where available; use null for inapplicable result. |
| [H10 — Creation result field names](../decisions/H10.md) | 1 change needed, 1 matches | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H11 — Empty trace-type selection](../decisions/H11.md) | 1 change needed, 1 matches | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H12 — Raw-transaction block argument](../decisions/H12.md) | 1 matches | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H13 — Signed transaction nonce validation](../decisions/H13.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H14 — Invalid-parameter error codes](../decisions/H14.md) | 1 matches | Normalize malformed input to -32602 and separate it from valid-but-rejected transactions; code changes affect consumers. |
| [H15 — Unsigned simulation fees and block environment](../decisions/H15.md) | 5 change needed | Review zero-fee unsigned calls without changing BASEFEE; fee admission and opcode context need separate checks. |
| [H16 — Fee accounting and sequential state diffs](../decisions/H16.md) | Not asserted / needs review | Confirm actual fee accounting and per-entry callMany diffs; storage sequencing alone does not prove the entire rule. |
| [H17 — New-account stateDiff encoding](../decisions/H17.md) | Not asserted / needs review | Review new-account + markers for empty code and zero nonce, independently of prefunded existing accounts. |
| [H18 — EIP-7702 code changes in stateDiff](../decisions/H18.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H19 — vmTrace executing bytecode](../decisions/H19.md) | 1 matches | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H20 — vmTrace step timing and deltas](../decisions/H20.md) | Not asserted / needs review | Review same-step VM memory effects, including MCOPY. |
| [H21 — vmTrace numeric and optional metadata encoding](../decisions/H21.md) | 6 matches | Review stack word canonicalization; optional op/idx must not become mandatory for consumers. |
| [H22 — Precompile return bytes](../decisions/H22.md) | 1 change needed | Preserve precompile return bytes in the call-frame result as well as the execution envelope. |
| [H23 — Special-action address matching](../decisions/H23.md) | Not asserted / needs review | Verify CREATE and SELFDESTRUCT matching against explicit from/to equivalents; do not infer behavior from ordinary CALL filters. |
| [H24 — Sibling failure isolation](../decisions/H24.md) | Not asserted / needs review | Keep sibling frame failure status isolated; a reverting sibling must not taint a successful one. |
| [H25 — Well-formed errors for rejected raw transactions](../decisions/H25.md) | 4 matches | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H26 — Account deletion across Cancun](../decisions/H26.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H27 — Filter execution across fork boundaries](../decisions/H27.md) | Not asserted / needs review | Investigate range/per-block discrepancies at fork boundaries; select fork rules separately per block. |
| [H28 — Historical state at system-operation boundaries](../decisions/H28.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |

<details><summary>H09: 4 assertion checks</summary>

- **change_needed** · `initial` / `transaction-tree`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^transaction-tree$" --output runs/reproduce`
- **change_needed** · `initial` / `transaction-revert`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^transaction-revert$" --output runs/reproduce`
- **change_needed** · `initial` / `block-tree`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^block-tree$" --output runs/reproduce`
- **change_needed** · `initial` / `call-tree-trace-priced`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`

</details>

<details><summary>H01: 13 assertion checks</summary>

- **unsupported** · `initial` / `replay-tree-trace`: trace_replayTransaction Method coverage remains a profile decision.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^replay-tree-trace$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-tree-stateDiff`: trace_replayTransaction Method coverage remains a profile decision.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^replay-tree-stateDiff$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-tree-vmTrace`: trace_replayTransaction Method coverage remains a profile decision.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^replay-tree-vmTrace$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-revert-trace`: trace_replayTransaction Method coverage remains a profile decision.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^replay-revert-trace$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-revert-stateDiff`: trace_replayTransaction Method coverage remains a profile decision.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^replay-revert-stateDiff$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-revert-vmTrace`: trace_replayTransaction Method coverage remains a profile decision.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^replay-revert-vmTrace$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-7702-trace`: trace_replayTransaction Method coverage remains a profile decision.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^replay-7702-trace$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-7702-stateDiff`: trace_replayTransaction Method coverage remains a profile decision.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^replay-7702-stateDiff$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-7702-vmTrace`: trace_replayTransaction Method coverage remains a profile decision.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^replay-7702-vmTrace$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-missing`: trace_replayTransaction Method coverage remains a profile decision.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^replay-missing$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-transfer-trace`: trace_replayTransaction Method coverage remains a profile decision.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^replay-transfer-trace$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-transfer-stateDiff`: trace_replayTransaction Method coverage remains a profile decision.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^replay-transfer-stateDiff$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-transfer-vmTrace`: trace_replayTransaction Method coverage remains a profile decision.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^replay-transfer-vmTrace$" --output runs/reproduce`

</details>

<details><summary>H05: 2 assertion checks</summary>

- **change_needed** · `initial` / `block-tree`: A PoS block has no synthetic PoW reward records.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^block-tree$" --output runs/reproduce`
- **change_needed** · `initial` / `block-transfer`: A PoS block has no synthetic PoW reward records.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^block-transfer$" --output runs/reproduce`

</details>

<details><summary>H02: 4 assertion checks</summary>

- **matches** · `initial` / `get-root`: Return one object whose traceAddress equals []. Observed [].
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^get-root$" --output runs/reproduce`
- **matches** · `initial` / `get-zero`: Return one object whose traceAddress equals [0]. Observed [0].
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^get-zero$" --output runs/reproduce`
- **matches** · `initial` / `get-one`: Return one object whose traceAddress equals [1]. Observed [1].
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^get-one$" --output runs/reproduce`
- **matches** · `initial` / `get-transfer-root`: Return one object whose traceAddress equals []. Observed [].
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^get-transfer-root$" --output runs/reproduce`

</details>

<details><summary>H06: 4 assertion checks</summary>

- **matches** · `initial` / `get-missing`: A missing transaction or tree path returns null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^get-missing$" --output runs/reproduce`
- **change_needed** · `initial` / `transaction-missing`: Unknown transaction returns null, not an empty collection or RPC error.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^transaction-missing$" --output runs/reproduce`
- **matches** · `initial` / `get-missing-tx`: A missing transaction or tree path returns null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^get-missing-tx$" --output runs/reproduce`
- **matches** · `initial` / `get-missing-tx`: Unknown transaction returns null, not an empty collection or RPC error.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^get-missing-tx$" --output runs/reproduce`

</details>

<details><summary>H03: 4 assertion checks</summary>

- **matches** · `initial` / `filter-all`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 14 records from this client's block trace.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^filter-all$" --output runs/reproduce`
- **matches** · `initial` / `filter-from`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 5 records from this client's block trace.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^filter-from$" --output runs/reproduce`
- **change_needed** · `initial` / `filter-to`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 2 records from this client's block trace.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^filter-to$" --output runs/reproduce`
- **matches** · `initial` / `filter-both`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 1 records from this client's block trace.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^filter-both$" --output runs/reproduce`

</details>

<details><summary>H04: 1 assertion checks</summary>

- **matches** · `initial` / `filter-empty`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 14 records from this client's block trace.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^filter-empty$" --output runs/reproduce`

</details>

<details><summary>H15: 5 assertion checks</summary>

- **change_needed** · `initial` / `call-tree-trace`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-tree-trace$" --output runs/reproduce`
- **change_needed** · `initial` / `call-tree-stateDiff`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-tree-stateDiff$" --output runs/reproduce`
- **change_needed** · `initial` / `call-tree-vmTrace`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-tree-vmTrace$" --output runs/reproduce`
- **change_needed** · `initial` / `call-empty-types`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-empty-types$" --output runs/reproduce`
- **change_needed** · `initial` / `call-constructor`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-constructor$" --output runs/reproduce`

</details>

<details><summary>H11: 2 assertion checks</summary>

- **change_needed** · `initial` / `call-empty-types`: An empty trace-type selection executes successfully.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-empty-types$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types-priced`: An empty trace-type selection executes successfully.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`

</details>

<details><summary>H25: 4 assertion checks</summary>

- **matches** · `initial` / `raw-valid`: Return one complete JSON-RPC response, including on validation failure.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^raw-valid$" --output runs/reproduce`
- **matches** · `initial` / `raw-invalid`: Return one complete JSON-RPC response, including on validation failure.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^raw-invalid$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid-default-block`: Return one complete JSON-RPC response, including on validation failure.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^raw-valid-default-block$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid-current-nonce`: Return one complete JSON-RPC response, including on validation failure.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^raw-valid-current-nonce$" --output runs/reproduce`

</details>

<details><summary>H12: 1 assertion checks</summary>

- **matches** · `initial` / `raw-valid`: The two-argument baseline rejects an extra block selector (extension policy remains open).
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^raw-valid$" --output runs/reproduce`

</details>

<details><summary>H14: 1 assertion checks</summary>

- **matches** · `initial` / `raw-invalid`: Malformed input returns invalid params (-32602).
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^raw-invalid$" --output runs/reproduce`

</details>

<details><summary>H08: 27 assertion checks</summary>

- **matches** · `initial` / `call-tree-trace-priced`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-trace-priced`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-trace-priced`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-stateDiff-priced`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-tree-stateDiff-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-stateDiff-priced`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-tree-stateDiff-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-stateDiff-priced`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-tree-stateDiff-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-vmTrace-priced`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-vmTrace-priced`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-vmTrace-priced`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types-priced`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types-priced`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types-priced`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types-priced`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-constructor-priced`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid-default-block`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^raw-valid-default-block$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid-current-nonce`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^raw-valid-current-nonce$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-trace`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-transfer-trace$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-trace`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-transfer-trace$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-trace`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-transfer-trace$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-stateDiff`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-stateDiff`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-stateDiff`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-vmTrace`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-vmTrace`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-vmTrace`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-identity`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-identity$" --output runs/reproduce`
- **matches** · `initial` / `call-identity`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-identity$" --output runs/reproduce`

</details>

<details><summary>H10: 2 assertion checks</summary>

- **change_needed** · `initial` / `call-tree-trace-priced`: Successful creation uses address, code and gasUsed.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-constructor-priced`: Successful creation uses address, code and gasUsed.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`

</details>

<details><summary>H21: 6 assertion checks</summary>

- **matches** · `initial` / `call-tree-vmTrace-priced`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-constructor-priced`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid-default-block`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^raw-valid-default-block$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid-current-nonce`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^raw-valid-current-nonce$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-identity`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-identity$" --output runs/reproduce`

</details>

<details><summary>H19: 1 assertion checks</summary>

- **matches** · `initial` / `call-constructor-priced`: Creation vmTrace.code is executing initcode.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`

</details>

<details><summary>H22: 1 assertion checks</summary>

- **change_needed** · `initial` / `call-identity`: The identity precompile call frame preserves its input as return bytes.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_development --corpus initial --case "^call-identity$" --output runs/reproduce`

</details>
