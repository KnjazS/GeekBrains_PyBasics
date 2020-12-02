#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from typing import Callable, Any, Iterable

# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию
# type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
# а указать явно, в программе.
type_expr = {str: "string",             int: "integer",             float: "real number",
             complex: "complex number", type(None): "None",         bool: "boolean",
             tuple: "tuple",            range: "range",             dict: "dictionary",
             list: "list",              set: "set",                 frozenset: "frozen set",
             bytes: "bytes",            bytearray: "array of byte", memoryview: "memory view"}


def case_1():
    elem_list = [1, None, 'string', 1., True, ()]
    for idx, elem in enumerate(elem_list):
        try:
            print(f"Element №{idx} is {type_expr[type(elem)]}")
        except KeyError:
            print(f"Element №{idx} is {type(elem)} (not builtin)")


# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
# элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
# сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().
def swap_elem(input_list: Iterable[Any]) -> Iterable[Any]:
    if not type(input_list) is list:
        raise ValueError()
    idx = 0
    while idx * 2 + 1 < len(input_list):
        input_list[idx * 2], input_list[idx * 2 + 1] = input_list[idx * 2 + 1], input_list[idx * 2]
        idx += 1
    return input_list


def sanitized_input(invite_message: str, error_message: str, translate: Callable[[str], Any] = int) -> Any:
    while True:
        try:
            return translate(input(invite_message))
        except EOFError as e:
            raise e
        except:
            print(error_message)


def case_2():
    count = sanitized_input("Введите кол-во элементов списка --> ",
                            "Так. Повторим. КОЛИЧЕСТВО. Это число")
    values = []
    for idx in range(count):
        values.append(input(f"Введите элемент №{idx} --> "))
    values = swap_elem(values)
    print("После замены элементов местами получис такой список:")
    for idx in range(count):
        print(values[idx])


# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому
# времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
def input_to_month(value: str) -> int:
    value = int(value)
    if 1 <= value <= 12:
        return value
    raise ValueError()


seasons_dict = {12: "зима", 1: "зима", 2: "зима",
                3: "весна", 4: "весна", 5: "весна",
                6: "лето", 7: "лето", 8: "лето",
                9: "осень", 10: "осень", 11: "осень"}

seasons_list = ["зима", "зима", "весна",
                "весна", "весна", "лето",
                "лето", "лето", "осень",
                "осень", "осень", "зима"]


def case_3():
    month = sanitized_input("Введите номер месяца --> ",
                            "Номер месяца - это число от 1 до 12",
                            input_to_month)
    # Вариант с использованием list
    print(f"Это {seasons_list[month - 1]}.")
    # Вариант с использованием dict
    print(f"Это {seasons_dict[month]}.")


# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
def case_4():
    words = input("Введите слова через пробел --> ")
    words = words.split(" ")
    for idx, line in enumerate(words):
        if len(line) > 10:
            print(f"{idx}: {line[:10]}...")
        else:
            print(f"{idx}: {line}")


# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы
# с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
class Rating:
    __iter_idx__ = None
    __rates__ = None

    def __init__(self):
        self.__rates__ = []

    def __str__(self):
        return self.__rates__.__str__()

    def __len__(self):
        return len(self.__rates__)

    def __getitem__(self, item):
        return self.__rates__[item]

    def __iter__(self):
        self.__iter_idx__ = 0
        return self

    def __next__(self):
        if self.__iter_idx__ < len(self.__rates__):
            self.__iter_idx__ += 1
            return self.__rates__[self.__iter_idx__ - 1]
        raise StopIteration()

    def append(self, value: int):
        if not type(value) is int:
            raise ValueError()
        idx = 0
        while idx < len(self.__rates__):
            if value > self.__rates__[idx]:
                break
            idx += 1
        self.__rates__.insert(idx, value)


def trans_natural(value: str) -> int:
    value = int(value)
    if value < 1:
        raise ValueError()
    return value


def case_5():
    rate = Rating()
    rate_count = sanitized_input("Введите количество элементов рейтинга --> ",
                                 "Это должно быть натуральное число (1 и больше)",
                                 trans_natural)
    for idx in range(rate_count):
        cur_rate = sanitized_input(f"Введите рейтинг №{idx+1} --> ",
                                   "Это должно быть натуральное число (1 и больше)",
                                   trans_natural)
        rate.append(cur_rate)
    print("Итог:", rate)


# 6. *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара
# и словарь с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
def trans_price(value: str) -> float:
    value = float(value)
    if value < 0:
        raise ValueError()
    return value


class Goods(object):
    __goods__ = None
    __idx__ = None
    __analytics__ = None

    class AnalyticDict(object):
        __parent__ = None

        def __init__(self, parent):
            self.__parent__ = parent

        def __getitem__(self, item):
            result = set()
            for good in self.__parent__.__goods__:
                result.add(good[1][item])
            return list(result)

        def __str__(self):
            result = "{"
            for key in ["Название", "Цена", "Ед.", "Количество"]:
                result += f"\n{key}: {self[key]}"
            result += "\n}"
            return result

    def __init__(self):
        self.__goods__ = []
        self.__analytics__ = Goods.AnalyticDict(self)

    def __getitem__(self, item):
        return self.__goods__[item]

    def __iter__(self):
        self.__idx__ = 0
        return self

    def __next__(self):
        self.__idx__ += 1
        if self.__idx__ == len(self.__goods__):
            raise StopIteration()
        return self.__goods__[self.__idx__ - 1]

    def __str__(self):
        return str(self.__goods__)

    def add(self):
        name = sanitized_input("Введите название товара --> ",
                               "",
                               str)
        price = sanitized_input("Введите цену товара --> ",
                                "Это должно быть действительное число больше 0",
                                trans_price)
        unit = sanitized_input("Введите единицу измерения товара --> ",
                               "",
                               str)
        count = sanitized_input("Введите количество товара --> ",
                                "",
                                trans_price)
        self.__goods__.append((len(self.__goods__) + 1, {"Название": name,
                                                         "Цена": price,
                                                         "Ед.": unit,
                                                         "Количество": count})
                              )

    def analyse(self):
        return self.__analytics__


def case_6():
    goods_count = sanitized_input("Введите количество товаров --> ",
                                  "Это должно быть натуральное число (1 и больше)",
                                  trans_natural)
    goods = Goods()
    for idx in range(goods_count):
        print(f"Товар №{idx+1}:")
        goods.add()
    print(goods.analyse())


if __name__ == "__main__":
    print("\nЗадание 1:\n")
    case_1()
    print("\nЗадание 2:\n")
    case_2()
    print("\nЗадание 3:\n")
    case_3()
    print("\nЗадание 4:\n")
    case_4()
    print("\nЗадание 5:\n")
    case_5()
    print("\nЗадание 6*:\n")
    case_6()
