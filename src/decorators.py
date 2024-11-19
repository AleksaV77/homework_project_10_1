import logging
from functools import wraps
from typing import Any, Callable

logging.basicConfig(level=logging.INFO, filename='mylog.txt', filemode='w')


def log(filename: Any = None) -> Callable:
    """Декоратор, который логирует начало и конец выполнения функции и результаты или возникшие ошибки."""
    def my_decorator(func: Any) -> Any:
        @wraps(func)
        def timer(*args: int, **kwargs: int) -> Any:
            if filename:
                try:
                    result = func(*args, **kwargs)
                    if result == sum(args):
                        with open(filename, "w") as file:
                            file.write(f"{func.__name__} ok")
                except BaseException as err:
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(f'{func.__name__} error: {err.__class__.__name__}. Inputs:{args}, {kwargs}')
                    raise BaseException(f"{func.__name__} error: {err.__class__.__name__}. Inputs:{args}, {kwargs}")
            else:
                try:
                    result = func(*args, **kwargs)
                    if result == sum(args):
                        print(f"{func.__name__} ok")
                except BaseException as err:
                    raise BaseException(f"{func.__name__} error: {err.__class__.__name__}. Inputs:{args}, {kwargs}")
            return result
        return timer
    return my_decorator


@log(filename='mylog.txt')
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)
