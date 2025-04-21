from pathlib import Path
path = Path("Unit3/learning_python.txt")
contents = path.read_text()
print(contents)
lines = contents.splitlines()
for i in lines:
    print(i)
c = contents.replace("Python","C")
print(c)