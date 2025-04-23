import random
class VirtualPet:
    day = 1
    def __init__(self,id,gender=str,name=str,price=float,owned=False,condition=random.randint(75,125),happiness=random.randint(75,125),hunger=random.randint(75,125),energy=random.randint(75,125),days_sad=0):
        """Initializes class VirtualPet

        Args:
            id (str): unique id of pet
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
        self.id = id
        self.gender = gender
        self.name = name
        self.owned = owned
        self.condition = condition
        self.happiness = happiness
        self.hunger = hunger
        self.energy = energy
        self.__price = price
        self.days_sad = days_sad
    def __repr__(self):
        """Returns pet stats when class is printed

        Returns:
            str: name, species, condition, happiness, hunger, energy, price
        """
        print()
        self.check_stats()
        return f"Name: {self.name}\nSpecies: {self.species}\nGender: {self.gender}\nCondition: {self.condition_status()}%\nOwned: {self.owned}\nHappiness: {self.status(self.happiness,1)}\nHunger: {self.status(self.hunger,2)}\nEnergy: {self.status(self.energy,3)}\nPrice: ${self.price_status():0.2f}"
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
        return self.condition_status()/100*self.get_price()*VirtualPet.day
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
            self.hunger += self.happiness*self.days_sad
            self.energy += self.happiness*self.days_sad
            self.happiness = 0
        if self.hunger <= 0:
            self.happiness += self.hunger*self.days_sad
            self.energy += self.hunger*self.days_sad
            self.hunger = 0
        if self.energy <= 0:
            self.happiness += self.energy*self.days_sad
            self.hunger += self.energy*self.days_sad
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
        print()
        play_input = int(input(f"How hard do you want to play with {self.name}?\n1. Neglect\n2. Gentle\n3. Normal\n4. Hard\n(1/2/3/4) "))
        if 2 <= play_input <=4:
            self.happiness += random.randint(1*play_input,10*play_input)
            self.energy -= random.randint(1*play_input,5*play_input)
            self.hunger -= 1*play_input
        else:
            self.days_sad += 1
            self.happiness -= self.days_sad*self.days_sad
            self.energy -= self.days_sad*self.days_sad
            self.happiness -= self.days_sad*self.days_sad
    def eat(self,money):
        """eat increases all stats but costs money. you can also starve your pet
        """
        food_list = [random.randint(10,20),random.randint(20,30),random.randint(35,50)]
        print()
        eat_input = int(input(f"How much do you want to feed {self.name}? (You have ${money:.2f})\n1. Nothing\n2. A little: ${food_list[0]}\n3. Normal: ${food_list[1]}\n4. A lot: ${food_list[2]}\n(1/2/3/4) "))
        if eat_input != 1:
            if self.species == "cat":
                if random.randint(1,2+eat_input) == 1:
                    print(f"{self.name} turns their nose up at the food and won't eat it")
                    self.days_sad += 1
                    money -= food_list[eat_input-2]
                    self.happiness -= self.days_sad*self.days_sad
                    self.energy -= self.days_sad*self.days_sad
                    return money
            self.days_sad = 0
            money -= food_list[eat_input-2]
            self.hunger += random.randint(eat_input,food_list[eat_input-2])
            self.energy += random.randint(1,food_list[eat_input-2])
            self.happiness += eat_input*random.randint(0,food_list[eat_input-2])
        else:
            self.days_sad += 1
            self.hunger -= self.days_sad*self.days_sad
            self.happiness -= self.days_sad*self.days_sad
            self.energy -= self.days_sad*self.days_sad
        return money
    def rest(self):
        rest_input = int(input(f"How much rest should {self.name} get?\n1. Nothing\n2. A little\n3. Normal\n4. A lot\n(1/2/3/4) "))
        if 2 <= rest_input <=4:
            self.energy += random.randint(1*rest_input,10*rest_input)
            self.hunger -= random.randint(1*rest_input,5*rest_input)
            self.happiness += random.randint(-5,5)
        else:
            self.days_sad += 1
            self.happiness -= self.days_sad*self.days_sad
            self.energy -= self.days_sad*self.days_sad
            self.hunger -= self.days_sad*self.days_sad
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
        continue_play = input(f"Play with {self.name}? (y/n) ")
        if continue_play == "y":
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
        while male_pet_names[male_name] in name_list:
            male_name = random.randint(0,99)
        name_list.append(male_pet_names[male_name])
    else:
        female_name = random.randint(0,99)
        while female_pet_names[female_name] in name_list:
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
def display_pet_id(pet_list,name_list):
    """debug tool to display pet IDs
    """
    for i in range(len(name_list)):
        print(f"Pet ID: {pet_list[i]}, Pet Name: {name_list[i]}")
def display_pet_names(pet_list,name_list,owned,day,money):
    """displays pet names and lets user select specific pet

    Args:
        code_list (list): list of generated codes
        name_list (list): list of generated names

    Returns:
        int: returns user's choice of pet
    """
    num_pets = ""
    bullet_num = 0
    spot_list = []
    print()
    print("Select Pet:")
    for i in range(len(name_list)):
        if pet_list[i].owned==owned:
            spot_list.append(i)
            bullet_num += 1
            if num_pets == "":
                num_pets += f"{bullet_num}"
            else:
                num_pets += f"/{bullet_num}"
            print(f"{bullet_num}. {name_list[i]} ({pet_list[i].species})")
    bullet_num += 1
    if num_pets == "":
        num_pets += f"{bullet_num}"
    else:
        num_pets += f"/{bullet_num}"
    print(f"{bullet_num}. Back")
    name_choice = int(input(f"({num_pets}) "))
    if name_choice == bullet_num:
        hub_choices(day,pet_list,name_list,money,owned)
    else:
        return spot_list[name_choice-1]
def generate_pet_id(pet_list):
    """generates a unique ID for reference whenever new pet is created
    """
    digits_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
    check_duplicates = True
    while check_duplicates:
        code_generator = ""
        for i in range(10):
            code_generator += digits_list[random.randint(30,35)]
        if code_generator not in pet_list:
            return code_generator
        else:
            continue
def generate_pet(pet_list,name_list,num_pets,owned=False):
    """generates a pet from VirtualPet class

    Args:
        code_list (list): stores the codes for generated pets
        name_list (liat): stores the names of generated pets
        num_pets (int): the number of pets to be generated
        owned (bool, optional): if the pet is owned or not. Defaults to False.

    Returns:
        list: returns the name, and code of generated pet(s)
    """
    for i in range(num_pets):
        rand_price = random.randint(10,50)
        random_gender = gender()
        name_list = name(random_gender,name_list)
        code_id = generate_pet_id(pet_list)
        pet = species()(code_id,random_gender,name_list[-1],rand_price)
        if owned:
            pet.owned = True
        pet_list.append(pet)
    return pet_list, name_list
def pet_choices(current_pet,pet_list,money,name_list,day,owned):
    """Choices for individual pets

    Args:
        current_pet (int): the choice of pet to pull code from code_list
        code_list (list): list of all pet codes
        money (float): user's money to buy, sell, and feed pets
    """
    num_choices = ""
    pet_choice_list = []
    print()
    if not pet_list[current_pet].owned and pet_list[current_pet].get_price() > money:
        print(f"You have ${money:.2f} (Not enough to buy pet):")
    else:
        print(f"You have ${money:.2f}:")
    if pet_list[current_pet].get_price() < money and not pet_list[current_pet].owned:
        pet_choice_list.append("Buy pet")
    if pet_list[current_pet].owned:
        pet_choice_list.append("Sell pet")
        pet_choice_list.append("Play with pet")
        pet_choice_list.append("Feed pet")
    pet_choice_list.append("Back")
    for i in range(len(pet_choice_list)):
        if num_choices == "":
            num_choices += f"{i+1}"
        else:
            num_choices += f"/{i+1}"
        print(f"{i+1}. {pet_choice_list[i]}")
    pet_choice = int(input(f"({num_choices}) "))
    if pet_choice == 1 and pet_list[current_pet].get_price() < money and not pet_list[current_pet].owned:
        money -= pet_list[current_pet].price_status()
        pet_list[current_pet].owned = True
        hub_choices(day,pet_list,name_list,money,owned)
    elif pet_choice == 1 and pet_list[current_pet].owned:
        money += pet_list[current_pet].price_status()
        pet_list[current_pet].owned = False
        hub_choices(day,pet_list,name_list,money,owned)
    elif pet_choice == 2 and pet_list[current_pet].owned:
        pet_list[current_pet].play()
        hub_choices(day,pet_list,name_list,money,owned)
    elif pet_choice == 3 and pet_list[current_pet].owned:
        money = pet_list[current_pet].eat(money)
        hub_choices(day,pet_list,name_list,money,owned)
    else:
        current_pet = display_pet_names(pet_list,name_list,owned,day,money)
        print(pet_list[current_pet])
        pet_choices(current_pet,pet_list,money,name_list,day,owned)
def hub_choices(day,pet_list,name_list,money,owned):
    num_list = 0
    num_choices = "1"
    pet_owned = False
    pet_available = False
    print()
    print(f"Day {day} (${money:.2f}):")
    for i in range(len(pet_list)):
        if pet_list[i].owned:
            num_list += 1
            pet_owned = True
            danger_str = ""
            danger_meter = False
            num_choices += f"/{num_list+1}"
            for i in pet_list:
                if i.condition_status() <= 20:
                    if danger_str == "":
                        danger_str += f"{i.name}"
                    else:
                        danger_meter = True
                        danger_str += f", {i.name}"
            if danger_str == "":
                print(f"{num_list}. Owned pets")
            else:
                if danger_meter:
                    danger_str += " are"
                else:
                    danger_str += " is"
                print(f"{num_list}. Owned pets (Warning: {danger_str} about to perish)")
            break
    for i in range(len(pet_list)):
        if not pet_list[i].owned:
            num_list += 1
            pet_available = True
            num_choices += f"/{num_list+1}"
            print(f"{num_list}. Pet market")
            break
    num_list += 1
    print(f"{num_list}. Next day")
    hub_choice = int(input(f"({num_choices}) "))
    if hub_choice == 1 and pet_owned:
        current_pet = display_pet_names(pet_list,name_list,True,day,money)
        print(pet_list[current_pet])
        pet_choices(current_pet,pet_list,money,name_list,day,True)
    elif hub_choice == 1 and pet_available and not pet_owned or hub_choice == 2 and pet_available and pet_owned:
        current_pet = display_pet_names(pet_list,name_list,False,day,money)
        print(pet_list[current_pet])
        pet_choices(current_pet,pet_list,money,name_list,day,False)
    elif hub_choice == 1 or hub_choice == 2 or hub_choice == 3:
        next_day(day,owned,pet_list,name_list,money)
    else:
        hub_choices(day,pet_list,name_list,money,owned)
def next_day(day,owned,pet_list,name_list,money):
    day += 1
    day_pet_list = []
    day_name_list = []
    VirtualPet.day += 1
    for i in range(len(pet_list)):
        if pet_list[i].owned:
            day_pet_list.append(pet_list[i])
            day_name_list.append(pet_list[i].name)
    pet_list = day_pet_list
    name_list = day_name_list
    decrease_stats(pet_list,name_list)
    generate_pet(pet_list,name_list,random.randint(1,day))
    hub_choices(day,pet_list,name_list,money,owned)
def decrease_stats(pet_list,name_list):
    for i in pet_list[:]:
        if not i.owned:
            continue
        ds = i.days_sad**2
        if i.species == "dog":
            i.happiness -= random.randint(ds*5 + 4, (ds*5 + 4)*(150 - i.energy) // 10 + 6)
        else:
            i.happiness -= random.randint(ds + 2, (ds + 2)*(150 - i.energy) // 15 + 3)
        if i.species == "cat":
            i.hunger -= random.randint(ds*5 + 4, (ds*5 + 4)*(150 - i.energy) // 7 + 6)
        elif i.species == "fish" or i.species == "hamster":
            i.hunger -= random.randint(ds + 2, (ds + 2)*(150 - i.energy) // 15 + 3)
        else:
            i.hunger -= random.randint(ds + 2, (ds + 2)*(150 - i.energy) // 20 + 2)
        if i.species == "fish" or i.species == "hamster":
            i.energy -= random.randint(i.energy // 3, (ds + 2)*(ds + 2) // 1 + i.energy // 2)
        elif i.species == "cat":
            i.energy -= random.randint(i.energy // 4, (ds + 2)*(ds + 2) // 2 + i.energy // 3)
        else:
            i.energy -= random.randint(i.energy // 5, (ds + 2)*(ds + 2) // 3 + i.energy // 4)
        if i.condition_status() <= 0:
            print()
            print(f"{i.name} the {i.species} has perished!")
            name_list.remove(i.name)
            pet_list.remove(i)
def main():
    """main
    """
    money = random.randint(85,120)
    day = 1
    pet_list = []
    name_list = []
    owned = False
    generate_pet(pet_list,name_list,random.randint(1,5))
    #generate_pet(pet_list,name_list,1,True)
    hub_choices(day,pet_list,name_list,money,owned)
if __name__ == "__main__":
    main()
#things to add: stock market, animal wellfare, pet personalities, more species, more names
