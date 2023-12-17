class Dec:
    def __call__(self, func):
        def wrapper (*args, **kwargs):
            arg = [i*i for i in args]
            res = func(*arg)
            return res
        return wrapper

@Dec()
def my_func(x1, x2):
    return x1 + x2

print(my_func(2,5))

