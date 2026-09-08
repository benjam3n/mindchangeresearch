"""Package the complete corpus and generate verifiable repository-safe parts."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = 'Mind_Change_Research_Checkpoint.zip'
MANIFEST = 'Checkpoint_Manifest.sha256'
PART_BYTES = 524288


def corpus_files():
    for path in sorted(ROOT.rglob('*')):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if any(p in {'.git', '__pycache__', 'node_modules', 'checkpoint-parts'} for p in relative.parts):
            continue
        if path.name in {ARCHIVE, MANIFEST, 'library-folders.json'} or path.suffix == '.pyc':
            continue
        yield path


def build():
    files = list(corpus_files())
    lines = [hashlib.sha256(p.read_bytes()).hexdigest() + '  ' + p.relative_to(ROOT).as_posix() for p in files]
    (ROOT / MANIFEST).write_text('\n'.join(lines) + '\n')
    with zipfile.ZipFile(ROOT / ARCHIVE, 'w', zipfile.ZIP_DEFLATED) as z:
        for path in files + [ROOT / MANIFEST]:
            # Stable archive metadata avoids recording unrelated local mtimes.
            info = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(), (2026, 9, 8, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            z.writestr(info, path.read_bytes())
    data = (ROOT / ARCHIVE).read_bytes()
    folder = ROOT / 'checkpoint-parts'
    folder.mkdir(exist_ok=True)
    new_names = []
    for offset in range(0, len(data), PART_BYTES):
        name = f'part-{offset // PART_BYTES:03d}'
        (folder / name).write_bytes(data[offset:offset + PART_BYTES])
        new_names.append(name)
    for old in folder.glob('part-[0-9][0-9][0-9]'):
        if old.name not in new_names:
            old.unlink()
    specification = {'archive': ARCHIVE, 'sha256': hashlib.sha256(data).hexdigest(),
                     'file_count': len(files) + 1,
                     'parts': [{'name': name, 'bytes': (folder / name).stat().st_size,
                                'sha256': hashlib.sha256((folder / name).read_bytes()).hexdigest()}
                               for name in new_names]}
    (folder / 'manifest.json').write_text(json.dumps(specification, indent=2) + '\n')
    (folder / 'README.md').write_text(
        '# Complete research checkpoint\n\n'
        'The numbered parts reconstruct the complete current corpus, including original sources, '
        'receipts, ledgers, rejected and unresolved records, chat material, current subject views, and generators.\n\n'
        'Run `python3 checkpoint-parts/reassemble.py` from the repository root. '
        'The command verifies every part, the complete ZIP, every archived file hash, and archive coverage.\n\n'
        f'Archive SHA-256: `{specification["sha256"]}`. '
        f'Files: {specification["file_count"]}. '
        '[Exact part specification](manifest.json).\n\n'
        'Checkpoint parts and their transport metadata are outside the corpus to prevent recursive packaging. '
        'The reconstruction program is also preserved as `tools/reassemble_checkpoint.py` inside the archive. '
        'A checkpoint preserves work without changing its evidential standing.\n')
    (folder / 'reassemble.py').write_bytes((ROOT / 'tools/reassemble_checkpoint.py').read_bytes())
    print(json.dumps({'archive_sha256': specification['sha256'], 'archive_bytes': len(data),
                      'files': specification['file_count'], 'parts': len(new_names)}))


if __name__ == '__main__':
    build()
