# Reviewing a proposed rule

Start with [your client's impact page](../reports/README.md), then follow a decision ID.
Each record contains proposed behavior, rationale, observations and open questions.
Release and development results appear side by side. Each example links the exact
request, response evidence and relevant client code.

Discuss specification changes on [execution-apis #895](https://github.com/ethereum/execution-apis/pull/895).
The PR is a draft; client agreement and upstream fixture integration remain open.

For a disagreement, record:

1. The proposed rule and a minimal discriminating case.
2. Each affected build's observation, including unsupported/error/setup outcomes.
3. Whether the question is execution correctness, API semantics, output encoding or scope.
4. The recommended behavior and evidence supporting it.
5. Compatibility consequences for existing consumers; do not infer implementation effort
   from the number of failing cases.
6. Client feedback and disposition: proposed, agreed, superseded, or deferred.

Client agreement does not prove correct EVM semantics. Use the applicable execution rules,
independent state controls and bytecode reasoning where correctness is at issue. Keep
optional extensions and pending policy choices explicit instead of calling them bugs.

## Contribution path

See [upstream acceptance criteria](upstream-acceptance.md) for the documented rules and
review precedents, and [client fixes](client-fixes.md) for the current patch queue.

The fork's YAML is the single specification source. Once a rule is agreed, promote its
assertions into upstream `.io` fixtures on the upstream test chain, extending that chain
only when necessary. Existing research-chain hashes cannot simply be pasted into upstream
tests. Keep unresolved examples in this project. Reuse Hive and its client adapters;
upstream reusable runner improvements independently.

The normal test-generation path uses upstream Geth. Published guidance permits explicit
maintainer CI exceptions for new methods awaiting Geth support; it does not automatically
waive fixtures or schema validation. Optional-method policy remains unresolved.
No upstream PR is created by these tools.

## Maintaining the reports

Edit human descriptions and proposed client changes in `decisions/impact.json`;
keep the behavior decisions in `decisions/ledger.json`. Source entry points live in
`decisions/sources.json`, pinned to a tested revision with a line anchor and file hash.
When updating a source link, fetch that revision and verify both the anchor and hash.
Record exact tested versions and upstream committer timestamps in
`locks/source-revisions.json`; image creation dates do not establish source chronology.

Run `uv run python scripts/build_reports.py` to regenerate the pages. Keep summaries
focused on what a maintainer needs to change. Full assertions, run inventories and
schema diagnostics belong in the linked examples and technical appendix.
