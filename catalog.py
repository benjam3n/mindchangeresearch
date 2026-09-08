"""Exact access to perspectives, modification operations, and linked procedures."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def read(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('kind', choices=['perspective', 'operation', 'recipe', 'subject', 'search'])
    parser.add_argument('query')
    args = parser.parse_args()
    perspectives = read('perspectives/catalog.json')['perspectives']
    operations = read('operations/catalog.json')['operations']
    recipes = read('recipes.json')['recipes']
    pmap = {x['id']: x for x in perspectives}
    omap = {x['id']: x for x in operations}
    query = args.query.casefold()
    if args.kind == 'recipe':
        matches = [r for r in recipes if r['id'].casefold() == query]
        for r in matches:
            print(r['subject'] + ': ' + r['method'])
            print(r['description'])
            for i, step in enumerate(r['procedure'], 1): print(f'{i}. {step}')
            print(r['case'])
            print(r['support'])
            for pid in r['perspectives']: print(pid + ': ' + pmap[pid]['statement'])
            for oid in r['operations']: print(oid + ': ' + omap[oid]['operation'])
            for path in r['records']: print(path)
    elif args.kind == 'perspective':
        matches = [p for p in perspectives if p['id'].casefold() == query]
        for p in matches:
            print(p['id'] + ': ' + p['statement'])
            print(p['subject'])
            for r in recipes:
                if p['id'] in r['perspectives']: print('recipe ' + r['id'] + ': ' + r['method'])
    elif args.kind == 'operation':
        matches = [o for o in operations if o['id'].casefold() == query]
        for o in matches:
            print(o['id'] + ': ' + o['operation'])
            print(o['category'])
            for r in recipes:
                if o['id'] in r['operations']: print('recipe ' + r['id'] + ': ' + r['method'])
    elif args.kind == 'subject':
        matches = [p for p in perspectives if p['subject'].casefold() == query]
        for p in matches: print(p['id'] + ': ' + p['statement'])
        related = [r for r in recipes if r['subject'].casefold() == query]
        for r in related: print('recipe ' + r['id'] + ': ' + r['description'])
        matches += related
    else:
        matches = []
        for p in perspectives:
            if query in (p['subject'] + ' ' + p['statement']).casefold():
                matches.append(p)
                print(p['id'] + ': ' + p['statement'])
        for o in operations:
            if query in (o['category'] + ' ' + o['operation']).casefold():
                matches.append(o)
                print(o['id'] + ': ' + o['operation'])
        for r in recipes:
            fields = [r['subject'], r['method'], r['description'], *r['procedure'], r['case'], r['support']]
            matching_fields = [value for value in fields if query in value.casefold()]
            if matching_fields:
                matches.append(r)
                print('recipe ' + r['id'] + ': ' + r['method'])
                for value in matching_fields:
                    print(value)
    if not matches:
        parser.exit(1, 'No exact ID, subject, or literal text match.\n')

if __name__ == '__main__':
    main()
