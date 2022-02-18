"""
Описать класс Warrior:

- атрибут name - имя юнита (тип str)
- атрибут health_points - показатель здоровья (тип int от 0 до 100)
- магический метод __init__, который принимает аргумент name и создает юнита со
  100 health_points
- метод hit, который принимает аргумент other типа Warrior. Если значение
 health_points у other <= 0 бросить исключение ValueError("Второй воин мертв").
 Если нет, то снять у other 20 health_points и вывести на экран сообщение
 "{self.name} атаковал {other.name}. У {other.name} {other.health_points} HP"

Описать класс Arena:

- атрибут warriors - все воины на арене (тип list)
- магический метод __init__, который принимает необязательный аргумент warriors.
 Если был передан список warriors, та заполняет им атрибут. Если нет, то заполняет
 пустым списком.
- метод add_warrior, который принимает аргумент warrior и добавляет его к warriors.
 Если данный воин уже есть в списке, то бросить исключение ValueError("Воин уже на арене").
 Если нет, то добавить воина к списку warriors и вывести сообщение на экран
 "{warrior.name} участвует в битве"
- метод choose_warrior, который не принимает аргументов и возвращает случайного
  воина из warriors
- метод battle, который не принимает аргументов и симулирует битву. Сперва
 должна пройти проверка, что воинов на арене больше 1. Если меньше, то бросить
 исключение ValueError("Количество воинов на арене должно быть больше 1").
 Битва продолжается, пока на арене не останется только один воин. Сперва
 в случайном порядке выбираются атакующий и защищающийся. Атакующий ударяет
 защищающегося. Если у защищающегося осталось 0 health_points, то удалить его
 из списка воинов и вывести на экран сообщение "{defender.name} пал в битве".
 Когда останется только один воин, то вывести сообщение "Победил воин: {winner.name}".
 Вернуть данного воина из метода battle.
"""
import random
from typing import List


class Warrior:

    name: str
    health_points: int

    def __init__(self, name: str):
        self.name = name
        self.health_points = 100

    def hit(self, other: 'Warrior'):
        if other.health_points <= 0:
            raise ValueError('Второй воин мертв')
        other.health_points -= 20
        print(f'{self.name} атакавал {other.name}. У {other.name} {other.health_points} HP')


class Arena:

    warriors: List[Warrior]

    def __init__(self, warriors: List[Warrior] = None):
        self.warriors = warriors if warriors else []

    def add_warriors(self, warrior: Warrior):
        if warrior in self.warriors:
            raise ValueError('Воин уже на арене')

        self.warriors.append(warrior)
        print(f'{warrior.name} участвует в битве')

    def choose_warrior(self):
        return random.choices(self.warriors, k=1)

    def battle(self):
        if len(self.warriors) < 2:
            raise ValueError('Количество воинов на арене должно быть больше 1')
        while len(self.warriors) != 1:
            warriors = self.warriors.copy()
            attacker, = random.choices(warriors, k=1)
            warriors.remove(attacker)
            defender, = random.choices(warriors, k=1)

            attacker.hit(defender)
            if defender.health_points == 0:
                self.warriors.remove(defender)
                print(f'{defender.name} пал в битве')
        winner = self.warriors.pop()
        print(f'Победил воин: {winner.name}')
        return winner


if __name__ == '__main__':
    w1 = Warrior('Коля1')
    w2 = Warrior('Коля2')
    w3 = Warrior('Коля3')
    w4 = Warrior('Коля4')
    w5 = Warrior('Коля5')
    w6 = Warrior('Коля6')
    w7 = Warrior('Коля7')
    w8 = Warrior('Коля8')
    warrior_list = [w1, w2, w3, w4, w5, w6, w7, w8]
    arena = Arena(warrior_list)
    winner = arena.battle()
