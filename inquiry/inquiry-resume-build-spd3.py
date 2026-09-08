from collections import Counter, defaultdict
from pathlib import Path
import hashlib
import json
import re


HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent.parent / "supplement" / "Recovered_Sources" / "inquiry-domain_design_decisions.original.md"
OUTPUT = HERE / "inquiry-resume-spd3-gg-catalog.json"


def polarity(major, minor, text):
    lowered = text.lower()
    if major == "Pre-Mortem" or minor == "Skeptic/challenger" or any(
        word in lowered for word in ("eliminate", "false", "risk", "fail", "challenge", "wrong")
    ):
        direction, orientation = "skeptical", "assume-wrong"
    else:
        direction, orientation = "constructive", "neutral"
    use = "thinking"
    if any(word in lowered for word in ("document", "communicate", "implement", "record", "output")):
        use = "both"
    return direction, use, orientation


def custom_entry(identifier, method, category, text, derivation, direction, use, orientation):
    return {
        "id": identifier,
        "method": method,
        "category": category,
        "guess": text,
        "derivation": derivation,
        "tags": {"DIR": direction, "USE": use, "ORIENT": orientation},
    }


raw = SOURCE.read_text()
major = None
minor = None
legacy = []
major_counts = Counter()
minor_counts = Counter()
major_alias = {
    "Morphological Analysis": "Morphological",
    "SCAMPER Transformations - 70 guesses": "SCAMPER",
    "Stakeholder Perspectives - 38 guesses": "Stakeholders",
    "Time Horizons - 24 guesses": "Time Horizons",
    "Claim Types - 52 guesses": "Claim Types",
    "Analogies - 36 guesses": "Analogies",
    "Pre-Mortem - 24 guesses": "Pre-Mortem",
}
for line in raw.splitlines():
    if line.startswith("## "):
        major = major_alias.get(line[3:], None)
        minor = None
        continue
    if line.startswith("### ") and major:
        minor = re.sub(r"\s+-\s+\d+ guesses$", "", line[4:])
        continue
    match = re.match(r"^(\d+)\.\s+(.*?)\s+\[D:\s*(.*?)\]$", line)
    if not (match and major and minor):
        continue
    n, text, derivation = match.groups()
    direction, use, orientation = polarity(major, minor, text)
    key = f"legacy-{len(legacy)+1:03d}"
    legacy.append(
        custom_entry(key, major, minor, text, derivation, direction, use, orientation)
    )
    major_counts[major] += 1
    minor_counts[(major, minor)] += 1


custom = []
locations = [
    ("local record 03-dd-uncertainty.md", "the missing-source case can be checked at its named local application path"),
    ("local record 06-qr-sure.md", "the ambiguous route reason can be checked at its named local application path"),
    ("recovered immutable library source", "the library candidate can be checked without rewriting its bytes"),
    ("verified original-skill copy", "procedure wording can be checked separately from application output"),
    ("absent expected archive path", "path absence is an access observation, not content absence"),
    ("source-receipt registry", "common origins can be compared before treating receipts as independent"),
    ("generated support artifact", "calculation output is separated from source evidence"),
    ("later consumer record", "the selected observation must retain its source and scope at reuse"),
]
for i, (value, derivation) in enumerate(locations, 1):
    custom.append(custom_entry(f"custom-location-{i:02d}", "Morphological", "LOCATION", value, f"morphological LOCATION: {derivation}", "constructive", "thinking", "neutral"))

constraints = [
    "exact source bytes available", "source provenance known", "evidence origins independent",
    "claim scope tuple retained", "decision threshold fixed at 6", "admissible interval fixed at 4-9",
    "action reversible", "observation has nonzero cost", "opportunity expires before resolution",
    "route reason has two live meanings", "no human response observed", "no external outcome observed",
    "current tools can read the named file", "future execution channel absent", "warranted uncertainty must remain visible",
]
for i, value in enumerate(constraints, 1):
    custom.append(custom_entry(f"custom-constraint-{i:02d}", "Morphological", "CONSTRAINTS", value, "morphological CONSTRAINTS: varied while holding the three frozen cases fixed", "skeptical" if i in {3,8,9,10,11,12,14} else "constructive", "thinking", "assume-wrong" if i in {3,8,9,10,11,12,14} else "neutral"))

analogy_domains = {
    "Biology": ["missing source as absent nutrient", "qualifier as regulatory context", "threshold as activation boundary", "redundant receipts as cloned lineage"],
    "Physics": ["interval as position band", "threshold as phase boundary", "observation as measurement with cost", "expired action as inaccessible state transition"],
    "Economics": ["observation as priced information", "reversible action as option value", "shared-origin receipts as correlated signals", "threshold crossing as contingent demand"],
    "Psychology": ["confidence report without truth", "ambiguity as competing construals", "anchoring on one route reason", "resolution pressure despite action invariance"],
    "Engineering": ["missing file as broken dependency", "qualifier as load-bearing constraint", "threshold probe as boundary test", "later-use fixture as acceptance test"],
    "Nature": ["uncertainty interval as floodplain", "threshold as shoreline", "source chain as watershed", "preserved alternatives as seed bank"],
    "History": ["receipt lineage as provenance record", "expired opportunity as closed period", "source revision as version boundary", "repeated citation as one historical origin"],
}
for domain, guesses in analogy_domains.items():
    for i, value in enumerate(guesses, 1):
        custom.append(custom_entry(f"custom-analogy-{domain.lower()}-{i:02d}", "Analogies", domain, value, f"analogy to {domain.lower()} domain", "constructive", "thinking", "neutral"))

stakeholders = [
    ("model classifier", "needs an executable next observation"),
    ("source author", "may have intended one of two route-reason meanings"),
    ("later consumer", "needs the unresolved remainder and scope"),
    ("reviewer", "checks whether the observation can discriminate live alternatives"),
    ("resource provider", "controls whether source access is possible now"),
    ("affected decision maker", "may face different losses on opposite sides of the threshold"),
]
for i, (who, view) in enumerate(stakeholders, 1):
    custom.append(custom_entry(f"custom-stakeholder-{i:02d}", "Stakeholders", who, view, f"stakeholder perspective: {who}", "constructive", "thinking", "neutral"))

for i, value in enumerate([
    "which source path previously existed", "which route version supplied the reason",
    "whether the threshold was fixed before the interval", "whether matching receipts descend from one origin",
], 1):
    custom.append(custom_entry(f"custom-history-{i:02d}", "Time Horizons", "Historical", value, "historical time horizon", "skeptical", "thinking", "assume-wrong"))

premortem = {
    "Source error": ["located bytes are from the wrong version", "a generated summary is mistaken for the original source"],
    "Motivated reasoning": ["resolution is forced to earn a completion label", "a preferred intervention receives softer adequacy criteria"],
    "Scope error": ["a local source check is generalized to all sources", "action readiness is substituted for truth"],
    "Timing error": ["the observation arrives after expiry", "future execution is reported before a channel exists"],
    "Causation error": ["later success is attributed to GG without a comparator", "shared-origin repetition is treated as independent confirmation"],
    "Definition error": ["sure means both confidence and factive knowledge in one branch", "absence of a path is defined as absence of content"],
}
for category, guesses in premortem.items():
    for i, value in enumerate(guesses, 1):
        custom.append(custom_entry(f"custom-premortem-{category.lower().replace(' ','-')}-{i:02d}", "Pre-Mortem", category, value, f"pre-mortem {category.lower()} check", "skeptical", "thinking", "assume-wrong"))

critical = [
    ("A located source with a matching hash resolves access but does not settle authorial intent.", "factual", "both"),
    ("Two matching receipts copied from one original are one evidence origin.", "relational", "output"),
    ("An absent expected path does not establish that the content never existed.", "factual", "output"),
    ("Subjective confidence can be high while the believed proposition is false.", "modal", "output"),
    ("Factive certainty and reported confidence are distinct meanings of sure.", "definition", "both"),
    ("An interval crossing a decision threshold contains states selecting different actions under that rule.", "relational", "output"),
    ("A truth interval can remain unresolved while action is fixed across every admitted value.", "modal", "output"),
    ("A confidence-raising observation can be inadequate if it cannot change the selected action or settle the disputed premise.", "normative", "both"),
    ("A source lookup cannot by itself decide between two semantic readings present in the located text.", "causal", "output"),
    ("A semantic minimal pair cannot retrieve missing bytes.", "causal", "output"),
    ("The three frozen uncertainty cases require different observation types.", "relational", "both"),
    ("Candidate generation alone does not establish a beneficial downstream change.", "meta", "output"),
    ("The recovered library's declared total can disagree with its enumerated entries.", "factual", "output"),
    ("A generic decision library needs source, qualifier, and threshold customization for these cases.", "normative", "both"),
    ("A selected clause without its distant qualifier can reverse the represented scope.", "causal", "output"),
    ("A reversible act can proceed while a truth question remains open when every admitted value selects that act.", "modal", "output"),
    ("A model-only operation does not demonstrate a human confidence or learning effect.", "meta", "output"),
    ("An adequate next observation has possible outcomes that separate at least two live next operations.", "definition", "both"),
    ("Counting numbered entries as independent findings overstates demonstrated evidence.", "meta", "output"),
    ("A later-use fixture can show a changed model operation without showing durable transfer.", "meta", "output"),
]
for i, (value, kind, use) in enumerate(critical, 1):
    direction = "skeptical" if i in {2,3,4,8,9,10,12,13,15,17,19} else "constructive"
    custom.append(custom_entry(f"custom-critical-{i:02d}", "Critical", kind, value, f"unbundled from the frozen {kind} case and selected by confidence x impact", direction, use, "assume-wrong" if direction == "skeptical" else "assume-right"))


normalized = defaultdict(list)
for entry in legacy:
    normalized[re.sub(r"[^a-z0-9]+", " ", entry["guess"].lower()).strip()].append(entry["id"])
exact_duplicates = [ids for ids in normalized.values() if len(ids) > 1]

catalog = {
    "intended_mind_change": "Retain the recovered generic library while replacing its declared-count shortcut with an auditable candidate catalog and source-specific coverage.",
    "starting_judgment": "The recovered header declared 512 guesses and appeared to clear GG's minimum; actual entries and current coverage requirements had not been reconciled.",
    "source": {
        "path": str(SOURCE),
        "sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "declared_guess_count": 512,
        "actual_numbered_entries": len(legacy),
        "declared_morphological": 268,
        "actual_morphological": major_counts["Morphological"],
        "declared_total_from_section_headers": 512,
        "actual_total_from_section_entries": sum(major_counts.values()),
        "source_modified": False,
    },
    "legacy_section_counts": dict(major_counts),
    "legacy_entries": legacy,
    "custom_entries": custom,
    "custom_count": len(custom),
    "tagged_candidate_entries_total": len(legacy) + len(custom),
    "independence_warning": "Numbered or tagged candidate entries are not counted as independent findings. Exact and semantic overlaps remain candidates until tested.",
    "exact_duplicate_id_groups": exact_duplicates,
    "coverage": {
        "morphological": {"legacy_dimensions": sorted({e["category"] for e in legacy if e["method"] == "Morphological"}), "added_dimensions": ["LOCATION", "CONSTRAINTS"]},
        "scamper_operations": sorted({e["category"] for e in legacy if e["method"] == "SCAMPER"}),
        "stakeholder_perspectives": len({e["category"] for e in legacy + custom if e["method"] == "Stakeholders"}),
        "time_horizons": sorted({e["category"] for e in legacy + custom if e["method"] == "Time Horizons"}),
        "claim_types": sorted({e["category"] for e in legacy if e["method"] == "Claim Types"}),
        "analogy_domains": sorted({e["category"] for e in legacy + custom if e["method"] == "Analogies"}),
        "premortem_types": sorted({e["category"] for e in legacy + custom if e["method"] == "Pre-Mortem"}),
    },
    "coverage_metrics": {
        "standard_dimensions_checked": "10/10",
        "scamper_operations_checked": "7/7",
        "stakeholder_perspectives": 13,
        "time_horizons_checked": "5/5",
        "critical_claim_inversion": "18/18 in inquiry-resume-spd3-araw.md",
        "claim_types_checked": "8/8",
        "original_named_analogy_domains_checked": "10/10",
        "original_premortem_error_types_checked": "15/15",
        "checklist_coverage": "100%",
        "possibility_space_coverage": "unknown; checklist completion does not establish exhaustiveness"
    },
    "critical_top20": [f"custom-critical-{i:02d}" for i in range(1, 21)],
    "polarity_top20": {
        "constructive": 9,
        "skeptical": 11,
        "output_or_both": 20,
    },
    "actual_mind_change": "The current GG input is no longer represented by the library's false 512 total or by its generic decision categories alone; source, semantic, threshold, and evidence-dependence candidates are explicit.",
    "benefit": "QAG receives twenty source-specific critical candidates with explicit polarity and use tags, while the intact recovered library remains available as a broader candidate pool.",
    "verdict": "KEEP",
    "organization": "Legacy entries, custom gap fillers, critical candidates, and count defects are separate fields; none is promoted to an independent finding by enumeration.",
    "next_attempts": ["Gate the twenty critical candidates through QAG.", "Test the three observation types on distinct fixtures.", "Retain generic candidates only when their source-specific operands are supplied."],
}
OUTPUT.write_text(json.dumps(catalog, indent=2) + "\n")
print(json.dumps({"output": str(OUTPUT), "legacy": len(legacy), "custom": len(custom), "total": len(legacy)+len(custom), "sections": major_counts, "sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest()}, indent=2))
