'''Объявите класс StringDigit, который наследуется от стандартного класса str.
Если в строке string окажется хотя бы один не цифровой символ, то генерировать исключение.
Также в классе StringDigit нужно переопределить оператор + (конкатенации строк) так, чтобы операции
создавали новые объекты класса StringDigit (а не класса str). Если же при соединении строк появляется не цифровой символ,
то генерировать исключение'''


class StringDigit(str):
    def __init__(self, items):
        self.__check(items)
        super().__init__()

    def __check(self, string):
        if not string.isdigit():
            raise ValueError("в строке должны быть только цифры")

    def __add__(self, other):
        self.__check(other)
        return self.__class__(super().__add__(other))

    def __radd__(self, other):
        self.__check(other)
        return self.__class__(other.__add__(self))


sd = StringDigit("123")
assert str(sd) == "123", "неверно работает метод __str__ класса StringDigit"

try:
    sd2 = StringDigit("123a")
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

sd = sd + "345"
assert sd == "123345", "неверно отработал оператор +"

sd = "0" + sd
assert sd == "0123345", "неверно отработал оператор +"

try:
    sd = sd + "12d"
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"

try:
    sd = "12d" + sd
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при выполнении оператора +"