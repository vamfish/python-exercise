import random
import os
import sys

from hero import Hero

class Engine(object):

    def __init__(self):
        pass
    
    def play(self):
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
                # self.enter('store')
                print("B")
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
        pass

engine = Engine()
engine.play()