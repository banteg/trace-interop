# Mirror checks and TraceStore round-trip reproduction, 2026-09-30

The harness now checks the requested path in L05 and the transaction's presence and identity in L08 when the pinned trace profile applies. Native tests confirm both Nethermind TraceStore round-trip failures at the supplied revision.

## Harness

`evaluate(..., profile=True)` enables the profile requirements. Report generation enables them only when it has the pinned specification. Without that profile, record membership and component comparisons retain their prior semantics. Both sides must be successful results without embedded RPC errors, and the run must represent a frozen chain.

L05 decodes canonical hexadecimal selectors and compares the entire selected record with the same client's transaction tree. It covers roots, children, nested paths, null for an absent path, and a wrongly returned null. An empty reference tree does not establish that the transaction exists, so no profile path assertion is inferred from it. Invalid integer selectors remain the request-validation checks' responsibility.

L08 uses the independently decoded transaction block and index. An omitted envelope fails; the envelope at that index must carry the requested transaction hash, even if the single replay is also mislabeled. Identity applies even with disjoint trace selections. Output and shared components are compared, while unshared components are excluded. Unknown blocks and moving-chain scenarios are not paired.

The frozen reports now expose 18 L05 violations: five each in Anvil release and development, and eight in Nethermind 2.0.0. L08 has five violations in Nethermind 2.0.0, including one additional instance of its known stateDiff-only missing output. No new captured omission or wrong-hash defect is claimed. These are additional law observations, not new client runtime captures or changes to decision progress counts.

Validation: all 351 unit tests passed, nine-method schema checks passed, and `trace-interop verify` confirmed 72 frozen inputs and 33 decisions. Reports were regenerated after the final assessment-source change.

## Nethermind reproduction

Source: `2cb4e9e655b695063557df2eb57312128941e88c`, the exact revision in the supplied finding. Source archive SHA-256: `057ffc2a4c5712346b4d52bf300d7b0e2fce2ed51e10df46c5ee94191fc0d565`.

Fedora, .NET SDK 10.0.300, Release: seven serializer tests executed, two failed and five passed ([complete log](nethermind-roundtrip.log)). The non-null vmTrace case throws NotSupportedException from ParityVmTraceConverter.Read. The nonempty stateDiff case throws NotImplementedException from ParityAccountStateChangeJsonConverter.Read. Both reach those readers through production ParityLikeTraceSerializer.Deserialize after serialization succeeds. Trace-only and empty-stateDiff controls pass, as do the three existing serializer tests. This is a reproduced client defect, not merely a predicted exception. No client fix is included.

The [test patch](nethermind-roundtrip-test.patch) adds four cases to the existing TraceSerializerTests fixture. Each constructs a call trace, serializes it with the production gzip TraceStore serializer, deserializes those bytes, and compares the RPC JSON before and after. Cases are trace-only, empty stateDiff, non-null vmTrace with one code byte and no operations, and a nonempty stateDiff containing one account code change. No production source is modified.

[add-roundtrip-test.py](add-roundtrip-test.py) applies the test to an isolated unpacked source tree. Run with .NET SDK 10.0.300:

```sh
python3 add-roundtrip-test.py /path/to/nethermind
cd /path/to/nethermind
dotnet test --project src/Nethermind/Nethermind.JsonRpc.TraceStore.Test/Nethermind.JsonRpc.TraceStore.Test.csproj -c release -- --filter FullyQualifiedName~TraceSerializerTests
```

The source path corroborates the downstream consequence: TraceStoreRpcModule.TryGetBlockTraces deserializes the full stored list before TryGetStoredTrace filters the selected transaction's components. TraceStoreConfig defaults to Trace | Rewards. Native serializer reproduction does not by itself claim an HTTP RPC capture of the configured cache path.

Reth pending-state and Geth Frontier CREATE remain supplied source-backed candidates; this follow-up does not claim native execution of either.
