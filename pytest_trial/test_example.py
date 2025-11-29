import pytest


def division(dividend, divisor):
    return dividend / divisor

def get_sort_list(string):
    # Сортировка и пробел после запятой в аргументе.
    new_list = sorted(string.split(', '))  
    return new_list

def test_zero_division():
    with pytest.raises(ZeroDivisionError):  # Ожидается ошибка деления на 0.
        # При вызове функции с такими аргументами возникнет ошибка.
        result = division(1, 0)

def test_sort():
    """Тестируем функцию get_sort_list()."""
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert result  == ['Даша', 'Маша', 'Саша', 'Яша']  # 'Маша', а не 'Миша'. 