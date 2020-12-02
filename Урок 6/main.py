#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from time import sleep, time
from sys import exc_info

# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный,
# желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
COLOR_RED = 0
COLOR_YELLOW = 1
COLOR_GREEN = 2


class TrafficLight(object):
    __color: int

    def running(self):
        self.__color = COLOR_RED
        print("Светофор: КРАСНЫЙ!")
        sleep(7)
        self.__color = COLOR_YELLOW
        print("Светофор: ЖЕЛТЫЙ!")
        sleep(2)
        self.__color = COLOR_GREEN
        print("Светофор: ЗЕЛЁНЫЙ!")
        sleep(5)
        self.__color = COLOR_YELLOW
        print("Светофор: ЖЕЛТЫЙ!")
        sleep(2)


def case_1():
    traffic_light = TrafficLight()
    print("Включаем светофор на 35 секунд!")
    start_time = time()
    while time() - start_time < 35:
        traffic_light.running()
    print("Светофор выключен")


# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). Значения данных
# атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными. Определить метод расчета
# массы асфальта, необходимого для покрытия всего дорожного полотна. Использовать формулу: длина*ширина*масса асфальта
# для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. Проверить работу метода.
class Road(object):
    __length__: float
    __width__: float

    def __init__(self, length, width):
        self.__length__ = length
        self.__width__ = width

    def get_mass(self):
        """
        Method counts asphalt mass is needed for building such road. (25 kg asphalt per 1 square meter of road with 1 cm
        thickness)

        :return: mass of asphalt is needed in kg
        """
        return self.__width__ * self.__length__ * 125


def case_2():
    road = Road(1000, 3.5)
    print(f"Для одного километра дороги понадобится {road.get_mass()} кг асфальта")


# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker. В классе Position
# реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров).
class Worker(object):
    __first_name__: str
    __last_name__: str
    __position__: str
    __income__: dict


class Position(Worker):
    def __init__(self, position_name: str, name: str, surname: str, wage: float, bonus: float):
        try:
            self.__position__ = str(position_name).title()
            self.__first_name__ = str(name).title()
            self.__last_name__ = str(surname).title()
            self.__income__ = {"wage": float(wage), "bonus": float(bonus)}
        except ValueError:
            _, _, tb_info = exc_info()
            if tb_info.tb_lineno == 90:
                if tb_info.tb_lasti == 48:
                    raise ValueError("Wrong wage value")
                raise ValueError("Wrong bonus value")

    def get_full_name(self):
        return f"{self.__first_name__} {self.__last_name__}"

    def get_total_income(self):
        return self.__income__["wage"] + self.__income__["bonus"]


def case_3():
    pos = Position("CSO", "Kris", "Kaspersky", 500000, 120000)
    print(f"CSO Name: {pos.get_full_name()}")
    print(f"His income: {pos.get_total_income()}")


# 4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
# скорости.
TURN_LEFT = 0
TURN_RIGHT = 1
TURN_AROUND = 2


class Car(object):
    __speed__: int
    __color__: str
    __car_name__: str
    __is_police__: bool

    def __init__(self, color: str, car_name: str):
        self.__speed__ = 0
        self.__color__ = color
        self.__car_name__ = car_name
        self.__is_police__ = False

    def go(self, new_speed: int):
        if type(new_speed) is not int:
            raise ValueError("Speed must be integer.")
        if self.__speed__ == 0:
            print(f"{self.__car_name__} поехала. Скорость {new_speed} км/ч")
        else:
            print(f"{self.__car_name__} изменила скорость. Скорость {new_speed} км/ч")
        self.__speed__ = new_speed

    def stop(self):
        print(f"{self.__car_name__} остановилась")
        self.__speed__ = 0

    def turn(self, direction: int):
        if direction == TURN_LEFT:
            print(f"{self.__car_name__} повернула налево")
        if direction == TURN_RIGHT:
            print(f"{self.__car_name__} повернула направо")
        if direction == TURN_AROUND:
            print(f"{self.__car_name__} повернула развернулась")

    def show_speed(self):
        print(f"Текущая скорость {self.__speed__} км/ч")


class TownCar(Car):
    def go(self, new_speed: int):
        Car.go(self, new_speed)
        if new_speed > 60:
            print(f"Внимание! {self.__car_name__} превышает дозволенные 60 км/ч!")

    def show_speed(self):
        Car.show_speed(self)
        if self.__speed__ > 60:
            print(f"Внимание! {self.__car_name__} превышает скорость.")


class SportCar(Car):
    def show_speed(self):
        Car.show_speed(self)
        if self.__speed__ > 100:
            print("Открываем спойлер! Эрон-дон-дон!")


class WorkCar(Car):
    def go(self, new_speed: int):
        Car.go(self, new_speed)
        if new_speed > 40:
            print(f"Внимание! {self.__car_name__} превышает дозволенные 40 км/ч!")

    def show_speed(self):
        Car.show_speed(self)
        if self.__speed__ > 40:
            print(f"Внимание! {self.__car_name__} превышает скорость.")


class PoliceCar(Car):
    def __init__(self, color: str, car_name: str):
        super().__init__(color, car_name)
        self.__is_police__ = True

    def show_speed(self):
        Car.show_speed(self)
        if self.__speed__ > 60:
            print(f"Внимание! {self.__car_name__} надо включить мигалки.")


def case_4():
    print("Создаем городскую машину")
    town_car = TownCar("Blue", "Honda Civic")
    print("Поехали. Скорость 40!")
    town_car.go(40)
    print("Скорость 80!")
    town_car.go(80)
    print("Проверим скорость")
    town_car.show_speed()


# 5. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
# 6. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw
# (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш),
# Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен
# выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого
# экземпляра.
class Stationery(object):
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = "PEN: " + self.title

    def draw(self):
        print("Это было отрисовано при помощи ручки " + self.title)


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = "PENCIL: " + self.title

    def draw(self):
        print("Это было отрисовано при помощи карандаша " + self.title)


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
        self.title = "HANDLE: " + self.title

    def draw(self):
        print("Это было отрисовано при помощи маркера " + self.title)


def case_6():
    pen = Pen("Erich Krause Gold TOP SUPER MEGA OVER COOL")
    pen.draw()


if __name__ == "__main__":
    print("Задание 1:\n")
    case_1()
    print("\nЗадание 2:\n")
    case_2()
    print("\nЗадание 3:\n")
    case_3()
    print("\nЗадание 4:\n")
    case_4()
    print("\nЗадание 5:\n")
    print("\nТолько что все сделал в задании 4\n")
    print("\nЗадание 6:\n")
    case_6()
