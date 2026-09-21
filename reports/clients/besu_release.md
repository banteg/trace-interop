# besu_release: proposed changes

Tested builds: `besu/v26.8.1/linux-x86_64/openjdk-java-25`.

Matches mean only the linked assertions matched. They do not certify a whole decision or method.

| Decision | Assertion results | Required change / review task |
| --- | --- | --- |
| [H01 — Method coverage](../decisions/H01.md) | 26 unsupported | Decide whether to add trace_replayTransaction or declare it unsupported in the agreed profile. |
| [H02 — trace_get selector and return shape](../decisions/H02.md) | 8 matches | No change identified by these checks. |
| [H03 — Filter composition and mode](../decisions/H03.md) | 2 change needed, 6 matches | Address matching is OR within each list, AND across lists, with action-specific endpoints. |
| [H04 — Empty address lists](../decisions/H04.md) | 2 matches | No change identified by these checks. |
| [H05 — Post-merge reward records](../decisions/H05.md) | 11 change needed | Remove synthetic zero PoW reward records on PoS blocks; pagination counts will change. |
| [H06 — Missing transactions and paths](../decisions/H06.md) | 2 change needed, 6 matches | Return null rather than [] for unknown transaction lookup. |
| [H07 — Replay transactionHash field](../decisions/H07.md) | Not asserted / needs review | Needs review; no assertion covers this decision. |
| [H08 — Empty output and unrequested components](../decisions/H08.md) | 138 matches | No change identified by these checks. |
| [H09 — Failed frame results and error labels](../decisions/H09.md) | 16 change needed | Retain revert bytes and gas where available; use null for inapplicable result. |
| [H10 — Creation result field names](../decisions/H10.md) | 2 change needed, 5 matches | Use address, code and gasUsed consistently for successful creation frames. |
| [H11 — Empty trace-type selection](../decisions/H11.md) | 2 change needed, 2 matches | An empty trace-type selection executes successfully. |
| [H12 — Raw-transaction block argument](../decisions/H12.md) | 2 matches | No change identified by these checks. |
| [H13 — Signed transaction nonce validation](../decisions/H13.md) | 1 change needed | Reject signed nonce mismatches without substituting the account nonce. |
| [H14 — Invalid-parameter error codes](../decisions/H14.md) | 2 matches | No change identified by these checks. |
| [H15 — Unsigned simulation fees and block environment](../decisions/H15.md) | 10 change needed | Review zero-fee unsigned calls without changing BASEFEE; fee admission and opcode context need separate checks. |
| [H16 — Fee accounting and sequential state diffs](../decisions/H16.md) | 1 matches | No change identified by these checks. |
| [H17 — New-account stateDiff encoding](../decisions/H17.md) | Not asserted / needs review | Needs review; no assertion covers this decision. |
| [H18 — EIP-7702 code changes in stateDiff](../decisions/H18.md) | 2 matches | No change identified by these checks. |
| [H19 — vmTrace executing bytecode](../decisions/H19.md) | 3 matches | No change identified by these checks. |
| [H20 — vmTrace step timing and deltas](../decisions/H20.md) | 1 change needed | Review same-step VM memory effects, including MCOPY. |
| [H21 — vmTrace numeric and optional metadata encoding](../decisions/H21.md) | 38 matches | No change identified by these checks. |
| [H22 — Precompile return bytes](../decisions/H22.md) | 2 change needed | Preserve precompile return bytes in the call-frame result as well as the execution envelope. |
| [H23 — Special-action address matching](../decisions/H23.md) | Not asserted / needs review | Needs review; no assertion covers this decision. |
| [H24 — Sibling failure isolation](../decisions/H24.md) | 1 change needed | Keep sibling frame failure status isolated; a reverting sibling must not taint a successful one. |
| [H25 — Well-formed errors for rejected raw transactions](../decisions/H25.md) | 34 matches | No change identified by these checks. |
| [H26 — Account deletion across Cancun](../decisions/H26.md) | 4 matches | No change identified by these checks. |
| [H27 — Filter execution across fork boundaries](../decisions/H27.md) | 3 change needed, 12 matches | Investigate range/per-block discrepancies at fork boundaries; select fork rules separately per block. |
| [H28 — Historical state at system-operation boundaries](../decisions/H28.md) | 12 matches | No change identified by these checks. |

<details><summary>H09: 16 assertion checks</summary>

- **change_needed** · `initial` / `transaction-tree`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/initial/transaction-tree.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^transaction-tree$" --output runs/reproduce`
- **change_needed** · `initial` / `transaction-revert`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/initial/transaction-revert.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^transaction-revert$" --output runs/reproduce`
- **change_needed** · `initial` / `block-tree`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/initial/block-tree.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^block-tree$" --output runs/reproduce`
- **change_needed** · `initial` / `call-tree-trace-priced`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/initial/call-tree-trace-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **change_needed** · `verified-fork-followup` / `beacon-call-55`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/fork-followup/beacon-call-55.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^beacon-call-55$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-36`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/forks/block-36.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^block-36$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-48`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/forks/block-48.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^block-48$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-51`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/forks/block-51.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^block-51$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-60`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/forks/block-60.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^block-60$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `mcopy-trace-55`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/forks/mcopy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^mcopy-trace-55$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `transaction-tree`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/initial/transaction-tree.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^transaction-tree$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `transaction-revert`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/initial/transaction-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^transaction-revert$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `block-tree`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/initial/block-tree.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^block-tree$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-tree-trace-priced`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/initial/call-tree-trace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `call-siblings-revert-ok`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/repeat/call-siblings-revert-ok.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^call-siblings-revert-ok$" --output runs/reproduce`
- **change_needed** · `verified-repeat` / `auth-set-revert`: Failed frames have an explicit result; REVERT preserves return bytes and measured gas.
  [Compare responses](../cases/repeat/auth-set-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^auth-set-revert$" --output runs/reproduce`

</details>

<details><summary>H01: 26 assertion checks</summary>

- **unsupported** · `initial` / `replay-tree-trace`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-tree-trace.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^replay-tree-trace$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-tree-stateDiff`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-tree-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^replay-tree-stateDiff$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-tree-vmTrace`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-tree-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^replay-tree-vmTrace$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-revert-trace`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-revert-trace.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^replay-revert-trace$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-revert-stateDiff`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-revert-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^replay-revert-stateDiff$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-revert-vmTrace`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-revert-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^replay-revert-vmTrace$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-7702-trace`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-7702-trace.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^replay-7702-trace$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-7702-stateDiff`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-7702-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^replay-7702-stateDiff$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-7702-vmTrace`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-7702-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^replay-7702-vmTrace$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-missing`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-missing.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^replay-missing$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-transfer-trace`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-transfer-trace.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^replay-transfer-trace$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-transfer-stateDiff`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-transfer-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^replay-transfer-stateDiff$" --output runs/reproduce`
- **unsupported** · `initial` / `replay-transfer-vmTrace`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^replay-transfer-vmTrace$" --output runs/reproduce`
- **unsupported** · `verified-initial` / `replay-tree-trace`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-tree-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^replay-tree-trace$" --output runs/reproduce`
- **unsupported** · `verified-initial` / `replay-tree-stateDiff`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-tree-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^replay-tree-stateDiff$" --output runs/reproduce`
- **unsupported** · `verified-initial` / `replay-tree-vmTrace`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-tree-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^replay-tree-vmTrace$" --output runs/reproduce`
- **unsupported** · `verified-initial` / `replay-revert-trace`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-revert-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^replay-revert-trace$" --output runs/reproduce`
- **unsupported** · `verified-initial` / `replay-revert-stateDiff`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-revert-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^replay-revert-stateDiff$" --output runs/reproduce`
- **unsupported** · `verified-initial` / `replay-revert-vmTrace`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-revert-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^replay-revert-vmTrace$" --output runs/reproduce`
- **unsupported** · `verified-initial` / `replay-7702-trace`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-7702-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^replay-7702-trace$" --output runs/reproduce`
- **unsupported** · `verified-initial` / `replay-7702-stateDiff`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-7702-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^replay-7702-stateDiff$" --output runs/reproduce`
- **unsupported** · `verified-initial` / `replay-7702-vmTrace`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-7702-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^replay-7702-vmTrace$" --output runs/reproduce`
- **unsupported** · `verified-initial` / `replay-missing`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-missing.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^replay-missing$" --output runs/reproduce`
- **unsupported** · `verified-initial` / `replay-transfer-trace`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-transfer-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^replay-transfer-trace$" --output runs/reproduce`
- **unsupported** · `verified-initial` / `replay-transfer-stateDiff`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-transfer-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^replay-transfer-stateDiff$" --output runs/reproduce`
- **unsupported** · `verified-initial` / `replay-transfer-vmTrace`: trace_replayTransaction Method coverage remains a profile decision.
  [Compare responses](../cases/initial/replay-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^replay-transfer-vmTrace$" --output runs/reproduce`

</details>

<details><summary>H05: 11 assertion checks</summary>

- **change_needed** · `initial` / `block-tree`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/initial/block-tree.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^block-tree$" --output runs/reproduce`
- **change_needed** · `initial` / `block-transfer`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/initial/block-transfer.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^block-transfer$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-48`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/forks/block-48.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^block-48$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-51`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/forks/block-51.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^block-51$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-52`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/forks/block-52.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^block-52$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-55`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/forks/block-55.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^block-55$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-56`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/forks/block-56.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^block-56$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-59`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/forks/block-59.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^block-59$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `block-60`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/forks/block-60.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^block-60$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `block-tree`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/initial/block-tree.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^block-tree$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `block-transfer`: A PoS block has no synthetic PoW reward records.
  [Compare responses](../cases/initial/block-transfer.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^block-transfer$" --output runs/reproduce`

</details>

<details><summary>H02: 8 assertion checks</summary>

- **matches** · `initial` / `get-root`: Return one object whose traceAddress equals []. Observed [].
  [Compare responses](../cases/initial/get-root.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^get-root$" --output runs/reproduce`
- **matches** · `initial` / `get-zero`: Return one object whose traceAddress equals [0]. Observed [0].
  [Compare responses](../cases/initial/get-zero.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^get-zero$" --output runs/reproduce`
- **matches** · `initial` / `get-one`: Return one object whose traceAddress equals [1]. Observed [1].
  [Compare responses](../cases/initial/get-one.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^get-one$" --output runs/reproduce`
- **matches** · `initial` / `get-transfer-root`: Return one object whose traceAddress equals []. Observed [].
  [Compare responses](../cases/initial/get-transfer-root.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^get-transfer-root$" --output runs/reproduce`
- **matches** · `verified-initial` / `get-root`: Return one object whose traceAddress equals []. Observed [].
  [Compare responses](../cases/initial/get-root.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^get-root$" --output runs/reproduce`
- **matches** · `verified-initial` / `get-zero`: Return one object whose traceAddress equals [0]. Observed [0].
  [Compare responses](../cases/initial/get-zero.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^get-zero$" --output runs/reproduce`
- **matches** · `verified-initial` / `get-one`: Return one object whose traceAddress equals [1]. Observed [1].
  [Compare responses](../cases/initial/get-one.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^get-one$" --output runs/reproduce`
- **matches** · `verified-initial` / `get-transfer-root`: Return one object whose traceAddress equals []. Observed [].
  [Compare responses](../cases/initial/get-transfer-root.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^get-transfer-root$" --output runs/reproduce`

</details>

<details><summary>H06: 8 assertion checks</summary>

- **matches** · `initial` / `get-missing`: A missing transaction or tree path returns null.
  [Compare responses](../cases/initial/get-missing.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^get-missing$" --output runs/reproduce`
- **change_needed** · `initial` / `transaction-missing`: Unknown transaction returns null, not an empty collection or RPC error.
  [Compare responses](../cases/initial/transaction-missing.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^transaction-missing$" --output runs/reproduce`
- **matches** · `initial` / `get-missing-tx`: A missing transaction or tree path returns null.
  [Compare responses](../cases/initial/get-missing-tx.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^get-missing-tx$" --output runs/reproduce`
- **matches** · `initial` / `get-missing-tx`: Unknown transaction returns null, not an empty collection or RPC error.
  [Compare responses](../cases/initial/get-missing-tx.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^get-missing-tx$" --output runs/reproduce`
- **matches** · `verified-initial` / `get-missing`: A missing transaction or tree path returns null.
  [Compare responses](../cases/initial/get-missing.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^get-missing$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `transaction-missing`: Unknown transaction returns null, not an empty collection or RPC error.
  [Compare responses](../cases/initial/transaction-missing.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^transaction-missing$" --output runs/reproduce`
- **matches** · `verified-initial` / `get-missing-tx`: A missing transaction or tree path returns null.
  [Compare responses](../cases/initial/get-missing-tx.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^get-missing-tx$" --output runs/reproduce`
- **matches** · `verified-initial` / `get-missing-tx`: Unknown transaction returns null, not an empty collection or RPC error.
  [Compare responses](../cases/initial/get-missing-tx.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^get-missing-tx$" --output runs/reproduce`

</details>

<details><summary>H03: 8 assertion checks</summary>

- **matches** · `initial` / `filter-all`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 14 records from this client's block trace.
  [Compare responses](../cases/initial/filter-all.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^filter-all$" --output runs/reproduce`
- **matches** · `initial` / `filter-from`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 5 records from this client's block trace.
  [Compare responses](../cases/initial/filter-from.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^filter-from$" --output runs/reproduce`
- **change_needed** · `initial` / `filter-to`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 2 records from this client's block trace.
  [Compare responses](../cases/initial/filter-to.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^filter-to$" --output runs/reproduce`
- **matches** · `initial` / `filter-both`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 1 records from this client's block trace.
  [Compare responses](../cases/initial/filter-both.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^filter-both$" --output runs/reproduce`
- **matches** · `verified-initial` / `filter-all`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 14 records from this client's block trace.
  [Compare responses](../cases/initial/filter-all.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^filter-all$" --output runs/reproduce`
- **matches** · `verified-initial` / `filter-from`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 5 records from this client's block trace.
  [Compare responses](../cases/initial/filter-from.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^filter-from$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `filter-to`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 2 records from this client's block trace.
  [Compare responses](../cases/initial/filter-to.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^filter-to$" --output runs/reproduce`
- **matches** · `verified-initial` / `filter-both`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 1 records from this client's block trace.
  [Compare responses](../cases/initial/filter-both.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^filter-both$" --output runs/reproduce`

</details>

<details><summary>H04: 2 assertion checks</summary>

- **matches** · `initial` / `filter-empty`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 14 records from this client's block trace.
  [Compare responses](../cases/initial/filter-empty.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^filter-empty$" --output runs/reproduce`
- **matches** · `verified-initial` / `filter-empty`: Address matching is OR within each list, AND across lists, with action-specific endpoints. Expected 14 records from this client's block trace.
  [Compare responses](../cases/initial/filter-empty.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^filter-empty$" --output runs/reproduce`

</details>

<details><summary>H15: 10 assertion checks</summary>

- **change_needed** · `initial` / `call-tree-trace`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Compare responses](../cases/initial/call-tree-trace.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-trace$" --output runs/reproduce`
- **change_needed** · `initial` / `call-tree-stateDiff`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Compare responses](../cases/initial/call-tree-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-stateDiff$" --output runs/reproduce`
- **change_needed** · `initial` / `call-tree-vmTrace`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Compare responses](../cases/initial/call-tree-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-vmTrace$" --output runs/reproduce`
- **change_needed** · `initial` / `call-empty-types`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Compare responses](../cases/initial/call-empty-types.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-empty-types$" --output runs/reproduce`
- **change_needed** · `initial` / `call-constructor`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Compare responses](../cases/initial/call-constructor.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-constructor$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-tree-trace`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Compare responses](../cases/initial/call-tree-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-trace$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-tree-stateDiff`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Compare responses](../cases/initial/call-tree-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-stateDiff$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-tree-vmTrace`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Compare responses](../cases/initial/call-tree-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-vmTrace$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-empty-types`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Compare responses](../cases/initial/call-empty-types.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-empty-types$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-constructor`: Explicit zero-fee unsigned execution is accepted; block-environment preservation needs additional checks.
  [Compare responses](../cases/initial/call-constructor.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-constructor$" --output runs/reproduce`

</details>

<details><summary>H11: 4 assertion checks</summary>

- **change_needed** · `initial` / `call-empty-types`: An empty trace-type selection executes successfully.
  [Compare responses](../cases/initial/call-empty-types.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-empty-types$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types-priced`: An empty trace-type selection executes successfully.
  [Compare responses](../cases/initial/call-empty-types-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-empty-types`: An empty trace-type selection executes successfully.
  [Compare responses](../cases/initial/call-empty-types.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-empty-types$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-empty-types-priced`: An empty trace-type selection executes successfully.
  [Compare responses](../cases/initial/call-empty-types-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`

</details>

<details><summary>H25: 34 assertion checks</summary>

- **matches** · `initial` / `raw-valid`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/initial/raw-valid.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^raw-valid$" --output runs/reproduce`
- **matches** · `initial` / `raw-invalid`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/initial/raw-invalid.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^raw-invalid$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid-default-block`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/initial/raw-valid-default-block.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^raw-valid-default-block$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid-current-nonce`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/initial/raw-valid-current-nonce.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^raw-valid-current-nonce$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-valid`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/initial/raw-valid.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^raw-valid$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-invalid`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/initial/raw-invalid.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^raw-invalid$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-valid-default-block`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/initial/raw-valid-default-block.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^raw-valid-default-block$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-valid-current-nonce`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/initial/raw-valid-current-nonce.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^raw-valid-current-nonce$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-valid.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-valid$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-nonce-high.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-nonce-high$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-wrong-chain`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-wrong-chain.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-wrong-chain$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-insufficient-funds`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-insufficient-funds.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-insufficient-funds$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-low-gas`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-low-gas.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-low-gas$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-below-basefee`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-below-basefee.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-below-basefee$" --output runs/reproduce`
- **matches** · `verified-repeat` / `auth-clear`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/auth-clear.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^auth-clear$" --output runs/reproduce`
- **matches** · `verified-repeat` / `auth-set-revert`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/auth-set-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^auth-set-revert$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-trace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-valid-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-valid-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-stateDiff`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-valid-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-valid-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-vmTrace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-valid-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-valid-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-trace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-nonce-high-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-nonce-high-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-stateDiff`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-nonce-high-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-nonce-high-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-vmTrace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-nonce-high-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-nonce-high-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-wrong-chain-trace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-wrong-chain-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-wrong-chain-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-wrong-chain-stateDiff`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-wrong-chain-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-wrong-chain-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-wrong-chain-vmTrace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-wrong-chain-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-wrong-chain-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-insufficient-funds-trace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-insufficient-funds-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-insufficient-funds-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-insufficient-funds-stateDiff`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-insufficient-funds-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-insufficient-funds-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-insufficient-funds-vmTrace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-insufficient-funds-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-insufficient-funds-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-low-gas-trace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-low-gas-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-low-gas-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-low-gas-stateDiff`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-low-gas-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-low-gas-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-low-gas-vmTrace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-low-gas-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-low-gas-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-below-basefee-trace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-below-basefee-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-below-basefee-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-below-basefee-stateDiff`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-below-basefee-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-below-basefee-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-below-basefee-vmTrace`: Return one complete JSON-RPC response, including on validation failure.
  [Compare responses](../cases/repeat/raw-below-basefee-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-below-basefee-vmTrace$" --output runs/reproduce`

</details>

<details><summary>H12: 2 assertion checks</summary>

- **matches** · `initial` / `raw-valid`: The two-argument baseline rejects an extra block selector (extension policy remains open).
  [Compare responses](../cases/initial/raw-valid.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^raw-valid$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-valid`: The two-argument baseline rejects an extra block selector (extension policy remains open).
  [Compare responses](../cases/initial/raw-valid.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^raw-valid$" --output runs/reproduce`

</details>

<details><summary>H14: 2 assertion checks</summary>

- **matches** · `initial` / `raw-invalid`: Malformed input returns invalid params (-32602).
  [Compare responses](../cases/initial/raw-invalid.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^raw-invalid$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-invalid`: Malformed input returns invalid params (-32602).
  [Compare responses](../cases/initial/raw-invalid.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^raw-invalid$" --output runs/reproduce`

</details>

<details><summary>H08: 138 assertion checks</summary>

- **matches** · `initial` / `call-tree-trace-priced`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/call-tree-trace-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-trace-priced`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-tree-trace-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-trace-priced`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-tree-trace-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-stateDiff-priced`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/call-tree-stateDiff-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-stateDiff-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-stateDiff-priced`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/call-tree-stateDiff-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-stateDiff-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-stateDiff-priced`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-tree-stateDiff-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-stateDiff-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-vmTrace-priced`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/call-tree-vmTrace-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-vmTrace-priced`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-tree-vmTrace-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-tree-vmTrace-priced`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-tree-vmTrace-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types-priced`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/call-empty-types-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types-priced`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/call-empty-types-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types-priced`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-empty-types-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-empty-types-priced`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-empty-types-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-constructor-priced`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-constructor-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid-default-block`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/raw-valid-default-block.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^raw-valid-default-block$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid-current-nonce`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/raw-valid-current-nonce.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^raw-valid-current-nonce$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-trace`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/call-transfer-trace.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-trace$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-trace`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-transfer-trace.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-trace$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-trace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-transfer-trace.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-trace$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-stateDiff`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/call-transfer-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-stateDiff`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/call-transfer-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-stateDiff`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-transfer-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-vmTrace`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/call-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-vmTrace`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-vmTrace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-identity`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-identity.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-identity$" --output runs/reproduce`
- **matches** · `initial` / `call-identity`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-identity.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-identity$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `destroy-trace-55`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/fork-followup/destroy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^destroy-trace-55$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `destroy-trace-56`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/fork-followup/destroy-trace-56.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^destroy-trace-56$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `beacon-call-55`: Unrequested vmTrace is null.
  [Compare responses](../cases/fork-followup/beacon-call-55.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^beacon-call-55$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `beacon-call-55`: Unrequested stateDiff is null.
  [Compare responses](../cases/fork-followup/beacon-call-55.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^beacon-call-55$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `beacon-call-55`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/fork-followup/beacon-call-55.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^beacon-call-55$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `beacon-call-56`: Unrequested vmTrace is null.
  [Compare responses](../cases/fork-followup/beacon-call-56.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^beacon-call-56$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `beacon-call-56`: Unrequested stateDiff is null.
  [Compare responses](../cases/fork-followup/beacon-call-56.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^beacon-call-56$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `beacon-call-56`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/fork-followup/beacon-call-56.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^beacon-call-56$" --output runs/reproduce`
- **matches** · `verified-forks` / `destroy-trace-55`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/forks/destroy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^destroy-trace-55$" --output runs/reproduce`
- **matches** · `verified-forks` / `mcopy-trace-55`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/forks/mcopy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^mcopy-trace-55$" --output runs/reproduce`
- **matches** · `verified-forks` / `destroy-trace-56`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/forks/destroy-trace-56.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^destroy-trace-56$" --output runs/reproduce`
- **matches** · `verified-forks` / `mcopy-trace-56`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/forks/mcopy-trace-56.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^mcopy-trace-56$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-trace-priced`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/call-tree-trace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-trace-priced`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-tree-trace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-trace-priced`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-tree-trace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-stateDiff-priced`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/call-tree-stateDiff-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-stateDiff-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-stateDiff-priced`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/call-tree-stateDiff-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-stateDiff-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-stateDiff-priced`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-tree-stateDiff-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-stateDiff-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-vmTrace-priced`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/call-tree-vmTrace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-vmTrace-priced`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-tree-vmTrace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-vmTrace-priced`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-tree-vmTrace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-empty-types-priced`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/call-empty-types-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-empty-types-priced`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/call-empty-types-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-empty-types-priced`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-empty-types-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-empty-types-priced`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-empty-types-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-empty-types-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-constructor-priced`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-constructor-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-valid-default-block`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/raw-valid-default-block.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^raw-valid-default-block$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-valid-current-nonce`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/raw-valid-current-nonce.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^raw-valid-current-nonce$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-trace`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/call-transfer-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-trace`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-transfer-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-trace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-transfer-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-trace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-stateDiff`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/call-transfer-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-stateDiff`: Unrequested vmTrace is null.
  [Compare responses](../cases/initial/call-transfer-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-stateDiff`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-transfer-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-stateDiff$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-vmTrace`: Unrequested trace is an empty array.
  [Compare responses](../cases/initial/call-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-vmTrace`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-vmTrace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-identity`: Unrequested stateDiff is null.
  [Compare responses](../cases/initial/call-identity.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-identity$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-identity`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/initial/call-identity.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-identity$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-return42`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/call-return42.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^call-return42$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-siblings-revert-ok`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/call-siblings-revert-ok.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^call-siblings-revert-ok$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-mixed-create`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/call-mixed-create.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^call-mixed-create$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-gas7400`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/call-gas7400.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^call-gas7400$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-mcopy`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/call-mcopy.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^call-mcopy$" --output runs/reproduce`
- **matches** · `verified-repeat` / `state-only-nonempty-output`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/state-only-nonempty-output.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^state-only-nonempty-output$" --output runs/reproduce`
- **matches** · `verified-repeat` / `state-only-nonempty-output`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/state-only-nonempty-output.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^state-only-nonempty-output$" --output runs/reproduce`
- **matches** · `verified-repeat` / `state-only-nonempty-output`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/state-only-nonempty-output.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^state-only-nonempty-output$" --output runs/reproduce`
- **matches** · `verified-repeat` / `state-only-nonempty-output`: The return42 contract still returns word 42.
  [Compare responses](../cases/repeat/state-only-nonempty-output.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^state-only-nonempty-output$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-valid.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-valid$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-nonce-high.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-nonce-high$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-wrong-chain`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-wrong-chain.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-wrong-chain$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-insufficient-funds`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-insufficient-funds.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-insufficient-funds$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-low-gas`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-low-gas.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-low-gas$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-below-basefee`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-below-basefee.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-below-basefee$" --output runs/reproduce`
- **matches** · `verified-repeat` / `auth-clear`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/auth-clear.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^auth-clear$" --output runs/reproduce`
- **matches** · `verified-repeat` / `auth-set-revert`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/auth-set-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^auth-set-revert$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-trace`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/raw-valid-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-valid-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-trace`: Unrequested stateDiff is null.
  [Compare responses](../cases/repeat/raw-valid-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-valid-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-trace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-valid-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-valid-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-stateDiff`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/raw-valid-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-valid-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-stateDiff`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/raw-valid-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-valid-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-stateDiff`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-valid-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-valid-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-vmTrace`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/raw-valid-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-valid-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-vmTrace`: Unrequested stateDiff is null.
  [Compare responses](../cases/repeat/raw-valid-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-valid-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-vmTrace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-valid-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-valid-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-trace`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/raw-nonce-high-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-nonce-high-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-trace`: Unrequested stateDiff is null.
  [Compare responses](../cases/repeat/raw-nonce-high-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-nonce-high-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-trace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-nonce-high-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-nonce-high-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-stateDiff`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/raw-nonce-high-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-nonce-high-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-stateDiff`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/raw-nonce-high-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-nonce-high-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-stateDiff`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-nonce-high-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-nonce-high-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-vmTrace`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/raw-nonce-high-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-nonce-high-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-vmTrace`: Unrequested stateDiff is null.
  [Compare responses](../cases/repeat/raw-nonce-high-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-nonce-high-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-vmTrace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-nonce-high-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-nonce-high-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-wrong-chain-trace`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/raw-wrong-chain-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-wrong-chain-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-wrong-chain-trace`: Unrequested stateDiff is null.
  [Compare responses](../cases/repeat/raw-wrong-chain-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-wrong-chain-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-wrong-chain-trace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-wrong-chain-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-wrong-chain-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-wrong-chain-stateDiff`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/raw-wrong-chain-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-wrong-chain-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-wrong-chain-stateDiff`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/raw-wrong-chain-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-wrong-chain-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-wrong-chain-stateDiff`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-wrong-chain-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-wrong-chain-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-wrong-chain-vmTrace`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/raw-wrong-chain-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-wrong-chain-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-wrong-chain-vmTrace`: Unrequested stateDiff is null.
  [Compare responses](../cases/repeat/raw-wrong-chain-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-wrong-chain-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-wrong-chain-vmTrace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-wrong-chain-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-wrong-chain-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-insufficient-funds-trace`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/raw-insufficient-funds-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-insufficient-funds-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-insufficient-funds-trace`: Unrequested stateDiff is null.
  [Compare responses](../cases/repeat/raw-insufficient-funds-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-insufficient-funds-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-insufficient-funds-trace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-insufficient-funds-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-insufficient-funds-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-insufficient-funds-stateDiff`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/raw-insufficient-funds-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-insufficient-funds-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-insufficient-funds-stateDiff`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/raw-insufficient-funds-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-insufficient-funds-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-insufficient-funds-stateDiff`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-insufficient-funds-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-insufficient-funds-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-insufficient-funds-vmTrace`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/raw-insufficient-funds-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-insufficient-funds-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-insufficient-funds-vmTrace`: Unrequested stateDiff is null.
  [Compare responses](../cases/repeat/raw-insufficient-funds-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-insufficient-funds-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-insufficient-funds-vmTrace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-insufficient-funds-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-insufficient-funds-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-low-gas-trace`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/raw-low-gas-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-low-gas-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-low-gas-trace`: Unrequested stateDiff is null.
  [Compare responses](../cases/repeat/raw-low-gas-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-low-gas-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-low-gas-trace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-low-gas-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-low-gas-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-low-gas-stateDiff`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/raw-low-gas-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-low-gas-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-low-gas-stateDiff`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/raw-low-gas-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-low-gas-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-low-gas-stateDiff`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-low-gas-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-low-gas-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-low-gas-vmTrace`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/raw-low-gas-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-low-gas-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-low-gas-vmTrace`: Unrequested stateDiff is null.
  [Compare responses](../cases/repeat/raw-low-gas-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-low-gas-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-low-gas-vmTrace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-low-gas-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-low-gas-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-below-basefee-trace`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/raw-below-basefee-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-below-basefee-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-below-basefee-trace`: Unrequested stateDiff is null.
  [Compare responses](../cases/repeat/raw-below-basefee-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-below-basefee-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-below-basefee-trace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-below-basefee-trace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-below-basefee-trace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-below-basefee-stateDiff`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/raw-below-basefee-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-below-basefee-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-below-basefee-stateDiff`: Unrequested vmTrace is null.
  [Compare responses](../cases/repeat/raw-below-basefee-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-below-basefee-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-below-basefee-stateDiff`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-below-basefee-stateDiff.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-below-basefee-stateDiff$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-below-basefee-vmTrace`: Unrequested trace is an empty array.
  [Compare responses](../cases/repeat/raw-below-basefee-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-below-basefee-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-below-basefee-vmTrace`: Unrequested stateDiff is null.
  [Compare responses](../cases/repeat/raw-below-basefee-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-below-basefee-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-below-basefee-vmTrace`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/raw-below-basefee-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-below-basefee-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `constructor`: Output remains a byte string under every trace selection.
  [Compare responses](../cases/repeat/constructor.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^constructor$" --output runs/reproduce`

</details>

<details><summary>H10: 7 assertion checks</summary>

- **change_needed** · `initial` / `call-tree-trace-priced`: Successful creation uses address, code and gasUsed.
  [Compare responses](../cases/initial/call-tree-trace-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-constructor-priced`: Successful creation uses address, code and gasUsed.
  [Compare responses](../cases/initial/call-constructor-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-tree-trace-priced`: Successful creation uses address, code and gasUsed.
  [Compare responses](../cases/initial/call-tree-trace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-trace-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-constructor-priced`: Successful creation uses address, code and gasUsed.
  [Compare responses](../cases/initial/call-constructor-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-mixed-create`: Successful creation uses address, code and gasUsed.
  [Compare responses](../cases/repeat/call-mixed-create.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^call-mixed-create$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-mixed-create`: Successful creation uses address, code and gasUsed.
  [Compare responses](../cases/repeat/call-mixed-create.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^call-mixed-create$" --output runs/reproduce`
- **matches** · `verified-repeat` / `constructor`: Successful creation uses address, code and gasUsed.
  [Compare responses](../cases/repeat/constructor.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^constructor$" --output runs/reproduce`

</details>

<details><summary>H21: 38 assertion checks</summary>

- **matches** · `initial` / `call-tree-vmTrace-priced`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/call-tree-vmTrace-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `initial` / `call-constructor-priced`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/call-constructor-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid-default-block`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/raw-valid-default-block.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^raw-valid-default-block$" --output runs/reproduce`
- **matches** · `initial` / `raw-valid-current-nonce`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/raw-valid-current-nonce.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^raw-valid-current-nonce$" --output runs/reproduce`
- **matches** · `initial` / `call-transfer-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/call-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `initial` / `call-identity`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/call-identity.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-identity$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `destroy-trace-55`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/fork-followup/destroy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^destroy-trace-55$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `destroy-trace-56`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/fork-followup/destroy-trace-56.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^destroy-trace-56$" --output runs/reproduce`
- **matches** · `verified-forks` / `destroy-trace-55`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/forks/destroy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^destroy-trace-55$" --output runs/reproduce`
- **matches** · `verified-forks` / `mcopy-trace-55`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/forks/mcopy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^mcopy-trace-55$" --output runs/reproduce`
- **matches** · `verified-forks` / `destroy-trace-56`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/forks/destroy-trace-56.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^destroy-trace-56$" --output runs/reproduce`
- **matches** · `verified-forks` / `mcopy-trace-56`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/forks/mcopy-trace-56.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^mcopy-trace-56$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-tree-vmTrace-priced`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/call-tree-vmTrace-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-tree-vmTrace-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-constructor-priced`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/call-constructor-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-valid-default-block`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/raw-valid-default-block.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^raw-valid-default-block$" --output runs/reproduce`
- **matches** · `verified-initial` / `raw-valid-current-nonce`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/raw-valid-current-nonce.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^raw-valid-current-nonce$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-transfer-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/call-transfer-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-transfer-vmTrace$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-identity`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/initial/call-identity.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-identity$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-return42`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/call-return42.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^call-return42$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-siblings-revert-ok`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/call-siblings-revert-ok.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^call-siblings-revert-ok$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-mixed-create`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/call-mixed-create.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^call-mixed-create$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-gas7400`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/call-gas7400.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^call-gas7400$" --output runs/reproduce`
- **matches** · `verified-repeat` / `call-mcopy`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/call-mcopy.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^call-mcopy$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/raw-valid.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-valid$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/raw-nonce-high.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-nonce-high$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-wrong-chain`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/raw-wrong-chain.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-wrong-chain$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-insufficient-funds`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/raw-insufficient-funds.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-insufficient-funds$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-low-gas`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/raw-low-gas.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-low-gas$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-below-basefee`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/raw-below-basefee.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-below-basefee$" --output runs/reproduce`
- **matches** · `verified-repeat` / `auth-clear`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/auth-clear.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^auth-clear$" --output runs/reproduce`
- **matches** · `verified-repeat` / `auth-set-revert`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/auth-set-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^auth-set-revert$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-valid-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/raw-valid-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-valid-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-nonce-high-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/raw-nonce-high-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-nonce-high-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-wrong-chain-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/raw-wrong-chain-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-wrong-chain-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-insufficient-funds-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/raw-insufficient-funds-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-insufficient-funds-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-low-gas-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/raw-low-gas-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-low-gas-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `raw-below-basefee-vmTrace`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/raw-below-basefee-vmTrace.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-below-basefee-vmTrace$" --output runs/reproduce`
- **matches** · `verified-repeat` / `constructor`: Stack words use minimal hex quantities at every depth.
  [Compare responses](../cases/repeat/constructor.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^constructor$" --output runs/reproduce`

</details>

<details><summary>H19: 3 assertion checks</summary>

- **matches** · `initial` / `call-constructor-priced`: Creation vmTrace.code is executing initcode.
  [Compare responses](../cases/initial/call-constructor-priced.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`
- **matches** · `verified-initial` / `call-constructor-priced`: Creation vmTrace.code is executing initcode.
  [Compare responses](../cases/initial/call-constructor-priced.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-constructor-priced$" --output runs/reproduce`
- **matches** · `verified-repeat` / `constructor`: Creation vmTrace.code is executing initcode.
  [Compare responses](../cases/repeat/constructor.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^constructor$" --output runs/reproduce`

</details>

<details><summary>H22: 2 assertion checks</summary>

- **change_needed** · `initial` / `call-identity`: The identity precompile call frame preserves its input as return bytes.
  [Compare responses](../cases/initial/call-identity.md) · [Raw responses](../../evidence/2026-09-21/initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/initial/manifest.json --clients besu_release --corpus initial --case "^call-identity$" --output runs/reproduce`
- **change_needed** · `verified-initial` / `call-identity`: The identity precompile call frame preserves its input as return bytes.
  [Compare responses](../cases/initial/call-identity.md) · [Raw responses](../../evidence/2026-09-21/verified-initial/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-initial/manifest.json --clients besu_release --corpus initial --case "^call-identity$" --output runs/reproduce`

</details>

<details><summary>H26: 4 assertion checks</summary>

- **matches** · `verified-fork-followup` / `destroy-trace-55`: Delete code/nonce before Cancun; preserve an existing account after EIP-6780.
  [Compare responses](../cases/fork-followup/destroy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^destroy-trace-55$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `destroy-trace-56`: Delete code/nonce before Cancun; preserve an existing account after EIP-6780.
  [Compare responses](../cases/fork-followup/destroy-trace-56.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^destroy-trace-56$" --output runs/reproduce`
- **matches** · `verified-forks` / `destroy-trace-55`: Delete code/nonce before Cancun; preserve an existing account after EIP-6780.
  [Compare responses](../cases/forks/destroy-trace-55.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^destroy-trace-55$" --output runs/reproduce`
- **matches** · `verified-forks` / `destroy-trace-56`: Delete code/nonce before Cancun; preserve an existing account after EIP-6780.
  [Compare responses](../cases/forks/destroy-trace-56.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^destroy-trace-56$" --output runs/reproduce`

</details>

<details><summary>H28: 12 assertion checks</summary>

- **matches** · `verified-fork-followup` / `system-beacon-55-560`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/fork-followup/system-beacon-55-560.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^system-beacon-55-560$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `system-beacon-55-8751`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/fork-followup/system-beacon-55-8751.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^system-beacon-55-8751$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `system-beacon-56-560`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/fork-followup/system-beacon-56-560.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^system-beacon-56-560$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `system-beacon-56-8751`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/fork-followup/system-beacon-56-8751.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^system-beacon-56-8751$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `beacon-call-55`: Historical trace_call uses only system changes through the selected block.
  [Compare responses](../cases/fork-followup/beacon-call-55.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^beacon-call-55$" --output runs/reproduce`
- **matches** · `verified-fork-followup` / `beacon-call-56`: Historical trace_call uses only system changes through the selected block.
  [Compare responses](../cases/fork-followup/beacon-call-56.md) · [Raw responses](../../evidence/2026-09-21/verified-fork-followup/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-fork-followup/manifest.json --clients besu_release --corpus fork-followup --case "^beacon-call-56$" --output runs/reproduce`
- **matches** · `verified-forks` / `system-beacon-55-560`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/forks/system-beacon-55-560.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^system-beacon-55-560$" --output runs/reproduce`
- **matches** · `verified-forks` / `system-beacon-55-8751`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/forks/system-beacon-55-8751.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^system-beacon-55-8751$" --output runs/reproduce`
- **matches** · `verified-forks` / `system-beacon-56-560`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/forks/system-beacon-56-560.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^system-beacon-56-560$" --output runs/reproduce`
- **matches** · `verified-forks` / `system-beacon-56-8751`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/forks/system-beacon-56-8751.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^system-beacon-56-8751$" --output runs/reproduce`
- **matches** · `verified-forks` / `system-beacon-57-560`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/forks/system-beacon-57-560.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^system-beacon-57-560$" --output runs/reproduce`
- **matches** · `verified-forks` / `system-beacon-57-8751`: Historical beacon-root storage excludes the following block system update.
  [Compare responses](../cases/forks/system-beacon-57-8751.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^system-beacon-57-8751$" --output runs/reproduce`

</details>

<details><summary>H27: 15 assertion checks</summary>

- **matches** · `verified-forks` / `filter-35`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-35.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^filter-35$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-36`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-36.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^filter-36$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-47`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-47.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^filter-47$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-48`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-48.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^filter-48$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-51`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-51.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^filter-51$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-52`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-52.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^filter-52$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-55`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-55.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^filter-55$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-56`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-56.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^filter-56$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-59`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-59.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^filter-59$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-60`: A single-block filter agrees with trace_block at the same fork.
  [Compare responses](../cases/forks/filter-60.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^filter-60$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `filter-across-36`: A fork-crossing range equals the corresponding per-block traces.
  [Compare responses](../cases/forks/filter-across-36.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^filter-across-36$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-across-48`: A fork-crossing range equals the corresponding per-block traces.
  [Compare responses](../cases/forks/filter-across-48.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^filter-across-48$" --output runs/reproduce`
- **matches** · `verified-forks` / `filter-across-52`: A fork-crossing range equals the corresponding per-block traces.
  [Compare responses](../cases/forks/filter-across-52.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^filter-across-52$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `filter-across-56`: A fork-crossing range equals the corresponding per-block traces.
  [Compare responses](../cases/forks/filter-across-56.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^filter-across-56$" --output runs/reproduce`
- **change_needed** · `verified-forks` / `filter-across-60`: A fork-crossing range equals the corresponding per-block traces.
  [Compare responses](../cases/forks/filter-across-60.md) · [Raw responses](../../evidence/2026-09-21/verified-forks/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-forks/manifest.json --clients besu_release --corpus forks --case "^filter-across-60$" --output runs/reproduce`

</details>

<details><summary>H24: 1 assertion checks</summary>

- **change_needed** · `verified-repeat` / `call-siblings-revert-ok`: The successful second sibling retains its output and has no error.
  [Compare responses](../cases/repeat/call-siblings-revert-ok.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^call-siblings-revert-ok$" --output runs/reproduce`

</details>

<details><summary>H20: 1 assertion checks</summary>

- **change_needed** · `verified-repeat` / `call-mcopy`: MCOPY reports its same-step write of word 42 at offset 32.
  [Compare responses](../cases/repeat/call-mcopy.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^call-mcopy$" --output runs/reproduce`

</details>

<details><summary>H16: 1 assertion checks</summary>

- **matches** · `verified-repeat` / `many-storage-write-revert-read`: Sequential calls retain prior writes and roll back reverted writes.
  [Compare responses](../cases/repeat/many-storage-write-revert-read.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^many-storage-write-revert-read$" --output runs/reproduce`

</details>

<details><summary>H13: 1 assertion checks</summary>

- **change_needed** · `verified-repeat` / `raw-nonce-high`: A signed nonce mismatch is rejected rather than replaced.
  [Compare responses](../cases/repeat/raw-nonce-high.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^raw-nonce-high$" --output runs/reproduce`

</details>

<details><summary>H18: 2 assertion checks</summary>

- **matches** · `verified-repeat` / `auth-clear`: EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.
  [Compare responses](../cases/repeat/auth-clear.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^auth-clear$" --output runs/reproduce`
- **matches** · `verified-repeat` / `auth-set-revert`: EIP-7702 reports the actual delegation-code transition, including clear and changes surviving execution revert.
  [Compare responses](../cases/repeat/auth-set-revert.md) · [Raw responses](../../evidence/2026-09-21/verified-repeat/observations.json).
  Reproduce: `uv run trace-interop run --lock evidence/2026-09-21/verified-repeat/manifest.json --clients besu_release --corpus repeat --case "^auth-set-revert$" --output runs/reproduce`

</details>
