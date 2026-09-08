from pathlib import Path
from collections import Counter
import json

ROOT = Path(__file__).parent
LINES = ["inquiry", "representation", "values", "conditions", "methods", "systems"]

exact_missing = {
    ("inquiry", "rca", 1): [
        "Original RCA nine-level causal-chain depth remains unperformed; the record contains shorter performed branches and tests.",
        "Historical and human incident causes needed to validate the causal chain are unavailable."
    ],
    ("inquiry", "rca", 2): [
        "Original RCA nine-level causal-chain depth remains unperformed; the record contains shorter performed branches and tests.",
        "Historical and human causes of the qualifying dependency failure are unavailable."
    ],
    ("inquiry", "sdc", 1): [
        "Human bodily response, emotional observation, read-aloud reaction, and recurring personal-pattern evidence are unavailable."
    ],
}

all_rows = []
for line in LINES:
    p = ROOT / line / "application-ledger.json"
    rows = json.loads(p.read_text())
    for row in rows:
        key = (line, row["skill_id"], row["application_number"])
        if key in exact_missing:
            row["missing_requirements"] = exact_missing[key]
            row["depth_status"] = row.get("depth_status", "") + " Exact remaining causal or human stages are named in missing_requirements."
        f = row.get("file")
        if f:
            fp = Path(f)
            if fp.is_absolute():
                try:
                    fp = fp.relative_to(ROOT)
                except ValueError:
                    candidates = list(ROOT.rglob(fp.name))
                    if len(candidates) != 1:
                        raise ValueError((key, f, [str(x) for x in candidates]))
                    fp = candidates[0].relative_to(ROOT)
            elif fp.parts[0] != line:
                fp = Path(line) / fp
            row["file"] = str(fp)
            if not (ROOT / fp).is_file():
                raise FileNotFoundError((key, fp))
        all_rows.append((line, row))
    p.write_text(json.dumps(rows, indent=2) + "\n")

for line in LINES:
    rows = [r for ln, r in all_rows if ln == line]
    status = Counter(r["status"] for r in rows)
    verdicts = Counter(r["verdict"] for r in rows)
    by_skill = Counter(r["skill_id"] for r in rows if r["status"] != "pending")
    progress_path = ROOT / line / "progress.json"
    old = json.loads(progress_path.read_text()) if progress_path.exists() else {}
    progress = {
        "line": line,
        "assigned_applications": len(rows),
        "status_counts": {k: status.get(k, 0) for k in ["complete", "partial", "blocked", "pending"]},
        "addressed_applications": len(rows) - status.get("pending", 0),
        "applications_by_skill": dict(sorted(by_skill.items())),
        "verdicts": {k: verdicts.get(k, 0) for k in ["KEEP", "REJECT", "UNRESOLVED"]},
        "keeps": [r["file"] for r in rows if r["verdict"] == "KEEP" and r.get("file")],
        "consolidations": old.get("consolidations", []),
        "status": "all_slots_addressed_with_open_partial_or_blocked_gates" if not status.get("pending") else "in_progress",
        "scope_note": "Completion is procedural within the stated scope. Verdict and human/external effect status are independent; partial and blocked gates remain explicit."
    }
    progress_path.write_text(json.dumps(progress, indent=2) + "\n")

slots = [(ln, r["skill_id"], r["application_number"]) for ln, r in all_rows]
assert len(slots) == 300 and len(set(slots)) == 300
statuses = Counter(r["status"] for _, r in all_rows)
assert statuses == Counter({"complete": 233, "partial": 66, "blocked": 1})
assert all(r.get("file") and (ROOT / r["file"]).is_file() for _, r in all_rows)
assert all(r.get("missing_requirements") for _, r in all_rows if r["status"] in {"partial", "blocked"})
assert all(not r.get("missing_requirements") for _, r in all_rows if r["status"] == "complete")

print(json.dumps({"status_counts": dict(statuses), "paths": "300 root-relative existing files", "generic_gates_repaired": 3}, indent=2))
