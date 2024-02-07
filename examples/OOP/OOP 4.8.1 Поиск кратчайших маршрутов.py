class Vertex:
    __id = -1

    def __new__(cls, *args, **kwargs):
        cls.__id += 1
        return super().__new__(cls)

    def __init__(self):
        self._links = []
        self._id = self.__id

    @property
    def link(self):
        return self._links

    @link.setter
    def link(self, value):
        if value not in self._links:
            self._links.append(value)

    @property
    def id(self):
        return self._id

    def __hash__(self):
        return hash(self._id)

    def __eq__(self, other):
        return hash(self) == hash(other)


class Link:
    def __init__(self, v1, v2, dist=1):
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise ValueError("Ссылки должны быть обьектами Vertex")
        if v1 == v2:
            raise ValueError("Ссылки должны быть разными")
        self._v1 = v1
        self._v2 = v2
        self._dist = dist
        v1.links = self
        v2.links = self

    @property
    def v1(self):
        return self._v1

    @v1.setter
    def v1(self, val):
        if not isinstance(val, Vertex):
            raise ValueError("val должен быть обьектом Vertex")
        self._v1 = val

    @property
    def v2(self):
        return self._v2

    @v2.setter
    def v2(self, val):
        if not isinstance(val, Vertex):
            raise ValueError("val должен быть обьектом Vertex")
        self._v2 = val

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        if not isinstance(value, int):
            raise ValueError("val должен быть обьектом int")
        self._dist = value

    def __eq__(self, other):
        return hash((self.v1, self.v2)) == hash((other.v1, other.v2)) or hash((self.v1, self.v2)) == hash(
            (other.v2, other.v1))


class LinkedGraph:
    def __init__(self):
        self._links = []  # связи между станциями, расстояние
        self._vertex = []  # список станций

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        if link not in self._links:
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)

    def find_path(self, start_v, stop_v):
        pass


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class LinkMetro(Link):
    # def __init__(self, v1, v2, dist):
    #     super().__init__()
    #     self.dist = dist
    pass


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 1))
map_metro.add_link(LinkMetro(v2, v3, 1))
map_metro.add_link(LinkMetro(v1, v3, 1))

map_metro.add_link(LinkMetro(v4, v5, 1))
map_metro.add_link(LinkMetro(v6, v7, 1))

map_metro.add_link(LinkMetro(v2, v7, 5))
map_metro.add_link(LinkMetro(v3, v4, 3))
map_metro.add_link(LinkMetro(v5, v6, 3))

print(len(map_metro._vertex))

for _ in map_metro._links:
    print(_.v1.__dict__, _.v2.__dict__, _.dist)
for _ in map_metro._vertex:
    print(_)
