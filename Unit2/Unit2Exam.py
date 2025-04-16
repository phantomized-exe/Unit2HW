class VirtualPet:
    def __init__(self,name=str,price=float,condition=100.00,happiness=100,hunger=100,energy=100):
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
    def __repr__(self):
        """Returns pet stats when class is printed

        Returns:
            str: name, species, condition, happiness, hunger, energy, price
        """
        return f"Name: {self.name}\nSpecies: {self.species}\nCondition: {self.condition_status()}%\nHappiness: {self.status(self.happiness,1)}\nHunger: {self.status(self.hunger,2)}\nEnergy: {self.status(self.energy,3)}\nPrice: ${self.price_status():0.2f}"
    def __add__(self,other):
        """Overrides adding for VirtualPet class

        Args:
            other (int): other value

        Returns:
            int: self value
        """
        return self.happiness+other.happiness,self.hunger+other.hunger,self.energy+other.energy
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
        """_summary_

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
    pet2 = Fish("Billy",50)
    print(pet2)
if __name__ == main():
    main()