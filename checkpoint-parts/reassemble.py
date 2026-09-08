"""Recover the complete corpus archive from verified transport parts."""
from pathlib import Path
import hashlib, io, json, zipfile
root = Path(__file__).resolve().parent
meta = json.loads((root / 'metadata.json').read_text())
if sorted(p.name for p in root.glob('part-[0-9][0-9][0-9]')) != [p['name'] for p in meta['parts']]:
    raise SystemExit('Unexpected or missing checkpoint parts')
chunks = []
for part in meta['parts']:
    data = (root / part['name']).read_bytes()
    if len(data) != part['bytes'] or hashlib.sha256(data).hexdigest() != part['sha256']:
        raise SystemExit(f"Invalid part: {part['name']}")
    chunks.append(data)
data = b''.join(chunks)
if len(data) != meta['archive_bytes'] or hashlib.sha256(data).hexdigest() != meta['archive_sha256']:
    raise SystemExit('Reassembled archive hash or length mismatch')
with zipfile.ZipFile(io.BytesIO(data)) as archive:
    if archive.testzip() or len(archive.namelist()) != meta['archive_entries']:
        raise SystemExit('Archive integrity failure')
    lines = archive.read('Checkpoint_Manifest.sha256').decode().splitlines()
    if len(lines) != meta['corpus_files']:
        raise SystemExit('Manifest entry count mismatch')
    names = set()
    for line in lines:
        checksum, name = line.split('  ', 1)
        path = Path(name)
        if path.is_absolute() or '..' in path.parts or name in names:
            raise SystemExit(f'Invalid manifest path: {name}')
        names.add(name)
        if hashlib.sha256(archive.read(name)).hexdigest() != checksum:
            raise SystemExit(f'Manifest mismatch: {name}')
    if set(archive.namelist()) != names | {'Checkpoint_Manifest.sha256'}:
        raise SystemExit('Unexpected archive entry')
out = root.parent / meta['archive']
out.write_bytes(data)
print(f"Verified {out.name}: {meta['archive_sha256']}; {meta['corpus_files']} corpus files")
