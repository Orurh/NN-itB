class Cell:
    def __init__(self, data):
        self.__data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value


class TableValues:
    def __init__(self, rows, cols, type_data=int):
        self.rows = rows
        self.cols = cols
        self.type_data = type_data
        self.table = [[Cell(0) for _ in range(self.cols)] for x in range(self.rows)]

    def check_type(self, value):
        if type(value) != self.type_data:
            raise TypeError('неверный тип присваиваемых данных')

    def __setitem__(self, key, value):
        self.check_type(value)
        if key[0] not in range(self.rows) or key[1] not in range(self.cols):
            raise IndexError('неверный индекс')
        self.table[key[0]][key[1]].data = value

    def __getitem__(self, key):
        if key[0] not in range(self.rows) or key[1] not in range(self.cols):
            raise IndexError('неверный индекс')
        return self.table[key[0]][key[1]].data

    def __iter__(self):
        for i in self.table:
            yield (x.data for x in i)


tb = TableValues(3, 2)
n = m = 0
for row in tb:
    n += 1
    for value in row:
        m += 1
        assert type(
            value) == int and value == 0, "при переборе объекта класса TableValues с помощью вложенных циклов for, должен сначала возвращаться итератор для строк, а затем, этот итератор должен возвращать целые числа (значения соответствующих ячеек)"

assert n > 1 and m > 1, "неверно отработали вложенные циклы для перебора ячеек таблицы"

tb[0, 0] = 10
print(tb[0, 0])
assert tb[0, 0] == 10, "не работает запись нового значения в ячейку таблицы"

try:
    tb[2, 0] = 5.2
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError"

try:
    a = tb[2, 4]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"