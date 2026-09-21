# What execution-apis needs to accept a tracing proposal

Assessment as of **2026-09-22**, based on upstream main at `465d1b98d43e` and the reviews below.
The practical target is a reviewable contract, explicit client support, and fixtures that can
be validated and replayed upstream. No published fixed vote count or universal all-clients-pass
gate was found.

## Written requirements

| Requirement | Implication for this proposal | Source |
| --- | --- | --- |
| Motivation, specification changes, test cases, supporting acknowledgements and rationale for non-obvious choices | Supply the YAML, link the discrepancy cases, explain compatibility consequences, and link actual client feedback. A supportive call does not approve every proposed rule. | [Proposal guidance](https://github.com/ethereum/execution-apis/blob/465d1b98d43e94ff3d57e904fd7d4bea7f6b804c/docs-api/docs/contributors-guide.md#proposal) |
| Rough consensus through review by execution-client developers; no formal standardization process | Seek named reviews of specific contracts. Neither a four-of-six arithmetic majority nor silence establishes acceptance. | [Standardization](https://github.com/ethereum/execution-apis/blob/465d1b98d43e94ff3d57e904fd7d4bea7f6b804c/docs-api/docs/contributors-guide.md#standardization) |
| Specifications in the repository are canonical and required for Hive rpc-compat | Optional implementation or a tracing profile still needs explicit maintainer agreement; it cannot be inferred from our draft or harness. | [Introduction](https://github.com/ethereum/execution-apis/blob/465d1b98d43e94ff3d57e904fd7d4bea7f6b804c/docs-api/docs/contributors-guide.md#introduction) |
| Specification and speccheck must pass. Test generation is required for existing methods; maintainers may permit CI exceptions for new methods awaiting upstream Geth support | The normal path is Geth implementation plus reproducible `rpctestgen` fixtures. A Geth fork demonstrates feasibility but does not automatically satisfy that path. An explicit exception is possible; it is not an automatic right to merge without tests. | [CI requirements](https://github.com/ethereum/execution-apis/blob/465d1b98d43e94ff3d57e904fd7d4bea7f6b804c/docs-api/docs/contributors-guide.md#ci-requirements) |
| Backward compatibility is a guiding constraint; the guide has no generally accepted path for incompatible API changes | Explain how existing users of flat indexing or OR filtering would migrate. Being new to this repository does not erase an existing method's users. | [Compatibility guidance](https://github.com/ethereum/execution-apis/blob/465d1b98d43e94ff3d57e904fd7d4bea7f6b804c/docs-api/docs/contributors-guide.md#backwards-compatibility) |
| `.io` is tool-agnostic, though `rpctestgen` is preferred; fixtures use the repository's genesis and chain | Handwritten cases are a viable proposal artifact. Adapt them to the upstream chain and test them in Hive; do not copy research-chain hashes. Generation CI still needs the normal integration or an explicit exception. | [Test format and generation](https://github.com/ethereum/execution-apis/blob/465d1b98d43e94ff3d57e904fd7d4bea7f6b804c/docs-api/docs/tests.md) |

## What recent reviews show

| Precedent | Observed acceptance/review pattern | What we can infer |
| --- | --- | --- |
| [Opcode tracing #762](https://github.com/ethereum/execution-apis/pull/762), merged June 16 | Scoped the default opcode tracer, leaving named tracers out. Nethermind, Reth and Besu submitted approvals; reviewers raised implementation concerns such as timeout support. The author documented remaining coverage gaps. [A later comment](https://github.com/ethereum/execution-apis/pull/762#issuecomment-4192722688) says the Geth implementation merged and the dependency pin needed updating. | A bounded tracing specification can land before every edge case is covered. This is not proof that Geth integration was waived: the PR body records an earlier fill failure, while later discussion records a merged Geth fix. |
| [callTracer #855](https://github.com/ethereum/execution-apis/pull/855), still open | The proposal combines a per-client impact table, targeted fixtures and draft client fixes after a concrete log-index decision. [The maintainer describes those draft fixes](https://github.com/ethereum/execution-apis/pull/855#issuecomment-5764798743). | This is a directly relevant review model, not an accepted policy precedent. Its recursive-schema tooling overlaps our branch; compare and consolidate that work before submitting a separate tooling PR. |
| [net methods #843](https://github.com/ethereum/execution-apis/pull/843), merged August 24 | The maintainer [explicitly waited for the remaining ethrex fix](https://github.com/ethereum/execution-apis/pull/843#issuecomment-5398922115). | Avoidable client regressions can block an otherwise small proposal. There is no basis for promising that a majority alone will be enough. |
| [testing_commitBlockV1 #801](https://github.com/ethereum/execution-apis/pull/801), merged August 27 | The method, Geth generator integration and fixtures landed with companion implementation work. A [fresh Hive replay](https://github.com/ethereum/execution-apis/pull/801#issuecomment-5412217059) passed on Geth and Nethermind after a simulator dependency merged. | Concrete implementation and replay evidence matter. This testing-namespace example does not establish optional support policy for the trace namespace. |

## Recommended submission criteria for our draft

These are our inferred readiness criteria, not additional upstream rules:

1. Keep the complete proposal visible, with clearly marked unresolved contracts and no extension-support failures disguised as baseline failures.
2. Make every proposed rule discoverable in the pinned specification, including the shared precompile-inclusion rule. Keep JSON-schema checks distinct from semantic execution checks.
3. Present the affected clients, migration consequences and explicit support or objections for each disputed behavior. Advance independent reporting fixes through the [client-fix tracker](client-fixes.md).
4. Prepare a small upstream-chain fixture set, starting with an ordinary successful transaction and one discriminating edge case. Successful replay of the easy case is an integration milestone, not agreement on the whole method.
5. Show passing build/schema/lint checks and Hive results on exact client commits. State separately whether generator integration works with upstream Geth, only with our fork, or requires an agreed exception.
6. Resolve overlap with #855's schema/dereferencing and documentation changes before choosing an upstream patch split.

A draft PR can solicit the missing reviews; it does not need final agreement to be opened.
For a merge, the remaining questions requiring an actual maintainer decision are the supported-method
policy, any generator exception, and acceptance of specific compatibility transitions. The published
guidance already establishes the rest of the process, so a general request to invent acceptance criteria
would add little.
