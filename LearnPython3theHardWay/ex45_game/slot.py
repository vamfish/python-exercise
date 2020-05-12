import random

class Slot(object):

    def __init__(self, slot_things, weight):
        self.slot_things = slot_things
        self.weight = weight

    def run(self):
        return (random.choices(self.slot_things, self.weight), random.choices(self.slot_things, self.weight), random.choices(self.slot_things, self.weight))