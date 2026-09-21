# Reviewing a proposed rule

Start with [your client's impact page](../reports/README.md), then follow a decision ID.
Each record contains proposed behavior, rationale, observations and open questions.
Assertion results identify exact builds and cases. Response previews link
to the immutable source evidence.

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

The fork's YAML is the single specification source. Once a rule is agreed, promote its
assertions into upstream `.io` fixtures on the upstream test chain, extending that chain
only when necessary. Existing research-chain hashes cannot simply be pasted into upstream
tests. Keep unresolved examples in this project. Reuse Hive and its client adapters;
upstream reusable runner improvements independently.

Geth-based `rpctestgen` support and optional-method policy remain upstream decisions.
Neither is silently assumed by this project. No upstream PR is created by these tools.
