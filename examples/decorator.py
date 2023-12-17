class Dec:
    '''class Decorator for func'''
    def __call__(self, func):
        def wrapper (*args, **kwargs):
            arg = [i*i for i in args]
            res = func(*arg)
            return res
        return wrapper

@Dec() # invocker
def my_func(x1, x2):
    return x1 + x2

print(my_func(2,5))

'''------------------------------------------------------------------------------------------------------------'''
class Dec1:
    '''class Decorator for func'''
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        arg = [i*i for i in args]
        res = self.func(*arg)
        return res

@Dec1 # not invocker
def my_func1(x1, x2):
    return x1 + x2


print(my_func(2,5))
# print(Dec1(my_func1)(2,5))

'''------------------------------------------------------------------------------------------------------------'''
class Dec3:
    ''' class Decorator for class'''
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            x = func(self.name)
            return x
        return wrapper




@Dec3('Georg')
class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

obj = Person('Иванов')
print(obj.get_name())


# class Counter:
#     def __init__(self, start=0):
#         self.count = start
#
#     def __call__(self):
#         self.count += 1
#         print(f'Всего вызовов {self.count}')