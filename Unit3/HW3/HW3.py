def add_num():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
    except ValueError:
        return "Values must be numbers"
    else:
        return a+b
while True:
    print(add_num())
