"""Compress the checksummed capture logs of retained runs in place.

A run's checksums.json is never rewritten: each compressed log keeps its original digest,
which verification checks against the decompressed bytes. The original is deleted only
after its deterministic gzip decompresses to exactly those bytes.
"""
import argparse
import hashlib
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from trace_interop.cli import gzip_bytes, log_bytes, read, verify_evidence


def convert(folder):
    """Return (folder, original bytes, compressed bytes, logs converted)."""
    before = after = count = 0
    for name, digest in read(folder/'checksums.json').items():
        path = folder/name
        if not name.endswith('.log') or not path.exists():
            continue
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != digest:
            raise ValueError(f'{path} does not match checksums.json')
        packed = gzip_bytes(data)
        Path(str(path) + '.gz').write_bytes(packed)
        if log_bytes(Path(str(path) + '.gz').with_suffix('')) != data:
            raise ValueError(f'{path} does not round-trip')
        path.unlink()
        before, after, count = before+len(data), after+len(packed), count+1
    verify_evidence(folder)
    return folder, before, after, count


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('evidence', type=Path, help='an evidence tree, e.g. evidence')
    parser.add_argument('--jobs', type=int, help='parallel runs (default: CPU count)')
    args = parser.parse_args()
    folders = sorted(p.parent for p in args.evidence.rglob('checksums.json'))
    before = after = count = 0
    with ProcessPoolExecutor(args.jobs) as pool:
        for folder, b, a, n in pool.map(convert, folders):
            before, after, count = before+b, after+a, count+n
    print(f'compressed {count} logs in {len(folders)} runs: {before:,} -> {after:,} bytes')


if __name__ == '__main__':
    main()
