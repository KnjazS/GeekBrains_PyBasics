#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from typing import Callable, Any, List, Iterable
from os import path, lstat
from random import randint
from io import SEEK_END
from json import dump
ERROR_INVALID_NAME = 123


def sanitized_input(invite_message: str, error_message: str, translate: Callable[[str], Any]) -> Any:
    """
    Function filtering input. It try to read string from STDIN and translate it with "translate" param function

    :param invite_message: prompt message printing to STDOUT before reading input without trailing newline
    :param error_message: message printing to STDOUT if translate function raises exception
    :param translate: function for translating string from stdin. Have to raise anything if it is needed to ask for
    values until right one will be entered
    :return: value returned by translate function param
    :raises: EOFError: if user hits EOF
    """
    while True:
        # noinspection PyBroadException
        try:
            return translate(input(invite_message))
        except EOFError as e:
            raise e
        except Exception:
            print(error_message)


# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании
# ввода данных свидетельствует пустая строка.
def filename_check(value: str) -> str:
    """
    Checking filename is correct. Works only in Windows.

    :param value: filename (can be absolute or relative)
    :return: filename if it is correct
    :raises OSError: if filename is invalid
    """
    try:
        lstat(value)
    except OSError as exc:
        if hasattr(exc, 'winerror') and exc.winerror == ERROR_INVALID_NAME:
            raise exc
    return value


def case_1():
    filename = sanitized_input("Введите имя файла для записи (Расширение будет добавлено автоматически)\
                               \r\n(Если файл создан, то он будет дозаписан) --> ",
                               "Странное имя файла.",
                               filename_check)
    filename = filename+".txt"
    if path.exists(filename):
        mode = "at"
    else:
        mode = "wt"

    with open(filename, mode, encoding="UTF-8") as f_obj:
        print("А теперь введите что-то для записи в файл. Для окончания записи введите пустую строку.")
        while True:
            line = input()
            if line == "":
                break
            print(line, file=f_obj)
    print("Всё записано в файл", filename)


# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.
def case_2():
    lines_count = 0
    words_count = 0
    with open("case2_file.txt", "w+t", encoding="UTF-8") as f_obj:
        f_obj.writelines(["line1\n", "line2\n", "line3 line4 line5"])
        eof_point = f_obj.tell()
        f_obj.seek(0)
        while f_obj.tell() < eof_point:
            try:
                line = f_obj.readline()
            except EOFError:
                break
            lines_count += 1
            words_count += len(line.split())
            print(f"В строке {lines_count} {words_count} слов.")
        print(f"В файле всего {lines_count} строк")


# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10
# строк). Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет
# средней величины дохода сотрудников.
def case_3():
    with open("case3_file.txt", "w+t", encoding="UTF-8") as f_obj:
        [print(f"worker_{idx} {randint(1000000, 5000000) / 100}", file=f_obj) for idx in range(randint(10, 20))]
        print("Файл case3_file.txt сгенерирован случайным образом")
        eof_point = f_obj.tell()
        f_obj.seek(0)
        lines_count = 0
        salary_sum = 0
        while f_obj.tell() < eof_point:
            line = f_obj.readline()
            lines_count += 1
            line = line.split()
            line[1] = float(line[1])
            salary_sum += line[1]
            if line[1] < 20000:
                print(line[0])
        print(f"Средний оклад равен {salary_sum / lines_count:.2f}")


# 4. Создать (не программно) текстовый файл со следующим содержимым. Необходимо написать программу, открывающую файл на
# чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк
# должен записываться в новый текстовый файл.
numeral_trans = {"One": "Один",         "Two": "Два",           "Three": "Три",
                 "Four": "Четыре",      "Five": "Пять",         "Six": "Шесть",
                 "Seven": "Семь",       "Eight": "Восемь",      "Nine": "Девять"}


def case_4():
    with open("case4_file1.txt", "wt", encoding="UTF-8") as f_obj:
        for numeral, name in enumerate(numeral_trans.keys(), 1):
            print(f"{name} - {numeral}", file=f_obj)
    print("Файл case4_file1.txt сгенерирован")
    input_f_obj = open("case4_file1.txt", "rt", encoding="UTF-8")
    output_f_obj = open("case4_file2.txt", "wt", encoding="UTF-8")

    eof_point = input_f_obj.seek(0, SEEK_END)
    input_f_obj.seek(0)

    while input_f_obj.tell() < eof_point:
        line = input_f_obj.readline()
        line = line[:-1]
        line = line.split(" - ")
        line[0] = numeral_trans[line[0]]
        print(f"{line[0]} - {line[1]}", file=output_f_obj)

    input_f_obj.close()
    output_f_obj.close()
    print("Файл case4_file2.txt успешно транлирован")


# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа
# должна подсчитывать сумму чисел в файле и выводить ее на экран.
def case_5():
    print("Введите числа через пробел. Если число невозможно преобразовать оно будет пропущено")
    line = input("--> ")
    line = line.split()
    result = 0
    with open("case5_file.txt", "wt", encoding="UTF-8") as f_obj:
        for number in line:
            try:
                number = float(number)
                result += number
                print(number, end=" ", file=f_obj)
            except ValueError:
                continue
    print("Все записано в файл case5_file.txt. Сумма чисел равна", result)


# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести словарь на экран.
def case_6():
    with open("case6_file1.txt", "wt", encoding="UTF-8") as f_obj:
        print("""Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —""", file=f_obj)
    print("Файл case6_file1.txt сгенерирован")

    subjects = {}
    with open("case6_file1.txt", "rt", encoding="UTF-8") as f_obj:      # Читается код сложно, простите
        eof_point = f_obj.seek(0, SEEK_END)
        f_obj.seek(0)
        while f_obj.tell() < eof_point:
            line = f_obj.readline()
            line = line.split()
            subjects[line[0][:-1]] = 0
            for part in line[1:]:
                subj_parts = part.split("(")
                if len(subj_parts) < 2:
                    continue
                subjects[line[0][:-1]] += int(subj_parts[0])
    print(subjects)


# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о
# фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
# убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
class Firm(object):
    """
    This class realises firm entity for case 7 of the homework for lesson 5.
    """
    name = None
    form = None
    profit = 0
    costs = 0

    def __init__(self, name_value: str, form_value: str, profit_value: float, costs_value: float):
        """
        Init function for class

        :param name_value: Name of the firm. Must be str.
        :param form_value: Organisation form of the firm. Must be str.
        :param profit_value: Profit of the firm in current year. Must be float.
        :param costs_value: Costs of the firm. Must be float.
        :raises ValueError: if form_value is wrong organization form or if profit is negative number
        """
        self.name = name_value
        if form_value not in ["ООО", "АО", "ФГУП", "ПАО", "НАО", "ИП"]:
            raise ValueError(f"{form_value} is wrong organization form")
        self.form_value = form_value
        if profit_value < 0:
            raise ValueError("Profit can't be negative.")
        self.profit = profit_value
        self.costs = costs_value

    @staticmethod
    def parse(value: str) -> 'Firm':
        """
        Parsing string with params separated by whitespaces

        :param value: string to parse
        :return: new instance of class Firm
        :raises ValueError: if string contains not enough params to create instance of Firm
        """
        value = value.split()
        if len(value) < 4:
            raise ValueError("Not enough arguments in string.")
        return Firm(value[0], value[1], float(value[2]), float(value[3]))


def count(values: Iterable[Any], predicate: Callable[[Any], bool]) -> int:
    """
    Function counts items of list values which return true in predicate

    :param values: list to count
    :param predicate: function which return true or false with item of list values as param
    :return: count of items
    """
    result = 0
    for value in values:
        if predicate(value):
            result += 1
    return result


def serialize_firms(values: List[Firm], filename: str) -> None:
    """
    Function serialises list of Firm and write it to file

    :param values: list of Firm class instances
    :param filename: Name of json files
    :raises ValueError: if values contains not only Firm class instances
    :raises OSError: if filename is invalid
    """
    firms = {}
    average_profit = 0
    for firm in values:
        if not type(firm) is Firm:
            raise ValueError("In values must be only instances of firm.")
        firms[firm.name] = firm.profit - firm.costs
        if firm.profit - firm.costs > 0:
            average_profit += firm.profit - firm.costs
    average_profit = average_profit / count(firms.values(), lambda x: x > 0)
    with open(filename, "wt", encoding="UTF-8") as f_obj:
        dump([firms, {"average_profit": average_profit}], f_obj)


def case_7():
    with open("case7_file1.txt", "wt", encoding="UTF-8") as f_obj:
        f_obj.write("firm_0 ООО 10000 5000\n")
        [f_obj.write(f"firm_{idx} ООО {randint(500000, 2000000)/100:.2f} {randint(100000, 1000000)/100:.2f}\n")
         for idx in range(1, randint(5,10))]
    print("Файл с фирмами сгенерирован случайным образом. case7_file1.txt")

    firms = []
    with open("case7_file1.txt", "rt", encoding="UTF-8") as f_obj:
        eof_point = f_obj.seek(0, SEEK_END)
        f_obj.seek(0)
        while f_obj.tell() < eof_point:
            firms.append(Firm.parse(f_obj.readline()))
    serialize_firms(firms, "case7_file2.json")
    print("Итоговый файл с фирмами сгенерирован. case7_file2.json")


if __name__ == "__main__":
    print("Задание 1:\n")
    case_1()
    input("Нажмите ENTER для продолжения.")
    print("\nЗадание 2:\n")
    case_2()
    input("Нажмите ENTER для продолжения.")
    print("\nЗадание 3:\n")
    case_3()
    input("Нажмите ENTER для продолжения.")
    print("\nЗадание 4:\n")
    case_4()
    input("Нажмите ENTER для продолжения.")
    print("\nЗадание 5:\n")
    case_5()
    input("Нажмите ENTER для продолжения.")
    print("\nЗадание 6:\n")
    case_6()
    input("Нажмите ENTER для продолжения.")
    print("\nЗадание 7:\n")
    case_7()
