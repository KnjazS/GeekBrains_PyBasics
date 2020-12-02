#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from typing import List
from abc import ABC, abstractmethod


# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), который должен
# принимать данные (список списков) для формирования матрицы.
class Matrix(object):
    __width: int = None
    __height: int = None
    __inner: List[int] = None

    def __init__(self, values: List[List[int]]) -> None:
        self.__height = len(values)
        self.__width = len(values[0])
        self.__inner = []
        for line in values:
            if len(line) != self.__width:
                raise ValueError("Strings in a matrix must be the same length.")
            for elem in line:
                if not isinstance(elem, int):
                    raise ValueError("All the elements of matrix must be int.")
                self.__inner.append(elem)

    def __getitem__(self, keys: tuple[int, int]) -> int:
        if not isinstance(keys[0], int) or not isinstance(keys[1], int):
            raise ValueError("Indices must be integer")
        if keys[0] > self.__height or keys[0] < 0 or keys[1] > self.__width or keys[1] < 0:
            raise KeyError("Second index is wrong")
        return self.__inner[keys[0] * self.__width + keys[1]]

    def __setitem__(self, keys: tuple[int, int], value: int):
        if not isinstance(keys[0], int) or not isinstance(keys[1], int):
            raise ValueError("Indices must be integer")
        if keys[0] > self.__height or keys[0] < 0 or keys[1] > self.__width or keys[1] < 0:
            raise KeyError("Index is wrong")
        if not isinstance(value, int):
            raise ValueError("Value must be int")
        self.__inner[keys[0] * self.__width + keys[1]] = value

    def __str__(self):
        result = ""
        for idx, elem in enumerate(self.__inner):
            if idx % self.__width == 0:
                result += "|\t"
            result += f"{str(elem)}\t"
            if idx % self.__width == self.__width - 1:
                result += "|\n"
        return result

    def __repr__(self) -> str:
        return f"Matrix object: size {self.__height}x{self.__width}"

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def __add__(self, other: 'Matrix') -> 'Matrix':
        if self.__width != other.__width or self.__height != other.__height:
            raise ValueError("Sizes of matrices must be the same.")
        result = []
        for row in range(self.__height):
            tmp_row = []
            for column in range(self.__width):
                tmp_row.append(self[row, column] + other[row, column])
            result.append(tmp_row)
        return Matrix(result)


def case_1():
    matrix1 = Matrix([[0, 1, 2],
                      [2, 3, 4],
                      [3, 4, 5]])
    print(matrix1)
    matrix2 = Matrix([[1, 1, 1],
                      [1, 1, 1],
                      [1, 1, 1]])
    print(matrix1 + matrix2)


# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно. Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных. Реализовать общий подсчет
# расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные классы для основных
# классов проекта, проверить на практике работу декоратора @property.
class Clothing(ABC):
    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothing):
    __size: int

    def __init__(self, size: int):
        if not isinstance(size, int):
            raise ValueError("Size must be integer")
        if size < 40 or size > 60:
            raise ValueError("Wrong size")
        self.__size = size

    @property
    def tissue_consumption(self) -> float:
        return self.__size / 6.5 + 0.5


class Suit(Clothing):
    __height: int

    def __init__(self, height: int):
        if not isinstance(height, int):
            raise ValueError("Height must be integer")
        if height < 120 or height > 240:
            raise ValueError("Wrong height")
        self.__height = height

    @property
    def tissue_consumption(self) -> float:
        return 2 * self.__height + 0.3


def case_2():
    new_coat = Coat(48)
    print(f"На пальто 48 размера уйдет {new_coat.tissue_consumption:.2f} ткани.")
    new_suit = Suit(182)
    print(f"Для костюма на рост 182 пойдёт {new_suit.tissue_consumption:.2f} ткани.")


# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка. В его
# конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны быть
# реализованы методы перегрузки арифметических операторов: сложение (add()), вычитание (sub()), умножение (mul()),
# деление (truediv()). Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# целочисленное (с округлением до целого) деление клеток, соответственно. В классе необходимо реализовать метод
# make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по
# рядам. Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному
# аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
class Cell(object):
    __nucleus: int

    def __init__(self, nucleus_num: int) -> None:
        if not isinstance(nucleus_num, int):
            raise ValueError("Number of nucleus in cell must be integer.")
        self.__nucleus = nucleus_num if nucleus_num > 0 else 0

    @property
    def nucleus(self):
        return self.__nucleus

    def __add__(self, other: 'Cell'):
        if not isinstance(other, Cell):
            raise ValueError("You can add to a cell only another cell.")
        return Cell(self.__nucleus + other.__nucleus)

    def __sub__(self, other: 'Cell'):
        if not isinstance(other, Cell):
            raise ValueError("You can subtract from a cell only another cell.")
        return Cell(self.__nucleus - other.__nucleus)

    def __mul__(self, other: 'Cell'):
        if not isinstance(other, Cell):
            raise ValueError("You can subtract from a cell only another cell.")
        return Cell(self.__nucleus * other.__nucleus)

    def __truediv__(self, other: 'Cell'):
        if not isinstance(other, Cell):
            raise ValueError("You can subtract from a cell only another cell.")
        return Cell(self.__nucleus // other.__nucleus)

    def __str__(self):
        return "*" * self.__nucleus

    def make_order(self, row_len: int) -> str:
        if not isinstance(row_len, int):
            raise ValueError("Length of row must be integer.")
        row = f"{'*' * row_len}\n"
        return row * (self.__nucleus // row_len) + "*" * (self.__nucleus % row_len)


def case_3():
    cell1 = Cell(10)
    cell2 = Cell(5)
    print(f"{cell1} + {cell2} = {cell1 + cell2}")
    print(f"{cell1} - {cell2} = {cell1 - cell2}")
    print(f"{cell1} * {cell2} = {cell1 * cell2}")
    print(f"{cell1} / {cell2} = {cell1 / cell2}\n")
    print(f"{cell1}.make_order(3)\n\t=\n{cell1.make_order(3)}")


if __name__ == "__main__":
    print("Задание 1:\n")
    case_1()
    print("\nЗадание 2:\n")
    case_2()
    print("\nЗадание 3:\n")
    case_3()
