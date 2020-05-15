import random
import os
import sys

from hero import Hero
from slot import Slot

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
                # self.enter('tower')
                print("E")
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

    def enter(self, scene_name):
        if scene_name == 'tower':
            pass
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