from tasks.medium.garden.gardener import Gardener
from tasks.medium.garden.tomato import Tomato
from tasks.medium.garden.tomato_bush import TomatoBush

if __name__ == '__main__':
    tomato_1 = Tomato(0)
    tomato_2 = Tomato(0)
    tomato_3 = Tomato(0)
    tomato_4 = Tomato(0)
    tomato_bush_1 = TomatoBush(tomato_1, tomato_2)
    tomato_bush_2 = TomatoBush(tomato_3, tomato_4)
    gardener = Gardener('Иван', tomato_bush_1, tomato_bush_2)
    gardener.harvest()
    gardener.work()
    gardener.work()
    gardener.work()
    number = sum(len(x) for x in gardener.harvest())
    print(f'Собранно {number} томата(ов)')