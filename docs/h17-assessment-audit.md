# H17 account-existence assessment audit

Audited on 2026-09-24 against the [11:07 UTC captured matrix](../evidence/2026-09-24/current-matrix/README.md)
and source pinned to its tested development builds. The retained responses first
established the assessment corrections. The subsequent
[fresh matrix rerun](../evidence/2026-09-24/h17-retest/README.md) and
[inspector patch tests](../evidence/2026-09-24/h17-client-fix/README.md)
retain separate published-build and proposed-fix evidence.

**The original all-native-clients-differ verdict overstated H17.** Besu's only
failure was an unavailable state diff, and Erigon's only failure was an environment
value being checked again as deployed code. Nethermind and Reth have reproducible
account-existence marker differences on independently valid transfers.

## What the assessment got wrong

| Build(s) | Old H17 failure | Correction |
|---|---|---|
| Besu, both | `initial/raw-valid-default-block` returns `stateDiff: null`. Despite its name, the signed request has nonce 0 at a state where the sender nonce is 133. | Mark account-marker inspection blocked. The H13 invalid-transaction response finding remains. |
| Erigon, both | `coverage/model-environment` creates code containing its substituted `GASLIMIT`. Its balance, nonce and code all have `+` markers. | H17 accepts the markers; independent H08/H15 output/environment checks still fail. |
| Reth, both | `coverage/model-environment-free` creates code containing `BASEFEE = 0`. It also uses `+` correctly for the new contract. | Same separation. Other Reth H17 failures remain. |

The corrected creation check compares `stateDiff.code` with the returned runtime
under `+`, while still requiring the independently known creation nonce and
transferred balance. H08/H15 continue comparing output with the independent EVM
model. A wrong environment cannot become a second account-marker failure, and
a wrong marker or a diff inconsistent with the returned runtime still fails.

The generic model now treats a missing state-diff object as blocked for H17.
It does not turn that absence into evidence of incorrect account markers.
Raw captures are unchanged.

## Independent evidence for the remaining differences

The [model-transfer](../reports/cases/coverage/model-transfer.md) probe transfers
7 wei to `0x0000000000000000000000000000000000004444`. This address is absent
from the frozen genesis allocation and the selected chain has only two empty
blocks. The funded sender starts at nonce 10. No prior transaction could have
created the recipient, and its positive post-transfer balance makes its existence
unambiguous. The expectation does not come from another client's output.

The following is the recipient's complete account diff in both tested builds of
each native client in the earlier 11:07 UTC snapshot:

| Client | Balance | Nonce | Code | Storage |
|---|---|---|---|---|
| Besu | `{"+":"0x7"}` | `{"+":"0x0"}` | `{"+":"0x"}` | `{}` |
| Erigon | `{"+":"0x7"}` | `{"+":"0x0"}` | `{"+":"0x"}` | `{}` |
| Nethermind | `{"+":"0x7"}` | `{"+":"0x0"}` | `"="` | `{}` |
| Reth | `{"*":{"from":"0x0","to":"0x7"}}` | `"="` | `"="` | `{}` |

The Geth draft fork agrees with the first two rows. The
[two-transfer probe](../reports/cases/coverage/model-many-transfers.md) checks the
transition to an existing account in the second call. The
[prefunded-empty control](../reports/cases/a/prefunded-empty.md) passes on all nine
builds: its code and nonce correctly remain `=` because the account already
existed. That control is a transfer, not CREATE into a prefunded address.

The [empty-runtime creation](../reports/cases/coverage/model-empty-runtime.md)
probe independently derives its address from the sender and nonce 10. All clients
mark balance zero and nonce one as added. Nethermind alone reports empty code as
`=`; Reth correctly reports `{"+":"0x"}` for this contract creation. Nethermind
also omits the empty-code birth marker for the newly funded fee recipient.

## Why the code produces these results

### Nethermind: absent code and empty code collapse

At tested revision `2a3b2531`, [`StateProvider.ReportChanges`][nm-provider]
distinguishes absent and present accounts using nullable values. That produces
the correct balance and nonce births. But it suppresses `ReportCodeChange` when
both byte lengths, with null treated as zero, are zero. An absent account becoming
an account with empty code therefore produces no code callback.

[`ParityLikeTxTracer.ReportCodeChange`][nm-tracer] would retain a null pre-value
if called. Instead, the account's `Code` remains null and the
[`ParityAccountStateChangeJsonConverter`][nm-json] serializes that as `=`.
This explains the precise empty-code difference, including empty-runtime CREATE.
[Nethermind PR #13668](https://github.com/NethermindEth/nethermind/pull/13668)
addresses this birth case as well as deletion and merged on 2026-09-24 at
12:08 UTC as `7df26c3d48657a7f38f3cf56f9dff54401b30123`, after the matrix snapshot. Its converter reconstructs
`+ 0x` when code is unreported but balance changes from absent to present, and its
RPC expectations include the newly funded recipient. This corrects the earlier
shortlist claim that the birth fix was separate. The patch is absent from the
11:07 UTC captured builds. The fresh 12:21 UTC matrix resolves Nethermind
`9d6e8b8d`, a descendant of the merge, and confirms `+ 0x` for the fresh transfer
recipient, fee recipient and empty-runtime contract. Its second transfer retains
`=` for existing nonce/code. Release `bec830cd` still has the original difference.
The new [converter](https://github.com/NethermindEth/nethermind/blob/9d6e8b8d4f8f1d3518cfbc852725d8ab35c8f027/src/Nethermind/Nethermind.Blockchain/Tracing/ParityStyle/ParityAccountStateChangeJsonConverter.cs#L140-L152) and
[retained responses](../evidence/2026-09-24/h17-retest/coverage/observations.json)
show both the mechanism and its observed result.

### Reth: contract creation is used as a proxy for account birth

Tested Reth `58a51b3e` calls the state-diff builder from its locked
`revm-inspectors 0.43.0`, revision `453c67d7`.
[`populate_state_diff`][reth-builder] first replaces a missing database account
with default zero values. It uses `Delta::Added` only when
`changed_acc.is_created()` and the original balance is zero.

An ordinary transfer to a previously absent recipient is outside that contract
creation branch. Its balance becomes a change from zero; nonce zero and empty
code stay unchanged. This matches the retained response exactly. A correction
needs to preserve original account existence rather than infer it from contract
creation or a zero balance. The [trace-call path][reth-call] builds the diff before
committing the simulated state, so this is not a comparison against the already
updated database.

### Besu and Erigon: explicit pre/post existence

Besu `f9572aa8` obtains the pre-account from the parent updater and passes absent
accounts as null to [`StateTraceGenerator.createDiffNode`][besu-state].
[`DiffNode.Serializer`][besu-json] selects `+` whenever only the post-value exists,
including empty code and zero nonce. The generator returns no diff when its
execution-frame list is empty; its missing-diff response is a separate issue.

Erigon `e26d9bd4` uses [`CompareStates`][erigon-state] to inspect both account
existence flags. The absent-to-present branch unconditionally sets balance, code
and nonce under `+`. Its environment probe's code bytes differ, but its existence
classification agrees with H17.

The Geth draft's [`stateDiff`][geth-state] likewise passes the pre/post existence
flags into each field's change encoder.

## Policy provenance and limits

Parity's [`diff_pod`][parity-state] applies `Born` to every field when the pre-account
is absent, and its [create/delete regression][parity-test] explicitly includes
zero nonce and empty code. H17's empty-field requirement is therefore supported
by historical semantics as well as the independent existence model. It remains
a proposal under review, not a claim of client-team agreement.

This audit confirms the captured transfer and simple-creation differences. It
does not establish complete behavior for reverted internal creations, CREATE into
prefunded addresses, same-transaction creation/destruction or storage enumeration.
Those require dedicated RPC endpoint-existence probes; H26 owns deletion semantics.

[Regression tests](../tests/test_h17.py) exercise both release/development frozen
responses, retain the environment failures under H08/H15, reject mutated markers
and inconsistent runtime bytes, and check the independent prestate and prefunded
control.

## Inspector fix and regression tests

[revm-inspectors PR #526](https://github.com/paradigmxyz/revm-inspectors/pull/526)
preserves the prestate database's `Some`/`None` result before defaulting the field
values. It uses birth markers for an absent account with a nonempty final state,
including transfer and fee recipients, as well as newly created contracts.
Existing accounts retain ordinary changed/unchanged fields. The omission of empty
non-created accounts and the existing selfdestruct handling are preserved.

The real-EVM tests exposed a second consequence of the old condition: CREATE
into an already existing account with zero balance was also incorrectly treated
as account birth. The new tests distinguish that case from both an absent address
and a prefunded address, using empty and nonempty runtime code.

On Fedora, the unchanged implementation fails two of the three new tests; with
commit `af80e453`, all **34 Parity integration tests pass**, including the existing
EIP-7702 and pre/post-Cancun selfdestruct cases. First and second transfers,
newly funded beneficiaries and zero-value controls are covered. The
[before/after evidence](../evidence/2026-09-24/h17-client-fix/README.md) records the
exact base, patch, dependency lock, commands and logs. This tests the inspector
directly; it is not a patched Reth RPC run or a claim that published Reth builds
already include the change. Historical empty-account clearing and complete
storage enumeration remain outside this fix.

[nm-provider]: https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.State/StateProvider.cs#L1150-L1200
[nm-tracer]: https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.Blockchain/Tracing/ParityStyle/ParityLikeTxTracer.cs#L362-L382
[nm-json]: https://github.com/NethermindEth/nethermind/blob/2a3b2531b4dcfaa58b21e4197c27cbab959a7f3e/src/Nethermind/Nethermind.Blockchain/Tracing/ParityStyle/ParityAccountStateChangeJsonConverter.cs#L130-L139
[reth-builder]: https://github.com/paradigmxyz/revm-inspectors/blob/453c67d7ccdf51327c9e7687ac6ba0b8651e7f87/src/tracing/builder/parity.rs#L509-L590
[reth-call]: https://github.com/paradigmxyz/reth/blob/58a51b3ee3f6714ded9207b244a273c8afb592fd/crates/rpc/rpc/src/trace.rs#L97-L116
[besu-state]: https://github.com/besu-eth/besu/blob/f9572aa82a2dadb3dd1b218d3ca97101540faf97/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/results/tracing/diff/StateTraceGenerator.java#L148-L163
[besu-json]: https://github.com/besu-eth/besu/blob/f9572aa82a2dadb3dd1b218d3ca97101540faf97/ethereum/api/src/main/java/org/hyperledger/besu/ethereum/api/jsonrpc/internal/results/tracing/diff/DiffNode.java#L64-L94
[erigon-state]: https://github.com/erigontech/erigon/blob/e26d9bd4056586e004488c31b561fb2663d46019/rpc/jsonrpc/trace_adhoc.go#L781-L917
[geth-state]: https://github.com/banteg/go-ethereum/blob/fa8ecb9242dda61858c44cf43c70d00548fbd7cd/eth/tracers/trace_capture.go#L233-L263
[parity-state]: https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/ethcore/pod/src/account.rs#L106-L140
[parity-test]: https://github.com/openethereum/parity-ethereum/blob/55c90d4016505317034e3e98f699af07f5404b63/ethcore/pod/src/state.rs#L88-L115
