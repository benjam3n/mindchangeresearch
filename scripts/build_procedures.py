"""Render subject descriptions from the substantive records in recipes.json."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
data = json.loads((ROOT / 'recipes.json').read_text(encoding='utf-8'))
recipes = data['recipes']
titles = data['record_titles']
for subject in dict.fromkeys(r['subject'] for r in recipes):
    lines = ['# ' + subject, '']
    for recipe in recipes:
        if recipe['subject'] != subject:
            continue
        lines.extend(['## ' + recipe['method'], '', recipe['description'], ''])
        lines.extend(f'{i}. {step}' for i, step in enumerate(recipe['procedure'], 1))
        lines.extend(['', recipe['case'], '', recipe['support'], ''])
        lines.append('; '.join(f'[{titles[path]}](../{path})' for path in recipe['records']) + '.')
        lines.append('')
    (ROOT / 'changes' / (subject.lower() + '.md')).write_text('\n'.join(lines), encoding='utf-8')
