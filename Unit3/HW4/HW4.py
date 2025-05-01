from pathlib import Path
import json
def fav_num():
    path = Path('fav_num.json')
    if path.exists():
        num_path = path.read_text()
        num = json.loads(num_path)
        print(f"I know your favorite number! Its {num}.")
    else:
        fav_num = int(input("What is your favorite number? "))
        num_store = json.dumps(fav_num)
        path.write_text(num_store)
fav_num()