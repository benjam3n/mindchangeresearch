#!/usr/bin/env python3
"""
GOSM Guess Library

Manages pre-generated comprehensive guess sets for common goals.
Retrieves existing guesses instead of regenerating from scratch.

Usage:
    python guess_library.py lookup "I want to make money"
    python guess_library.py get goal_make_money
    python guess_library.py related goal_make_money
    python guess_library.py list
    python guess_library.py stats
"""

import json
import re
import sys
from pathlib import Path
from datetime import datetime
from typing import Optional, List, Dict

LIBRARY_DIR = Path(__file__).parent.parent / "data" / "guess_libraries"
INDEX_FILE = LIBRARY_DIR / "index.json"


def load_index() -> dict:
    """Load the library index."""
    if not INDEX_FILE.exists():
        return {"libraries": [], "related_goal_chains": {}}
    return json.loads(INDEX_FILE.read_text())


def save_index(index: dict):
    """Save the library index."""
    INDEX_FILE.write_text(json.dumps(index, indent=2))


def lookup_library(user_input: str) -> Optional[dict]:
    """
    Find a guess library that matches the user input.

    Returns the best matching library or None if no match.
    """
    index = load_index()
    user_words = set(re.findall(r'\w+', user_input.lower()))

    best_match = None
    best_score = 0

    for library in index["libraries"]:
        keywords = set(kw.lower() for kw in library["keywords"])
        overlap = len(user_words & keywords)

        if overlap > best_score:
            best_score = overlap
            best_match = library

    if best_match and best_score >= 1:
        # Update usage stats
        best_match["last_used"] = datetime.now().isoformat()
        best_match["use_count"] = best_match.get("use_count", 0) + 1
        save_index(index)
        return best_match

    return None


def get_library_content(library_id: str) -> Optional[str]:
    """Get the full content of a guess library."""
    index = load_index()

    for library in index["libraries"]:
        if library["id"] == library_id:
            file_path = LIBRARY_DIR / library["file"]
            if file_path.exists():
                return file_path.read_text()

    return None


def get_related_goals(library_id: str) -> List[str]:
    """Get related goals for a library."""
    index = load_index()

    for library in index["libraries"]:
        if library["id"] == library_id:
            return library.get("related_goals", [])

    return []


def get_goal_chain(goal: str) -> List[str]:
    """Get the goal chain for a related goal."""
    index = load_index()
    chains = index.get("related_goal_chains", {})
    return chains.get(goal, [])


def list_libraries() -> List[dict]:
    """List all available guess libraries."""
    index = load_index()
    return index["libraries"]


def get_stats() -> dict:
    """Get statistics about the guess library."""
    index = load_index()
    libraries = index["libraries"]

    total_guesses = sum(lib.get("guess_count", 0) for lib in libraries)
    total_uses = sum(lib.get("use_count", 0) for lib in libraries)

    return {
        "library_count": len(libraries),
        "total_guesses": total_guesses,
        "total_uses": total_uses,
        "libraries": [
            {
                "id": lib["id"],
                "guess_count": lib.get("guess_count", 0),
                "use_count": lib.get("use_count", 0),
                "keywords": lib.get("keywords", [])[:5]
            }
            for lib in libraries
        ]
    }


def add_library(
    library_id: str,
    file_name: str,
    input_type: str,
    keywords: List[str],
    guess_count: int,
    related_goals: List[str] = None,
    coverage: Dict[str, int] = None
) -> dict:
    """Add a new library to the index."""
    index = load_index()

    library = {
        "id": library_id,
        "file": file_name,
        "input_type": input_type,
        "keywords": keywords,
        "related_goals": related_goals or [],
        "guess_count": guess_count,
        "coverage": coverage or {},
        "created": datetime.now().isoformat(),
        "last_used": None,
        "use_count": 0
    }

    # Check if already exists
    for i, lib in enumerate(index["libraries"]):
        if lib["id"] == library_id:
            index["libraries"][i] = library
            save_index(index)
            return library

    index["libraries"].append(library)
    save_index(index)
    return library


def format_library_summary(library: dict) -> str:
    """Format a library for display."""
    return f"""
Library: {library['id']}
Type: {library['input_type']}
Keywords: {', '.join(library['keywords'][:10])}
Guesses: {library.get('guess_count', 'unknown')}
Related Goals: {', '.join(library.get('related_goals', []))}
Uses: {library.get('use_count', 0)}
"""


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]

    if command == "lookup":
        if len(sys.argv) < 3:
            print("Usage: guess_library.py lookup \"user input\"")
            sys.exit(1)

        user_input = sys.argv[2]
        library = lookup_library(user_input)

        if library:
            print(f"Found matching library: {library['id']}")
            print(format_library_summary(library))
            print(f"\nTo get content: python guess_library.py get {library['id']}")
        else:
            print("No matching library found.")
            print("Will need to generate guesses from scratch.")

    elif command == "get":
        if len(sys.argv) < 3:
            print("Usage: guess_library.py get <library_id>")
            sys.exit(1)

        library_id = sys.argv[2]
        content = get_library_content(library_id)

        if content:
            print(content)
        else:
            print(f"Library {library_id} not found.")

    elif command == "related":
        if len(sys.argv) < 3:
            print("Usage: guess_library.py related <library_id>")
            sys.exit(1)

        library_id = sys.argv[2]
        related = get_related_goals(library_id)

        if related:
            print(f"Related goals for {library_id}:")
            for goal in related:
                chain = get_goal_chain(goal)
                print(f"  - {goal}")
                if chain:
                    print(f"    Chain: {' → '.join(chain)}")
        else:
            print(f"No related goals found for {library_id}.")

    elif command == "list":
        libraries = list_libraries()

        if libraries:
            print(f"Available guess libraries: {len(libraries)}\n")
            for lib in libraries:
                print(f"  - {lib['id']}: {lib.get('guess_count', '?')} guesses")
                print(f"    Keywords: {', '.join(lib['keywords'][:5])}...")
        else:
            print("No libraries available.")

    elif command == "stats":
        stats = get_stats()
        print(f"Guess Library Statistics")
        print(f"========================")
        print(f"Libraries: {stats['library_count']}")
        print(f"Total Guesses: {stats['total_guesses']}")
        print(f"Total Uses: {stats['total_uses']}")
        print(f"\nPer Library:")
        for lib in stats['libraries']:
            print(f"  - {lib['id']}: {lib['guess_count']} guesses, used {lib['use_count']}x")

    elif command == "add":
        if len(sys.argv) < 6:
            print("Usage: guess_library.py add <id> <file> <type> <keywords_comma_sep> <guess_count>")
            sys.exit(1)

        library_id = sys.argv[2]
        file_name = sys.argv[3]
        input_type = sys.argv[4]
        keywords = sys.argv[5].split(",")
        guess_count = int(sys.argv[6]) if len(sys.argv) > 6 else 0

        library = add_library(library_id, file_name, input_type, keywords, guess_count)
        print(f"Added library: {library['id']}")

    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
