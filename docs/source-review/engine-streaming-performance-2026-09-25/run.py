"""Run the same built StartupTests benchmark on three Nethermind revisions."""
import argparse
import os
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
for arm in ("base", "submitted", "revised"):
    parser.add_argument("--" + arm, type=Path, required=True)
parser.add_argument("--cpus", default="0-11", help="Linux CPU affinity shared by all arms")
parser.add_argument("--output", type=Path, required=True)
args = parser.parse_args()
args.output.mkdir(parents=True, exist_ok=True)
project = "src/Nethermind/Nethermind.Runner.Test/Nethermind.Runner.Test.csproj"
for round_number, order in enumerate((("base", "submitted", "revised"), ("revised", "submitted", "base")), 1):
    for arm in order:
        prefix = args.output.resolve() / f"{arm}-{round_number}"
        raw = prefix.with_suffix(".txt")
        raw.write_text("")
        env = os.environ | {"ENGINE_BENCH_OUTPUT": str(raw), "DOTNET_TieredCompilation": "0"}
        with prefix.with_suffix(".log").open("w") as log:
            result = subprocess.run(
                ["taskset", "-c", args.cpus, "dotnet", "test", "--project", project, "-c", "release", "--no-build", "--", "--filter",
                 "FullyQualifiedName~Engine_direct_response_performance"],
                cwd=getattr(args, arm), env=env, stdout=log, stderr=subprocess.STDOUT,
            )
        rows = [line for line in raw.read_text().splitlines() if line.startswith("ENGINE_BENCH ")]
        print(arm, round_number, "exit", result.returncode, "rows", len(rows), flush=True)
        if result.returncode or len(rows) != 28:
            raise SystemExit(f"Invalid benchmark arm: inspect {prefix.with_suffix('.log')}")
