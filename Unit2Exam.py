class VirtualPet:
    def __init__(self,name=str,price=int,happiness=100,hunger=100,energy=100):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self.energy = energy
        self.__price = price
    def __repr__(self):
        return f"Name: {self.name}\nSpecies: {self.species}\nHappiness: {self.status(self.happiness,1)}\nHunger: {self.status(self.hunger,2)}\nEnergy: {self.status(self.energy,3)}\nPrice: ${self.price_status():0.2f}"
    def get_price(self):
        return self.__price
    def set_price(self,amount):
        return self.__price*amount
    def status(self,status_num,num_list,
                happiness_list=['feral','mad','sad','bored','happy','joyful','schizophrenic'],
                hunger_list=['dying of hunger','starving','hungry','peckish','full','glutted','stomach bursting'],
                energy_list=['zombie-like','weak','sluggish','lazy','energetic','frantic','crazy']):
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
    def price_status(self):
        for i in range(7):
            if (self.happiness+self.hunger+self.energy)/3 <= 50:
                if i*25 <= (self.happiness+self.hunger+self.energy)/3 < i*25+25:
                    return self.set_price((self.happiness+self.hunger+self.energy)/3/100)
            else:
                if i*25 <= (self.happiness+self.hunger+self.energy)/3 < i*25+25:
                    return self.set_price((self.happiness+self.hunger+self.energy)/3/100)
    def __add__(self,other):
        return self.hunger + other.hunger, self.energy + other.energy
class Dog(VirtualPet):
    species = "dog"
class Cat(VirtualPet):
    species = "cat"
class Fish(VirtualPet):
    species = "fish"
class Hamster(VirtualPet):
    species = "hampster"

pet1 = Dog("Joe",200)
print(pet1)
