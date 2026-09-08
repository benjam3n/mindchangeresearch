from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PARTS = ROOT / 'checkpoint-parts'


def main():
    spec = json.loads((PARTS / 'manifest.json').read_text())
    expected_parts = [p['name'] for p in spec['parts']]
    assert expected_parts == [f'part-{i:03d}' for i in range(len(expected_parts))]
    assert sorted(p.name for p in PARTS.glob('part-[0-9][0-9][0-9]')) == expected_parts
    chunks = []
    for part in spec['parts']:
        data = (PARTS / part['name']).read_bytes()
        assert len(data) == part['bytes']
        assert hashlib.sha256(data).hexdigest() == part['sha256']
        chunks.append(data)
    data = b''.join(chunks)
    assert hashlib.sha256(data).hexdigest() == spec['sha256']
    output = ROOT / spec['archive']
    output.write_bytes(data)
    with zipfile.ZipFile(output) as archive:
        assert archive.testzip() is None
        assert len(archive.namelist()) == spec['file_count']
        assert len(archive.namelist()) == len(set(archive.namelist()))
        expected = {}
        for line in archive.read('Checkpoint_Manifest.sha256').decode().splitlines():
            digest, name = line.split('  ', 1)
            assert not Path(name).is_absolute() and '..' not in Path(name).parts
            assert name not in expected
            expected[name] = digest
            assert hashlib.sha256(archive.read(name)).hexdigest() == digest, name
        assert set(archive.namelist()) == set(expected) | {'Checkpoint_Manifest.sha256'}
    print(f'Verified {spec["file_count"]} archived files; SHA-256 {spec["sha256"]}')


if __name__ == '__main__':
    main()
