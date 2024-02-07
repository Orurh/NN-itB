'''Объявите класс Furniture.
В каждом объекте класса Furniture должны создаваться защищенные локальные атрибуты с именами _name и _weight. В самом классе Furniture нужно объявить приватные методы:

__verify_name() - для проверки корректности имени;
__verify_weight() - для проверки корректности веса.

Данные методы следует вызывать всякий раз при записи новых значений в атрибуты _name и _weight (а также при их создании).

На основе базового класса Furniture объявить следующие дочерние классы:

Closet - для представления шкафов;
Chair - для представления стульев;
Table - для представления столов.

Объявить метод:
get_attrs()
который возвращает кортеж из значений локальных защищенных атрибутов объектов этих классов.'''


class Furniture:
    def __init__(self, name, weight):
        self.__verify_name(name)
        self._name = name
        self.__verify_weight(weight)
        self._weight = weight

    def __verify_name(self, name):
        if not isinstance(name, str):
            raise TypeError('название должно быть строкой')

    def __verify_weight(self, weight):
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise TypeError('вес должен быть положительным числом')

    def get_attrs(self):
        return tuple(self.__dict__.keys())


class Closet(Furniture):
    def __init__(self, name, weight, tp, doors):
        super().__init__(name, weight)
        self._tp = tp
        self._doors = doors


class Chair(Furniture):
    def __init__(self, name, weight, height):
        super().__init__(name, weight)
        self._height = height


class Table(Furniture):
    def __init__(self, name, weight, height, square):
        super().__init__(name, weight)
        self._height = height
        self._square = square


cl = Closet('шкаф-купе', 342.56, True, 3)
chair = Chair('стул', 14, 55.6)
tb = Table('стол', 34.5, 75, 10)
print(tb.get_attrs())
