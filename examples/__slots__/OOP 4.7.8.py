# class Note:
#     def __init__(self, name, ton = 0):
#         self._name = name
#         self._ton = ton
#
#
#
# class Notes:
#     __slots__ = '_do', '_re', '_mi', '_fa', '_solt', '_la', '_si'
#     __cyrillic_notes = 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'
#
#     def __init__(self):
#         for k, v in list(zip(self.__slots__, self.__cyrillic_notes)):
#             setattr(self, k, Note(v, 0))
#
#         self._lst = [setattr(self, k, Note(v, 0)) for k, v in list(zip(self.__slots__, self.__cyrillic_notes))]
#
#
#     def __getattr__(self, name):
#         return self._lst[name]
#
# nt = Notes()
# print(nt[3])

# x, y, z = map(int, input())




z = sorted([int(input()), int(input()), int(input())], reverse=True)
print(*sorted([int(input()), int(input()), int(input())], reverse=True), sep = '\n')

