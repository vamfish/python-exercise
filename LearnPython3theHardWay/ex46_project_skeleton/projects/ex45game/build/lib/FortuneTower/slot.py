import random

class Slot(object):

    def __init__(self, slot_things, weight):
        self.slot_things = slot_things
        self.weight = weight

    def run(self):
        return (random.choices(self.slot_things, self.weight), random.choices(self.slot_things, self.weight), random.choices(self.slot_things, self.weight))

    def result(self, run_returned):
        a, b, c = run_returned
        times = 1
        if b == a:
            if c == a:
                times = 5
            else:
                times = 2
        return (a, times)