#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from typing import List


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
        if not isinstance(value):
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

    def __add__(self, other) -> 'Matrix':
        if self.__width != other.width or self.__height != other.height:
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
    print(matrix1+matrix2)


if __name__ == "__main__":
    print("Задание 1:\n")
    case_1()
