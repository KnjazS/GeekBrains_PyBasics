#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

from typing import List, Any


# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
def generator_a(start: int):
    while True:
        yield start
        start += 1


def generator_b(init_list: List[Any]):
    idx = 0
    while True:
        yield init_list[idx]
        idx = (idx + 1) % len(init_list)


def case_6():
    counter = 0                             # Используем первый генератор
    for value in generator_a(3):
        print(value, end=" ")
        counter += 1
        if counter == 10:
            print("...")
            break

    counter = 0                             # Используем второй генератор
    for value in generator_b(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']):
        print(value, end=" ")
        counter += 1
        if counter == 10:
            print("...")
            break


if __name__ == "__main__":
    print("Задание №6:\n")
    case_6()
