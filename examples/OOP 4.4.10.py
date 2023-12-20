def class_log(func):
    def wtf(cls):  # определяем список вызываемых функций и декорируем их
        methods = {k: v for k, v in cls.__dict__.items() if callable(v)}
        for k, v in methods.items():
            setattr(cls, k, decor(v))
        return cls

    def decor(item): #  список всех вызываемых функций для декорации
        def wrapper(*args): #  список только вызыванных функций
            print(item)
            func.append(item.__name__)
            return item(*args)

        return wrapper

    return wtf


vector_log = []  # наименование (vector_log) в программе не менять!


@class_log(vector_log)
class Vector:
    def __init__(self, *args):
        self.__coords = list(args)

    def __getitem__(self, item):
        return self.__coords[item]

    def __setitem__(self, key, value):
        self.__coords[key] = value


v = Vector(1, 2, 3)
v[0] = 10
