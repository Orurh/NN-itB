class Note:
    def __init__(self, name, ton=0):
        self._name = name
        self._ton = ton

    def __setattr__(self, key, value):
        print(key, value)
        if key =='_ton' and value not in range(-1,2):
            raise ValueError('недопустимое значение аргумента')
        if key == '_name' and value not in ('до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'):
            raise ValueError('недопустимое значение аргумента')
        super().__setattr__(key, value)


class Notes:
    __slots__ = ('_do', '_re', '_mi', '_fa', '_solt', '_la', '_si')
    __cyrillic_notes = 'до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си'

    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        for k, v in list(zip(self.__slots__, self.__cyrillic_notes)):
            setattr(self, k, Note(v, 0))

    def __getitem__(self, item):
        if item not in range(0,7):
            raise IndexError('недопустимый индекс')
        return getattr(self, self.__slots__[item])



nt = Notes()
nt[0]._ton = -2
print(nt[0]._ton)
