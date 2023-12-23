class Aircraft:
    def __init__(self, model, mass, speed, top):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, key, value):
        if key == '_model':
            if type(value) != str:
                raise TypeError('неверный тип аргумента')
        elif key in ('_mass', '_speed', '_top'):
            if not isinstance(value, (int, float)) or value <= 0:
                raise TypeError(f'неверный тип аргумента')
        object.__setattr__(self, key, value)

class PassengerAircraft(Aircraft):
    def __init__(self, model, mass, speed, top, chairs):
        self._chairs = chairs
        super().__init__(model, mass, speed, top)

    def __setattr__(self, key, value):
        if key == '_chairs':
            if not isinstance(value, int) or value <= 0:
                raise TypeError(f'неверный тип аргумента')
        object.__setattr__(self, key, value)

class WarPlane(Aircraft):
    def __init__(self, model, mass, speed, top, weapons):
        if isinstance(weapons, list):
            self._weapons = dict(weapons)
        self._weapons = weapons
        super().__init__(model, mass, speed, top)

#

# ''' VAR #2'''
# class Aircraft:
#     def __init__(self, model, mass, speed, top):
#         self.check_str(model), self.check_falint(mass), self.check_falint(top), self.check_falint(speed)
#         self._model = model
#         self._mass = mass
#         self._speed = speed
#         self._top = top
#
#     def check_str(self, value):
#         if not isinstance(value, str):
#             raise TypeError('неверный тип аргумента')
#
#     def check_falint(self, value):
#         print(value)
#         if not isinstance(value, (float, int)) or not value > 0:
#             raise TypeError('неверный тип аргумента')
#
#
#
# class PassengerAircraft(Aircraft):
#     def __init__(self, model, mass, speed, top, chairs):
#         self.check_int(chairs)
#         self._chairs = chairs
#         super().__init__(model, mass, speed, top)
#
#     def check_int(self, value):
#         if not isinstance(value, int) or not value > 0:
#             raise TypeError('неверный тип аргумента')
#
#
# class WarPlane(Aircraft):
#     def __init__(self, model, mass, speed, top, weapons):
#         super().__init__(model, mass, speed, top)
#         if isinstance(weapons, list):
#             self.check_dict(dict(weapons))
#             self._weapons = dict(weapons)
#         else:
#             self.check_dict(weapons)
#             self._weapons = weapons
#
#     def check_dict(self, item):
#         for x, y in item.items():
#             self.check_str(x)
#             self.check_falint(y)


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]

air = Aircraft('model', 1, 2, 3)
assert air._model == 'model' and air._mass == 1 and air._speed == 2 and air._top == 3, "неверные значения атрибутов объекта класса Aircraft"


try:
    air = Aircraft('4', 1, -2, 3)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при выполнении команды Aircraft('4', 1, -2, 3)"

try:
    PassengerAircraft('model', 1, 2, 3, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при выполнении команды PassengerAircraft('model', 1, 2, 3, 0)"


try:
    WarPlane('model', 1, 2, 3, [1, 2])
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError при выполнении команды WarPlane('model', 1, 2, 3, [1, 2])"