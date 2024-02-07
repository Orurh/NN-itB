class Digit:
    def __init__(self, name):
        if not isinstance(name, (int, float)):
            raise TypeError('значение не соответствует типу объекта')
        self.name = name


class Integer(Digit):
    def __init__(self, name=int):
        if not isinstance(name, int):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(name)


class Float(Digit):
    def __init__(self, name):
        if not isinstance(name, float):
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(name)


class Positive(Digit):
    def __init__(self, name):
        if name < 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(name)


class Negative(Digit):
    def __init__(self, name):
        if name > 0:
            raise TypeError('значение не соответствует типу объекта')
        super().__init__(name)


class PrimeNumber(Integer, Positive):
    pass


class FloatPositive(Float, Positive):
    pass


digits = [PrimeNumber(3), PrimeNumber(1), PrimeNumber(4), FloatPositive(1.5), FloatPositive(9.2), FloatPositive(6.5),
          FloatPositive(3.5), FloatPositive(8.9)]

lst_float = list(filter(lambda x: isinstance(x, Float), digits))
lst_positive = list(filter(lambda x: isinstance(x, Positive), digits))
