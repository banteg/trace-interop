from pathlib import Path
from trace_interop.report import generate
root=Path(__file__).resolve().parents[1]
runs=sorted(p.parent for p in (root/'evidence/2026-09-21').glob('*/manifest.json'))
generate(root,runs,root/'reports')
