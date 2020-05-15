floor_name = {1:"The Root", 2:"The Gate", 3:"The Eyes", 4:"The Spine", 5:"The Melt", 6:"The Heart", 7:"The Bridge", 8:"The Mouth", 9:"The Halo"}

enemy_1 = {"small":"Reaper", "middle":"Bone Reaper", "large":"Soul Reaper", "boss":"Great Reaper"}
enemy_2 = {"small":"Dr. Scraper", "middle":"Metal Scraper", "large":"Giant Scraper", "boss":"Great Scraper"}
enemy_3 = {"small":"Watcher", "middle":"Tower Watcher", "large":"Mind Watcher", "boss":"Great Watcher"}
enemy_4 = {"small":"Nuwa Herald", "middle":"Nuwa Envoy", "large":"Nuwa Elder", "boss":"Great Nuwa"}
enemy_5 = {"small":"Tar Crawler", "middle":"Tar Walker", "large":"Tar Grinner", "boss":"Tar Shadow"}
enemy_6 = {"small":"Drifter", "middle":"Wanderer", "large":"Meditator", "boss":"False Prophet"}
enemy_7 = {"small":"Pale Howler", "middle":"Pale Guard", "large":"Pale Wing", "boss":"Great Flyer"}
enemy_8 = {"small":"Spreader", "middle":"Swallower", "large":"Giant Eater", "boss":"Great Eater"}
enemy_9 = {1:"Thorn Lady", 2:"Elder One", 3:"Tower Master"}

enemy_all = [enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6, enemy_7, enemy_8]

def enemy_floor(floor):
    for i in range(8):
        if floor == i + 1:
            return enemy_all[i] # get the enemy dict for floor #i


def enemy_status(name):# return the parameters corresponding to the name
    for i in range(8):
        if name == enemy_all[i]["small"]:
            return (5*(i+1)*1, (i+1)*1, 10*(i+1)*1)
        elif name == enemy_all[i]["middle"]:
            return (5*(i+1)*2, (i+1)*2, 10*(i+1)*2)
        elif name == enemy_all[i]["large"]:
            return (5*(i+1)*3, (i+1)*3, 10*(i+1)*3)
        elif name == enemy_all[i]["boss"]:
            return (5*(i+1)*5, (i+1)*5, 10*(i+1)*5)

class Enemy(object):

    def __init__(self, name, level, floor, hp, atk, gold):
        self.name = name
        self.level = level
        self.floor = floor
        self.hp = hp
        self.atk = atk
        self.gold = gold
        pass

    def print_status(self):
        print(f"\tHP: {self.hp}\n\tATK: {self.atk}\n\tGold: {self.gold}\n")
