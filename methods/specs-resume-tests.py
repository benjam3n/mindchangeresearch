#!/usr/bin/env python3
"""Finite later-use checks for the four corrected local specifications.

The tests consume declared mappings in constructed fixtures. They do not test
natural-language interpretation, external interaction, preference, learning,
timing, or transfer.
"""

from __future__ import annotations

import copy
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def load(name: str):
    return json.loads((ROOT / name).read_text())


checks: list[dict[str, object]] = []


def check(check_id: str, condition: bool, detail: object) -> None:
    checks.append({"id": check_id, "pass": bool(condition), "detail": detail})


def canonical_event(event: dict) -> str:
    return json.dumps(event, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def validate_event_identity(events: list[dict]) -> tuple[str, list[dict]]:
    if not events:
        return "empty", []
    scope = {(e["record_set_id"], e["participant_id"], e["invitation_id"]) for e in events}
    if len(scope) != 1:
        return "mixed_scope", []
    seen: dict[str, str] = {}
    unique: list[dict] = []
    for event in events:
        eid = event["event_id"]
        encoded = canonical_event(event)
        if eid in seen and seen[eid] != encoded:
            return "identity_conflict", []
        if eid not in seen:
            seen[eid] = encoded
            unique.append(event)
    return "ok", unique


def reduce_participant_events(events: list[dict]) -> dict:
    identity_status, unique = validate_event_identity(events)
    if identity_status != "ok":
        return {"status": identity_status}
    participant = [e for e in unique if e["evidence_role"] == "participant_statement"]
    orders: dict[int, list[dict]] = {}
    for event in participant:
        orders.setdefault(event["effective_order"], []).append(event)
    for tied in orders.values():
        if len(tied) > 1:
            values: dict[tuple[str, str], set[str]] = {}
            for event in tied:
                for component, attrs in event["updates"].items():
                    for attr, value in attrs.items():
                        values.setdefault((component, attr), set()).add(json.dumps(value, sort_keys=True))
            if any(len(v) > 1 for v in values.values()):
                return {"status": "unresolved_chronology"}
    current: dict[str, dict[str, dict]] = {}
    superseded: list[dict] = []
    reaffirmations: list[dict] = []
    for event in sorted(participant, key=lambda e: e["effective_order"]):
        for component, attrs in event["updates"].items():
            current.setdefault(component, {})
            for attr, value in attrs.items():
                previous = current[component].get(attr)
                if previous and previous["value"] == value:
                    reaffirmations.append({"event_id": event["event_id"], "component_id": component, "attribute": attr})
                    continue
                revision = {
                    "value": value,
                    "source_event_id": event["event_id"],
                    "revision_id": f'{event["event_id"]}:{component}:{attr}',
                }
                if previous:
                    superseded.append({"component_id": component, "attribute": attr, "old": previous, "new": revision})
                current[component][attr] = revision
    return {
        "status": "ok",
        "current": current,
        "superseded": superseded,
        "reaffirmations": reaffirmations,
        "excluded": sorted(e["event_id"] for e in unique if e["evidence_role"] != "participant_statement"),
    }


social = load("values-handoff-iteration-social-use.json")
invitation_spec = load("values-handoff-invitation-record.iterate.json")
followup_spec = load("values-handoff-followup-choice.iterate.json")
trace_spec = load("values-handoff-curiosity-trace.iterate.json")
choice_spec = load("values-handoff-continuation-choice.iterate.json")

check("S01-correction-input", "correction_of" in invitation_spec["inputs"]["prior_response"], invitation_spec["inputs"]["prior_response"])
check("S02-correction-step", any("correction" in s and "unchanged" in s for s in invitation_spec["steps"]), "correction step carries unchanged attributes")
check("S03-independent-trace-status", all(k in trace_spec["inputs"] for k in ("evidence_dimensions", "relation", "identity")), sorted(trace_spec["inputs"]))
check("S04-selection-mode", "revisit-for-interest" in " ".join(choice_spec["success_criteria"]), choice_spec["success_criteria"][0])

reduced = reduce_participant_events(social["inputs"])
expected = social["current_typed_output"]
check("L01-event-identity", reduced["status"] == "ok", reduced["status"])
check("L02-corrected-day", reduced.get("current", {}).get("read", {}).get("when") == expected["current"]["read"]["when"], reduced.get("current", {}).get("read", {}).get("when"))
check("L03-inherited-amount", reduced.get("current", {}).get("read", {}).get("amount") == expected["current"]["read"]["amount"], reduced.get("current", {}).get("read", {}).get("amount"))
check("L04-corrected-medium", reduced.get("current", {}).get("join", {}).get("medium") == expected["current"]["join"]["medium"], reduced.get("current", {}).get("join", {}).get("medium"))
check("L05-refusal-retained", reduced.get("current", {}).get("host", {}).get("stance") == expected["current"]["host"]["stance"], reduced.get("current", {}).get("host", {}).get("stance"))
check("L06-role-exclusions", reduced.get("excluded") == ["R2", "R4"], reduced.get("excluded"))
check("L07-superseded-set", {(x["component_id"], x["attribute"]) for x in reduced.get("superseded", [])} == {("read", "when"), ("join", "stance"), ("join", "medium")}, reduced.get("superseded"))
check("L08-reaffirmations", {(x["event_id"], x["component_id"], x["attribute"]) for x in reduced.get("reaffirmations", [])} == {("R3", "read", "when"), ("R1", "join", "frequency"), ("R1", "host", "stance")}, reduced.get("reaffirmations"))

duplicate = social["inputs"] + [copy.deepcopy(next(e for e in social["inputs"] if e["event_id"] == "R1"))]
check("L09-identical-replay", reduce_participant_events(duplicate).get("current") == reduced.get("current"), "same event bytes produce the same state")
conflict = copy.deepcopy(duplicate)
conflict[-1]["text"] = "different payload under R1"
check("L10-conflicting-id", reduce_participant_events(conflict)["status"] == "identity_conflict", reduce_participant_events(conflict)["status"])
mixed = copy.deepcopy(social["inputs"])
mixed[-1]["participant_id"] = "different-participant"
check("L11-mixed-scope", reduce_participant_events(mixed)["status"] == "mixed_scope", reduce_participant_events(mixed)["status"])
tied = copy.deepcopy([social["inputs"][0], social["inputs"][1]])
tied[1]["effective_order"] = 0
check("L12-ambiguous-order", reduce_participant_events(tied)["status"] == "unresolved_chronology", reduce_participant_events(tied)["status"])

current_revision_ids = sorted(v["revision_id"] for attrs in expected["current"].values() for v in attrs.values())
check("L13-current-draft-bindings", sorted(social["current_draft"]["source_component_revision_ids"]) == current_revision_ids and social["current_draft"]["source_state_id"] == expected["state_id"], current_revision_ids)
changed_revision_ids = {x["old"]["revision_id"] for x in expected["superseded"]}
check("L14-stale-draft", bool(changed_revision_ids.intersection(social["old_draft"]["source_component_revision_ids"])) and social["old_draft"]["state"].startswith("superseded"), sorted(changed_revision_ids))
available = social["availability_case"]["input"]
matched = [o for o in available["supplied_options"] if o["medium"] == available["condition"]]
check("L15-no-matching-option", matched == social["availability_case"]["matching_options"] == [], matched)

exploration = load("values-handoff-iteration-exploration-use.json")
traces = exploration["traces"]
trace_by_id = {t["id"]: t for t in traces}
trace_ids = [t["id"] for t in traces]
claim_ids = [c["id"] for t in traces for c in t["claims"]]
check("T01-unique-identities", len(trace_ids) == len(set(trace_ids)) and len(claim_ids) == len(set(claim_ids)), {"traces": len(trace_ids), "claims": len(claim_ids)})

relations_resolve = True
for trace in traces:
    relation = trace["relation"]
    if relation is None:
        continue
    parent = trace_by_id.get(relation["parent_trace_id"])
    parent_claims = {c["id"] for c in parent["claims"]} if parent else set()
    if parent is None or not set(relation["target_claim_ids"]).issubset(parent_claims):
        relations_resolve = False
check("T02-typed-relations", relations_resolve, "every parent and target claim resolves")

def lineage(start: str, records: dict[str, dict]) -> dict:
    path: list[str] = []
    seen: set[str] = set()
    cur = start
    while True:
        if cur in seen:
            return {"status": "cycle", "path": path, "at": cur}
        seen.add(cur)
        path.append(cur)
        trace = records.get(cur)
        if trace is None:
            return {"status": "missing_parent", "path": path[:-1], "at": cur}
        relation = trace.get("relation")
        if relation is None:
            return {"status": "resolved", "path": path}
        cur = relation["parent_trace_id"]


computed_lineages = {tid: lineage(tid, trace_by_id) for tid in trace_ids}
check("T03-lineages", computed_lineages == exploration["lineages"], computed_lineages)
missing_records = {"Qx": {"id": "Qx", "relation": {"type": "continues", "parent_trace_id": "absent", "target_claim_ids": []}}}
check("T04-missing-parent", lineage("Qx", missing_records)["status"] == "missing_parent", lineage("Qx", missing_records))
cycle_records = {
    "Qa": {"id": "Qa", "relation": {"type": "continues", "parent_trace_id": "Qb", "target_claim_ids": []}},
    "Qb": {"id": "Qb", "relation": {"type": "continues", "parent_trace_id": "Qa", "target_claim_ids": []}},
}
check("T05-cycle", lineage("Qa", cycle_records)["status"] == "cycle", lineage("Qa", cycle_records))
bad_target = copy.deepcopy(traces)
bad_target[1]["relation"]["target_claim_ids"] = ["absent-claim"]
bad_by_id = {t["id"]: t for t in bad_target}
bad_parent = bad_by_id[bad_target[1]["relation"]["parent_trace_id"]]
check("T06-missing-target", not set(bad_target[1]["relation"]["target_claim_ids"]).issubset({c["id"] for c in bad_parent["claims"]}), "absent-claim rejected")
q1 = trace_by_id["Q1"]
check("T07-mixed-status-separated", q1["input"]["origin"] == "constructed" and q1["operation"]["state"] == "performed" and {c["kind"] for c in q1["claims"]} == {"interpretation"}, {"origin": q1["input"]["origin"], "operation": q1["operation"]["state"], "claim_kinds": sorted({c["kind"] for c in q1["claims"]})})
q3 = trace_by_id["Q3"]
check("T08-unavailable-human-stage", q3["operation"]["state"] == "unavailable" and q3["state"] == "paused_for_resource" and all(c["kind"] == "prediction" for c in q3["claims"]), q3["reopening_condition"])
q4 = trace_by_id["Q4"]
selection = exploration["after_selection"]
check("T09-revisit-no-novelty", selection["selected"] == "Q4" and selection["novel_evidence"] is False and selection["actual_product"] == q4["claims"][0]["text"], selection["selection_id"])

registry = load("values-handoff-iteration-registry.json")
expected_ids = [f"I{i:02d}" for i in range(1, 73)]
normalized = [re.sub(r"\W+", " ", row["finding"].lower()).strip() for row in registry]
check("R01-registry-count-ids", len(registry) == 72 and [r["id"] for r in registry] == expected_ids, len(registry))
check("R02-registry-kinds", {r["kind"] for r in registry}.issubset({"OBSERVED", "DERIVED", "TESTED"}), sorted({r["kind"] for r in registry}))
check("R03-no-exact-semantic-duplicates", len(normalized) == len(set(normalized)), len(set(normalized)))

reflection_fields = ["Intended mind change:", "Actual mind change:", "Benefit:", "Verdict:", "Organization:", "Next attempts:"]
docs = ["pcd-01.md", "pcd-02.md", "pci-01.md", "pci-02.md", "iterate-01.md"]
missing_reflections = {name: [field for field in reflection_fields if field not in (ROOT / name).read_text()] for name in docs}
check("D01-reflection-fields", not any(missing_reflections.values()), missing_reflections)

result = {
    "scope": "Finite checks of declared constructed mappings, corrected identity contracts, cross-references, registry structure and document reflection fields. No natural-language reliability or human outcome is tested.",
    "total": len(checks),
    "passed": sum(1 for item in checks if item["pass"]),
    "failed": [item["id"] for item in checks if not item["pass"]],
    "checks": checks,
}
print(json.dumps(result, indent=2, ensure_ascii=False))
raise SystemExit(0 if not result["failed"] else 1)
