# Harness Bug Audit (2026-10-14)

A line-by-line audit of `trace_interop/`, `scripts/`, and `site/` identified **26 concrete bugs** across five categories:
1. **Unsound assertions (false positives)** where invalid, incomplete, or corrupted client trace responses pass with `status: 'matches'`.
2. **Unhandled exceptions (crashes)** where malformed JSON-RPC responses or valid explicit-`null` parameter combinations raise uncaught `TypeError`, `AttributeError`, `ValueError`, `KeyError`, or `IndexError`.
3. **False negatives / normalization bugs** where conforming client responses fail due to case-sensitive hex address/hash comparisons or missing EIP-1898 block resolution.
4. **Isolation & consistency-law bugs** where cross-decision dependency resolution or consistency laws silently drop checks or convert failures into `blocked`.
5. **Reporting, provenance & tooling bugs** in `report.py`, `presentation.py`, `cli.py`, `replica.py`, and `scripts/`.

Every finding below was verified against the live codebase.

---

## Summary Table

| # | Category | File & Lines | Topic / Component | Impact |
| --- | --- | --- | --- | --- |
| 1 | False positive | `trace_interop/coverage.py:242-254` | `H21` (`vmTrace` encoding) | `ex: {}` or non-dict `ex` (`"bad"`, `[]`, `123`) makes `obj(op.get('ex'))` falsy, skipping `used` and `encoding_valid(ex)` checks |
| 2 | False positive | `trace_interop/vm_model.py:420-474` | `H20` (`local_invariants`) | Non-dict non-null `ex`, negative `cost` on halted steps (`ex: null`), and missing/wrong `ex.store` on `SSTORE`/`SLOAD`/`TSTORE` pass |
| 3 | False positive | `trace_interop/vm_model.py:268, 455, 465` | `H20` (`differences`, `local_invariants`) | Python `False == 0` / `True == 1` accepts JSON boolean `ex.mem.off` (`false`/`true`) without `type(...) is int` check |
| 4 | False positive | `trace_interop/execution_models.py:319-327, 552-565` | `H16` / `H15` (`settled_gas`) | Value transfer conservation not checked per sender/recipient: omitting recipient credit and reducing sender debit by `value` preserves `sum(deltas)` and passes |
| 5 | False positive | `trace_interop/execution_models.py:427-446` | `H17` (endpoint existence) | Born accounts with `{'+': None}` pass `account.get(k) == {'+': mapping(account.get(k)).get('+')}`; surviving accounts with `-` deletion markers pass; born storage markers unchecked |
| 6 | False positive | `trace_interop/probes.py:398-417` | `H20` (`push` / `store` probes) | `ops[:len(model)]` and `zip(ops, model)` silently ignore extra trailing operations in `vmTrace.ops`; `push` ignores non-`DUP`/`SWAP` opcodes |
| 7 | False positive | `trace_interop/probes.py:379-385` | `H26` (`deleted-storage` probe) | Partial non-empty `storage` dict omitting known nonzero pre-state slots in `probe['expected']` passes `all(...)` |
| 8 | False positive | `trace_interop/probes.py:356-378` | `H29` / `H09` (`depth` probe) | Only checks `len(path(f)) == depth + 1`, never verifying that failed depth-attempt frames have `path(deepest)` as parent prefix |
| 9 | False positive | `trace_interop/mined_probes.py:106-135` | `mined-probes` (`trace_block`) | Per-tx hash filtering ignores reversed transaction ordering, extra fabricated frames with unknown `transactionHash`, and non-dict elements in `result` |
| 10 | False positive | `trace_interop/validation.py:26-28, 40-45` | `H14` (`RequestValidator`) | `on_folded` only wraps `properties` and `additionalProperties`, bypassing `if`/`then` (`blockHash` + `fromBlock`), `not`/`required` (`state` + `stateDiff`), and `data`/`input` equality on case-variant keys |
| 11 | False positive | `trace_interop/rules.py:410-413`, `coverage.py:124-127` | `H10` (creation fields) | Only checks `all(k in value for k in ['address', 'code', 'gasUsed'])`; ignores missing `action.creationMethod`, `None` values, or forbidden `result.output` |
| 12 | False positive | `trace_interop/coverage.py:160-162`, `rules.py:630-631` | `H05` (PoS rewards) | Vacuously passes when `trace_block` or `trace_filter` returns `[]` or `[None]` on non-empty PoS blocks |
| 13 | False positive | `trace_interop/laws.py:216-243` | `L07` (stored vs replayed) | `replays.setdefault(tx, ...)` keyed by tx hash drops `trace_replayBlockTransactions` whenever `trace_replayTransaction` succeeded |
| 14 | Crash | `trace_interop/execution_models.py:86-92` | `transactions()` | Explicit `null` fields (`'from': None`, `'value': None`, `'data': None`, `'gasPrice': None`) in `trace_call` / `trace_callMany` raise `AttributeError` / `TypeError` |
| 15 | Crash | `trace_interop/execution_models.py:252-255, 302-307` | `traced_refund()` | Storage key/value hex parsing at lines 302–307 is outside `try...except`, raising `ValueError`/`TypeError` on malformed `stateDiff` |
| 16 | Crash | `trace_interop/probes.py:165-171`, `rules.py:155, 158, 292` | `H33` / `H32` | Unhashable `blockNumber`/`blockHash`/`transactionHash` (e.g. `[]` or `{}`) raises `TypeError: unhashable type`; mixed `None` and `int` in `filter-pending` raises `TypeError` in `sorted()` |
| 17 | Crash | `trace_interop/laws.py:279-295` | `L10` (filter law) | Non-dict element in `trace_filter` result list (e.g. `[None]`) raises `AttributeError: 'NoneType' object has no attribute 'get'` |
| 18 | Crash | `trace_interop/fee_policy.py:133-135`, `scenarios.py:159, 225` | `H15` / setup verification | `.get('response', {})` returns `None` when `response` is `None`, raising `AttributeError` on `.get(...)` |
| 19 | False negative | `trace_interop/execution_models.py:422, 553`, `fee_policy.py:191-195`, `rules.py:671-685` | `H15`, `H16`, `H18`, `H26` | Case-sensitive address lookups in `stateDiff` and `_alloc` fail when a client formats `stateDiff` keys as EIP-55 mixed-case hex; missing `_alloc` skips `balance` check in `destroy-trace-55` |
| 20 | False negative | `trace_interop/chain_model.py:13-32`, `vm_model.py:181, 188` | Block & VM models | `resolve_block` rejects EIP-1898 dict selectors and uppercase hex block numbers; `execute()` raises `IndexError` -> `UnsupportedProgram` on `CALLDATALOAD`/`CALLDATACOPY` with offsets $\ge 2^{63}$ |
| 21 | Isolation | `trace_interop/isolation.py:50-86` | `isolate()`, `resolve_dependencies()` | `isolate()` converts `role='result'` failures to `'blocked'` even when the error owner has no check in `checks`; `resolve_dependencies()` fails to block when a same-record dependency check is `'blocked'` |
| 22 | Isolation | `trace_interop/oracles.py:73-105` | `anchor()` | Structural contradictions in reference trace (`len(roots) != 1`, `len(ordinary) != 7`, `len(suicides) != 1`) return `(None, None)` instead of a mismatch, silently blocking/skipping dependent checks |
| 23 | Reporting | `trace_interop/report.py:16`, `presentation.py:182, 235, 345, 616` | Reports & fixes | `decisions/fixes.json` omitted from `ASSESSMENT_SOURCES`; `fixes_graph` crashes with `ValueError` if a dependency PR is `closed`; `client_page` family view hides per-build assessment gaps and `matched` rows |
| 24 | Tooling | `scripts/refresh_fixes.py:85-96, 155, 188-200` | Fix refresh | PRs from a fork's `main`/`develop` branch poison `branches` dict and corrupt `via`/`uptake` for all PRs in that repo; Cargo `>=` version strings crash `version()` |
| 25 | Runner / CLI | `trace_interop/cli.py:352-385`, `replica.py:86-90` | `--case` & `replica` | `selected_cases` omits probe `reference` and `fee_reference` twins when running `--case "^CASE$"`; `replica.translate` uses sequential non-atomic `str.replace` |
| 26 | Scripts / Site | `scripts/compare_responses.py:16, 41`, `scripts/build_tech_tree.py:114` | Utility scripts & site | `compare_responses.py` crashes with `KeyError: 'raw_response'` on `transport_error` and misses nested evidence dirs; `build_tech_tree.py` includes Anvil in totals despite `tree.toml` stating Anvil is excluded |

---

## Detailed Findings

### 1. `coverage.py`: `H21` passes vacuously when `op['ex']` is `{}` or any non-dict JSON value
- **Location**: `trace_interop/coverage.py:242-254`
- **Mechanism**:
  ```python
  if 'H21' in declared and not covered('H21') and status == 'result':
      vms = [obj(e).get('vmTrace') for e in envelopes]
      valid = bool(vms)
      while vms:
          vm = vms.pop()
          valid &= isinstance(vm, dict) and isinstance(obj(vm).get('ops'), list)
          for op in seq(obj(vm).get('ops')):
              ex = obj(obj(op).get('ex'))
              valid &= all(type(obj(op).get(k)) is int and obj(op)[k] >= 0 for k in ['pc','cost'])
              if ex:
                  valid &= type(ex.get('used')) is int and ex['used'] >= 0
                  valid &= encoding_valid(ex)
              if obj(op).get('sub') is not None:
                  vms.append(op['sub'])
      add('H21', bool(valid), ...)
  ```
  `obj(x)` returns `x if isinstance(x, dict) else {}`. When `op['ex']` is `{}` (an empty object missing required `'used'` and `'push'`) or any non-dict value (`"corrupted"`, `[]`, `123`), `ex` evaluates to `{}` which is falsy in Python (`bool({}) is False`). Consequently, `if ex:` is skipped, neither `ex.get('used')` nor `encoding_valid(ex)` is checked, and `H21` passes with `status: 'matches'`. Additionally, `vm.get('code')` is never checked against even-length lowercase hex (`DATA`) in `H21`.
- **Reproduction**:
  ```python
  case = {'name': 'replay-block-tree', 'request': {'method': 'trace_replayBlockTransactions', 'params': ['0x2', ['vmTrace']]}, 'topics': ['H21'], 'context': {}}
  obs = {'status': 'result', 'response': {'result': [{'vmTrace': {'code': '0x123', 'ops': [{'pc': 0, 'cost': 3, 'ex': 'corrupted', 'sub': None}]}}]}}
  coverage.properties(case, obs, {}, [], {'H21'})
  # -> [{'topic': 'H21', 'status': 'matches', ...}]
  ```

---

### 2. `vm_model.py`: `local_invariants()` ignores non-dict non-null `ex`, negative `cost` on halted steps, and `ex.store` invariants
- **Location**: `trace_interop/vm_model.py:420-474`
- **Mechanism**:
  1. At line 429: `if isinstance(ex, dict):` guards the `type(cost) is not int or cost < 0` check (line 431) and all other step checks. If `ex` is neither a `dict` nor `None` (e.g., `ex: "bad"` or `ex: []`), `local_invariants` silently ignores the step without recording an error. Even when `ex is None` (an exceptional halt), `cost` is never checked to be a non-negative integer (`cost: -999` or `cost: None` passes).
  2. `local_invariants` never inspects `ex.store` at all: if a completed `SSTORE` (`0x55`) omits `store` (`store: null`) or records wrong key/value words, or if `SLOAD` (`0x54`), `TSTORE` (`0x5d`), or `PUSH1` (`0x60`) sets a non-null `ex.store`, `local_invariants` returns `[]`.
- **Reproduction**:
  ```python
  vm = {'code': '0x600160005500', 'ops': [
      {'pc': 0, 'cost': 3, 'ex': {'used': 97, 'push': ['0x1'], 'mem': None, 'store': {'key': '0x0', 'val': '0x1'}}, 'sub': None},
      {'pc': 2, 'cost': 3, 'ex': {'used': 94, 'push': ['0x0'], 'mem': None, 'store': None}, 'sub': None},
      {'pc': 4, 'cost': 20, 'ex': {'used': 74, 'push': [], 'mem': None, 'store': None}, 'sub': None},
      {'pc': 5, 'cost': -999, 'ex': 'not_a_dict_or_null', 'sub': None}
  ]}
  vm_model.local_invariants(vm)  # -> []
  ```

---

### 3. `vm_model.py`: `differences()` and `local_invariants()` accept JSON booleans (`false`/`true`) for `ex.mem.off`
- **Location**: `trace_interop/vm_model.py:268, 455, 465`
- **Mechanism**:
  In Python, `isinstance(False, int)` is `True` and `False == 0` / `True == 1`. While `pc`, `cost`, and `used` explicitly check `type(...) is int`, `differences()` compares `ex.get('mem') != want['ex']['mem']` via dict equality (`{'off': False, 'data': '0x...'} == {'off': 0, 'data': '0x...'}` is `True`), and `local_invariants()` checks `mem.get('off') != operands[0]` and `mem.get('off') == offset` without `type(mem.get('off')) is int`.
- **Reproduction**:
  ```python
  expected, _, _ = vm_model.execute('0x602a60005260206000f3', 100)
  actual = copy.deepcopy(expected)
  actual['ops'][2]['ex']['mem']['off'] = False
  vm_model.differences(actual, expected)   # -> []
  vm_model.local_invariants(actual)        # -> []
  ```

---

### 4. `execution_models.py`: `settled_gas()` does not verify sender or recipient balance deltas on value transfers
- **Location**: `trace_interop/execution_models.py:319-327, 552-565`
- **Mechanism**:
  ```python
  def settled_gas(deltas, miner, low, high, tip_price, burn_price, blob):
      if any(v is None for v in deltas) or miner is None:
          return None
      total=sum(deltas)
      gas=miner//tip_price if tip_price else -(total+blob)//burn_price if burn_price else low
      return gas if low<=gas<=high and miner==tip_price*gas and total==-(burn_price*gas+blob) else None
  ```
  `settled_gas` only checks `sum(deltas) == -(burn_price * gas + blob)` and `miner == tip_price * gas`. It never checks that the sender's balance delta includes `-tx['value']` or that the recipient's balance delta includes `+tx['value']`. If a client omits the recipient's balance credit and reduces the sender's debit by `tx['value']` (or fabricates any offsetting balance deltas between non-miner accounts), `sum(deltas)` and `miner` are unchanged and `H16` passes with `status: 'matches'`.
- **Reproduction**:
  In `initial/replay-transfer-stateDiff`, set `stateDiff[recipient]['balance'] = '='` and add `tx['value']` (`10000` wei) to `stateDiff[sender]['balance']['*']['to']`. `execution_models.assess(case, mutated, peers, {'H16'})` returns `status: 'matches'`.

---

### 5. `execution_models.py`: `H17` accepts `{'+': None}` on born accounts, `-` deletion markers on surviving accounts, and wrong storage markers on born accounts
- **Location**: `trace_interop/execution_models.py:427-446`
- **Mechanism**:
  ```python
  if address.lower() in exists:
      if any(isinstance(account.get(k),dict) and '+' in account[k] for k in ['balance','nonce','code']):
          bad.append(address+': existing account has creation markers')
  elif any(account.get(k) != {'+':mapping(account.get(k)).get('+')} for k in ['balance','nonce','code']):
      bad.append(address+': new account lacks creation markers for all fields')
  ```
  1. For a born account (`address.lower() not in exists`), if `account[k]` is `{'+': None}` (or `{'+': 123}`), `mapping(account.get(k)).get('+')` is `None`, so `account.get(k) != {'+': None}` is `False` and `H17` passes.
  2. For a born account, `account.get('storage')` is never checked, so a born account reporting storage slots with `'*'` instead of `'+'` passes `H17`.
  3. For a surviving existing account (`address.lower() in exists`), only `'+' in account[k]` is rejected; reporting deletion markers `{'-': '0x1'}` or missing fields on a surviving account passes `H17`.

---

### 6. `probes.py`: `push` and `store` VM probes ignore extra trailing operations in `vmTrace.ops`
- **Location**: `trace_interop/probes.py:398-417`
- **Mechanism**:
  `[mapping(o).get('pc') for o in ops[:len(model)]] != [o['pc'] for o in model]` only compares the prefix of `ops` of length `len(model)`, and `for got, want in zip(ops, model):` stops at `len(model)`. For `kind in ('push', 'store')`, any extra trailing operations in `ops[len(model):]` (such as a fabricated step with a bogus `store` or `push`) are ignored.

---

### 7. `probes.py`: `deleted-storage` probe passes when non-empty `storage` omits expected nonzero pre-state slots
- **Location**: `trace_interop/probes.py:379-385`
- **Mechanism**:
  ```python
  ok = deleted_storage_shape(storage) and all(
      int(change['-'], 16) == int(probe['expected'].get(slot.lower(), '0x'+'0'*64), 16)
      for slot, change in storage.items())
  ```
  If a client reports a non-empty `storage` map on a deleted account that includes only zero-valued slots (e.g., `{'0x...01': {'-': '0x00...00'}}`) while omitting the nonzero dirty slot in `probe['expected']` (slot `0x00...00` = `42` in `probes-forks/many-write-delete-storage`), `all(...)` only checks the keys present in `storage` and passes with `status: 'matches'`.

---

### 8. `probes.py`: `depth` probe does not check parent `traceAddress` prefix on depth-limit attempt frames
- **Location**: `trace_interop/probes.py:356-378`
- **Mechanism**:
  `attempts = [f for f in frames if len(path(f)) == depth + 1]` only checks the length of `traceAddress`, never checking that `path(f)[:-1] == path(deepest)` (or `path(f) == path(deepest) + [i]`). In `probes-forks/depth-limit`, failed attempt frames with `traceAddress: [999]*1025` and `[888]*1025` pass both `H29` and `H09`.

---

### 9. `mined_probes.py`: `trace_block` assessment ignores out-of-order transactions, extra frames with unknown `transactionHash`, and non-dict elements
- **Location**: `trace_interop/mined_probes.py:106-135`
- **Mechanism**:
  In `mined_probes.assess()`, for `trace_block`, `frames = [f for f in seq(result) if isinstance(f, dict) and f.get('transactionHash') == txhash]` extracts each transaction's frames independently by `txhash`. Reversing the order of transactions in `trace_block`, appending fabricated frames with an unknown `transactionHash`, or appending `None` to `result` still produces `status: 'matches'` on every check in `mined_probes.assess()` and `coverage.supplement()`.

---

### 10. `validation.py`: Case-folded member validation bypasses `if`/`then`, `not`, `required`, and `data`/`input` agreement
- **Location**: `trace_interop/validation.py:26-28, 40-45`
- **Mechanism**:
  `RequestValidator` only wraps `properties` and `additionalProperties` with `on_folded`. Schema keywords `if`, `then`, `not`, and `required` on closed objects receive the unfolded instance:
  - `request_errors({'method': 'trace_filter', 'params': [{'BLOCKHASH': '0x' + '11'*32, 'fromBlock': '0x2'}]}, methods)` returns `[]` (bypassing the `if`/`then` exclusivity between `blockHash` and `fromBlock`/`toBlock`).
  - `request_errors({'method': 'trace_call', 'params': [{}, ['trace'], 'latest', {'0x' + '11'*20: {'STATE': {}, 'stateDiff': {}}}]}, methods)` returns `[]` (bypassing `not: {required: [state, stateDiff]}`).
  - In `request_errors` line 43, `call.get('data')` and `call.get('input')` only check exact lowercase keys.

---

### 11. `rules.py` & `coverage.py`: `H10` creation check ignores `action.creationMethod`, `None` values, and forbidden `result.output`
- **Location**: `trace_interop/rules.py:410-413`, `trace_interop/coverage.py:124-127`
- **Mechanism**:
  Both checks only evaluate `all(k in value for k in ['address', 'code', 'gasUsed'])`. A creation frame with `result: {'address': None, 'code': None, 'gasUsed': None, 'output': '0x1234'}` and no `action.creationMethod` passes `H10` (`status: 'matches'`). Furthermore, if `trace_call` returns `trace: []` on a creation call, `rules.evaluate()` emits no `H10` check at all.

---

### 12. `coverage.py` & `rules.py`: `H05` passes vacuously when `trace_block` or `trace_filter` returns `[]` or `[None]`
- **Location**: `trace_interop/coverage.py:160-162`, `trace_interop/rules.py:630-631`
- **Mechanism**:
  `isinstance(result, list) and all(obj(f).get('type') != 'reward' for f in result)` evaluates to `True` when `result` is `[]` or `[None]` on a non-empty PoS block (`initial/block-transfer`, `initial/block-tree`, `fork-followup/withdrawal-filter-52`).

---

### 13. `laws.py`: Law `L07` (`Stored and replayed frames agree`) overwrites `trace_replayBlockTransactions` when `trace_replayTransaction` is present
- **Location**: `trace_interop/laws.py:216-243`
- **Mechanism**:
  `replays` is a dict keyed solely by `tx` (`replays.setdefault(params[0], case)` for `trace_replayTransaction`, followed by `replays.setdefault(tx, dict(case, _index=index))` for `trace_replayBlockTransactions`). Whenever a corpus contains both `trace_replayTransaction` and `trace_replayBlockTransactions` for the same transaction (as in `initial`), `replays.setdefault` keeps only the first `trace_replayTransaction` case and never checks `trace_replayBlockTransactions` (or additional `trace_replayTransaction` mode combinations) against stored traces (`trace_transaction` / `trace_block`).

---

### 14. `execution_models.py`: `transactions()` crashes with `AttributeError` / `TypeError` when `trace_call` / `trace_callMany` has explicit `null` fields
- **Location**: `trace_interop/execution_models.py:86-92`
- **Mechanism**:
  Per `H14`, explicit `null` in optional call object fields (`'from': None`, `'value': None`, `'data': None`, `'gasPrice': None`, `'nonce': None`) is equivalent to omitting the field. However, `c.get('from', '0x' + '00'*20)` returns `None` when `'from'` is present with value `None`, so `.lower()` raises `AttributeError: 'NoneType' object has no attribute 'lower'`. Similarly, `'value': None` or `'gasPrice': None` causes `quantity(...)` to return `None`, crashing downstream arithmetic with `TypeError`, and `'data': None` crashes `intrinsic()` with `AttributeError`. (The same `call.get('data', call.get('input', '0x'))` bug in `rules.py:111` crashes `observed_number` with `AttributeError` when `'data': None` is passed alongside `'input'`).

---

### 15. `execution_models.py`: `traced_refund()` crashes with uncaught `ValueError` / `TypeError` on malformed `stateDiff` storage keys or values
- **Location**: `trace_interop/execution_models.py:252-255, 302-307`
- **Mechanism**:
  In `traced_refund()`, the `try ... except (ValueError, KeyError, TypeError):` block ends at line 300, leaving lines 302–307 (`original[(address.lower(), int(key, 16))] = int(start, 16)`) unprotected. Any non-hex storage key or `start` value (e.g. `{'-': 'not_hex'}` or `{'*': {'from': 123}}`) raises an uncaught `ValueError` or `TypeError`. Likewise, line 255 (`tuple(f['traceAddress'][:-1])`) is outside `try...except` and raises `TypeError` if `traceAddress` contains a nested list or dict.

---

### 16. `probes.py` & `rules.py`: Uncaught `TypeError` when `blockNumber`, `blockHash`, or `transactionHash` is unhashable or `None`
- **Location**: `trace_interop/probes.py:165-171`, `trace_interop/rules.py:155, 158, 292`
- **Mechanism**:
  - `probes.py:170`: `dict.fromkeys(at(r) for r in records)` raises `TypeError: unhashable type: 'list'` if a record in `result` has `blockNumber: []` or `blockHash: {}`.
  - `rules.py:155, 158`: `{mapping(f).get('blockNumber') for f in result}` and `{mapping(e).get('transactionHash') for e in result}` raise `TypeError` on list/dict values.
  - `rules.py:292`: `blocks = sorted({frame.get('blockNumber') for frame in result if isinstance(frame, dict)})` (without `key=str`) raises `TypeError: '<' not supported between instances of 'NoneType' and 'int'` if one frame has `blockNumber: 48` and another has `blockNumber: None` or `'0x30'`.

---

### 17. `laws.py`: Law `L10` crashes with `AttributeError` when `trace_filter` returns a list containing non-dict elements
- **Location**: `trace_interop/laws.py:279-295`
- **Mechanism**:
  `L10` checks `isinstance(result, list)` but does not check `all(isinstance(f, dict) for f in result)`. When a `trace_filter` response is `[None]`, `frame.get("type")` at line 293 raises `AttributeError: 'NoneType' object has no attribute 'get'`. Also, in `L01` (`laws.py:160`), `if frames and all(isinstance(f, dict) for f in frames):` silently skips `tree_violations` if `frames` contains a non-dict element.

---

### 18. `fee_policy.py` & `scenarios.py`: Uncaught `AttributeError` when `observation['response']` or `response['error']` is `None` or non-dict
- **Location**: `trace_interop/fee_policy.py:133-135`, `trace_interop/scenarios.py:159, 225`
- **Mechanism**:
  `observation.get('response', {})` returns `None` when `'response': None` is present in `observation`, and `response.get('error', {})` returns `None` or `str` when `'error'` is `None` or a string, raising `AttributeError: ... object has no attribute 'get'`. In `scenarios.py:225`, `head['number']` also raises `KeyError: 'number'` if `manifest['head']` is `{}`.

---

### 19. `execution_models.py`, `fee_policy.py`, `rules.py`, `coverage.py`: Case-sensitive `stateDiff` and `_alloc` address lookups
- **Location**: `trace_interop/execution_models.py:422, 553`, `trace_interop/fee_policy.py:175, 191-195`, `trace_interop/rules.py:671-689`, `trace_interop/coverage.py:300`
- **Mechanism**:
  While `execution_models.py` normalizes `stateDiff` keys with `.lower()` for `H26` (line 408) and `H17` (line 437), it uses case-sensitive `diff.get(authority)` for `H18` (line 422) and `diff.get(block.get('miner'))` for `H16` (line 553). Similarly, `fee_policy.py:191-195` (`diff.get(step['sender'])`, `diff.get(MINER)`, `diff.get(step['recipient'])`), `rules.py:671-689` (`prefunded-empty`, `auth-*`, `destroy-trace-*`), and `coverage.py:300` perform case-sensitive lookups on `stateDiff`, causing false negatives if a client formats `stateDiff` keys with EIP-55 checksums. Furthermore, in `rules.py:688` (`destroy-trace-55`), `(balance is None or mapping(change).get('balance') == ...)` silently skips the deleted balance check whenever `_alloc` is absent from `context`.

---

### 20. `chain_model.py` & `vm_model.py`: `resolve_block()` fails on EIP-1898 dicts and uppercase hex numbers; `execute()` raises `UnsupportedProgram` on large calldata/code offsets
- **Location**: `trace_interop/chain_model.py:13-32`, `trace_interop/vm_model.py:181, 188`, `trace_interop/chain_model.py:67-70`
- **Mechanism**:
  1. `resolve_block(context, selector)` immediately returns `None` if `not isinstance(selector, str)` (rejecting EIP-1898 object selectors `{'blockNumber': ...}` / `{'blockHash': ...}`) and checks `if selector in blocks:` without `.lower()` (failing on uppercase hex numbers like `'0x1A'`).
  2. In `vm_model.execute()`, `data[offset:offset+32]` (line 188, `CALLDATALOAD`) and `origin[source:source+size]` (line 181, `CALLDATACOPY`/`CODECOPY`) raise `IndexError: cannot fit 'int' into an index-sized integer` when `offset >= 2**63` (e.g. `PUSH32 0xff..ff CALLDATALOAD`), which the outer `except (IndexError, OverflowError)` misclassifies as `UnsupportedProgram('invalid model program')` instead of pushing `0`.
  3. In `vm_model.execute()` lines 133 and 139, `SLOAD` and `SSTORE` call `slot_value(slot)` before checking whether `gas` is sufficient (`gas < cost` or `gas <= 2300`), raising `UnsupportedProgram('unanchored storage read')` instead of `OutOfGas` on low-gas calls.

---

### 21. `isolation.py` & `fee_policy.py`: Spurious `blocked` status hides failures in `isolate()`, `resolve_dependencies()`, and `assess_compatibility()`
- **Location**: `trace_interop/isolation.py:50-86`, `trace_interop/fee_policy.py:204-243`
- **Mechanism**:
  1. In `isolation.isolate()` (lines 60–62), when `error_owner()` matches a validation message on `trace_call`, `trace_callMany`, or `trace_rawTransaction`, it rewrites every `role='result'` check from `'change_needed'` to `'blocked'` even if no check for `owner[0]` (`H15` or `H13`) exists on that case—resulting in zero `change_needed` checks on a failing response.
  2. In `isolation.resolve_dependencies()` (lines 76–77), `cases = [record['case']] if any(c['status'] == 'change_needed' for c in own) else [] if own else differing[topic]`: if the same record has a check for `topic` whose status is `'blocked'`, `own` is non-empty so `differing[topic]` (from other cases in the same run where `topic` failed with `'change_needed'`) is ignored, leaving the dependent check as `'change_needed'` instead of `'blocked'`.
  3. In `fee_policy.assess_compatibility()` (lines 214–219), if `eth_call` succeeds (`left = ('output', '0x...')`) and `trace_call` fails with a root trace error other than `'insufficient balance for transfer'` (such as `'Out of gas'` or `'Reverted'`), `outcome` returns `(None, 'unclassified root execution error: ...')`, causing `assess_compatibility` to return `status: 'blocked'` instead of `'change_needed'`.

---

### 22. `oracles.py`: `anchor()` returns `(None, None)` instead of a mismatch when reference traces have wrong root, depth-1 call, or suicide counts
- **Location**: `trace_interop/oracles.py:73-105`
- **Mechanism**:
  When `tx-calltree` in a reference trace (`block-tree` or `transaction-tree`) has `len(roots) != 1` (line 73), invalid `traceAddress`/`subtraces` (lines 78–84), `len(ordinary) != 7` (line 97), or `len(suicides) != 1` (line 103), `anchor()` returns `(None, None)` instead of appending to `mismatches`. Callers (`coverage.py:139`, `rules.py:721`) treat `(None, None)` as an unavailable reference rather than a fixture contradiction, turning reference trace bugs into `unassessed`/`blocked` checks. Also, `extra` at line 66 ignores `f.get('type') == 'reward'`, allowing fabricated reward frames in `anchor()` baselines.

---

### 23. `report.py` & `presentation.py`: Missing `decisions/fixes.json` in `ASSESSMENT_SOURCES`, `fixes_graph` crash on closed dependency PRs, and family page omissions
- **Location**: `trace_interop/report.py:16`, `trace_interop/presentation.py:182, 235-255, 345, 616-618`
- **Mechanism**:
  1. `report.py:16`: `ASSESSMENT_SOURCES` omits `'decisions/fixes.json'`, even though `presentation.render()` reads `decisions/fixes.json` to compute verdicts (`🛠️ Fix submitted`), `reports/progress.json`, `reports/progress.svg`, `reports/clients/*-work.svg`, `decisions/README.md`, and `docs/client-fixes.md`.
  2. `presentation.py:235, 255`: In `fixes_graph()`, if an unfinished PR has `depends_on: [url]` where `prs[url]['state'] == 'closed'`, `prs[url]['stage']` is `'closed'`, which is absent from `STAGE_STYLES`, causing `list(STAGE_STYLES).index('closed')` to crash with `ValueError: 'closed' is not in list`.
  3. `presentation.py:616-618`: On multi-build family pages (`reports/clients/besu.md`, `anvil.md`), `checks` combines both release and development builds. When `besu_release` has `change_needed` on H15/H33 and `besu_development` is `Partially assessed` (0 `change_needed`, 2 `blocked`), `any(q['status'] in BAD for q in checks)` puts the topic only in `## Changes to discuss` and omits `besu_development`'s gaps from `## Assessment gaps`. Conversely, when `anvil_release` is `Blocked` on H18/H28 and `anvil_development` has 100% `matches`, the topic is placed in `partial` (`## Assessment gaps`) and omitted from `✅ Behaviors with no difference in the checked cases` for `anvil_development`.
  4. `presentation.py:345`: `examples()` ranks `'observation'` (priority 2) ahead of `'matches'` (priority 3), so for `H12` in the `✅ Behaviors with no difference in the checked cases` table, it links only the 3-arg extension `observation` cases (where clients returned `-32602`) instead of the passing 2-arg baseline cases.

---

### 24. `scripts/refresh_fixes.py`: Branch-map collision corrupts `via`/`uptake` for merged PRs, and `version()` crashes on `>=` Cargo requirements
- **Location**: `scripts/refresh_fixes.py:85-96, 155, 188-200`
- **Mechanism**:
  1. Line 188 builds `branches = {(repository(url), info['headRefName']): url for url, info in infos.items()}`. Because `headRefName` does not include the head repository owner, any PR opened from a contributor fork's `main` or `develop` branch registers `(repo, 'main')` or `(repo, 'develop')` in `branches`. Line 198 (`via = branches.get((repository(pr['url']), info['baseRefName']))`) then matches every normal PR targeting `main`/`develop` in that repository, overwriting its `merge_commit` and `uptake` with the fork PR's state.
  2. Line 87: `re.match(r'[\^=~v ]*(\d+(?:\.\d+)*)', text)[1]` raises `TypeError: 'NoneType' object is not subscriptable` on Cargo requirements starting with `>=` or `<=`, and `admits("0.0", "0.0.5")` returns `False` because `version("0.0")` pads to `(0, 0, 0)` before locating the rightmost nonzero component.
  3. Line 155: `target, = {ref['repository']... for ref in own}` raises `ValueError: not enough values to unpack` if a library PR's client has no measured builds in `builds`.

---

### 25. `cli.py` & `replica.py`: `selected_cases()` drops reference twins on `--case`, and `replica.translate()` uses sequential `str.replace`
- **Location**: `trace_interop/cli.py:352-385`, `trace_interop/replica.py:86-90`
- **Mechanism**:
  1. When running a focused case reproduction (`trace-interop run ... --case "^CASE$"`) as instructed in `reports/technical.md`, `selected_cases()` includes `control-*` / `_control/*` cases, and `execute()` includes `trace_transaction` / `block-*` for `trace_filter` and `trace_get`. However, neither includes cases referenced via `probe['reference']` (such as `field-gas-omitted-eth-call` for `field-gas-omitted`, `filter-block-2` for `filter-blockhash`, `blob-fee-none-stateDiff` for `blob-fee-priced-stateDiff`) or `case['fee_reference']` (in `fee-compat`). Assessing the resulting capture marks the target case as `blocked` (`"The reference ... returned no result"`).
  2. `replica.translate(text, mapping)` loops `for old, new in mapping.items(): text = text.replace(old[2:], new[2:])`. Sequential replacement is non-atomic (if `new_1` matches `old_2`, it is replaced twice) and matches unprefixed 64-hex substrings at arbitrary offsets inside bytecode, memory, or return data.

---

### 26. `scripts/compare_responses.py` & `scripts/build_tech_tree.py`: KeyError / shallow glob in `compare_responses.py`, and Anvil total mismatch in `build_tech_tree.py`
- **Location**: `scripts/compare_responses.py:16-18, 41`, `scripts/build_tech_tree.py:113-118`, `site/tech-tree/tree.toml:154`
- **Mechanism**:
  1. `compare_responses.result()` accesses `observation['raw_response']` whenever `'response' not in observation`, raising `KeyError: 'raw_response'` on `transport_error` and `harness_error` observations (which have `'raw_log'` and `'detail'`, not `'raw_response'`). Also, `groups()` uses `Path(args.evidence).glob('*/' + name)` (1 level deep) instead of `rglob(name)`, finding 0 runs when given `evidence` or `evidence/2026-10-11`.
  2. `site/tech-tree/tree.toml:154` states that Anvil is *"tracked for tooling compatibility and left out of the totals"*, but `scripts/build_tech_tree.py:107-118` iterates over all `progress['clients']` (which includes Anvil), counting Anvil in `totals.agree`, `totals.of` (`5 * 33 = 165`), `totals.merged`, `totals.open`, and `totals.clients`.
