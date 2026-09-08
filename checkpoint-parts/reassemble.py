from pathlib import Path
import hashlib
import zipfile

root = Path(__file__).resolve().parent
parts = sorted(root.glob("part-[0-9][0-9][0-9]"))
if [p.name for p in parts] != [f"part-{i:03d}" for i in range(11)]:
    raise SystemExit("expected exactly part-000 through part-010")

out = root.parent / "Mind_Change_Research_Checkpoint.zip"
with out.open("wb") as target:
    for part in parts:
        target.write(part.read_bytes())

expected = "7ba425b197be8d38ba9715873464dd0ba2eca43e2da3aeb985ab5ffda83fba6b"
actual = hashlib.sha256(out.read_bytes()).hexdigest()
if actual != expected:
    raise SystemExit(f"SHA-256 mismatch: {actual}")

with zipfile.ZipFile(out) as archive:
    bad = archive.testzip()
    if bad is not None:
        raise SystemExit(f"ZIP integrity failure at {bad}")
    count = len(archive.namelist())

print(f"verified {out.name}: {actual}; {count} files")
