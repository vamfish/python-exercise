import random
import enemy_list

# Hero class
# Attributes: life, atk, gold, where
# Methods: enter_floor, attack_enemy
class Hero(object):

    # 英雄角色的初始化函数，指定初始HP, ATK和GOLD
    def __init__(self, init_life, init_atk, init_gold):
        self.life = init_life
        self.atk = init_atk
        self.gold = init_gold
        self.where = "Home"
        print(
            f"Hello! Our hero!\nYou now have life of {self.life}, atk of {self.atk}, and gold of {self.gold}!\nGo ahead! Kill all enemies!")

    # 让英雄角色进入指定楼层的函数
    def enter_floor(self, which_floor):
        if "Home" in self.where:
            self.where = f"Floor{which_floor}"
            print(f"You have entered the {self.where}")
            pass

    # 让英雄角色回到主界面的函数
    def exit_home(self):
        print(
            f"Where: {hero.where}\nHero Life: {hero.life}\nEnemy Life: {enemy_test.life}")
        if "Floor" in self.where and enemy_test.life > 0:
            print("You have fled!")
        elif "Floor" in self.where and enemy_test.life == 0:
            print("You have left the tower!")
        elif "Home" in self.where:
            print("ERROR: You are at home already!")
        self.where = "Home"


# Enemy class
class Enemy(object):

    def __init__(self, name, life, atk, gold):
        self.name = name
        self.life = life
        self.atk = atk
        self.gold = gold
        pass


# Slot_Machine class
class Slot_Machine(object):

    # 初始化老虎机的参数，指定备选列表以及对应的权重
    def __init__(self, slot_list, slot_weight):
        self.slot_list = slot_list
        self.slot_weight = slot_weight
        self.slot_results = [None, None, None]
        pass

    # 按照参数抽选三次，组成老虎机的结果
    def spin(self):
        for i in range(3):
            self.slot_results[i] = random.choices(
                self.slot_list, self.slot_weight)
        print(
            f"The result is <<{self.slot_results[0]}{self.slot_results[1]}{self.slot_results[2]}>>")


# 按照老虎机的结果确定在基础上的倍数
def decide(slot_results):
    a, b, c = slot_results
    times = 1
    if b == a:
        times = 3
        if c == b:
            times = 9
    return times


# Main program

list1 = ['h_atk', 'e_atk', 'h_rec', 'e_rec']
list2 = ['small', 'middle', 'large', 'boss']
weight1 = [40, 40, 10, 10]
SM_1 = Slot_Machine(list1, weight1)
hero = Hero(50, 10, 50)


while True:

    if hero.where == "Home":
        print("Which floor do you want to enter?")
        floorNum = int(input("> "))
        hero.enter_floor(floorNum)  # 进入用户指定的楼层

        enemy_names = enemy_list.enemy_list(floorNum)
        enemy_name = enemy_names[random.choice(list2)]
        enemy_paras = enemy_list.enemy_para(enemy_name)
        enemy_test = Enemy(enemy_name, enemy_paras[0], enemy_paras[1], enemy_paras[2])  # 初始化一个敌人

        print(f"You have seen an enemy called {enemy_test.name}! What do you want to do? Fight OR Exit?")
        choice = input('> ')

    elif "Floor" in hero.where:
        print(
            f"{enemy_test.name} is still there! What do you want to do? Fight OR Exit?")
        choice = input('> ')

    else:
        print("ERROR: Unknown hero.where!")
        exit(0)

    if choice == "Fight":
        SM_1.spin()  # 转动老虎机
        times = decide(SM_1.slot_results)

        if SM_1.slot_results[0] == ['h_atk']:  # 攻击敌人

            enemy_test.life -= hero.atk * times
            print(
                f"Where: {hero.where}\nHero Life: {hero.life}\nEnemy Life: {enemy_test.life}")

            if enemy_test.life > 0:
                print(
                    f"You attack {enemy_test.name}, its life is {enemy_test.life} now!")
            else:  # 敌人被击败时
                enemy_test.life = 0
                print(f"You defeat {enemy_test.name}!")
                hero.exit_home()

        elif SM_1.slot_results[0] == ['e_atk']:  # 被敌人攻击

            hero.life -= enemy_test.atk * times
            print(
                f"Where: {hero.where}\nHero Life: {hero.life}\nEnemy Life: {enemy_test.life}")

            if hero.life > 0:
                print(f"Your life is {hero.life} now! Be careful!")
            else:  # 英雄被击败时
                print("You are dead! See you next time!")
                exit(0)

        elif SM_1.slot_results[0] == ['h_rec']:  # 恢复英雄血量
            hero.life += 5 * times
            print(
                f"Where: {hero.where}\nHero Life: {hero.life}\nEnemy Life: {enemy_test.life}")
            print(f"Your life is {hero.life} now! Lucky!")

        elif SM_1.slot_results[0] == ['e_rec']:  # 恢复敌人攻击
            enemy_test.life += 1 * times
            print(
                f"Where: {hero.where}\nHero Life: {hero.life}\nEnemy Life: {enemy_test.life}")
            print(f"{enemy_test.name} is cured! Its life is {enemy_test.life} now!")

    elif choice == "Exit":
        hero.exit_home()

    else:
        print("ERROR: Unknown input!")
        exit(0)
