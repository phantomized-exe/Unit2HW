import random
class VirtualPet:
    def __init__(self,gender=str,name=str,price=float,owned=False,condition=random.randint(75,125),happiness=random.randint(75,125),hunger=random.randint(75,125),energy=random.randint(75,125),days_starving=0):
        """Initializes class VirtualPet

        Args:
            gender (str, optional): gender of pet. Defaults to str.
            name (str, optional): name of pet. Defaults to str.
            price (float, optional): price of pet. Defaults to float.
            owned (str, optional): if the pet is owned or not
            condition (float, optional): condition of pet. Defaults to 100.00.
            gender (str, optional): gender of pet. Defaults to str.
            happiness (int, optional): happiness of pet. Defaults to 100.
            hunger (int, optional): hunger of pet. Defaults to 100.
            energy (int, optional): energy of pet. Defaults to 100.
        """
        self.gender = gender
        self.name = name
        self.owned = owned
        self.condition = condition
        self.happiness = happiness
        self.hunger = hunger
        self.energy = energy
        self.__price = price
        self.days_starving = days_starving
    def __repr__(self):
        """Returns pet stats when class is printed

        Returns:
            str: name, species, condition, happiness, hunger, energy, price
        """
        self.check_stats()
        return f"Name: {self.name}\nSpecies: {self.species}\nGender: {self.gender}\nCondition: {self.condition_status()}%\nHappiness: {self.status(self.happiness,1)}\nHunger: {self.status(self.hunger,2)}\nEnergy: {self.status(self.energy,3)}\nPrice: ${self.price_status():0.2f}\n"
    def __add__(self,other):
        """Overrides adding for VirtualPet class

        Args:
            other (int): other value

        Returns:
            int: self value
        """
        return self.happiness+other.happiness,self.hunger+other.hunger,self.energy+other.energy,self.__price+other.__price
    def __truediv__(self,other):
        """Overrides division for VirtualPet class

        Args:
            other (int): other value

        Returns:
            int: self value
        """
        return self.happiness/other.happiness,self.hunger/other.hunger,self.energy/other.energy,self.__price/other.__price
    def condition_status(self):
        """Gets the condition of the pet by averaging happiness, hunger, and energy
        Returns:
            float: percent condition of pet
        """
        return round((self.happiness+self.hunger+self.energy)/3,2)
    def get_price(self):
        """Getter method for hidden price

        Returns:
            float: __price
        """
        return self.__price
    def set_price(self,amount):
        """Setter method for hidden price

        Args:
            amount (float): amount to mult __price by

        Returns:
            float: the updated amount in __price
        """
        return self.__price+amount
    def price_status(self):
        """Returns updated condition of pet

        Returns:
            float: from 0 up
        """
        return self.condition_status()/100*self.get_price()
    def status(self,status_num,num_list,
                happiness_list=['feral','mad','sad','bored','happy','joyful','schizophrenic'],
                hunger_list=['dying of hunger','starving','hungry','peckish','full','glutted','stomach bursting'],
                energy_list=['zombie-like','weak','sluggish','lazy','energetic','frantic','crazy']):
        """list of all possible conditions

        Args:
            status_num (int): the num stat
            num_list (int): determines if status is for happy, hungry, or energy
            happiness_list (list, optional): list of happiness attributes. Defaults to ['feral','mad','sad','bored','happy','joyful','schizophrenic'].
            hunger_list (list, optional): list of hungry attributes. Defaults to ['dying of hunger','starving','hungry','peckish','full','glutted','stomach bursting'].
            energy_list (list, optional): list of energy emotions. Defaults to ['zombie-like','weak','sluggish','lazy','energetic','frantic','crazy'].

        Returns:
            str: returns current pet condition for happy, hungry, or energy
        """
        for i in range(7):
            if i*25 <= status_num < i*25+25:
                if num_list == 1:
                    return happiness_list[i]
                elif num_list == 2:
                    return hunger_list[i]
                else:
                    return energy_list[i]
            elif status_num >= 150:
                if num_list == 1:
                    return happiness_list[6]
                elif num_list == 2:
                    return hunger_list[6]
                else:
                    return energy_list[6]
    def check_stats(self):
        """resets the stats if they go too high or low
        """
        if self.happiness <= 0:
            self.hunger += self.happiness*self.days_starving
            self.energy += self.happiness*self.days_starving
            self.happiness = 0
        if self.hunger <= 0:
            self.happiness += self.hunger*self.days_starving
            self.energy += self.hunger*self.days_starving
            self.hunger = 0
        if self.energy <= 0:
            self.happiness += self.energy*self.days_starving
            self.hunger += self.energy*self.days_starving
            self.energy = 0
        if self.happiness > 150:
            self.happiness = 150
        if self.hunger > 150:
            self.hunger = 150
        if self.energy > 150:
            self.energy = 150
    def play(self):
        """play increases happiness and decreases energy and food
        """
        play_input = int(input(f"How hard do you want to play with {self.name}?\n1. Gentle\n2. Normal\n3. Hard\n(1/2/3) "))
        self.happiness += random.randint(1*play_input,10*play_input)
        self.energy -= random.randint(1*play_input,5*play_input)
        self.hunger -= 1*play_input
    def eat(self):
        """eat increases all stats but costs money. you can also starve your pet
        """
        food_list = [0,random.randint(1,5),random.randint(5,10),random.randint(10,15)]
        eat_input = int(input(f"How much do you want to feed {self.name}?\n1. Nothing\n2. A little: ${food_list[0]}\n3. Normal: ${food_list[1]}\n4. A lot: ${food_list[2]}\n(1/2/3/4) "))
        if eat_input != 1:
            if self.species == "cat":
                if random.randint(1,2+eat_input) == 1:
                    print(f"{self.name} turns their nose up at the food and won't eat it")
                    self.days_starving += 1
                    self.happiness -= self.days_starving*5
                    self.energy -= self.days_starving*5
                else:
                    self.days_starving = 0
                    self.hunger += random.randint(eat_input,food_list[eat_input-1])
                    self.energy += random.randint(1,food_list[eat_input-1]//1.5)
                    self.happiness += eat_input*random.randint(0,food_list[eat_input-1])//2
        else:
            self.days_starving += 1
            self.happiness -= self.days_starving*5
            self.energy -= self.days_starving*5
        if self.hunger < 25 or 75 < self.hunger:
            if self.hunger < 25:
                self.energy -= random.randint(5,10)
            elif 75 < self.hunger:
                self.energy -= random.randint(0,5)
        else:
            self.energy += random.randint(1*eat_input,5*eat_input)
    def change_name(self):
        """changes name of pet
        """
        name_choice = input(f"What do you want to change {self.name}'s name to? ")
        self.name = name_choice
class Dog(VirtualPet):
    """class Dog inherits from VirtualPet

    Args:
        VirtualPet (class): main class for virtual pet
    """
    species = "dog"
    happiness = random.randint(45,150)
    hunger = random.randint(26,75)
    energy = random.randint(hunger,150)
class Cat(VirtualPet):
    """class Cat inherits from VirtualPet

    Args:
        VirtualPet (class): main class for virtual pet
    """
    species = "cat"
    happiness = random.randint(30,150)
    hunger = random.randint(35,150)
    energy = random.randint(26,hunger)
class Fish(VirtualPet):
    """class Fish inherits from VirtualPet

    Args:
        VirtualPet (class): main class for virtual pet
    """
    species = "fish"
    happiness = random.randint(26,100)
    hunger = random.randint(50,125)
    energy = random.randint(30,hunger)
    def play(self):
        """overrides play method because fish dont like to be played with
        """
        print("Warning: It might not be a good idea to play with a fish")
        continue_play = input(f"Play with {self.name}? (yes/no) ")
        if continue_play == "yes":
            play_input = int(input(f"How hard do you want to play with {self.name}?\n1. Gentle\n2. Normal\n3. Hard\n(1/2/3) "))
            if random.randint(1,8-play_input) == 1:
                print(f"You accidentally squished {self.name} to death!")
            else:
                self.happiness += random.randint(1*play_input,10*play_input)
                self.energy -= random.randint(1*play_input,5*play_input)
class Hamster(VirtualPet):
    """class Hamster inherits from VirtualPet

    Args:
        VirtualPet (class): main class for virtual pet
    """
    species = "hamster"
    happiness = random.randint(26,150)
    hunger = random.randint(35,125)
    energy = random.randint(50,125)

def gender():
    random_gender = random.randint(1,2)
    if random_gender == 1:
        return "male"
    else:
        return "female"
def name(gender,name_list):
    """generates a random name depending on gender of pet

    Args:
        gender (str): either male or female, changes names
    """
    male_pet_names = [
    "Max", "Charlie", "Cooper", "Buddy", "Rocky", "Teddy", "Milo", "Leo", "Jack", "Toby",
    "Bear", "Duke", "Oliver", "Jake", "Zeus", "Louie", "Finn", "Oscar", "Sam", "Murphy",
    "Bailey", "Chester", "Rex", "Winston", "Simba", "Gus", "Bentley", "Rusty", "Bruno", "Jasper",
    "Marley", "Moose", "Baxter", "Apollo", "Boomer", "Tank", "Hank", "Shadow", "Ace", "Blue",
    "Frankie", "Ziggy", "Oreo", "Scooter", "Archie", "Rocco", "Diesel", "Casper", "Chico", "Peanut",
    "Remy", "Buzz", "Lucky", "Ranger", "Thor", "Roscoe", "Harley", "Cash", "Loki", "George",
    "Zeke", "Hunter", "Bruce", "Sparky", "Maverick", "Bandit", "Ralph", "Scooby", "Alfie", "Yogi",
    "Einstein", "Cody", "Frodo", "Porter", "Shadow", "Rusty", "Benny", "Tyson", "Nico", "Zorro",
    "Taco", "Toby", "Monty", "Chief", "Blaze", "Django", "Rebel", "Vinnie", "Watson", "Rowdy",
    "Jax", "Django", "Clifford", "Pablo", "Nugget", "Skip", "Mickey", "Romeo", "King", "Major"
]
    female_pet_names = [
    "Bella", "Luna", "Lucy", "Daisy", "Lola", "Sadie", "Maggie", "Chloe", "Sophie", "Lily",
    "Zoe", "Coco", "Roxy", "Gracie", "Molly", "Rosie", "Lulu", "Abby", "Stella", "Penny",
    "Mia", "Nala", "Ellie", "Ginger", "Ruby", "Olive", "Willow", "Hazel", "Harley", "Nova",
    "Annie", "Millie", "Honey", "Missy", "Bonnie", "Princess", "Izzy", "Angel", "Trixie", "Remy",
    "Pixie", "Peaches", "Sasha", "Fiona", "Layla", "Dixie", "Maddie", "Mocha", "Poppy", "Phoebe",
    "Sky", "Winnie", "Bambi", "Pumpkin", "Pearl", "Snowball", "Freya", "Minnie", "Precious", "Elsa",
    "Cupcake", "Nina", "Toffee", "Snickers", "Dotty", "Opal", "Tinkerbell", "Queenie", "Velvet", "Mochi",
    "Sugar", "Buttercup", "Gigi", "Kiki", "Lacey", "Jewel", "Summer", "Blossom", "Cherry", "Goldie",
    "Marley", "Hope", "Taffy", "Sassy", "Fluffy", "Cinnamon", "Bubbles", "Cookie", "Twinkle", "Snowflake",
    "Ivy", "Raven", "Stormy", "Peach", "Amber", "Callie", "Delilah", "Gypsy", "Noodle", "Kona"
]
    if gender == "male":
        male_name = random.randint(0,99)
        name_list.append(male_pet_names[male_name])
    else:
        female_name = random.randint(0,99)
        name_list.append(female_pet_names[female_name])
    return name_list
def species():
    """randomizes a species for pet

    Returns:
        class: either Dog, Cat, Fish, or Hamster
    """
    pet_list = [Dog,Cat,Fish,Hamster]
    return pet_list[random.randint(0,3)]
def generate_pet_id(code_list):
    """generates a unique ID for referrence whenever new pet is created
    """
    digits_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    check_duplicates = True
    while check_duplicates:
        code_generator = ""
        for i in range(10):
            code_generator += digits_list[random.randint(30,35)]
        if code_generator not in code_list:
            code_list.append(code_generator)
            check_duplicates = False
            return code_list
        else:
            continue
def display_pet_id(code_list,name_list):
    """debug tool to display pet IDs
    """
    for i in range(len(name_list)):
        print(f"Pet ID: {code_list[i]}, Pet Name: {name_list[i]}")
def display_pet_names(code_list,name_list):
    """displays pet names and lets user select specific pet

    Args:
        code_list (list): list of generated codes
        name_list (list): list of generated names

    Returns:
        int: retruns user's choice of pet
    """
    num_pets = ""
    print("Select Pet:")
    for i in range(len(name_list)):
        if num_pets == "":
            num_pets += f"{i+1}"
        else:
            num_pets += f"/{i+1}"
        print(f"{i+1}. {name_list[i]} ({code_list[i].species})")
    name_choice = int(input(f"({num_pets}) "))
    print()
    return name_choice-1
def generate_pet(code_list,name_list,num_pets):
    for i in range(num_pets):
        rand_price = random.randint(10,50)
        random_gender = gender()
        name_list = name(random_gender,name_list)
        code_list = generate_pet_id(code_list)
        code_list[i] = species()(random_gender,name_list[-1],rand_price)
        print(code_list[i])
    return code_list, name_list
def pet_choices(current_pet,code_list):
    if code_list[current_pet].owned:
        print("pass")
    else:
        print("fail")
def main():
    """main
    """
    code_list = []
    name_list = []
    generate_pet(code_list,name_list,5)
    current_pet = display_pet_names(code_list,name_list)
    print(code_list[current_pet])
    pet_choices(current_pet,code_list)
if __name__ == "__main__":
    main()