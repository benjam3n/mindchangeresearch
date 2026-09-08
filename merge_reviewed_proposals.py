from pathlib import Path
import json

ROOT = Path(__file__).parent


def load(name):
    return json.loads((ROOT / "continuation" / name).read_text())


def normalize(row, line):
    row = dict(row)
    status = row.get("status", "pending")
    custom_complete = status.startswith("complete") and status != "complete"
    if status not in {"complete", "partial", "pending", "blocked"}:
        if status.startswith("complete"):
            status = "complete"
        else:
            raise ValueError((line, row["skill_id"], row["application_number"], status))
    row["status"] = status
    if "source" in row and "source_fidelity" not in row:
        row["source_fidelity"] = row.pop("source")
    if "depth" in row and "depth_status" not in row:
        row["depth_status"] = row.pop("depth")
    if "missing" in row and "missing_requirements" not in row:
        row["missing_requirements"] = row.pop("missing")
    if custom_complete and row.get("missing_requirements"):
        limits = "; ".join(row["missing_requirements"])
        row["depth_status"] = row.get("depth_status", "") + " External or semantic effect limit retained: " + limits
        row["missing_requirements"] = []
    f = row.get("file")
    if f:
        p = Path(f)
        if p.is_absolute():
            p = p.relative_to(ROOT)
        elif p.parts[0] != line:
            p = Path(line) / p
        row["file"] = str(p)
    return row


def merge(line, rows):
    path = ROOT / line / "application-ledger.json"
    ledger = json.loads(path.read_text())
    positions = {(r["skill_id"], r["application_number"]): i for i, r in enumerate(ledger)}
    for raw in rows:
        row = normalize(raw, line)
        key = (row["skill_id"], row["application_number"])
        if key not in positions:
            raise KeyError((line, key))
        ledger[positions[key]] = row
    path.write_text(json.dumps(ledger, indent=2) + "\n")


inquiry = load("inquiry-proposal.json")["affected_slots"]
representation = load("representation-proposal.json")["slots"]
methods = (
    load("methods-core-proposal.json")["slots"]
    + load("utility-proposal.json")["slots"]
    + load("specs-proposal.json")["slots"]
)

# These fifteen representation records were authored in the preserved supplement.
# Their central ledger was intentionally not changed there. This merge retains the
# document's own scoped completion and verdict, including three human-gated partials.
rep_staged = [
    ("vdp", 1, "representation/029-vdp-1.md", "partial", "KEEP", ["real stranger-glance/human hierarchy check", "human attention and comprehension evidence"], "inspected non-color mapping; human effect unresolved"),
    ("prd", 1, "representation/030-prd-1.md", "partial", "KEEP", ["real-viewer check at actual distance", "external target-system and accessibility review"], "paired projection/reference package; human learning unresolved"),
    ("categorize", 1, "representation/031-categorize-1.md", "complete", "KEEP", [], "cross-classification selected the next representational test"),
    ("categorize", 2, "representation/032-categorize-2.md", "complete", "REJECT", [], "three retrieval uses favored the existing question routes"),
    ("txm", 1, "representation/033-txm-1.md", "complete", "KEEP", [], "partial observation changed the next action without erasing captured evidence"),
    ("txm", 2, "representation/034-txm-2.md", "complete", "KEEP", [], "compound intervention was decomposed before credit assignment"),
    ("mv", 1, "representation/035-mv-1.md", "complete", "REJECT", [], "multi-select loci retained; forced exclusive partition rejected"),
    ("ctgp", 1, "representation/036-ctgp-1.md", "complete", "KEEP", [], "negative-plus-unknown case changed which proposition was settled"),
    ("ro", 2, "representation/037-ro-2.md", "complete", "REJECT", [], "auditable ranking added no independent benefit beyond the existing representation"),
    ("ro", 3, "representation/038-ro-3.md", "complete", "REJECT", [], "six encodings preserved the finite answers; no independent benefit established"),
    ("cda", 1, "representation/039-cda-1.md", "complete", "KEEP", [], "typed relation semantics constrained a downstream operation"),
    ("cda", 2, "representation/040-cda-2.md", "complete", "REJECT", [], "partial-cue guard reused an established distinction"),
    ("ctcov", 2, "representation/041-ctcov-2.md", "complete", "KEEP", [], "nested composition preserved grouping and order under loss tests"),
    ("ctcov", 3, "representation/042-ctcov-3.md", "complete", "UNRESOLVED", [], "pacing comparison is designed but no human after-state exists; the local original procedure is complete"),
    ("sum", 1, "representation/043-sum-1.md", "complete", "REJECT", [], "synthesis preserved dependence and rejected false independent-convergence credit"),
]
for sid, app, file, status, verdict, missing, later in rep_staged:
    representation.append({
        "skill_id": sid,
        "application_number": app,
        "file": file,
        "status": status,
        "source_fidelity": "Exact original and separate requirements are linked in the application; source receipt retained.",
        "depth_status": "Application records the original products and its actual numerical floor where one exists; unavailable human stages remain explicit.",
        "missing_requirements": missing,
        "verdict": verdict,
        "novelty": "local_adoption" if verdict == "KEEP" else ("unresolved" if verdict == "UNRESOLVED" else "repeated"),
        "later_use": later,
    })

# SATR was a completed preserved handoff whose two records were reviewed in full.
methods.extend([
    {
        "skill_id": "satr", "application_number": 1, "file": "methods/satr-01.md", "status": "complete",
        "source_fidelity": "Exact original and separate requirements linked; receipt retained.",
        "depth_status": "No numerical 8x floor in SATR; all five stages cover 16 actual inputs, five overlap clusters, six unique roles, sensitivity, and a performed queue transformation.",
        "missing_requirements": [], "verdict": "KEEP", "novelty": "new_within_case",
        "later_use": "The 16-to-11 repeat queue selected distinct setup and service-continuity cases for UF01 and BOC01; learning equivalence remains unresolved."
    },
    {
        "skill_id": "satr", "application_number": 2, "file": "methods/satr-02.md", "status": "complete",
        "source_fidelity": "Exact original and separate requirements linked; receipt retained.",
        "depth_status": "No numerical 8x floor in SATR; all five stages cover eight actual cues, three overlap clusters, the finite usage log, and an explicit no-pruning decision.",
        "missing_requirements": [], "verdict": "REJECT", "novelty": "repeated",
        "later_use": "All eight cues were retained because each selected a distinct action condition; no new benefit credit."
    }
])

merge("inquiry", inquiry)
merge("representation", representation)
merge("methods", methods)

print(json.dumps({
    "merged": {"inquiry": len(inquiry), "representation": len(representation), "methods": len(methods)},
    "note": "Proposal metadata was normalized to the four central status values; benefit verdicts remain independent."
}, indent=2))
