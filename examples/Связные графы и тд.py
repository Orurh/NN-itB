# class Vertex:
#     def __init__(self):
#         self._links = []  # список связей с другими вершинами графа (список объектов класса Link). Зачем???
#
#     @property
#     def links(self):
#         return self._links
#
#
# class Link:
#     def __init__(self, v1, v2, dist=1):
#         self._v1 = v1
#         self._v2 = v2
#         self._dist = dist
#
#     @property
#     def v1(self):
#         return self._v1
#
#     @v1.setter
#     def v1(self, value):
#         self._v1 = value
#
#     @property
#     def v2(self):
#         return self._v2
#
#     @v2.setter
#     def v2(self, value):
#         self._v2 = value
#
#     @property
#     def dist(self):
#         return self._dist
#
#     @dist.setter
#     def dist(self, value):
#         self._dist = value
#
#
# class LinkedGraph:
#     def __init__(self):
#         self._links = []  # список из всех связей графа (из объектов класса Link);
#         self._vertex = []  # список из всех вершин графа (из объектов класса Vertex).
#
#     def add_vertex(self, v):
#         if v not in self._vertex:
#             self._vertex.append(v)
#
#     def add_link(self, link):
#         t = tuple(filter(
#             lambda x: (id(x.v1) == id(link.v1)) and (id(x.v2) == id(link.v2)) or (id(x.v2) == id(link.v1)) and (
#                         id(x.v1) == id(link.v2)), self._links))
#
#         if len(t) == 0:
#             self._links.append(link)
#             self.add_vertex(link.v1)
#             self.add_vertex(link.v2)
#             link.v1.links.append(link)
#             link.v2.links.append(link)
#
#     def find_path(self, start_v, stop_v):
#         print(start_v.__dict__, stop_v.__dict__)
#
#
# class Station(Vertex):
#     def __init__(self, name):
#         super().__init__()
#         self.name = name
#
#     # def __str__(self):
#     #     pass
#
#     # def __repr__(self):
#     #     pass
#
#
# class LinkMetro(Link):
#     def __init__(self, v1, v2, dist):
#         super().__init__(v1, v2, dist)
#
#
# map_metro = LinkedGraph()
# v1 = Station("Сретенский бульвар")
# v2 = Station("Тургеневская")
# v3 = Station("Чистые пруды")
#
# map_metro.add_link(LinkMetro(v1, v2, 1))
# map_metro.add_link(LinkMetro(v2, v3, 2))
# map_metro.add_link(LinkMetro(v1, v3, 4))
#
# path = map_metro.find_path(v1, v3)

def get_number(x):
    try:
        print(int(x))
    except:
        try:
            print(float(x))
        except:
            print(x)

res_1 = get_number(True)
res_2 = get_number('5.78')
res_3 = get_number('8(912)000-000-00')
