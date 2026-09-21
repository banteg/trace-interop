# nethermind_release: proposed changes

Tested builds: `1.39.3+28cbe2a0`.

Matches mean only the linked assertions matched. They do not certify a whole decision or method.

| Decision | Assertion results | Required change / review task |
| --- | --- | --- |
| [H01 — Method coverage](../decisions/H01.md) | Not asserted / needs review | Needs review; no assertion covers this decision. |
| [H02 — trace_get selector and return shape](../decisions/H02.md) | 6 change needed | Use one nested path and return a singular object/null instead of a list; this changes the response type. |
| [H03 — Filter composition and mode](../decisions/H03.md) | 5 matches | No change identified by these checks. |
| [H04 — Empty address lists](../decisions/H04.md) | 3 change needed | Treat [] address lists as unrestricted rather than matching nothing. |
| [H05 — Post-merge reward records](../decisions/H05.md) | 11 change needed | Remove synthetic zero PoW reward records on PoS blocks; pagination counts will change. |
| [H06 — Missing transactions and paths](../decisions/H06.md) | 5 change needed | Replace unknown-transaction/path exceptions with null; distinguish unavailable history. |
| [H07 — Replay transactionHash field](../decisions/H07.md) | 12 matches | No change identified by these checks. |
| [H08 — Empty output and unrequested components](../decisions/H08.md) | 13 change needed, 128 matches | Preserve actual output bytes when only stateDiff is selected; null loses nonempty output too. |
| [H09 — Failed frame results and error labels](../decisions/H09.md) | 21 change needed | Retain failed-frame result information where available instead of omitting result. |
| [H10 — Creation result field names](../decisions/H10.md) | 9 matches | No change identified by these checks. |
| [H11 — Empty trace-type selection](../decisions/H11.md) | 3 change needed | Accept empty trace selections without an internal reduction exception. |
| [H12 — Raw-transaction block argument](../decisions/H12.md) | 1 matches | No change identified by these checks. |
| [H13 — Signed transaction nonce validation](../decisions/H13.md) | 2 change needed | Reject signed nonce mismatches without substituting the account nonce. |
| [H14 — Invalid-parameter error codes](../decisions/H14.md) | 1 change needed, 4 matches | Normalize malformed input to -32602 and separate it from valid-but-rejected transactions; code changes affect consumers. |
| [H15 — Unsigned simulation fees and block environment](../decisions/H15.md) | 1 change needed, 4 matches | Review zero-fee unsigned calls without changing BASEFEE; fee admission and opcode context need separate checks. |
| [H16 — Fee accounting and sequential state diffs](../decisions/H16.md) | 2 matches | No change identified by these checks. |
| [H17 — New-account stateDiff encoding](../decisions/H17.md) | 1 matches | No change identified by these checks. |
| [H18 — EIP-7702 code changes in stateDiff](../decisions/H18.md) | 6 matches | No change identified by these checks. |
| [H19 — vmTrace executing bytecode](../decisions/H19.md) | 3 matches | No change identified by these checks. |
| [H20 — vmTrace step timing and deltas](../decisions/H20.md) | 2 matches | No change identified by these checks. |
| [H21 — vmTrace numeric and optional metadata encoding](../decisions/H21.md) | 25 change needed, 20 matches | Review stack word canonicalization; optional op/idx must not become mandatory for consumers. |
| [H22 — Precompile return bytes](../decisions/H22.md) | 1 matches | No change identified by these checks. |
| [H23 — Special-action address matching](../decisions/H23.md) | 4 matches | No change identified by these checks. |
| [H24 — Sibling failure isolation](../decisions/H24.md) | 2 matches | No change identified by these checks. |
| [H25 — Well-formed errors for rejected raw transactions](../decisions/H25.md) | 20 change needed, 20 matches | Avoid partial/malformed JSON when signed-transaction validation fails. |
| [H26 — Account deletion across Cancun](../decisions/H26.md) | 2 change needed, 2 matches | Delete code/nonce before Cancun; preserve an existing account after EIP-6780. |
| [H27 — Filter execution across fork boundaries](../decisions/H27.md) | 16 matches | No change identified by these checks. |
| [H28 — Historical state at system-operation boundaries](../decisions/H28.md) | 12 matches | No change identified by these checks. |

<details><summary>H02: 6 assertion checks</summary>

- **change_needed** · `verified-a` / `get-nested-positive`: Return one object whose traceAddress equals [6, 0]. Observed list.
  [Compare responses](../cases/a/get-nested-positive.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^get-nested-positive$" --output runs/reproduce`
- **change_needed** · `verified-a` / `get-nested-parent`: Return one object whose traceAddress equals [6]. Observed list.
  [Compare responses](../cases/a/get-nested-parent.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^get-nested-parent$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `get-root`: Return one object whose traceAddress equals []. Observed list.
  [Compare responses](../cases/initial/get-root.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^get-root$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `get-zero`: Return one object whose traceAddress equals [0]. Observed list.
  [Compare responses](../cases/initial/get-zero.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^get-zero$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `get-one`: Return one object whose traceAddress equals [1]. Observed list.
  [Compare responses](../cases/initial/get-one.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^get-one$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `get-transfer-root`: Return one object whose traceAddress equals []. Observed list.
  [Compare responses](../cases/initial/get-transfer-root.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^get-transfer-root$" --output runs/reproduce`

</details>

<details><summary>H14: 5 assertion checks</summary>

- **matches** · `verified-a` / `get-path-wrong-type`: Malformed input returns invalid params (-32602).
  [Compare responses](../cases/a/get-path-wrong-type.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^get-path-wrong-type$" --output runs/reproduce`
- **matches** · `verified-a` / `call-wrong-type`: Malformed input returns invalid params (-32602).
  [Compare responses](../cases/a/call-wrong-type.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-wrong-type$" --output runs/reproduce`
- **matches** · `verified-a` / `call-unknown-mode`: Malformed input returns invalid params (-32602).
  [Compare responses](../cases/a/call-unknown-mode.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-unknown-mode$" --output runs/reproduce`
- **matches** · `verified-a` / `call-scalar-mode`: Malformed input returns invalid params (-32602).
  [Compare responses](../cases/a/call-scalar-mode.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-scalar-mode$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `raw-invalid`: Malformed input returns invalid params (-32602).
  [Compare responses](../cases/initial/raw-invalid.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^raw-invalid$" --output runs/reproduce`

</details>

<details><summary>H09: 21 assertion checks</summary>

- **change_needed** · `verified-a` / `transaction-tree`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/a/transaction-tree.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^transaction-tree$" --output runs/reproduce`
- **change_needed** · `verified-a` / `call-siblings-ok-revert`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/a/call-siblings-ok-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-siblings-ok-revert$" --output runs/reproduce`
- **change_needed** · `verified-a` / `call-siblings-revert-ok`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/a/call-siblings-revert-ok.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-siblings-revert-ok$" --output runs/reproduce`
- **change_needed** · `verified-a` / `auth-replace`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/a/auth-replace.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-replace$" --output runs/reproduce`
- **change_needed** · `verified-a` / `auth-set-revert`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/a/auth-set-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-set-revert$" --output runs/reproduce`
- **change_needed** · `verified-a` / `block-2`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/a/block-2.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^block-2$" --output runs/reproduce`
- **change_needed** · `verified-fork-followup` / `beacon-call-55`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/fork-followup/beacon-call-55.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^beacon-call-55$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-36`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/forks/block-36.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^block-36$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-48`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/forks/block-48.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^block-48$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-51`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/forks/block-51.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^block-51$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-60`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/forks/block-60.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^block-60$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `mcopy-trace-55`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/forks/mcopy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^mcopy-trace-55$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `transaction-tree`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/initial/transaction-tree.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^transaction-tree$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `replay-tree-trace`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/initial/replay-tree-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-tree-trace$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `transaction-revert`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/initial/transaction-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^transaction-revert$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `replay-revert-trace`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/initial/replay-revert-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-revert-trace$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `block-tree`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/initial/block-tree.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^block-tree$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-tree-trace`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/initial/call-tree-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-trace$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-tree-trace-priced`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/initial/call-tree-trace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `call-siblings-revert-ok`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/repeat/call-siblings-revert-ok.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^call-siblings-revert-ok$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `auth-set-revert`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/repeat/auth-set-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^auth-set-revert$" --output runs/reproduce`

</details>

<details><summary>H03: 5 assertion checks</summary>

- **matches** · `verified-a` / `filter-all`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 14 records from this client's block trace.
  [Compare responses](../cases/a/filter-all.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^filter-all$" --output runs/reproduce`
- **matches** · `verified-initial` / `filter-all`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 14 records from this client's block trace.
  [Compare responses](../cases/initial/filter-all.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^filter-all$" --output runs/reproduce`
- **matches** · `verified-initial` / `filter-from`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 5 records from this client's block trace.
  [Compare responses](../cases/initial/filter-from.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^filter-from$" --output runs/reproduce`
- **matches** · `verified-initial` / `filter-to`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 2 records from this client's block trace.
  [Compare responses](../cases/initial/filter-to.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^filter-to$" --output runs/reproduce`
- **matches** · `verified-initial` / `filter-both`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 1 records from this client's block trace.
  [Compare responses](../cases/initial/filter-both.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^filter-both$" --output runs/reproduce`

</details>

<details><summary>H04: 3 assertion checks</summary>

- **change_needed** · `verified-a` / `filter-from-empty-to-set`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 2 records from this client's block trace.
  [Compare responses](../cases/a/filter-from-empty-to-set.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^filter-from-empty-to-set$" --output runs/reproduce`
- **change_needed** · `verified-a` / `filter-to-empty-from-set`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 5 records from this client's block trace.
  [Compare responses](../cases/a/filter-to-empty-from-set.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^filter-to-empty-from-set$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `filter-empty`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 14 records from this client's block trace.
  [Compare responses](../cases/initial/filter-empty.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^filter-empty$" --output runs/reproduce`

</details>

<details><summary>H23: 4 assertion checks</summary>

- **matches** · `verified-a` / `filter-created-to`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 1 records from this client's block trace.
  [Compare responses](../cases/a/filter-created-to.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^filter-created-to$" --output runs/reproduce`
- **matches** · `verified-a` / `filter-creator-from`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 7 records from this client's block trace.
  [Compare responses](../cases/a/filter-creator-from.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^filter-creator-from$" --output runs/reproduce`
- **matches** · `verified-a` / `filter-suicide-from`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 1 records from this client's block trace.
  [Compare responses](../cases/a/filter-suicide-from.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^filter-suicide-from$" --output runs/reproduce`
- **matches** · `verified-a` / `filter-suicide-beneficiary`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 2 records from this client's block trace.
  [Compare responses](../cases/a/filter-suicide-beneficiary.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^filter-suicide-beneficiary$" --output runs/reproduce`

</details>

<details><summary>H08: 141 assertion checks</summary>

- **matches** · `verified-a` / `call-return42`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/call-return42.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-return42$" --output runs/reproduce`
- **matches** · `verified-a` / `call-siblings-ok-revert`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/call-siblings-ok-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-siblings-ok-revert$" --output runs/reproduce`
- **matches** · `verified-a` / `call-siblings-revert-ok`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/call-siblings-revert-ok.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-siblings-revert-ok$" --output runs/reproduce`
- **matches** · `verified-a` / `call-mixed-create`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/call-mixed-create.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-mixed-create$" --output runs/reproduce`
- **matches** · `verified-a` / `call-gas7400`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/call-gas7400.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-gas7400$" --output runs/reproduce`
- **matches** · `verified-a` / `call-mcopy`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/call-mcopy.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-mcopy$" --output runs/reproduce`
- **matches** · `verified-a` / `call-destroy`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/call-destroy.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-destroy$" --output runs/reproduce`
- **matches** · `verified-a` / `state-only-nonempty-output`: Unrequested trace is an empty array.
  [Compare responses](../cases/a/state-only-nonempty-output.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^state-only-nonempty-output$" --output runs/reproduce`
- **matches** · `verified-a` / `state-only-nonempty-output`: Unrequested vmTrace is null.
  [Compare responses](../cases/a/state-only-nonempty-output.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^state-only-nonempty-output$" --output runs/reproduce`
- **change_needed** · `verified-a` / `state-only-nonempty-output`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/state-only-nonempty-output.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^state-only-nonempty-output$" --output runs/reproduce`
- **change_needed** · `verified-a` / `state-only-nonempty-output`: The return42 contract still returns word 42.
  [Compare responses](../cases/a/state-only-nonempty-output.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^state-only-nonempty-output$" --output runs/reproduce`
- **matches** · `verified-a` / `vm-only-nonempty-output`: Unrequested trace is an empty array.
  [Compare responses](../cases/a/vm-only-nonempty-output.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^vm-only-nonempty-output$" --output runs/reproduce`
- **matches** · `verified-a` / `vm-only-nonempty-output`: Unrequested stateDiff is null.
  [Compare responses](../cases/a/vm-only-nonempty-output.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^vm-only-nonempty-output$" --output runs/reproduce`
- **matches** · `verified-a` / `vm-only-nonempty-output`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/vm-only-nonempty-output.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^vm-only-nonempty-output$" --output runs/reproduce`
- **matches** · `verified-a` / `vm-only-nonempty-output`: The return42 contract still returns word 42.
  [Compare responses](../cases/a/vm-only-nonempty-output.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^vm-only-nonempty-output$" --output runs/reproduce`
- **matches** · `verified-a` / `prefunded-empty`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/prefunded-empty.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^prefunded-empty$" --output runs/reproduce`
- **matches** · `verified-a` / `control-storage-after-many`: Unrequested vmTrace is null.
  [Compare responses](../cases/a/control-storage-after-many.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^control-storage-after-many$" --output runs/reproduce`
- **matches** · `verified-a` / `control-storage-after-many`: Unrequested stateDiff is null.
  [Compare responses](../cases/a/control-storage-after-many.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^control-storage-after-many$" --output runs/reproduce`
- **matches** · `verified-a` / `control-storage-after-many`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/control-storage-after-many.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^control-storage-after-many$" --output runs/reproduce`
- **matches** · `verified-a` / `call-unknown-field`: Unrequested vmTrace is null.
  [Compare responses](../cases/a/call-unknown-field.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-unknown-field$" --output runs/reproduce`
- **matches** · `verified-a` / `call-unknown-field`: Unrequested stateDiff is null.
  [Compare responses](../cases/a/call-unknown-field.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-unknown-field$" --output runs/reproduce`
- **matches** · `verified-a` / `call-unknown-field`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/call-unknown-field.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-unknown-field$" --output runs/reproduce`
- **matches** · `verified-a` / `raw-valid`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/raw-valid.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^raw-valid$" --output runs/reproduce`
- **matches** · `verified-a` / `raw-nonce-high`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/raw-nonce-high.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^raw-nonce-high$" --output runs/reproduce`
- **matches** · `verified-a` / `auth-set`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/auth-set.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-set$" --output runs/reproduce`
- **matches** · `verified-a` / `auth-replace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/auth-replace.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-replace$" --output runs/reproduce`
- **matches** · `verified-a` / `auth-clear`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/auth-clear.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-clear$" --output runs/reproduce`
- **matches** · `verified-a` / `auth-set-revert`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/a/auth-set-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-set-revert$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `destroy-trace-55`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/fork-followup/destroy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^destroy-trace-55$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `destroy-trace-56`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/fork-followup/destroy-trace-56.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^destroy-trace-56$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `beacon-call-55`: Unrequested vmTrace is null.
  [Compare responses](../cases/fork-followup/beacon-call-55.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^beacon-call-55$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `beacon-call-55`: Unrequested stateDiff is null.
  [Compare responses](../cases/fork-followup/beacon-call-55.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^beacon-call-55$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `beacon-call-55`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/fork-followup/beacon-call-55.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^beacon-call-55$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `beacon-call-56`: Unrequested vmTrace is null.
  [Compare responses](../cases/fork-followup/beacon-call-56.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^beacon-call-56$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `beacon-call-56`: Unrequested stateDiff is null.
  [Compare responses](../cases/fork-followup/beacon-call-56.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^beacon-call-56$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `beacon-call-56`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/fork-followup/beacon-call-56.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^beacon-call-56$" --output runs/reproduce`
- **matches** · `verified-forks` / `destroy-trace-55`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/forks/destroy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^destroy-trace-55$" --output runs/reproduce`
- **matches** · `verified-forks` / `mcopy-trace-55`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/forks/mcopy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^mcopy-trace-55$" --output runs/reproduce`
- **matches** · `verified-forks` / `destroy-trace-56`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/forks/destroy-trace-56.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^destroy-trace-56$" --output runs/reproduce`
- **matches** · `verified-forks` / `mcopy-trace-56`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/forks/mcopy-trace-56.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^mcopy-trace-56$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-tree-trace`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/replay-tree-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-tree-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-tree-trace`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/replay-tree-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-tree-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-tree-trace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/replay-tree-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-tree-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-tree-stateDiff`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/replay-tree-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-tree-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-tree-stateDiff`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/replay-tree-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-tree-stateDiff$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `replay-tree-stateDiff`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/replay-tree-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-tree-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-tree-vmTrace`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/replay-tree-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-tree-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-tree-vmTrace`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/replay-tree-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-tree-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-tree-vmTrace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/replay-tree-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-tree-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-revert-trace`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/replay-revert-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-revert-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-revert-trace`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/replay-revert-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-revert-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-revert-trace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/replay-revert-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-revert-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-revert-stateDiff`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/replay-revert-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-revert-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-revert-stateDiff`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/replay-revert-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-revert-stateDiff$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `replay-revert-stateDiff`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/replay-revert-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-revert-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-revert-vmTrace`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/replay-revert-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-revert-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-revert-vmTrace`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/replay-revert-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-revert-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-revert-vmTrace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/replay-revert-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-revert-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-7702-trace`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/replay-7702-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-7702-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-7702-trace`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/replay-7702-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-7702-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-7702-trace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/replay-7702-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-7702-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-7702-stateDiff`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/replay-7702-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-7702-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-7702-stateDiff`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/replay-7702-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-7702-stateDiff$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `replay-7702-stateDiff`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/replay-7702-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-7702-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-7702-vmTrace`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/replay-7702-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-7702-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-7702-vmTrace`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/replay-7702-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-7702-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-7702-vmTrace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/replay-7702-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-7702-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-trace`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/call-tree-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-trace`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-tree-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-trace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-tree-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-stateDiff`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/call-tree-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-stateDiff`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/call-tree-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-stateDiff$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-tree-stateDiff`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-tree-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-vmTrace`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/call-tree-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-vmTrace`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-tree-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-vmTrace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-tree-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-constructor`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-constructor.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-constructor$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-trace-priced`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/call-tree-trace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-trace-priced`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-tree-trace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-trace-priced`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-tree-trace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-stateDiff-priced`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/call-tree-stateDiff-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-stateDiff-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-stateDiff-priced`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/call-tree-stateDiff-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-stateDiff-priced$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-tree-stateDiff-priced`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-tree-stateDiff-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-stateDiff-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-vmTrace-priced`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/call-tree-vmTrace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-vmTrace-priced`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-tree-vmTrace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-vmTrace-priced`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-tree-vmTrace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-constructor-priced`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-constructor-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-valid-default-block`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/raw-valid-default-block.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^raw-valid-default-block$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-valid-current-nonce`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/raw-valid-current-nonce.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^raw-valid-current-nonce$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-trace`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/call-transfer-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-transfer-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-trace`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-transfer-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-transfer-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-trace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-transfer-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-transfer-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-stateDiff`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/call-transfer-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-stateDiff`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/call-transfer-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-transfer-stateDiff$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-transfer-stateDiff`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-transfer-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-vmTrace`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/call-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-vmTrace`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-vmTrace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-identity`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-identity.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-identity$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-identity`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-identity.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-identity$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-transfer-trace`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/replay-transfer-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-transfer-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-transfer-trace`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/replay-transfer-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-transfer-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-transfer-trace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/replay-transfer-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-transfer-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-transfer-stateDiff`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/replay-transfer-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-transfer-stateDiff`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/replay-transfer-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-transfer-stateDiff$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `replay-transfer-stateDiff`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/replay-transfer-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-transfer-vmTrace`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/replay-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-transfer-vmTrace`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/replay-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-transfer-vmTrace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/replay-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-return42`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/call-return42.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^call-return42$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-siblings-revert-ok`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/call-siblings-revert-ok.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^call-siblings-revert-ok$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-mixed-create`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/call-mixed-create.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^call-mixed-create$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-gas7400`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/call-gas7400.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^call-gas7400$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-mcopy`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/call-mcopy.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^call-mcopy$" --output runs/reproduce`
- **matches** · `verified-repeat` / `state-only-nonempty-output`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/state-only-nonempty-output.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^state-only-nonempty-output$" --output runs/reproduce`
- **matches** · `verified-repeat` / `state-only-nonempty-output`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/state-only-nonempty-output.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^state-only-nonempty-output$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `state-only-nonempty-output`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/state-only-nonempty-output.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^state-only-nonempty-output$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `state-only-nonempty-output`: The return42 contract still returns word 42.
  [Compare responses](../cases/repeat/state-only-nonempty-output.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^state-only-nonempty-output$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-valid.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-valid$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-nonce-high.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-nonce-high$" --output runs/reproduce`
- **matches** · `verified-repeat` / `auth-clear`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/auth-clear.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^auth-clear$" --output runs/reproduce`
- **matches** · `verified-repeat` / `auth-set-revert`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/auth-set-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^auth-set-revert$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-trace`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/raw-valid-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-valid-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-trace`: Unrequested stateDiff is null.
  [Compare responses](../cases/repeat/raw-valid-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-valid-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-trace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-valid-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-valid-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-stateDiff`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/raw-valid-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-valid-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-stateDiff`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/raw-valid-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-valid-stateDiff$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-valid-stateDiff`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-valid-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-valid-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-vmTrace`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/raw-valid-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-valid-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-vmTrace`: Unrequested stateDiff is null.
  [Compare responses](../cases/repeat/raw-valid-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-valid-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-vmTrace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-valid-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-valid-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-trace`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/raw-nonce-high-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-nonce-high-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-trace`: Unrequested stateDiff is null.
  [Compare responses](../cases/repeat/raw-nonce-high-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-nonce-high-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-trace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-nonce-high-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-nonce-high-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-stateDiff`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/raw-nonce-high-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-nonce-high-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-stateDiff`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/raw-nonce-high-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-nonce-high-stateDiff$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-nonce-high-stateDiff`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-nonce-high-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-nonce-high-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-vmTrace`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/raw-nonce-high-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-nonce-high-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-vmTrace`: Unrequested stateDiff is null.
  [Compare responses](../cases/repeat/raw-nonce-high-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-nonce-high-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-vmTrace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-nonce-high-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-nonce-high-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `constructor`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/constructor.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^constructor$" --output runs/reproduce`

</details>

<details><summary>H21: 45 assertion checks</summary>

- **change_needed** · `verified-a` / `call-return42`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/a/call-return42.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-return42$" --output runs/reproduce`
- **change_needed** · `verified-a` / `call-siblings-ok-revert`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/a/call-siblings-ok-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-siblings-ok-revert$" --output runs/reproduce`
- **change_needed** · `verified-a` / `call-siblings-revert-ok`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/a/call-siblings-revert-ok.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-siblings-revert-ok$" --output runs/reproduce`
- **change_needed** · `verified-a` / `call-mixed-create`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/a/call-mixed-create.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-mixed-create$" --output runs/reproduce`
- **change_needed** · `verified-a` / `call-gas7400`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/a/call-gas7400.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-gas7400$" --output runs/reproduce`
- **change_needed** · `verified-a` / `call-mcopy`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/a/call-mcopy.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-mcopy$" --output runs/reproduce`
- **matches** · `verified-a` / `call-destroy`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/a/call-destroy.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-destroy$" --output runs/reproduce`
- **change_needed** · `verified-a` / `vm-only-nonempty-output`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/a/vm-only-nonempty-output.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^vm-only-nonempty-output$" --output runs/reproduce`
- **matches** · `verified-a` / `prefunded-empty`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/a/prefunded-empty.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^prefunded-empty$" --output runs/reproduce`
- **matches** · `verified-a` / `raw-valid`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/a/raw-valid.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^raw-valid$" --output runs/reproduce`
- **matches** · `verified-a` / `raw-nonce-high`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/a/raw-nonce-high.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^raw-nonce-high$" --output runs/reproduce`
- **change_needed** · `verified-a` / `auth-set`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/a/auth-set.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-set$" --output runs/reproduce`
- **change_needed** · `verified-a` / `auth-replace`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/a/auth-replace.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-replace$" --output runs/reproduce`
- **matches** · `verified-a` / `auth-clear`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/a/auth-clear.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-clear$" --output runs/reproduce`
- **change_needed** · `verified-a` / `auth-set-revert`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/a/auth-set-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-set-revert$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `destroy-trace-55`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/fork-followup/destroy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^destroy-trace-55$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `destroy-trace-56`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/fork-followup/destroy-trace-56.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^destroy-trace-56$" --output runs/reproduce`
- **matches** · `verified-forks` / `destroy-trace-55`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/forks/destroy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^destroy-trace-55$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `mcopy-trace-55`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/forks/mcopy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^mcopy-trace-55$" --output runs/reproduce`
- **matches** · `verified-forks` / `destroy-trace-56`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/forks/destroy-trace-56.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^destroy-trace-56$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `mcopy-trace-56`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/forks/mcopy-trace-56.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^mcopy-trace-56$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `replay-tree-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/replay-tree-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-tree-vmTrace$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `replay-revert-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/replay-revert-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-revert-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-7702-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/replay-7702-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-7702-vmTrace$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-tree-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/call-tree-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-vmTrace$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-constructor`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/call-constructor.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-constructor$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-tree-vmTrace-priced`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/call-tree-vmTrace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-constructor-priced`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/call-constructor-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-valid-default-block`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/raw-valid-default-block.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^raw-valid-default-block$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-valid-current-nonce`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/raw-valid-current-nonce.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^raw-valid-current-nonce$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/call-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-identity`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/call-identity.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-identity$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-transfer-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/replay-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-transfer-vmTrace$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `call-return42`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/call-return42.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^call-return42$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `call-siblings-revert-ok`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/call-siblings-revert-ok.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^call-siblings-revert-ok$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `call-mixed-create`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/call-mixed-create.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^call-mixed-create$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `call-gas7400`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/call-gas7400.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^call-gas7400$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `call-mcopy`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/call-mcopy.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^call-mcopy$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/raw-valid.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-valid$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/raw-nonce-high.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-nonce-high$" --output runs/reproduce`
- **matches** · `verified-repeat` / `auth-clear`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/auth-clear.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^auth-clear$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `auth-set-revert`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/auth-set-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^auth-set-revert$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/raw-valid-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-valid-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/raw-nonce-high-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-nonce-high-vmTrace$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `constructor`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/constructor.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^constructor$" --output runs/reproduce`

</details>

<details><summary>H24: 2 assertion checks</summary>

- **matches** · `verified-a` / `call-siblings-revert-ok`: The successful second sibling retains its output and has no error.
  [Compare responses](../cases/a/call-siblings-revert-ok.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-siblings-revert-ok$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-siblings-revert-ok`: The successful second sibling retains its output and has no error.
  [Compare responses](../cases/repeat/call-siblings-revert-ok.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^call-siblings-revert-ok$" --output runs/reproduce`

</details>

<details><summary>H10: 9 assertion checks</summary>

- **matches** · `verified-a` / `call-mixed-create`: Successful creation uses address, code and gasUsed.
  [Compare responses](../cases/a/call-mixed-create.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-mixed-create$" --output runs/reproduce`
- **matches** · `verified-a` / `call-mixed-create`: Successful creation uses address, code and gasUsed.
  [Compare responses](../cases/a/call-mixed-create.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-mixed-create$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-trace`: Successful creation uses address, code and gasUsed.
  [Compare responses](../cases/initial/call-tree-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-constructor`: Successful creation uses address, code and gasUsed.
  [Compare responses](../cases/initial/call-constructor.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-constructor$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-trace-priced`: Successful creation uses address, code and gasUsed.
  [Compare responses](../cases/initial/call-tree-trace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-constructor-priced`: Successful creation uses address, code and gasUsed.
  [Compare responses](../cases/initial/call-constructor-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-mixed-create`: Successful creation uses address, code and gasUsed.
  [Compare responses](../cases/repeat/call-mixed-create.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^call-mixed-create$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-mixed-create`: Successful creation uses address, code and gasUsed.
  [Compare responses](../cases/repeat/call-mixed-create.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^call-mixed-create$" --output runs/reproduce`
- **matches** · `verified-repeat` / `constructor`: Successful creation uses address, code and gasUsed.
  [Compare responses](../cases/repeat/constructor.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^constructor$" --output runs/reproduce`

</details>

<details><summary>H20: 2 assertion checks</summary>

- **matches** · `verified-a` / `call-mcopy`: MCOPY reports its same-step write of word 42 at offset 32.
  [Compare responses](../cases/a/call-mcopy.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^call-mcopy$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-mcopy`: MCOPY reports its same-step write of word 42 at offset 32.
  [Compare responses](../cases/repeat/call-mcopy.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^call-mcopy$" --output runs/reproduce`

</details>

<details><summary>H17: 1 assertion checks</summary>

- **matches** · `verified-a` / `prefunded-empty`: An existing prefunded account does not acquire creation markers for empty code or zero nonce.
  [Compare responses](../cases/a/prefunded-empty.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^prefunded-empty$" --output runs/reproduce`

</details>

<details><summary>H11: 3 assertion checks</summary>

- **change_needed** · `verified-a` / `empty-types`: An empty trace-type selection executes successfully.
  [Compare responses](../cases/a/empty-types.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^empty-types$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-empty-types`: An empty trace-type selection executes successfully.
  [Compare responses](../cases/initial/call-empty-types.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-empty-types$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-empty-types-priced`: An empty trace-type selection executes successfully.
  [Compare responses](../cases/initial/call-empty-types-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`

</details>

<details><summary>H16: 2 assertion checks</summary>

- **matches** · `verified-a` / `many-storage-write-revert-read`: Sequential calls retain prior writes and roll back reverted writes.
  [Compare responses](../cases/a/many-storage-write-revert-read.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^many-storage-write-revert-read$" --output runs/reproduce`
- **matches** · `verified-repeat` / `many-storage-write-revert-read`: Sequential calls retain prior writes and roll back reverted writes.
  [Compare responses](../cases/repeat/many-storage-write-revert-read.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^many-storage-write-revert-read$" --output runs/reproduce`

</details>

<details><summary>H25: 40 assertion checks</summary>

- **matches** · `verified-a` / `raw-valid`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/a/raw-valid.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^raw-valid$" --output runs/reproduce`
- **matches** · `verified-a` / `raw-nonce-high`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/a/raw-nonce-high.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^raw-nonce-high$" --output runs/reproduce`
- **change_needed** · `verified-a` / `raw-wrong-chain`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/a/raw-wrong-chain.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^raw-wrong-chain$" --output runs/reproduce`
- **change_needed** · `verified-a` / `raw-insufficient-funds`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/a/raw-insufficient-funds.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^raw-insufficient-funds$" --output runs/reproduce`
- **change_needed** · `verified-a` / `raw-low-gas`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/a/raw-low-gas.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^raw-low-gas$" --output runs/reproduce`
- **change_needed** · `verified-a` / `raw-below-basefee`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/a/raw-below-basefee.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^raw-below-basefee$" --output runs/reproduce`
- **matches** · `verified-a` / `auth-set`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/a/auth-set.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-set$" --output runs/reproduce`
- **matches** · `verified-a` / `auth-replace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/a/auth-replace.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-replace$" --output runs/reproduce`
- **matches** · `verified-a` / `auth-clear`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/a/auth-clear.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-clear$" --output runs/reproduce`
- **matches** · `verified-a` / `auth-set-revert`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/a/auth-set-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-set-revert$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-valid`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/initial/raw-valid.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^raw-valid$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-invalid`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/initial/raw-invalid.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^raw-invalid$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-valid-default-block`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/initial/raw-valid-default-block.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^raw-valid-default-block$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-valid-current-nonce`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/initial/raw-valid-current-nonce.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^raw-valid-current-nonce$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-valid.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-valid$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-nonce-high.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-nonce-high$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-wrong-chain`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-wrong-chain.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-wrong-chain$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-insufficient-funds`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-insufficient-funds.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-insufficient-funds$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-low-gas`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-low-gas.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-low-gas$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-below-basefee`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-below-basefee.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-below-basefee$" --output runs/reproduce`
- **matches** · `verified-repeat` / `auth-clear`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/auth-clear.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^auth-clear$" --output runs/reproduce`
- **matches** · `verified-repeat` / `auth-set-revert`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/auth-set-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^auth-set-revert$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-trace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-valid-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-valid-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-stateDiff`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-valid-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-valid-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-vmTrace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-valid-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-valid-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-trace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-nonce-high-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-nonce-high-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-stateDiff`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-nonce-high-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-nonce-high-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-vmTrace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-nonce-high-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-nonce-high-vmTrace$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-wrong-chain-trace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-wrong-chain-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-wrong-chain-trace$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-wrong-chain-stateDiff`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-wrong-chain-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-wrong-chain-stateDiff$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-wrong-chain-vmTrace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-wrong-chain-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-wrong-chain-vmTrace$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-insufficient-funds-trace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-insufficient-funds-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-insufficient-funds-trace$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-insufficient-funds-stateDiff`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-insufficient-funds-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-insufficient-funds-stateDiff$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-insufficient-funds-vmTrace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-insufficient-funds-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-insufficient-funds-vmTrace$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-low-gas-trace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-low-gas-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-low-gas-trace$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-low-gas-stateDiff`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-low-gas-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-low-gas-stateDiff$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-low-gas-vmTrace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-low-gas-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-low-gas-vmTrace$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-below-basefee-trace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-below-basefee-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-below-basefee-trace$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-below-basefee-stateDiff`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-below-basefee-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-below-basefee-stateDiff$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-below-basefee-vmTrace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-below-basefee-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-below-basefee-vmTrace$" --output runs/reproduce`

</details>

<details><summary>H13: 2 assertion checks</summary>

- **change_needed** · `verified-a` / `raw-nonce-high`: A signed nonce mismatch is rejected rather than replaced.
  [Compare responses](../cases/a/raw-nonce-high.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^raw-nonce-high$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `raw-nonce-high`: A signed nonce mismatch is rejected rather than replaced.
  [Compare responses](../cases/repeat/raw-nonce-high.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^raw-nonce-high$" --output runs/reproduce`

</details>

<details><summary>H18: 6 assertion checks</summary>

- **matches** · `verified-a` / `auth-set`: EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.
  [Compare responses](../cases/a/auth-set.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-set$" --output runs/reproduce`
- **matches** · `verified-a` / `auth-replace`: EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.
  [Compare responses](../cases/a/auth-replace.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-replace$" --output runs/reproduce`
- **matches** · `verified-a` / `auth-clear`: EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.
  [Compare responses](../cases/a/auth-clear.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-clear$" --output runs/reproduce`
- **matches** · `verified-a` / `auth-set-revert`: EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.
  [Compare responses](../cases/a/auth-set-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^auth-set-revert$" --output runs/reproduce`
- **matches** · `verified-repeat` / `auth-clear`: EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.
  [Compare responses](../cases/repeat/auth-clear.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^auth-clear$" --output runs/reproduce`
- **matches** · `verified-repeat` / `auth-set-revert`: EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.
  [Compare responses](../cases/repeat/auth-set-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^auth-set-revert$" --output runs/reproduce`

</details>

<details><summary>H05: 11 assertion checks</summary>

- **change_needed** · `verified-a` / `block-2`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/a/block-2.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^block-2$" --output runs/reproduce`
- **change_needed** · `verified-a` / `block-3`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/a/block-3.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^block-3$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-48`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/forks/block-48.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^block-48$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-51`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/forks/block-51.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^block-51$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-52`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/forks/block-52.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^block-52$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-55`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/forks/block-55.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^block-55$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-56`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/forks/block-56.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^block-56$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-59`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/forks/block-59.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^block-59$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-60`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/forks/block-60.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^block-60$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `block-tree`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/initial/block-tree.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^block-tree$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `block-transfer`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/initial/block-transfer.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^block-transfer$" --output runs/reproduce`

</details>

<details><summary>H27: 16 assertion checks</summary>

- **matches** · `verified-a` / `filter-two-blocks`: Range traces equal concatenated per-block traces in canonical order.
  [Compare responses](../cases/a/filter-two-blocks.md) · [Raw responses](../../evidence/2026-09-21/verified-a/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-a/manifest.json --clients nethermind_release --corpus a --case "^filter-two-blocks$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-35`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-35.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^filter-35$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-36`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-36.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^filter-36$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-47`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-47.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^filter-47$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-48`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-48.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^filter-48$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-51`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-51.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^filter-51$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-52`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-52.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^filter-52$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-55`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-55.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^filter-55$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-56`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-56.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^filter-56$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-59`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-59.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^filter-59$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-60`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-60.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^filter-60$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-across-36`: A fork-crossing range equals the corresponding per-block traces.
  [Compare responses](../cases/forks/filter-across-36.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^filter-across-36$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-across-48`: A fork-crossing range equals the corresponding per-block traces.
  [Compare responses](../cases/forks/filter-across-48.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^filter-across-48$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-across-52`: A fork-crossing range equals the corresponding per-block traces.
  [Compare responses](../cases/forks/filter-across-52.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^filter-across-52$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-across-56`: A fork-crossing range equals the corresponding per-block traces.
  [Compare responses](../cases/forks/filter-across-56.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^filter-across-56$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-across-60`: A fork-crossing range equals the corresponding per-block traces.
  [Compare responses](../cases/forks/filter-across-60.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^filter-across-60$" --output runs/reproduce`

</details>

<details><summary>H26: 4 assertion checks</summary>

- **change_needed** · `verified-fork-followup` / `destroy-trace-55`: Delete code/nonce before Cancun; preserve an existing account after EIP-6780.
  [Compare responses](../cases/fork-followup/destroy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^destroy-trace-55$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `destroy-trace-56`: Delete code/nonce before Cancun; preserve an existing account after EIP-6780.
  [Compare responses](../cases/fork-followup/destroy-trace-56.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^destroy-trace-56$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `destroy-trace-55`: Delete code/nonce before Cancun; preserve an existing account after EIP-6780.
  [Compare responses](../cases/forks/destroy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^destroy-trace-55$" --output runs/reproduce`
- **matches** · `verified-forks` / `destroy-trace-56`: Delete code/nonce before Cancun; preserve an existing account after EIP-6780.
  [Compare responses](../cases/forks/destroy-trace-56.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^destroy-trace-56$" --output runs/reproduce`

</details>

<details><summary>H28: 12 assertion checks</summary>

- **matches** · `verified-fork-followup` / `system-beacon-55-560`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/fork-followup/system-beacon-55-560.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^system-beacon-55-560$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `system-beacon-55-8751`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/fork-followup/system-beacon-55-8751.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^system-beacon-55-8751$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `system-beacon-56-560`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/fork-followup/system-beacon-56-560.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^system-beacon-56-560$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `system-beacon-56-8751`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/fork-followup/system-beacon-56-8751.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^system-beacon-56-8751$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `beacon-call-55`: Historical trace_call uses only system changes through the selected block.
  [Compare responses](../cases/fork-followup/beacon-call-55.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^beacon-call-55$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `beacon-call-56`: Historical trace_call uses only system changes through the selected block.
  [Compare responses](../cases/fork-followup/beacon-call-56.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients nethermind_release --corpus fork-followup --case "^beacon-call-56$" --output runs/reproduce`
- **matches** · `verified-forks` / `system-beacon-55-560`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/forks/system-beacon-55-560.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^system-beacon-55-560$" --output runs/reproduce`
- **matches** · `verified-forks` / `system-beacon-55-8751`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/forks/system-beacon-55-8751.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^system-beacon-55-8751$" --output runs/reproduce`
- **matches** · `verified-forks` / `system-beacon-56-560`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/forks/system-beacon-56-560.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^system-beacon-56-560$" --output runs/reproduce`
- **matches** · `verified-forks` / `system-beacon-56-8751`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/forks/system-beacon-56-8751.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^system-beacon-56-8751$" --output runs/reproduce`
- **matches** · `verified-forks` / `system-beacon-57-560`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/forks/system-beacon-57-560.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^system-beacon-57-560$" --output runs/reproduce`
- **matches** · `verified-forks` / `system-beacon-57-8751`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/forks/system-beacon-57-8751.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients nethermind_release --corpus forks --case "^system-beacon-57-8751$" --output runs/reproduce`

</details>

<details><summary>H07: 12 assertion checks</summary>

- **matches** · `verified-initial` / `replay-tree-trace`: Individual replay includes its transactionHash.
  [Compare responses](../cases/initial/replay-tree-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-tree-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-tree-stateDiff`: Individual replay includes its transactionHash.
  [Compare responses](../cases/initial/replay-tree-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-tree-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-tree-vmTrace`: Individual replay includes its transactionHash.
  [Compare responses](../cases/initial/replay-tree-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-tree-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-revert-trace`: Individual replay includes its transactionHash.
  [Compare responses](../cases/initial/replay-revert-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-revert-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-revert-stateDiff`: Individual replay includes its transactionHash.
  [Compare responses](../cases/initial/replay-revert-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-revert-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-revert-vmTrace`: Individual replay includes its transactionHash.
  [Compare responses](../cases/initial/replay-revert-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-revert-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-7702-trace`: Individual replay includes its transactionHash.
  [Compare responses](../cases/initial/replay-7702-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-7702-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-7702-stateDiff`: Individual replay includes its transactionHash.
  [Compare responses](../cases/initial/replay-7702-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-7702-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-7702-vmTrace`: Individual replay includes its transactionHash.
  [Compare responses](../cases/initial/replay-7702-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-7702-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-transfer-trace`: Individual replay includes its transactionHash.
  [Compare responses](../cases/initial/replay-transfer-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-transfer-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-transfer-stateDiff`: Individual replay includes its transactionHash.
  [Compare responses](../cases/initial/replay-transfer-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `replay-transfer-vmTrace`: Individual replay includes its transactionHash.
  [Compare responses](../cases/initial/replay-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-transfer-vmTrace$" --output runs/reproduce`

</details>

<details><summary>H06: 5 assertion checks</summary>

- **change_needed** · `verified-initial` / `get-missing`: A missing transaction or tree path returns null.
  [Compare responses](../cases/initial/get-missing.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^get-missing$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `transaction-missing`: Unknown transaction returns null, not an empty collection or RPC error.
  [Compare responses](../cases/initial/transaction-missing.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^transaction-missing$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `replay-missing`: Unknown transaction returns null, not an empty collection or RPC error.
  [Compare responses](../cases/initial/replay-missing.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^replay-missing$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `get-missing-tx`: A missing transaction or tree path returns null.
  [Compare responses](../cases/initial/get-missing-tx.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^get-missing-tx$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `get-missing-tx`: Unknown transaction returns null, not an empty collection or RPC error.
  [Compare responses](../cases/initial/get-missing-tx.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^get-missing-tx$" --output runs/reproduce`

</details>

<details><summary>H15: 5 assertion checks</summary>

- **matches** · `verified-initial` / `call-tree-trace`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Compare responses](../cases/initial/call-tree-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-stateDiff`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Compare responses](../cases/initial/call-tree-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-vmTrace`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Compare responses](../cases/initial/call-tree-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-tree-vmTrace$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-empty-types`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Compare responses](../cases/initial/call-empty-types.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-empty-types$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-constructor`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Compare responses](../cases/initial/call-constructor.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-constructor$" --output runs/reproduce`

</details>

<details><summary>H19: 3 assertion checks</summary>

- **matches** · `verified-initial` / `call-constructor`: Creation vmTrace.code is executing initcode.
  [Compare responses](../cases/initial/call-constructor.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-constructor$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-constructor-priced`: Creation vmTrace.code is executing initcode.
  [Compare responses](../cases/initial/call-constructor-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`
- **matches** · `verified-repeat` / `constructor`: Creation vmTrace.code is executing initcode.
  [Compare responses](../cases/repeat/constructor.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients nethermind_release --corpus repeat --case "^constructor$" --output runs/reproduce`

</details>

<details><summary>H12: 1 assertion checks</summary>

- **matches** · `verified-initial` / `raw-valid`: The two-argument baseline rejects an extra block selector (extension policy remains open).
  [Compare responses](../cases/initial/raw-valid.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^raw-valid$" --output runs/reproduce`

</details>

<details><summary>H22: 1 assertion checks</summary>

- **matches** · `verified-initial` / `call-identity`: The identity precompile call frame preserves its input as return bytes.
  [Compare responses](../cases/initial/call-identity.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients nethermind_release --corpus initial --case "^call-identity$" --output runs/reproduce`

</details>
