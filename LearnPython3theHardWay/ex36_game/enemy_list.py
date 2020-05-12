floor_name = {1:"The Root", 2:"The Gate", 3:"The Eyes", 4:"The Spine", 5:"The Melt", 6:"The Heart", 7:"The Bridge", 8:"The Mouth", 9:"The Halo"}

enemy_1 = {"small":"Reaper", "middle":"Bone Reaper", "large":"Soul Reaper", "boss":"Great Reaper"}
enemy_2 = {"small":"Dr. Scraper", "middle":"Metal Scraper", "large":"Giant Scraper", "boss":"Great Scraper"}
enemy_3 = {"small":"Watcher", "middle":"Tower Watcher", "large":"Mind Watcher", "boss":"Great Watcher"}
enemy_4 = {"small":"Nuwa Herald", "middle":"Nuwa Envoy", "large":"Nuwa Elder", "boss":"Great Nuwa"}
enemy_5 = {"small":"Tar Crawler", "middle":"Tar Walker", "large":"Tar Grinner", "boss":"Tar Shadow"}
enemy_6 = {"small":"Drifter", "middle":"Wanderer", "large":"Meditator", "boss":"False Prophet"}
enemy_7 = {"small":"Pale Howler", "middle":"Pale Guard", "large":"Pale Wing", "boss":"Great Flyer"}
enemy_8 = {"small":"Spreader", "middle":"Swallower", "large":"Giant Eater", "boss":"Great Eater"}
# enemy_9 = {"small":"Reaper", "middle":"Bone Reaper", "large":"Soul Reaper", "boss":"Great Reaper"}

enemy_all = [enemy_1, enemy_2, enemy_3, enemy_4, enemy_5, enemy_6, enemy_7, enemy_8]

def enemy_list(floor):
    for i in range(8):
        if floor == i + 1:
            return enemy_all[i]


def enemy_para(name):
    for i in range(8):
        for key in ("small", "middle", "large", "boss"):
            if name == enemy_all[i][key]:
                return 20, 5, 30#需要设定每个敌人的属性