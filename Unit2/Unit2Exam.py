import random
class VirtualPet:
    def __init__(self,name=str,price=float,condition=100.00,happiness=100,hunger=0,energy=100,days_starving=0):
        """Initializes class VirtualPet

        Args:
            name (str, optional): name of pet. Defaults to str.
            price (float, optional): cprice of pet. Defaults to float.
            condition (float, optional): condition of pet. Defaults to 100.00.
            happiness (int, optional): happiness of pet. Defaults to 100.
            hunger (int, optional): hunger of pet. Defaults to 100.
            energy (int, optional): energy of pet. Defaults to 100.
        """
        self.name = name
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
        return f"Name: {self.name}\nSpecies: {self.species}\nCondition: {self.condition_status()}%\nHappiness: {self.status(self.happiness,1)}\nHunger: {self.status(self.hunger,2)}\nEnergy: {self.status(self.energy,3)}\nPrice: ${self.price_status():0.2f}"
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
        return self.__price*amount
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
        if self.happiness < 0:
            self.happiness = 0
        if self.hunger < 0:
            self.hunger = 0
        if self.energy < 0:
            self.energy = 0
        if self.happiness > 150:
            self.happiness = 150
        if self.hunger < 150:
            self.hunger = 150
        if self.energy < 150:
            self.energy = 150
    def play(self):
        play_input = int(input(f"How hard do you want to play with {self.name}?\n1. Gentle\n2. Normal\n3. Hard\n(1/2/3) "))
        self.happiness += random.randint(1*play_input,10*play_input)
        self.energy -= random.randint(1*play_input,5*play_input)
    def eat(self):
        food_list = [0,random.randint(1,5),random.randint(5,10),random.randint(10,15)]
        eat_input = int(input(f"How much do you want to feed {self.name}?\n1. Nothing\n2. A little: ${food_list[0]}\n3. Normal: ${food_list[1]}\n4. A lot: ${food_list[2]}\n(1/2/3/4) "))
        if eat_input != 1:
            self.days_starving = 0
            self.hunger += random.randint(eat_input,food_list[eat_input-1])
            self.happiness += eat_input*random.randint(0,food_list[eat_input-1])//2
        else:
            self.days_starving += 1
            self.happiness -= self.days_starving*self.hunger//2
        if self.hunger < 25 or 75 < self.hunger:
            if self.hunger < 25:
                self.energy -= random.randint(5,10)
            elif 75 < self.hunger:
                self.energy -= random.randint(0,5)
        else:
            self.energy += random.randint(1*eat_input,5*eat_input)
    
class Dog(VirtualPet):
    species = "dog"
class Cat(VirtualPet):
    species = "cat"
class Fish(VirtualPet):
    species = "fish"
class Hamster(VirtualPet):
    species = "hampster"

def main():
    pet1 = Dog("Joe",250)
    print(pet1)
    pet1.play()
    pet1.eat()
    print(pet1)
    #pet2 = Fish("Billy",50)
    #print(pet2)
if __name__ == main():
    main()