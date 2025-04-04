import random
class Die:
    def __init__(self,sides=6):
        self.sides=sides
    def roll_die(self):
        print(random.randint(1,self.sides))
dice = Die(6)
dice.roll_die()
ten_dice = Die(10)
ten_dice.roll_die()
twenty_dice = Die(20)
twenty_dice.roll_die()

class Lottery:
    def __init__(self,my_ticket,random_list=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e'],lottery_list=[],lottery_win=0):
        self.my_ticket = my_ticket
        self.random_list = random_list
        self.lottery_list = lottery_list
        self.lottery_win = lottery_win
    def __eq__(self,other):
        return self.my_ticket == other.my_ticket and self.lottery_list == other.lottery_list
    def get_code(self):
        for i in range(4):
            self.lottery_list.append(self.random_list[random.randint(0,14)])
    def print_code(self):
        print("Any ticket matching this code is a winner: ",end="")
        for i in range(4):
            print(self.lottery_list[i],end="")
        print()
    def get_chance(self):
        while self.my_ticket != self.lottery_list:
            self.get_code()
            self.lottery_win += 1
            print(self.lottery_list)
            #if self.my_ticket == self.lottery_list:
                #break
            self.lottery_list = []
        print(f"It took {self.lottery_win} attempts to win the lottery")



ticket = Lottery(['6','e','8','a'])
ticket.get_code()
ticket.print_code()
ticket.get_chance()