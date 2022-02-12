"""
Описать абстрактный класс Animal у которого:

- атрибут name - кличка (тип str)
- магический метод __init__, который принимает аргумент name
- абстрактный метод says, который не принимает аргументов

На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод
says таким образом, чтобы он возвращал строку вида:

- "{кличка} - кошка. Говорит МЯУ!" для класса Cat
- "{кличка} - собака. Говорит ГАВ!" для класса Dog
- "{кличка} - корова. Говорит МУ!" для класса Cow
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    name: str

    @abstractmethod
    def __init__(self, name: str) -> None:
        pass

    @abstractmethod
    def says(self) -> None:
        pass


class Cat(Animal):
    name: str

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.name = name

    def says(self) -> None:
        print(f'{self.name} - кошка. Говорит МЯУ!')


class Dog(Animal):
    name: str

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.name = name

    def says(self) -> None:
        print(f'{self.name} - собака. Говорит ГАВ!')


class Cow(Animal):
    name: str

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.name = name

    def says(self) -> None:
        print(f'{self.name} - корова. Говорит МУ!')
