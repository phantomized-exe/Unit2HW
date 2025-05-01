from pathlib import Path
import json
path = Path("fav_num.json")
num_path = path.read_text()
num = json.loads(num_path)
print(f"I know your favorite number! Its {num}")