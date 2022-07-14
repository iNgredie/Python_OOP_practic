"""
Создать класс BookCard, в классе должны быть:

- private атрибут author - автор (тип str)
- private атрибут title - название книги (тип str)
- private атрибут year - год издания (тип int)
- магический метод __init__, который принимает author, title, year
- магические методы сравнения для сортировки книг по году издания
- сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
  на тип данных, если тип данных не подходит, то бросить ValueError. Для года
  издания дополнительно проверить на валидность (> 0, <= текущего года).

Аксессоры реализоваться через property.
"""
from datetime import date

CURRENT_YEAR = date.today().year


class BookCard:

    def __init__(self, author: str, tittle: str, year: int):
        self.author = author
        self.title = tittle
        self.year = year

    def __eq__(self, other):
        return self.__year == other.year

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise ValueError('Author variable must contain only string values')

        self.__author = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError('Title variable must contain only string values')

        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value: int):
        if not isinstance(value, int):
            raise ValueError('Year variable must contain only integer values')

        if value < 1:
            raise ValueError('Year must be greater than 0')

        if value > CURRENT_YEAR:
            raise ValueError('Year must be greater than current year')

        self.__year = value
