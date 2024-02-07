class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __getattr__(self, item):
        return "Атрибут с именем z не существует"

pt = Point(1, 2)
print(pt._z)