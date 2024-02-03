class Triangle:
    def __init__(self, a, b, c):
        self.is_digit(a), self.is_digit(b), self.is_digit(c)
        self._a = a
        self._b = b
        self._c = c
        if not 2 * max(self._a, self._b, self._c) < (self._a + self._b + self._c):
            raise ValueError('из указанных длин сторон нельзя составить треугольник')

    def is_digit(self, x):
        if not isinstance(x, (int, float)) or x <= 0:
            raise TypeError('стороны треугольника должны быть положительными числами')


input_data = [(1.0, 4.54, 3), ('abc', 1, 2, 3), (-3, 3, 5.2), (4.2, 5.7, 8.7), (True, 3, 5), (7, 4, 6)]


def nmp(x):
    try:
        return Triangle(*x)
    except:
        pass


lst_tr = list(filter(lambda x: isinstance(x, Triangle), list(map(nmp, input_data))))
