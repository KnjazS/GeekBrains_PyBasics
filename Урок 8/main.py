#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from abc import ABC, abstractmethod

# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
# месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
# числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
class Date(object):
    __day: int
    __month: int
    __year: int

    __days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    def __init__(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Date can be initialized only with str value")

        day, month, year = Date.extract_parts(value)
        if Date.validate(day, month, year):
            self.__day = day
            self.__month = month
            self.__year = year
        else:
            raise ValueError("Such date is not correct")

    @classmethod
    def extract_parts(cls, value: str) -> tuple[int, int, int]:
        value = value.split("-")
        if len(value) != 3:
            raise ValueError("Error when parsing string to construct date value.")
        try:
            day = int(value[0])
            month = int(value[1])
            year = int(value[2])
        except ValueError:
            raise ValueError("Error when parsing string to construct date value.")
        return day, month, year

    @staticmethod
    def validate(day: int, month: int, year: int) -> bool:
        if year < 0:
            return False
        if month < 1 or month > 12:
            return False
        max_days = Date.__days_in_month[month]
        if month == 2 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
            max_days += 1
        if day > max_days or day < 1:
            return False
        return True

    def __str__(self) -> str:
        return f"{self.__day:02d}.{self.__month:02d}.{self.__year}"

    def __repr__(self) -> str:
        return self.__str__()


def case_1():
    # Проверим кучу неправильных вариантов
    for incorrect_value in ["0-1-2010", "1-0-2010", "29-2-2009", "32-1-2010", "1-13-2010", "31-04-2020"]:
        try:
            Date(incorrect_value)
        except ValueError:
            print(f"{incorrect_value} не обработано. Ошибка.")
        except TypeError:
            print(f"{incorrect_value} не обработано. Ошибка.")
    for correct_value in ["29-2-2000", "03-12-2020", "31-12-2020"]:
        print(f"Обработана дата {Date(correct_value)}")


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.
class MyZeroDivisionException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


def division(dividend: int, divider: int) -> float:
    if divider == 0:
        raise MyZeroDivisionException(f"Unable to divide: {dividend} / {divider} ")
    return dividend / divider


def case_2():
    try:
        x = division(5, 0)
    except MyZeroDivisionException as exc:
        print(f"Error detected: {exc}")


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список
# только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами выводится на
# экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем
# очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.
class NotNumbersOnlyException(Exception):
    def __init__(self, *args):
        super().__init__(*args)


def append(values: list[int], new_value: str):
    try:
        values.append(int(new_value))
    except ValueError as exc:
        raise NotNumbersOnlyException(exc.args)


def input_numbers(prompt: str, error_message: str) -> list[int]:
    result = []
    while True:
        values = input(prompt)
        values = values.split()
        for value in values:
            if value == "stop":
                return result
            try:
                append(result, value)
            except NotNumbersOnlyException:
                print(error_message.format(value))


def case_3():
    numbers = input_numbers("Введите числа (или stop для остановки ввода) --> ",
                            "Пропущено значение '{0}' - это не целое число.")
    print(f"Введены числа {numbers}")


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
class OfficeEquip(ABC):
    __name: str
    __space: int

    def __init__(self, name: str, space: int):
        if not isinstance(name, str):
            raise TypeError("name param must be str.")
        if not isinstance(space, int):
            raise TypeError("space param must be int.")
        self.__name = name
        self.__space = space

    @property
    @abstractmethod
    def space(self):
        return self.__space

    @property
    def name(self):
        return self.__name


class Warehouse(object):
    __spaces_max: int
    __spaces_used: int
    __stored: dict[int, OfficeEquip]
    __spaces: list[bool]
    __name: str

    def __init__(self, name: str, space_max: int):
        if not isinstance(name, str):
            raise TypeError("name param must be str.")
        if not isinstance(space_max, int):
            raise TypeError("space_max param must be integer.")
        self.__name = name
        self.__spaces_max = space_max
        self.__spaces_used = 0
        self.__stored = {}
        self.__spaces = [True for i in range(self.__spaces_max)]

    def store(self, unit: OfficeEquip) -> None:
        for idx in range(self.__spaces_max - unit.space):
            if self.__spaces[idx]:
                can_place_here = True
                for idx2 in range(1, unit.space):
                    if not self.__spaces[idx + idx2]:
                        can_place_here = False
                        break
                if can_place_here:
                    self.__stored[idx] = unit
                    self.__spaces_used += unit.space
                    for idx2 in range(unit.space):
                        self.__spaces[idx + idx2] = False
                    return
        raise ValueError("Unable to store item.")

    def take(self, place: int) -> OfficeEquip:
        try:
            value = self.__stored.pop(place)
        except KeyError:
            raise KeyError(f"Nothing stored at place {place} at warehouse \"{self.__name}\".")
        for idx in range(value.space):
            self.__spaces[place + idx] = True
        self.__spaces_used -= value.space
        return value

    def list(self) -> dict[int, OfficeEquip]:
        return self.__stored.copy()

    def __str__(self):
        return f"Склад {self.__name} ({self.__spaces_used}/{self.__spaces_max})"

    def print_used_space(self):
        for space in self.__spaces:
            print("_", end='') if space else print("*", end="")
        print("")


class PC(OfficeEquip):
    def __init__(self, name, space):
        super().__init__(name, space)

    @property
    def space(self):
        return super().space

    def __str__(self):
        return f"Компьютер {super().name}"

    def __repr__(self):
        return self.__str__()


class Printer(OfficeEquip):
    def __init__(self, name, space):
        super().__init__(name, space)

    @property
    def space(self):
        return super().space

    def __str__(self):
        return f"Принтер {super().name}"

    def __repr__(self):
        return self.__str__()


class Scanner(OfficeEquip):
    def __init__(self, name, space):
        super().__init__(name, space)

    @property
    def space(self):
        return super().space

    def __str__(self):
        return f"Сканер {super().name}"

    def __repr__(self):
        return self.__str__()


class MultiFunctionalDevice(OfficeEquip):
    def __init__(self, name, space):
        super().__init__(name, space)

    @property
    def space(self):
        return super().space

    def __str__(self):
        return f"МФУ {super().name}"

    def __repr__(self):
        return self.__str__()


class Unit(object):
    __name: str
    __equip: list[OfficeEquip]

    def __init__(self, name: str):
        if not isinstance(name, str):
            raise TypeError("Name of the unit must be str.")
        self.__name = name
        self.__equip = []

    def __str__(self):
        return f"Подразделение {self.__name}. Снабжено {len(self.__equip)} единицами техники."

    def take_from_warehouse(self, warehouse: Warehouse, place: int):
        if not isinstance(warehouse, Warehouse):
            raise TypeError("warehouse param must be instance of Warehouse class.")
        if not isinstance(place, int):
            raise TypeError("place param must be int.")
        self.__equip.append(warehouse.take(place))

    @property
    def equipment(self):
        return str(self.__equip)[1:-1]


def case_4_6():
    new_warehouse = Warehouse("Главный", 50)
    print(f"{new_warehouse} открыт.")
    print("Начата загрузка склада.")
    load = [PC("HP Elite 7300", 2),
            PC("HP Elite 7500", 2),
            PC("HP Elite 7500", 2),
            Printer("HP LaserJet Pro M402", 1),
            Printer("HP LaserJet Pro M402", 1),
            MultiFunctionalDevice("HP LaserJet M28w", 1)]
    for comp in load:
        new_warehouse.store(comp)
    print(f"Загружено 3 компьютера, 2 принтера и МФУ. {new_warehouse}\nЗагрузка склада: ", end="")
    new_warehouse.print_used_space()
    unit = Unit("Отдел кадров")
    unit.take_from_warehouse(new_warehouse, 0)
    print(f"Отдел кадров забрали 1 компьютер из {new_warehouse}\nЗагрузка склада: ", end="")
    new_warehouse.print_used_space()
    load = [Printer("HP LaserJet Pro M402", 1),
            Printer("HP LaserJet Pro M402", 1)]
    for comp in load:
        new_warehouse.store(comp)
    print(f"Загружено ещё 2 принтера. {new_warehouse}\nЗагрузка склада: ", end="")
    new_warehouse.print_used_space()
    unit.take_from_warehouse(new_warehouse, 2)
    print(f"Отдел кадров забрали ещё 1 компьютер из {new_warehouse}\nЗагрузка склада: ", end="")
    new_warehouse.print_used_space()
    print(f"Теперь об отделе кадров\n{unit}")
    print(f"Он снабжен: {unit.equipment}")


if __name__ == "__main__":
    # print("Задание 1:\n")
    # case_1()
    # print("\nЗадание 2:\n")
    # case_2()
    # print("\nЗадание 3:\n")
    # case_3()
    print("\nЗадание 4-6:\n")
    case_4_6()
