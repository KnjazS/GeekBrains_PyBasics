#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

from random import randint


# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
# элемента. Для формирования списка использовать генератор.
def case_2():
    elem_list = [randint(1, 500) for x in range(35)]
    print(elem_list)
    print([elem_list[idx] for idx in range(1, len(elem_list)) if elem_list[idx] > elem_list[idx-1]])


if __name__ == "__main__":
    print("Задание №2:\n")
    case_2()
