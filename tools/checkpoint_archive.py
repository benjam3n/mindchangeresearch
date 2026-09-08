"""Compatibility entry: use the single current checkpoint builder."""
from pathlib import Path
import json
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from checkpoint import build, check

if __name__ == '__main__':
    print(json.dumps(build(), indent=2))
