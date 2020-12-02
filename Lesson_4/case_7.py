#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

from math import factorial


# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение. При вызове функции
# должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает
# за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
def fact(n: int):
    if type(n) != int or n < 1:
        raise ValueError()
    for i in range(1, n + 1):
        yield factorial(i)


def case_7():
    for idx, value in enumerate(fact(8)):
        print(f"{idx + 1}! = {value}")


if __name__ == "__main__":
    print("Задание №7:\n")
    case_7()
