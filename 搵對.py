import json
from collections import defaultdict
from pathlib import Path

base_path = Path(r'a:\1 testing zone')
json_path = base_path / '字.json'
report_path = base_path / 'duplicate_chars_report.md'

with json_path.open('r', encoding='utf-8') as f:
    data = json.load(f)

collections = data.get('collections', [])
char_groups = defaultdict(list)
for item in collections:
    char = item.get('char')
    if char is not None:
        char_groups[char].append(item)

duplicates = {char: items for char, items in char_groups.items() if len(items) > 1}

if duplicates:
    print(f'Found {len(duplicates)} duplicate "char" values.')
    for char, items in duplicates.items():
        safe_char = char.encode('unicode_escape').decode('ascii')
        print(f'- {safe_char}: {len(items)} entries')
else:
    print('No duplicate "char" values found.')

with report_path.open('w', encoding='utf-8') as f:
    f.write('# Duplicate `char` Report\n\n')
    if duplicates:
        f.write(f'This report lists {len(duplicates)} duplicate `char` values found in `collections` of `字.json`.\n\n')
        for char, items in duplicates.items():
            f.write(f'## `{char}` — {len(items)} entries\n\n')
            for item in items:
                f.write('```json\n')
                json.dump(item, f, ensure_ascii=False, indent=2)
                f.write('\n```\n\n')
    else:
        f.write('No duplicate `char` values found in `collections` of `字.json`.\n')

print(f'Report written to: {report_path}')
