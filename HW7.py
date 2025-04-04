# I couldn't find my original code so I just used the code from the book for the Restaurant and User classes
class Restaurant:
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type, flavors=[]):
        super().__init__(name, cuisine_type)
        self.flavors = flavors
    def display_flavors(self):
        for flavor in self.flavors:
            print(flavor)

icecreamstand = IceCreamStand("Dairy Queen","burgers",["chocolate","vanilla","strawberry"])
icecreamstand.display_flavors()

class Admin(User):
    def __init__(self, first_name,last_name,username,email,location,privileges=[]):
        super().__init__(first_name,last_name,username,email,location)
        self.privileges = privileges
class Privileges(Admin):
    def __init__(self, privileges=[]):
        self.privileges = privileges
    def show_priveliges(self):
        for privelige in self.privileges:
            print(privelige)

admin = Admin("John","Doe","j-doe","johndoe@gmail.com","West Linn, OR",["can add post","can delete post","can ban user"])
admin_privilege = Privileges(admin.privileges)
admin_privilege.show_priveliges()
