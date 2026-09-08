"""Retrieve target contributors without inferring an intervention or its efficacy."""
from pathlib import Path
import argparse
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    choice = parser.add_mutually_exclusive_group(required=True)
    choice.add_argument('--target', help='Inherited numeric ID, or AI-1 through AI-26')
    choice.add_argument('--search', help='Case-insensitive terms; every term must occur in a target record')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    targets = json.loads((ROOT / 'mind-change/targets.json').read_text())['targets']
    if args.target:
        selected = [t for t in targets if t['id'].upper() == args.target.upper()]
        if not selected:
            parser.error('Unknown target ID; inspect mind-change/targets.md')
    else:
        terms = re.findall(r'\S+', args.search.casefold())
        if not terms:
            parser.error('Provide at least one search term')
        selected = [t for t in targets if all(term in ' '.join(
            [t['definition'], t['candidate_contributors'], t['conditions']]).casefold() for term in terms)]
    if args.json:
        print(json.dumps(selected, ensure_ascii=False, indent=2))
    else:
        for t in selected:
            print(f'{t["id"]}. {t["definition"]}\n'
                  f'Candidate contributors: {t["candidate_contributors"]}\n'
                  f'Conditions: {t["conditions"]}\n'
                  f'Standing: {t["standing"]}\n'
                  f'Path: mind-change/{t["path"]}\n')


if __name__ == '__main__':
    main()
