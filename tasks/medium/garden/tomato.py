from typing import Tuple


class Tomato:

    index: int
    ripeness: str
    states: Tuple[str] = ('Отсутствует', 'Цветение', 'Зеленый', 'Красный')

    def __init__(self, index: int):
        self.index = index
        self.ripeness = self.states[0]

    def grow(self):
        if self.ripeness != self.states[-1]:
            self.index += 1
            self.ripeness = self.states[self.index]

    def is_ripe(self) -> bool:
        return self.ripeness == self.states[-1]



