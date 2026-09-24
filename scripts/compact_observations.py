"""Convert retained observations.json files to the compact observations.json.gz in place.

A run's checksums.json is never rewritten: it keeps the original observations.json digest,
which verification checks against the original writer's serialization of the reconstructed
observations. The original file is deleted only after its compact form reloads to exactly
the original bytes and that digest; a run that does not round-trip stays unconverted.
"""
import argparse
import hashlib
import json
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from trace_interop.cli import (
    COMPACT_OBSERVATIONS,
    OBSERVATIONS,
    compact_bytes,
    load_observations,
    read,
    serialize,
    verify_evidence,
)


def convert(folder):
    """Return (folder, original size, compact size, None) or (folder, size, None, reason to keep the original)."""
    original, compact = folder/OBSERVATIONS, folder/COMPACT_OBSERVATIONS
    data = original.read_bytes()
    if compact.exists():
        return folder, len(data), None, f'{COMPACT_OBSERVATIONS} already exists'
    digest = hashlib.sha256(data).hexdigest()
    if read(folder/'checksums.json').get(OBSERVATIONS) != digest:
        return folder, len(data), None, f'{OBSERVATIONS} does not match checksums.json'
    try:
        packed = compact_bytes(json.loads(data))
    except ValueError as exc:
        return folder, len(data), None, str(exc)
    compact.write_bytes(packed)
    restored = load_observations(folder)
    if serialize(restored).encode() != data or compact_bytes(restored) != packed:
        compact.unlink()
        return folder, len(data), None, 'compact form does not reproduce the original bytes'
    original.unlink()
    verify_evidence(folder)
    return folder, len(data), len(packed), None


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('evidence', type=Path, help='an evidence tree, e.g. evidence')
    parser.add_argument('--jobs', type=int, help='parallel conversions (default: CPU count)')
    args = parser.parse_args()
    folders = sorted(p.parent for p in args.evidence.rglob(OBSERVATIONS))
    before = after = 0
    skipped = []
    with ProcessPoolExecutor(args.jobs) as pool:
        for folder, size, packed, reason in pool.map(convert, folders):
            if reason:
                skipped.append((folder, reason))
                print(f'kept      {folder}: {reason}')
                continue
            before += size; after += packed
            print(f'converted {folder}: {size:,} -> {packed:,} bytes')
    print(f'{len(folders) - len(skipped)} converted ({before:,} -> {after:,} bytes), {len(skipped)} kept')
    for folder, reason in skipped:
        print(f'  {folder}: {reason}')


if __name__ == '__main__':
    main()
