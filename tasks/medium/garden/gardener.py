from typing import List

from tasks.medium.garden.tomato_bush import TomatoBush


class Gardener:

    name: str
    plants: List[TomatoBush]

    def __init__(self, name: str, *args):
        self.name = name
        self.plants = list(args)

    def work(self):
        [plant.grow_all() for plant in self.plants]

    def harvest(self):
        if all([plant.all_are_ripe() for plant in self.plants]):
            return [plant.give_away_all() for plant in self.plants]
        print('Томаты не созрели')

