class Matrix:
    def __init__(self, rows, cols=None, fill_value=None):
        if isinstance(rows, list):
            if (len(set([len(x) for x in rows])) != 1):
                raise TypeError('список должен быть прямоугольным, состоящим из чисел')
            for row in rows:
                for col in row:
                    if not isinstance(col, (float, int)):
                        raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
                self.cols = len(row)
            self.lst = rows
            self.rows = len(rows)
        else:
            self.rows = rows
            self.cols = cols
            if not isinstance(fill_value, (float, int)):
                raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')
            self.fill_value = fill_value
            self.lst = [[self.fill_value for row in range(self.cols)] for col in range(self.rows)]

    def check_index(self, index):
        if not isinstance(index[0], (float, int)):
            raise IndexError('недопустимые значения индексов')
        if not (0 <= index[0] < self.rows) or not (0 <= index[1] < self.cols):
            raise IndexError('недопустимые значения индексов')

    def __getitem__(self, key):
        self.check_index(key)
        return self.lst[key[0]][key[1]]

    def __setitem__(self, key, value):
        if not isinstance(value, (float, int)):
            raise TypeError('значения матрицы должны быть числами')
        self.check_index(key)
        self.lst[key[0]][key[1]] = value

    def __add__(self, other):
        if isinstance(other, Matrix):
            if len(self.lst) != len(other.lst) or len(self.lst[0]) != len(other.lst[0]):
                raise ValueError('операции возможны только с матрицами равных размеров')
            result = [[self.lst[i][j] + other.lst[i][j] for j in range(len(self.lst[0]))] for i in range(len(self.lst))]
        else:
            result = [[self.lst[i][j] + other for j in range(len(self.lst[0]))] for i in range(len(self.lst))]
        return Matrix(result)

    def __sub__(self, other):
        if isinstance(other, Matrix):
            print(other)
            if len(self.lst) != len(other.lst) or len(self.lst[0]) != len(other.lst[0]):
                raise ValueError('операции возможны только с матрицами равных размеров')
            result = [[self.lst[i][j] - other.lst[i][j] for j in range(len(self.lst[0]))] for i in range(len(self.lst))]
        else:
            result = [[self.lst[i][j] - other for j in range(len(self.lst[0]))] for i in range(len(self.lst))]
        return Matrix(result)

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"
