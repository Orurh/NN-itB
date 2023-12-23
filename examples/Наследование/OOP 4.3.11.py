'''Объявите базовый класс с именем ItemAttrs, который бы позволял обращаться к локальным атрибутам
объектов дочерних классов по индексу. Для этого в классе ItemAttrs нужно переопределить следующие методы:

__getitem__() - для получения значения атрибута по индексу;
__setitem__() - для изменения значения атрибута по индексу.

Объявите дочерний класс Point для представления координаты точки на плоскости.'''

class ItemAttrs:
    def __getitem__(self, item):
        return self.__dict__[[*self.__dict__.keys()][item]]

    def __setitem__(self, item, key):
        self.__dict__[[*self.__dict__.keys()][item]] = key


class Point(ItemAttrs):
    def __init__(self, x, y):
        self.x = x
        self.y = y


pt = Point(1, 2.5)
x = pt[0]   # 1
print(x)
y = pt[1]   # 2.5
pt[0] = 10
