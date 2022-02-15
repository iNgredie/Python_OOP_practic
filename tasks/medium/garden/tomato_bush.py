from typing import List

from tasks.medium.garden.tomato import Tomato


class TomatoBush:

    tomato_list: List[Tomato]

    def __init__(self, *args):
        self.tomato_list = list(args)

    def grow_all(self):
        [tomato.grow() for tomato in self.tomato_list]

    def all_are_ripe(self):
        return all(
            [tomato.is_ripe() for tomato in self.tomato_list]
        )

    def give_away_all(self) -> List[Tomato]:
        result = self.tomato_list[:]
        self.tomato_list = []
        return result

