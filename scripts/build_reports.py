from pathlib import Path
from trace_interop.report import generate
root=Path(__file__).resolve().parents[1]
from trace_interop.inventory import report_runs
runs=report_runs(root)
generate(root,runs,root/'reports')
