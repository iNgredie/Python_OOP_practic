"""
Написать логгирующий декоратор log_decorator, который будет логгировать
вызов функции. До выполнения функции необходимо вывести в консоль строку
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}". А после вывести
строку "Выполнено {func.__name__}".

Написать логгирующий метакласс LogMeta, который ко всем методам класса добавляет
функционал декоратора log_decorator.
"""
from abc import ABC


def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f'{func.__name__} с args: {args} и kwargs: {kwargs}')
        print(f'Выполненно {func.__name__}')
        return func()
    return wrapper


@log_decorator
class LogMeta(metaclass=ABC):
    pass
