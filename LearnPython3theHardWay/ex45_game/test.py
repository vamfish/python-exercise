import random
import os
import sys

from hero import Hero
from slot import Slot
import enemies

class Engine(object):

    def __init__(self):
        pass
    
    def initialize(self):
        print("Welcome to <<Tower of Fortune>>\nDo you want to LOAD a savefile?")
        while True:
            ans = input("(Y/N)> ")
            if ans == "Y" or ans == "y":
                # load the savefile, promote the name in the file, check again
                self.load()
                break
            elif ans == "N" or ans == "n":
                # wait for name of the hero, intialize it
                h_name = input("Enter your name: ")
                global hero1
                hero1 = Hero(h_name)
                # print(OPEN)
                # print(hero_paras)
                break
            else:
                print("Wrong Input!")
                continue

    def play(self):
        # Tips for next step
        while True:
            ans = input("E: enter tower\nS: save\nB: enter store\n> ")
            if ans == "E" or ans == "e":
                # Enter the tower
                self.enter('tower')
                break
            elif ans == "S" or ans == "s":
                # save the status
                self.save()
                continue
            elif ans == "B" or ans == "b":
                # Enter the store
                self.enter('store')
                break
            else:
                print("Wrong Input!")
                continue

    def save(self):
        # save current status into savefile
        savefile = open(f"{hero1.name}.save", 'w')
        hero_paras = [hero1.name, str(hero1.maxhp), str(hero1.hp), str(hero1.atk), str(hero1.gold), str(hero1.unlock_num)]
        savefile.write('\n'.join(hero_paras))
        savefile.close()
        print(f"Successfully saved {hero1.name}.save\nSaved parameters: {hero_paras}")

    def load(self):
        # load file and initialize the hero
        loadfile_name = input("Enter your name of character: ")
        loadfile = open(f"{loadfile_name}.save", 'r')
        hero_paras = []
        for i in range(6):
            hero_paras.append(loadfile.readline().strip())
        loadfile.close()
        global hero1
        hero1 = Hero(hero_paras[0], int(hero_paras[1]), int(hero_paras[2]), int(hero_paras[3]), int(hero_paras[4]), int(hero_paras[5]))
        print(f"Successfully loaded {hero1.name}.save\nLoaded parameters: {hero_paras}")

    def battle(self, enemy):
        # slot content
        inventory = {'Hero Attack':45, 'Enemy Attack':35, 'HP':10, 'Gold':10}# slot contents
        slot_battle = Slot(list(inventory.keys()), list(inventory.values()))
        while True:
            enemy.print_status()
            hero1.print_status()
            ans = input("B: battle\nE: back to home\n> ")
            if ans == "E" or ans == "e":
                # back to home
                print("Welcome back!")
                self.play()
                break
            elif ans == "B" or ans == "b":
                # battle
                slot_battle_results = slot_battle.run()
                print(f"RESULT:\n\t[{slot_battle_results[0]}|{slot_battle_results[1]}|{slot_battle_results[2]}]")
                slot_battle_true_result = slot_battle.result(slot_battle_results)
                if 'Hero Attack' in slot_battle_true_result[0]:
                    enemy.hp -= hero1.atk * slot_battle_true_result[1]
                    if enemy.hp <= 0:
                        print(f"You have defeated {enemy.name}!")
                        # get enemy's gold
                        self.due(enemy.gold, enemy.level, enemy.floor)
                        break
                    continue
                elif 'Enemy Attack' in slot_battle_true_result[0]:
                    hero1.hp -= enemy.atk * slot_battle_true_result[1]
                    if hero1.hp <= 0:
                        print(f"You have been defeated by {enemy.name}!")
                        exit(0)
                    continue
                else:
                    hero1.update(slot_battle_true_result)
                    continue
                continue
            else:
                print("Wrong Input!")
                continue
        
    def due(self, gold, level, floor):
        if floor == 9:
            if level == 1:
                print("The Hero rescued his daughter")
            elif level == 2:
                print("The Hero fell in combat during his quest")
            elif level == 3:
                print("The new master released")
        if level == 'boss' and floor == hero1.unlock_num:
            hero1.unlock_num += 1
        inventory = {gold:4, gold*2:2, gold*4:1}# slot contents
        slot_due = Slot(list(inventory.keys()), list(inventory.values()))
        slot_due_results = slot_due.run()
        print(f"RESULT:\n\t[{slot_due_results[0]}|{slot_due_results[1]}|{slot_due_results[2]}]")
        slot_due_true_result = slot_due.result(slot_due_results)
        # change status of hero and print
        hero1.gold += slot_due_true_result[0][0]*slot_due_true_result[1]
        hero1.print_status()
        self.save()
        self.enter('home')

    def boss_battle(self):
        print("You have made your best to get the top of the tower!\nThere are 3 doors in front of you:\n\t1: Thorn Lady\n\t2: Elder One\n\t3: Tower Master")
        ans = int(input("Which one do you take?> "))
        boss = enemies.Enemy(enemies.enemy_9[ans], ans, 9, 500, 100, 1000)
        self.battle(boss)

    def enter(self, scene_name):
        if scene_name == 'tower':
            # generate random enemy
            print("The floors you can go:")
            for i in range(hero1.unlock_num):
                print(f"\t{i+1}: {enemies.floor_name[i+1]}")
            ans_floor = int(input('Which floor would you like to go?> '))
            if ans_floor <= 8:
                enemy_list = enemies.enemy_floor(ans_floor)
                print(enemy_list)
                enemy_level = random.choices(['small','middle','large','boss'],[27,27,27,19])
                print(enemy_level)
                enemy_name = enemy_list[enemy_level[0]]
                print(enemy_name)
                enemy_para = enemies.enemy_status(enemy_name)
                print(enemy_para)
                global enemy_temp
                enemy_temp = enemies.Enemy(enemy_name,enemy_level[0],ans_floor,enemy_para[0],enemy_para[1],enemy_para[2])
                print(f"You have encounter a enemy named {enemy_name}.")
                # battle loop
                self.battle(enemy_temp)
            elif ans_floor == 9:
                self.boss_battle()
        elif scene_name == 'store':
            inventory = {'HP':60, 'MaxHP':20, 'ATK':20}# slot contents
            slot_store = Slot(list(inventory.keys()), list(inventory.values()))
            print("Welcome!! Our HERO!!\nAnd good luck!")
            hero1.print_status()
            print("Tips: Pay 10 gold, and you can get more HP/MaxHP/ATK")
            while True:
                ans = input("E: back to home\nS: save\nP: pay 10 gold\n> ")
                if ans == "E" or ans == "e":
                    # back to home
                    self.enter('home')
                    break
                elif ans == "S" or ans == "s":
                    # save the status
                    self.save()
                    continue
                elif ans == "P" or ans == "p":
                    # pay 10 gold
                    if hero1.pay(10):
                        # slot result and print
                        slot_store_results = slot_store.run()
                        print(f"RESULT:\n\t[{slot_store_results[0]}|{slot_store_results[1]}|{slot_store_results[2]}]")
                        slot_store_true_result = slot_store.result(slot_store_results)
                        # change status of hero and print
                        hero1.update(slot_store_true_result)
                    continue
                else:
                    print("Wrong Input!")
                    continue
        elif scene_name == 'home':
            print("Welcome home!")
            self.play()


engine = Engine()
engine.initialize()
engine.play()