#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
def case_3():
    print([x for x in range(20, 240) if x % 20 == 0 or x % 21 == 0])


if __name__ == "__main__":
    print("Задание №3:\n")
    case_3()
