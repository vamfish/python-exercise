class Hero(object):

    def __init__(self, name, maxhp=20, hp=20, atk=5, gold=50, unlock_num=1):
        self.name = name
        self.maxhp = maxhp
        self.hp = hp
        self.atk = atk
        self.gold = gold
        self.unlock_num = unlock_num

    def print_status(self):
        print(f"STATUS:\n\tName: {self.name}\n\tHP: {self.hp}/{self.maxhp}\n\tATK: {self.atk}\n\tGold: {self.gold}\n")

    def update(self, update_list):
        self.item, self.times = update_list
        if 'HP' in self.item:
            self.hp += 5*self.times
            print(f"You get {5*self.times} HP")
            if self.hp > self.maxhp:
                self.hp = self.maxhp
        elif 'MaxHP' in self.item:
            self.maxhp += self.times
            print(f"You get {self.times} MaxHP")
            self.hp += self.times
        elif 'ATK' in self.item:
            self.atk += self.times
            print(f"You get {self.times} ATK")
        elif 'Gold' in self.item:
            self.gold += 10*self.times
            print(f"You get {10*self.times} Gold")

        self.print_status()

    def pay(self, money):
        if money > self.gold:
            print("You have nothing to pay!!")
            return False
        else:
            self.gold -= money
            return True

    pass
