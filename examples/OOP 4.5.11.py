# class Food:
#     def __init__(self, name, weight, calories):
#         self._name = name
#         self._weight = weight
#         self._calories = calories
#
# class BreadFood(Food):
#     def __init__(self, name, weight, calories, white):
#         super().__init__(name, weight, calories)
#         self._white = white
#
# class SoupFood(Food):
#     def __init__(self, name, weight, calories, dietary):
#         super().__init__(name, weight, calories)
#         self._dietary = dietary
#
# class FishFood(Food):
#     def __init__(self, name, weight, calories, fish):
#         super().__init__(name, weight, calories)
#         self._fish = fish
#
# bf = BreadFood("Бородинский хлеб", 34.5, 512, False)
# sf = SoupFood("Черепаший суп", 520, 890.5, False)
# ff = FishFood("Консерва рыбная", 340, 1200, "семга")
#
# print(bf.__dict__)

class A:
    def __init__(self, name, old):
        super().__init__()
        self.name = name
        self.old = old


class B:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class C(A,B):
    def __init__(self, name, old, weight, height):
        super().__init__(name, old)
        self.weight = weight
        self.height = height

person = C("Balakirev", 33, 80, 185)