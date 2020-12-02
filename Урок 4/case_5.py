#!/usr/bin/env python3
# -*- coding:UTF-8 -*-


# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
def generate():
    for value in range(100, 1001):
        if value % 2 == 0:
            yield value


def case_5():
    result = 1
    for x in generate():
        result *= x
    print(f"Результат {result}")


if __name__ == "__main__":
    print("Задание №5:\n")
    case_5()
