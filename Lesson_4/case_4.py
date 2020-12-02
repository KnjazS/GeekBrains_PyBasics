#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

from random import randint


# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.
def case_4():
    elem_list = [randint(1, 500) for x in range(35)]
    print(elem_list)
    print([x for x in elem_list if elem_list.count(x) == 1])


if __name__ == "__main__":
    print("Задание №4:\n")
    case_4()
