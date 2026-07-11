import json
from pathlib import Path

json_path = Path(r"a:\3 Dictionary\字.json")

with json_path.open("r", encoding="utf-8") as f:
    data = json.load(f)

collections = data.get("collections", [])
print(len(collections))
