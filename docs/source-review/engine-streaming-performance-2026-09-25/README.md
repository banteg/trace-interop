# Engine streaming recovery performance, 2026-09-25

Three revisions of Nethermind are compared:

- **Base:** `afd6a6dfbbef785afa48cb4a3a09706b5b6cf2ca`, the latest upstream master merged into the submitted PR.
- **Submitted:** `6b84ffcb6dffa4721287fbe274501278b91aee1b`, staging every streamable result.
- **Revised:** `e774a5039b9e6f2079d233753489e7b1fa4a236d`, recovery restricted to deferred execution.

## Result

The revised implementation removes the Engine staging path and its associated rental/copy. Across the 28 case ratios (equal weight per case, averaging the two runs first), versus base:

| Metric | Submitted | Revised |
| --- | ---: | ---: |
| Allocated bytes/request | +0.768% | +0.040% |
| Requests/sec | -1.077% | +0.117% |
| p50 latency | +0.562% | +0.022% |
| p95 latency | +5.061% | -1.256% |

These medians describe this matrix, not a production-weighted workload. In the stable small responses, the submitted implementation added about 432–456 B/request; the revised implementation is typically about 24 B/request above base. It therefore removes almost all measured additional allocation but does **not** make the response architecture allocation-identical to base. The response retains one optional context reference.

There is no broad throughput or latency regression in this comparison. Per-case means remain noisy: revised throughput ranges from -24.4% to +18.9% versus base, and p95 from -31.3% to +34.8%. For example, the same revised getPayloadV5/8,200-byte/concurrency-1 case measured 3,742 and 2,174 requests/sec in the two runs, while base measured 3,498 and 3,549. That reversal is a reason to avoid attributing each mean difference to code. A dedicated quiet host and longer repeated sampling would be needed to enforce a tight per-case performance threshold; these measurements do not independently certify a strict zero-regression merge gate.

See [all 28 comparisons](results.md), [all 168 measured rows](results.csv), and [the calculated summary](summary.json). The six `*-benchmark-steady-*.txt` files preserve the original final-run measurements. The allocation and direct-writer identity evidence support the design change even where timing cannot resolve small effects.

## Method

The temporary NUnit fixture runs the production `Startup.ProcessJsonRpcRequestCoreAsync` and HTTP response sink behind a real Kestrel loopback listener. An Engine module substitute returns fresh **actual** GetPayloadV5DirectResponse, GetPayloadV6DirectResponse, BlobsV2DirectResponse and PayloadBodiesV1DirectResponse objects. Authentication returns true, selecting the authenticated Engine HTTP path; signature verification and payload construction/execution are outside the measurement. The client reuses HttpClient connections and consumes each complete response.

The matrix has 28 cases: four API methods, transaction data lengths 0/7,200/8,200/131,072 bytes, and concurrency 1/8. Blobs use empty or a full 128 KiB blob, because a blob cannot be sized around 16 KiB. The recorded response sizes verify coverage below/above the staging boundary for the other methods. Each case warms with 1,000 requests, then measures 1,000 requests per worker. Timings exclude explicit GC and result logging. Allocation is process-wide managed allocation, including the HTTP client, Kestrel and substitute; it is not server-only or a pooled-memory occupancy measurement.

Each arm runs in a fresh process. Order: base → submitted → revised, then revised → submitted → base. .NET SDK 10.0.300, .NET/ASP.NET runtime 10.0.8, Fedora 44 kernel 7.2.7, Intel Core Ultra 9 185H; `DOTNET_TieredCompilation=0` avoids tier transitions during short runs, and `taskset -c 0-11` keeps all arms on the same six physical performance cores. The machine also runs normal services: affinity does not reserve cores. These are comparative HTTP benchmarks, not a full execution-client throughput benchmark or a statistical guarantee of zero regression.

The initial exploratory pass used 100 warm-ups and 100 iterations/worker with default scheduling/JIT settings. Its allocation measurements showed the removal of staging costs, but its latency variance was too large for a performance conclusion. Those raw rows are retained under `exploratory/`. The final comparison uses the longer controlled configuration described above; no production code changed between the two experiments.

## Reproduce

Create isolated worktrees at the three SHAs and apply the matching `base-harness.patch`, `submitted-harness.patch`, or `revised-harness.patch`. Each patch changes only StartupTests; the harness is deliberately excluded from the production PR. Then build each worktree:

```sh
dotnet build src/Nethermind/Nethermind.Runner.Test/Nethermind.Runner.Test.csproj -c release
```

From this directory, run:

```sh
uv run python run.py --base /path/to/base --submitted /path/to/submitted --revised /path/to/revised --output /path/to/results --cpus 0-11
```

Use the same .NET SDK and CPU set for every arm. The runner checks both test success and exactly 28 recorded measurements per arm; a passing test with missing measurements is rejected. Allocation/op, requests/sec, p50 and p95 latency are retained in each raw text file.
