'''Объявите класс SoftList, который наследуется от стандартного класса list.
В классе SoftList следует объявить необходимые магические методы так, чтобы при обращении к несуществующему
элементу (по индексу) возвращалось значение False (а не исключение Out of Range). '''


# class SoftList(list):
#     def __init__(self, name):
#         super().__init__(name)
#
#     def __getitem__(self, key):
#         try:
#             return super().__getitem__(key)
#         except IndexError:
#             return False

class SoftList(list):
    def __getitem__(self, key):
        try:
            return super().__getitem__(key)
        except IndexError:
            return False


sl = SoftList("python")
assert sl[0] == "p"
assert sl[-1] == "n"
assert sl[6] == False
assert sl[-7] == False

