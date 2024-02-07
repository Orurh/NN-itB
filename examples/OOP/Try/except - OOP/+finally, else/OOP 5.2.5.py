class Point:
    def __init__(self, *args):
        if len(args) == 0:
            self._x = 0
            self._y = 0
        else:
            self._x = args[0]
            self._y = args[1]

x, y = input().split()
try:
    pt = Point(int(x), int(y))
except:
    pt = Point()
finally:
    print(f'Point: x = {pt._x}, y = {pt._y}')

