from pathlib import Path
path = Path("Unit3/HW2/guest.txt")
name = input("Name: ")
path.write_text(name)
path = Path("Unit3/HW2/guest_book.txt")
book_name = ""
for i in range(3):
    name = input("Name: ")
    book_name += f"{name}\n"
path.write_text(book_name)
book = path.read_text()
print(book)