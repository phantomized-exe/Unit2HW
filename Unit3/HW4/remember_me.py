from pathlib import Path
import json


# def greet_user():
#     """Greet the user by name."""
#
#     # Load the username, if it has been stored previously.
#     # Otherwise, prompt for the username and store it.
#
#     filename = "username.json"
#
#     try:
#         with open(filename) as file_object:
#             username = json.load(file_object)
#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(filename, "w") as file_object:
#             json.dump(username, file_object)
#             print("We\'ll remember you when you come back, " + username +
#                   "!")
#     else:
#         print("Welcome back, " + username + "!")
#
# greet_user()

def get_stored_username():
    """Get stored username if available."""
    filename = "username.json"

    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username
def get_stored_birthday():
    filename = "birthday.json"

    try:
        with open(filename) as file_object:
            birthday = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return birthday

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = "username.json"

    with open(filename, "w") as file_object:
        json.dump(username, file_object)

    return username


def get_new_birthday():
    birthmonth = input("What is your birth month? ")
    birthyear = int(input("What is your birth year? "))
    path = Path("username.json")
    user = path.read_text()
    load_user = json.loads(user)
    user_data = {}
    user_data[load_user] = f"{birthmonth} {birthyear}"
    filebirth = "birthday.json"
    with open(filebirth, "w") as file_object:
        json.dump(user_data, file_object)
    return user_data

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    birthday = get_stored_birthday()
    if username is not None and birthday is not None:
        print("Welcome back, " + username + "! You were born on " + birthday[username])
    else:
        username = get_new_username()
        birthday = get_new_birthday()
        print("We\'ll remember you when you come back, " + username)

greet_user()