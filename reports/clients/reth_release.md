# reth_release: proposed changes

Fresh builds: `Reth Version: 2.6.0+73a3a008`.

Matches mean only the linked assertions matched. They do not certify a whole decision or method. Historical change descriptions require review against fresh results.

| Decision | Fresh assertion results | Historical candidate change / review task |
| --- | --- | --- |
| [H01 — Method coverage](../decisions/H01.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H02 — trace_get selector and return shape](../decisions/H02.md) | 4 change needed | Replace flat/offset selection with one traceAddress path; [] must select root. Existing callers may depend on old indexing. |
| [H03 — Filter composition and mode](../decisions/H03.md) | 1 change needed, 3 matches | Change the default from union to intersection between address lists; explicit union would remain an extension. |
| [H04 — Empty address lists](../decisions/H04.md) | 1 matches | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H05 — Post-merge reward records](../decisions/H05.md) | 2 matches | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H06 — Missing transactions and paths](../decisions/H06.md) | 1 change needed, 4 matches | Return null for unknown individual replay rather than a missing-transaction error. |
| [H07 — Replay transactionHash field](../decisions/H07.md) | 12 change needed | Add transactionHash to individual replay envelopes. |
| [H08 — Empty output and unrequested components](../decisions/H08.md) | 77 matches | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H09 — Failed frame results and error labels](../decisions/H09.md) | 7 matches | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H10 — Creation result field names](../decisions/H10.md) | 4 matches | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H11 — Empty trace-type selection](../decisions/H11.md) | 2 matches | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H12 — Raw-transaction block argument](../decisions/H12.md) | 1 change needed | The baseline rejects a third block argument; preserve existing extension only under a separate profile. |
| [H13 — Signed transaction nonce validation](../decisions/H13.md) | Not asserted / needs review | Review signed nonce validation; ensure simulation does not replace the signed nonce. |
| [H14 — Invalid-parameter error codes](../decisions/H14.md) | 1 matches | Normalize malformed input to -32602 and separate it from valid-but-rejected transactions; code changes affect consumers. |
| [H15 — Unsigned simulation fees and block environment](../decisions/H15.md) | 5 matches | Review zero-fee unsigned calls without changing BASEFEE; fee admission and opcode context need separate checks. |
| [H16 — Fee accounting and sequential state diffs](../decisions/H16.md) | Not asserted / needs review | Confirm actual fee accounting and per-entry callMany diffs; storage sequencing alone does not prove the entire rule. |
| [H17 — New-account stateDiff encoding](../decisions/H17.md) | Not asserted / needs review | Review new-account + markers for empty code and zero nonce, independently of prefunded existing accounts. |
| [H18 — EIP-7702 code changes in stateDiff](../decisions/H18.md) | Not asserted / needs review | Capture EIP-7702 code set/replace/clear changes even when the account already exists; preserve authorization changes across execution revert. |
| [H19 — vmTrace executing bytecode](../decisions/H19.md) | 2 change needed | Capture actually executing constructor and delegated code rather than relying on pre-state address lookup. |
| [H20 — vmTrace step timing and deltas](../decisions/H20.md) | Not asserted / needs review | Refresh after the merged inspector fix; old gas/memory/call-return findings may now be resolved. |
| [H21 — vmTrace numeric and optional metadata encoding](../decisions/H21.md) | 12 matches | Review stack word canonicalization; optional op/idx must not become mandatory for consumers. |
| [H22 — Precompile return bytes](../decisions/H22.md) | 1 matches | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H23 — Special-action address matching](../decisions/H23.md) | Not asserted / needs review | Verify CREATE and SELFDESTRUCT matching against explicit from/to equivalents; do not infer behavior from ordinary CALL filters. |
| [H24 — Sibling failure isolation](../decisions/H24.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H25 — Well-formed errors for rejected raw transactions](../decisions/H25.md) | 4 matches | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H26 — Account deletion across Cancun](../decisions/H26.md) | Not asserted / needs review | Report real pre-Cancun deletion of account fields; preserve existing accounts after EIP-6780. |
| [H27 — Filter execution across fork boundaries](../decisions/H27.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |
| [H28 — Historical state at system-operation boundaries](../decisions/H28.md) | Not asserted / needs review | No specific change established by the historical summary; review the proposed rule and fresh evidence. This is not a pass verdict. |

<details><summary>H09: 7 assertion checks</summary>

- **matches** · `initial` / `transaction-tree`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^transaction-tree$" --output runs/reproduce`
- **matches** · `initial` / `replay-tree-trace`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-tree-trace$" --output runs/reproduce`
- **matches** · `initial` / `transaction-revert`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^transaction-revert$" --output runs/reproduce`
- **matches** · `initial` / `replay-revert-trace`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-revert-trace$" --output runs/reproduce`
- **matches** · `initial` / `block-tree`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^block-tree$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-trace`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-trace$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-trace-priced`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`

</details>

<details><summary>H07: 12 assertion checks</summary>

- **change_needed** · `initial` / `replay-tree-trace`: Individual replay includes its transactionHash.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-tree-trace$" --output runs/reproduce`
- **change_needed** · `initial` / `replay-tree-stateDiff`: Individual replay includes its transactionHash.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-tree-stateDiff$" --output runs/reproduce`
- **change_needed** · `initial` / `replay-tree-vmTrace`: Individual replay includes its transactionHash.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-tree-vmTrace$" --output runs/reproduce`
- **change_needed** · `initial` / `replay-revert-trace`: Individual replay includes its transactionHash.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-revert-trace$" --output runs/reproduce`
- **change_needed** · `initial` / `replay-revert-stateDiff`: Individual replay includes its transactionHash.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-revert-stateDiff$" --output runs/reproduce`
- **change_needed** · `initial` / `replay-revert-vmTrace`: Individual replay includes its transactionHash.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-revert-vmTrace$" --output runs/reproduce`
- **change_needed** · `initial` / `replay-7702-trace`: Individual replay includes its transactionHash.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-7702-trace$" --output runs/reproduce`
- **change_needed** · `initial` / `replay-7702-stateDiff`: Individual replay includes its transactionHash.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-7702-stateDiff$" --output runs/reproduce`
- **change_needed** · `initial` / `replay-7702-vmTrace`: Individual replay includes its transactionHash.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-7702-vmTrace$" --output runs/reproduce`
- **change_needed** · `initial` / `replay-transfer-trace`: Individual replay includes its transactionHash.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-transfer-trace$" --output runs/reproduce`
- **change_needed** · `initial` / `replay-transfer-stateDiff`: Individual replay includes its transactionHash.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-transfer-stateDiff$" --output runs/reproduce`
- **change_needed** · `initial` / `replay-transfer-vmTrace`: Individual replay includes its transactionHash.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-transfer-vmTrace$" --output runs/reproduce`

</details>

<details><summary>H08: 77 assertion checks</summary>

- **matches** · `initial` / `replay-tree-trace`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-tree-trace$" --output runs/reproduce`
- **matches** · `initial` / `replay-tree-trace`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-tree-trace$" --output runs/reproduce`
- **matches** · `initial` / `replay-tree-trace`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-tree-trace$" --output runs/reproduce`
- **matches** · `initial` / `replay-tree-stateDiff`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-tree-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `replay-tree-stateDiff`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-tree-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `replay-tree-stateDiff`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-tree-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `replay-tree-vmTrace`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-tree-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `replay-tree-vmTrace`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-tree-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `replay-tree-vmTrace`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-tree-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `replay-revert-trace`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-revert-trace$" --output runs/reproduce`
- **matches** · `initial` / `replay-revert-trace`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-revert-trace$" --output runs/reproduce`
- **matches** · `initial` / `replay-revert-trace`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-revert-trace$" --output runs/reproduce`
- **matches** · `initial` / `replay-revert-stateDiff`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-revert-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `replay-revert-stateDiff`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-revert-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `replay-revert-stateDiff`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-revert-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `replay-revert-vmTrace`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-revert-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `replay-revert-vmTrace`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-revert-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `replay-revert-vmTrace`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-revert-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `replay-7702-trace`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-7702-trace$" --output runs/reproduce`
- **matches** · `initial` / `replay-7702-trace`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-7702-trace$" --output runs/reproduce`
- **matches** · `initial` / `replay-7702-trace`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-7702-trace$" --output runs/reproduce`
- **matches** · `initial` / `replay-7702-stateDiff`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-7702-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `replay-7702-stateDiff`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-7702-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `replay-7702-stateDiff`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-7702-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `replay-7702-vmTrace`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-7702-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `replay-7702-vmTrace`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-7702-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `replay-7702-vmTrace`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-7702-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-trace`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-trace$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-trace`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-trace$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-trace`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-trace$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-stateDiff`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-stateDiff`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-stateDiff`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-vmTrace`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-vmTrace`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-vmTrace`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-empty-types$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-empty-types$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-empty-types$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-empty-types$" --output runs/reproduce`
- **matches** · `initial` / `call-constructor`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-constructor$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^raw-valid$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-trace-priced`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-trace-priced`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-trace-priced`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-stateDiff-priced`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-stateDiff-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-stateDiff-priced`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-stateDiff-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-stateDiff-priced`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-stateDiff-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-vmTrace-priced`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-vmTrace-priced`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-vmTrace-priced`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types-priced`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types-priced`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types-priced`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types-priced`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-constructor-priced`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid-current-nonce`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^raw-valid-current-nonce$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-trace`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-transfer-trace$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-trace`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-transfer-trace$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-trace`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-transfer-trace$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-stateDiff`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-stateDiff`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-stateDiff`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-vmTrace`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-vmTrace`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-vmTrace`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-identity`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-identity$" --output runs/reproduce`
- **matches** · `initial` / `call-identity`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-identity$" --output runs/reproduce`
- **matches** · `initial` / `replay-transfer-trace`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-transfer-trace$" --output runs/reproduce`
- **matches** · `initial` / `replay-transfer-trace`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-transfer-trace$" --output runs/reproduce`
- **matches** · `initial` / `replay-transfer-trace`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-transfer-trace$" --output runs/reproduce`
- **matches** · `initial` / `replay-transfer-stateDiff`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `replay-transfer-stateDiff`: Unrequested vmTrace is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `replay-transfer-stateDiff`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `replay-transfer-vmTrace`: Unrequested trace is an empty array.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `replay-transfer-vmTrace`: Unrequested stateDiff is null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `replay-transfer-vmTrace`: Output remains a byte string under every trace selection.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-transfer-vmTrace$" --output runs/reproduce`

</details>

<details><summary>H21: 12 assertion checks</summary>

- **matches** · `initial` / `replay-tree-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-tree-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `replay-revert-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-revert-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `replay-7702-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-7702-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-constructor`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-constructor$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^raw-valid$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-vmTrace-priced`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-constructor-priced`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid-current-nonce`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^raw-valid-current-nonce$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-identity`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-identity$" --output runs/reproduce`
- **matches** · `initial` / `replay-transfer-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-transfer-vmTrace$" --output runs/reproduce`

</details>

<details><summary>H05: 2 assertion checks</summary>

- **matches** · `initial` / `block-tree`: A PoS block has no synthetic PoW reward records.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^block-tree$" --output runs/reproduce`
- **matches** · `initial` / `block-transfer`: A PoS block has no synthetic PoW reward records.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^block-transfer$" --output runs/reproduce`

</details>

<details><summary>H02: 4 assertion checks</summary>

- **change_needed** · `initial` / `get-root`: Return one object whose traceAddress equals []. Observed NoneType.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^get-root$" --output runs/reproduce`
- **change_needed** · `initial` / `get-zero`: Return one object whose traceAddress equals [0]. Observed [].
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^get-zero$" --output runs/reproduce`
- **change_needed** · `initial` / `get-one`: Return one object whose traceAddress equals [1]. Observed [0].
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^get-one$" --output runs/reproduce`
- **change_needed** · `initial` / `get-transfer-root`: Return one object whose traceAddress equals []. Observed NoneType.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^get-transfer-root$" --output runs/reproduce`

</details>

<details><summary>H06: 5 assertion checks</summary>

- **matches** · `initial` / `get-missing`: A missing transaction or tree path returns null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^get-missing$" --output runs/reproduce`
- **matches** · `initial` / `transaction-missing`: Unknown transaction returns null, not an empty collection or RPC error.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^transaction-missing$" --output runs/reproduce`
- **change_needed** · `initial` / `replay-missing`: Unknown transaction returns null, not an empty collection or RPC error.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^replay-missing$" --output runs/reproduce`
- **matches** · `initial` / `get-missing-tx`: A missing transaction or tree path returns null.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^get-missing-tx$" --output runs/reproduce`
- **matches** · `initial` / `get-missing-tx`: Unknown transaction returns null, not an empty collection or RPC error.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^get-missing-tx$" --output runs/reproduce`

</details>

<details><summary>H03: 4 assertion checks</summary>

- **matches** · `initial` / `filter-all`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 13 records from this client's block trace.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^filter-all$" --output runs/reproduce`
- **matches** · `initial` / `filter-from`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 5 records from this client's block trace.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^filter-from$" --output runs/reproduce`
- **matches** · `initial` / `filter-to`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 2 records from this client's block trace.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^filter-to$" --output runs/reproduce`
- **change_needed** · `initial` / `filter-both`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 1 records from this client's block trace.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^filter-both$" --output runs/reproduce`

</details>

<details><summary>H04: 1 assertion checks</summary>

- **matches** · `initial` / `filter-empty`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 13 records from this client's block trace.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^filter-empty$" --output runs/reproduce`

</details>

<details><summary>H10: 4 assertion checks</summary>

- **matches** · `initial` / `call-tree-trace`: Successful creation uses address, code and gasUsed.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-trace$" --output runs/reproduce`
- **matches** · `initial` / `call-constructor`: Successful creation uses address, code and gasUsed.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-constructor$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-trace-priced`: Successful creation uses address, code and gasUsed.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-constructor-priced`: Successful creation uses address, code and gasUsed.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`

</details>

<details><summary>H15: 5 assertion checks</summary>

- **matches** · `initial` / `call-tree-trace`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-trace$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-stateDiff`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-vmTrace`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-tree-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-empty-types$" --output runs/reproduce`
- **matches** · `initial` / `call-constructor`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-constructor$" --output runs/reproduce`

</details>

<details><summary>H11: 2 assertion checks</summary>

- **matches** · `initial` / `call-empty-types`: An empty trace-type selection executes successfully.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-empty-types$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types-priced`: An empty trace-type selection executes successfully.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`

</details>

<details><summary>H19: 2 assertion checks</summary>

- **change_needed** · `initial` / `call-constructor`: Creation vmTrace.code is executing initcode.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-constructor$" --output runs/reproduce`
- **change_needed** · `initial` / `call-constructor-priced`: Creation vmTrace.code is executing initcode.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`

</details>

<details><summary>H25: 4 assertion checks</summary>

- **matches** · `initial` / `raw-valid`: Return one complete JSON-RPC response, including on validation failure.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^raw-valid$" --output runs/reproduce`
- **matches** · `initial` / `raw-invalid`: Return one complete JSON-RPC response, including on validation failure.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^raw-invalid$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid-default-block`: Return one complete JSON-RPC response, including on validation failure.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^raw-valid-default-block$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid-current-nonce`: Return one complete JSON-RPC response, including on validation failure.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^raw-valid-current-nonce$" --output runs/reproduce`

</details>

<details><summary>H12: 1 assertion checks</summary>

- **change_needed** · `initial` / `raw-valid`: The two-argument baseline rejects an extra block selector (extension policy remains open).
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^raw-valid$" --output runs/reproduce`

</details>

<details><summary>H14: 1 assertion checks</summary>

- **matches** · `initial` / `raw-invalid`: Malformed input returns invalid params (-32602).
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^raw-invalid$" --output runs/reproduce`

</details>

<details><summary>H22: 1 assertion checks</summary>

- **matches** · `initial` / `call-identity`: The identity precompile call frame preserves its input as return bytes.
  [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients reth_release --corpus initial --case "^call-identity$" --output runs/reproduce`

</details>
