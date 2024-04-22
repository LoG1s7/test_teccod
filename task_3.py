# Задание 3
# Создать класс Point, который представляет собой точку
# в двумерном пространстве. Класс должен иметь методы для
# инициализации координат точки, вычисления расстояния до другой точки,
# а также для получения и изменения координат.


import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        return math.sqrt(
            (self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

    def get_coordinates(self):
        return self.x, self.y

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y


# Пример использования
point1 = Point(0, 0)
point2 = Point(3, 4)
print(point1.distance_to(point2))  # Вывод: 5.0
print(point1.get_coordinates())  # Вывод: (0, 0)
point1.set_coordinates(1, 2)
print(point1.get_coordinates())  # Вывод: (1, 2)
