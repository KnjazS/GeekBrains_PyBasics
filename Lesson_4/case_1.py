#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

from sys import argv, exc_info


# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для выполнения расчета для конкретных
# значений необходимо запускать скрипт с параметрами.
def pos_float_trans(value: str) -> float:
    value = float(value)
    if value < 0:
        raise ValueError()
    return value


def case_1(time: float, rate: float, prize: float):
    print(f"Работник заработал {time * rate * (1 + prize / 100):.2f}")


if __name__ == "__main__":
    if len(argv) < 4:
        print("Недостаточно параметров.")
        exit()

    try:
        time = pos_float_trans(argv[1])
        rate = pos_float_trans(argv[2])
        prize = pos_float_trans(argv[3])
    except ValueError as e:
        print(f"Невозможно обработать параметр №{exc_info()[2].tb_lineno - 26}")
        exit()

    case_1(time, rate, prize)
