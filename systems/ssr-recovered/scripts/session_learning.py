#!/usr/bin/env python3
"""
GOSM Session Learning System

Captures, stores, and retrieves learnings from GOSM sessions to improve
future sessions. Implements the feedback loop for continuous improvement.

Usage:
    python session_learning.py capture [learning_type] [content] [context]
    python session_learning.py retrieve [domain] [limit]
    python session_learning.py search [query]
    python session_learning.py stats
    python session_learning.py validate [learning_id]
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional
import hashlib

# Storage location
LEARNING_DIR = Path(__file__).parent.parent / "data" / "learnings"
LEARNING_FILE = LEARNING_DIR / "session_learnings.json"


def ensure_storage():
    """Ensure storage directory and file exist."""
    LEARNING_DIR.mkdir(parents=True, exist_ok=True)
    if not LEARNING_FILE.exists():
        LEARNING_FILE.write_text(json.dumps({
            "learnings": [],
            "metadata": {
                "created": datetime.now().isoformat(),
                "version": "1.0.0"
            }
        }, indent=2))


def load_learnings() -> dict:
    """Load all learnings from storage."""
    ensure_storage()
    return json.loads(LEARNING_FILE.read_text())


def save_learnings(data: dict):
    """Save learnings to storage."""
    ensure_storage()
    LEARNING_FILE.write_text(json.dumps(data, indent=2))


def generate_id(content: str) -> str:
    """Generate unique ID for a learning."""
    hash_input = f"{content}{datetime.now().isoformat()}"
    return f"L{hashlib.sha256(hash_input.encode()).hexdigest()[:8]}"


def capture_learning(
    learning_type: str,
    content: str,
    context: str = "",
    domain: str = "general",
    confidence: str = "medium",
    evidence: str = "",
    grounding: str = ""
) -> dict:
    """
    Capture a new learning from a session.

    learning_type: what_worked | what_didnt | surprise | insight | pattern | procedure_gap
    content: The actual learning
    context: When/where this learning applies
    domain: Problem domain (goal, problem, question, decision, situation, feeling)
    confidence: low | medium | high
    evidence: Supporting evidence for the learning
    grounding: [O], [T], or [D] marker if available
    """
    data = load_learnings()

    learning = {
        "id": generate_id(content),
        "type": learning_type,
        "content": content,
        "context": context,
        "domain": domain,
        "confidence": confidence,
        "evidence": evidence,
        "grounding": grounding,
        "created": datetime.now().isoformat(),
        "validated_count": 0,
        "contradicted_count": 0,
        "status": "preliminary"  # preliminary | validated | contradicted | archived
    }

    # Contradiction detection before adding
    conflicts = detect_contradictions(learning, data["learnings"])
    if conflicts:
        learning["potential_conflicts"] = [c["id"] for c in conflicts]

    data["learnings"].append(learning)
    save_learnings(data)

    return learning


def detect_contradictions(new_learning: dict, existing_learnings: list) -> list:
    """
    Detect potential contradictions between new learning and existing ones.

    Contradiction defined as:
    - Same domain AND
    - Keyword overlap > 50% AND
    - Opposite types (what_worked vs what_didnt)
    """
    conflicts = []
    opposite_types = {
        "what_worked": "what_didnt",
        "what_didnt": "what_worked"
    }

    new_type = new_learning.get("type", "")
    new_domain = new_learning.get("domain", "")
    new_content = new_learning.get("content", "").lower()
    new_words = set(new_content.split())

    opposite = opposite_types.get(new_type)
    if not opposite:
        return []  # Only check worked/didnt pairs

    for existing in existing_learnings:
        if existing.get("status") == "archived":
            continue
        if existing.get("domain") != new_domain:
            continue
        if existing.get("type") != opposite:
            continue

        # Check keyword overlap
        existing_words = set(existing.get("content", "").lower().split())
        if not existing_words or not new_words:
            continue

        overlap = len(new_words & existing_words)
        overlap_ratio = overlap / min(len(new_words), len(existing_words))

        if overlap_ratio > 0.5:
            conflicts.append(existing)

    return conflicts


def aggregate_learnings() -> dict:
    """
    Aggregate learnings by domain and type to find patterns.

    Returns patterns found across multiple learnings.
    """
    data = load_learnings()
    learnings = [l for l in data["learnings"] if l.get("status") != "archived"]

    # Group by (domain, type)
    groups = {}
    for learning in learnings:
        key = (learning.get("domain", "general"), learning.get("type", "insight"))
        if key not in groups:
            groups[key] = []
        groups[key].append(learning)

    # Find patterns within groups
    patterns = []
    for (domain, ltype), group_learnings in groups.items():
        if len(group_learnings) < 2:
            continue

        # Simple pattern: count common words across learnings
        all_words = []
        for l in group_learnings:
            all_words.extend(l.get("content", "").lower().split())

        from collections import Counter
        word_counts = Counter(all_words)
        common_words = [w for w, c in word_counts.most_common(5) if c >= 2 and len(w) > 3]

        if common_words:
            patterns.append({
                "domain": domain,
                "type": ltype,
                "frequency": len(group_learnings),
                "common_themes": common_words,
                "source_ids": [l["id"] for l in group_learnings],
                "confidence": "high" if len(group_learnings) >= 3 else "medium"
            })

    return {"patterns": patterns, "total_learnings": len(learnings)}


def retrieve_learnings(
    domain: Optional[str] = None,
    learning_type: Optional[str] = None,
    status: Optional[str] = None,
    limit: int = 10
) -> list:
    """
    Retrieve relevant learnings for a new session.

    Filters by domain, type, and status. Returns most relevant learnings.
    """
    data = load_learnings()
    learnings = data["learnings"]

    # Filter
    if domain:
        learnings = [l for l in learnings if l.get("domain") == domain or l.get("domain") == "general"]
    if learning_type:
        learnings = [l for l in learnings if l.get("type") == learning_type]
    if status:
        learnings = [l for l in learnings if l.get("status") == status]

    # Exclude archived
    learnings = [l for l in learnings if l.get("status") != "archived"]

    # Sort by confidence and validation count
    confidence_order = {"high": 3, "medium": 2, "low": 1}
    learnings.sort(
        key=lambda x: (
            confidence_order.get(x.get("confidence", "medium"), 2),
            x.get("validated_count", 0)
        ),
        reverse=True
    )

    return learnings[:limit]


def search_learnings(query: str) -> list:
    """Search learnings by content or context."""
    data = load_learnings()
    query_lower = query.lower()

    results = []
    for learning in data["learnings"]:
        if learning.get("status") == "archived":
            continue
        content = learning.get("content", "").lower()
        context = learning.get("context", "").lower()
        if query_lower in content or query_lower in context:
            results.append(learning)

    return results


def validate_learning(learning_id: str, validate: bool = True):
    """
    Mark a learning as validated or contradicted based on new evidence.

    After enough validations, status changes to "validated".
    After enough contradictions, status changes to "contradicted".
    """
    data = load_learnings()

    for learning in data["learnings"]:
        if learning.get("id") == learning_id:
            if validate:
                learning["validated_count"] = learning.get("validated_count", 0) + 1
                if learning["validated_count"] >= 3 and learning["status"] == "preliminary":
                    learning["status"] = "validated"
                    learning["confidence"] = "high"
            else:
                learning["contradicted_count"] = learning.get("contradicted_count", 0) + 1
                if learning["contradicted_count"] >= 2:
                    learning["status"] = "contradicted"

            save_learnings(data)
            return learning

    return None


def get_stats() -> dict:
    """Get statistics about stored learnings."""
    data = load_learnings()
    learnings = data["learnings"]

    stats = {
        "total": len(learnings),
        "by_type": {},
        "by_domain": {},
        "by_status": {},
        "by_confidence": {}
    }

    for learning in learnings:
        # By type
        t = learning.get("type", "unknown")
        stats["by_type"][t] = stats["by_type"].get(t, 0) + 1

        # By domain
        d = learning.get("domain", "general")
        stats["by_domain"][d] = stats["by_domain"].get(d, 0) + 1

        # By status
        s = learning.get("status", "preliminary")
        stats["by_status"][s] = stats["by_status"].get(s, 0) + 1

        # By confidence
        c = learning.get("confidence", "medium")
        stats["by_confidence"][c] = stats["by_confidence"].get(c, 0) + 1

    return stats


def format_learning_for_display(learning: dict) -> str:
    """Format a learning for display."""
    status_icons = {
        "preliminary": "[PRELIM]",
        "validated": "[VALID]",
        "contradicted": "[CONTRA]",
        "archived": "[ARCH]"
    }
    confidence_levels = {
        "high": "HIGH",
        "medium": "MED",
        "low": "LOW"
    }

    return f"""
{status_icons.get(learning.get('status', 'preliminary'), '?')} [{learning.get('id')}] {learning.get('type', 'unknown').upper()}
   Content: {learning.get('content', '')}
   Context: {learning.get('context', 'general')}
   Domain: {learning.get('domain', 'general')} | Confidence: {confidence_levels.get(learning.get('confidence', 'medium'), '?')}
   Validated: {learning.get('validated_count', 0)}x | Contradicted: {learning.get('contradicted_count', 0)}x
   Grounding: {learning.get('grounding', 'none')}
"""


def format_learnings_for_context(learnings: list) -> str:
    """Format learnings for injection into session context."""
    if not learnings:
        return "No relevant learnings found."

    output = "## Relevant Learnings from Previous Sessions\n\n"

    for learning in learnings:
        status = learning.get("status", "preliminary")
        if status == "validated":
            confidence_note = "[VALIDATED]"
        elif status == "preliminary":
            confidence_note = f"[{learning.get('confidence', 'medium').upper()} confidence]"
        else:
            continue  # Skip contradicted/archived

        output += f"- **{learning.get('type', 'insight')}** {confidence_note}: {learning.get('content', '')}\n"
        if learning.get("context"):
            output += f"  - Applies when: {learning.get('context')}\n"

    return output


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]

    if command == "capture":
        if len(sys.argv) < 4:
            print("Usage: session_learning.py capture [type] [content] [context?]")
            print("Types: what_worked, what_didnt, surprise, insight, pattern, procedure_gap")
            sys.exit(1)

        learning_type = sys.argv[2]
        content = sys.argv[3]
        context = sys.argv[4] if len(sys.argv) > 4 else ""

        learning = capture_learning(learning_type, content, context)
        print(f"Captured learning: {learning['id']}")
        print(format_learning_for_display(learning))

    elif command == "retrieve":
        domain = sys.argv[2] if len(sys.argv) > 2 else None
        limit = int(sys.argv[3]) if len(sys.argv) > 3 else 10

        learnings = retrieve_learnings(domain=domain, limit=limit)
        print(f"Retrieved {len(learnings)} learnings:")
        for l in learnings:
            print(format_learning_for_display(l))

    elif command == "search":
        if len(sys.argv) < 3:
            print("Usage: session_learning.py search [query]")
            sys.exit(1)

        query = sys.argv[2]
        results = search_learnings(query)
        print(f"Found {len(results)} learnings matching '{query}':")
        for l in results:
            print(format_learning_for_display(l))

    elif command == "stats":
        stats = get_stats()
        print("Learning Statistics:")
        print(f"  Total: {stats['total']}")
        print(f"  By Type: {stats['by_type']}")
        print(f"  By Domain: {stats['by_domain']}")
        print(f"  By Status: {stats['by_status']}")
        print(f"  By Confidence: {stats['by_confidence']}")

    elif command == "validate":
        if len(sys.argv) < 3:
            print("Usage: session_learning.py validate [learning_id] [true/false?]")
            sys.exit(1)

        learning_id = sys.argv[2]
        validate = sys.argv[3].lower() != "false" if len(sys.argv) > 3 else True

        result = validate_learning(learning_id, validate)
        if result:
            action = "validated" if validate else "contradicted"
            print(f"Learning {learning_id} {action}:")
            print(format_learning_for_display(result))
        else:
            print(f"Learning {learning_id} not found")

    elif command == "context":
        # Output learnings formatted for session context
        domain = sys.argv[2] if len(sys.argv) > 2 else None
        learnings = retrieve_learnings(domain=domain, limit=5)
        print(format_learnings_for_context(learnings))

    elif command == "aggregate":
        # Aggregate learnings to find patterns
        result = aggregate_learnings()
        print(f"Aggregated {result['total_learnings']} learnings")
        print(f"Found {len(result['patterns'])} patterns:\n")
        for pattern in result["patterns"]:
            print(f"  [{pattern['domain']}] {pattern['type']} (x{pattern['frequency']})")
            print(f"    Common themes: {', '.join(pattern['common_themes'])}")
            print(f"    Confidence: {pattern['confidence']}")
            print()

    elif command == "conflicts":
        # Show learnings with potential conflicts
        data = load_learnings()
        conflicts_found = []
        for learning in data["learnings"]:
            if learning.get("potential_conflicts"):
                conflicts_found.append(learning)

        if conflicts_found:
            print(f"Found {len(conflicts_found)} learnings with potential conflicts:\n")
            for l in conflicts_found:
                print(f"  {l['id']}: {l['content'][:50]}...")
                print(f"    Conflicts with: {l['potential_conflicts']}")
                print()
        else:
            print("No conflicts detected.")

    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
