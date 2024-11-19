import pytest
import tempfile
from src.decorators import log


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y


my_function(1, 2)


def test_log_ok_console(capsys):
    """Тест - вывод успешного выполнения функции в консоль"""

    @log()
    def func(x, y):
        return x + y

    func(1, 2)
    captured = capsys.readouterr()
    assert captured.out == f"{func.__name__} ok\n"


def test_log_ok_txt(capsys):
    """Тест - вывод успешного выполнения функции в файл"""
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        log_file_path = tmp_file.name

    @log(filename=log_file_path)
    def func(x, y):
        return x + y

    func(1, 2)
    with open(log_file_path, "r", encoding="utf-8") as file:
        logs = file.read()
    assert f"{func.__name__} ok" in logs


def test_log_console(capsys):
    """Тест - вывод успешного выполнения функции в консоль"""

    @log()
    def func(x: int, y: int):
        return x + y

    result = func(1, 3)
    assert result == 4


def test_log_txt(capsys):
    """Тест - вывод успешного выполнения функции в файл"""

    @log(filename="mylog.txt")
    def func(x: int, y: int):
        return x + y

    result = func(1, 3)
    assert result == 4


def test_my_func_log_console():
    """Тест - вывод ошибки в консоль"""
    with pytest.raises(BaseException):
        my_function("1", "3") == "my_function error: TypeError. Inputs:('1', '3'), {}"


def test_my_func_log_console_2():
    """Тест - вывод ошибки в консоль"""
    with pytest.raises(BaseException):
        my_function(1, "3") == "my_function error: TypeError. Inputs:(1, '3'), {}"
