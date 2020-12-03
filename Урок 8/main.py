#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

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


if __name__ == "__main__":
    print("Задание 1:\n")
    case_1()
