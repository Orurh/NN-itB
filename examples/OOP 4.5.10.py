class PointTrack:
    def __init__(self, x, y):
        self.check_numb(x), self.check_numb(y)
        self.x = x
        self.y = y

    def __str__(self):
        return f'PointTrack: {self.x}, {self.y}'

    def check_numb(self, i):
        if not isinstance(i, (float, int)):
            raise TypeError('координаты должны быть числами')

class Track:
    def __init__(self, *args):
        self._points = list(args)

    @property
    def points(self):
        return tuple(self._points)

    def add_back(self, pt):
        self._points.append(pt)

    def add_front(self, pt):
        self._points.insert(0, pt)

    def pop_back(self):
        self._points.pop

    def pop_front(self):
        self._points.pop(0)

tr = Track(PointTrack(0, 0), PointTrack(1.2, -0.5), PointTrack(2.4, -1.5))
tr.add_back(PointTrack(1.4, 0))
tr.pop_front()
for pt in tr.points:
    print(pt)