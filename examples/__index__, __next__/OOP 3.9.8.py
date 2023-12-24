class IterColumn:
    def __init__(self, lst, column):
        self._lst = lst
        self._column = column

    def __iter__(self):
        for i in self._lst:
            yield i[self._column]

lst = [[1, 11, 111],
       [2, 22, 222, 2222, 22222, 222222],
       [3, 33, 333, 3333, 33333, 333333],
       [4, 44, 444, 4444, 44444, 444444]]

it = IterColumn(lst, 2)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)
#
it_iter = iter(it)
x = next(it_iter)