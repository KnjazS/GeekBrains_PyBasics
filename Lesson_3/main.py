#!/usr/bin/env python3
# -*- coding:UTF-8 -*-
from typing import Callable, Any
from math import nan


def sanitized_input(invite_message: str, error_message: str, translate: Callable[[str], Any]) -> Any:
    while True:
        # noinspection PyBroadException
        try:
            return translate(input(invite_message))
        except EOFError as e:
            raise e
        except Exception:
            print(error_message)


# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def func(dividend: float, divider: float) -> float:
    try:
        return dividend / divider
    except ZeroDivisionError as e:
        print("Я не буду делить на ноль")   # Такая обработка плохая, я знаю. Надо за один раз всё обработать
        raise e                             # и не вспоминать, но задание именно сделать обработку.


def case_1():
    dividend = sanitized_input("Введите делимое --> ",
                               "Неее, подходят только числа.",
                               float)
    divider = sanitized_input("Введите делимое --> ",
                              "Неее, подходят только числа.",
                              float)
    try:
        result = func(dividend, divider)
    except ZeroDivisionError:
        return
    print(f"Ваш результат: {result:.3f}")


print("Задание 1:\n")
# case_1()


# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
# как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
def year_trans(value: str) -> int:
    value = int(value)
    if 0 <= value <= 2020:
        return value
    raise ValueError("Year must be in range (0, 2020).")


def email_trans(value: str) -> str:
    if value.find("@") == -1:
        raise ValueError("E-mail address must have @.")
    return value


def phone_trans(value: str) -> str:
    for char in value:
        if not (char.isdigit() or char in ["(", ")", "-", " "]):
            raise ValueError("Phone number can contain only digits")
    return value


def print_user(name: str, surname: str, year_born: int, city: str, email: str, phone_number: str):
    print(f"{name.title()} {surname.title()} ({year_born}, {city.title()}) - {phone_number}, {email}")


def case_2():
    name = sanitized_input("Введите имя --> ",
                           "",
                           str)
    surname = sanitized_input("Введите фамилию --> ",
                              "",
                              str)
    year_born = sanitized_input("Введите год рождения --> ",
                                "Так, год рождения - число от 0 до 2020",
                                year_trans)
    city = sanitized_input("Введите город рождения --> ",
                           "",
                           lambda x: x.title())
    email = sanitized_input("Введите адрес электронной почты --> ",
                            "Так. Это же не адрес. Попробуй ещё раз.",
                            email_trans)
    phone_number = sanitized_input("Введите телефонный номер --> ",
                                   "Мы ж не в СССР. Телефон только из цифр.",
                                   phone_trans)
    print_user(name, surname, year_born, city, email, phone_number)


print("\n\nЗадание 2:\n")
# case_2()


# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
def my_func(a: float, b: float, c: float) -> float:
    values = [a, b, c]
    max_value = max(values)
    values.remove(max_value)
    return max_value + max(values)


def case_3():
    a = sanitized_input("Введите первое число --> ",
                        "Эту фигню нельзя представить, как действительное число.",
                        float)
    b = sanitized_input("Введите второе число --> ",
                        "Эту фигню нельзя представить, как действительное число.",
                        float)
    c = sanitized_input("Введите третье число --> ",
                        "Эту фигню нельзя представить, как действительное число.",
                        float)
    print(f"Результат: {my_func(a, b, c):.3f}")


print("\n\nЗадание 3:\n")
# case_3()


# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции
# my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
def my_func(x: float, y: int) -> float:
    if x == y == 0:
        return nan
    result = 1
    for idx in range(abs(y)):
        result *= x
    if y < 0:
        try:
            return 1.0 / result
        except ZeroDivisionError:
            return nan
    return result


def case_4():
    x = sanitized_input("Введите основание --> ",
                        "Эту фигню нельзя представить, как действительное число.",
                        float)
    y = sanitized_input("Введите показатель --> ",
                        "Эту фигню нельзя представить, как целое число.",
                        int)
    print(f"Результат: {my_func(x, y):f}")


print("\n\nЗадание 4:\n")
# case_4()


# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к
# уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
# завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.
def case_5():
    print("Введите действительные числа через пробел (Для выхода введите $)", end="")
    result = 0.0
    is_exit = False
    while not is_exit:
        try:
            string = input(": ")
        except EOFError:
            break
        string = string.split(" ")
        for number in string:
            if number == "$":
                is_exit = True
                break
            if number[-1] == "$":
                number = number[:-1]
                is_exit = True
            try:
                number = float(number)
            except ValueError:
                print(f"Пропускаем '{number}' - невозможно преобразовать")
                continue
            result += number
    print("Результат:", result)


print("\n\nЗадание 5:\n")
# case_5()


# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое
# слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
# начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
def int_func(value: str) -> str:
    if not value.isalpha():
        raise ValueError()
    return value[0].upper() + value[1:]


def case_6():
    input_value = input("Введите строку --> ")
    input_value = input_value.split(" ")
    for word in input_value:
        print(int_func(word), end=" ")


print("\n\nЗадание 6:\n")
case_6()
