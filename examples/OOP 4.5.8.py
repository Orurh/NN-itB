from abc import ABC, abstractmethod


<<<<<<< HEAD
class StackInterface:
=======
class StackInterface(ABC):
>>>>>>> ab0503e (связный список с абстрактным классом)
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
<<<<<<< HEAD
        raise TypeError
=======
        pass
>>>>>>> ab0503e (связный список с абстрактным классом)

class StackObj:
    def __init__(self, data):
        self._data = data
        self._next = None



class Stack(StackInterface):
    def __init__(self):
        self._top = None

    def push_back(self, obj):
        if not self._top:
            self._top = obj
<<<<<<< HEAD
            return
=======
            return None
>>>>>>> ab0503e (связный список с абстрактным классом)
        next = self._top
        while next._next != None:
            next = next._next
        next._next = obj

    def __add__(self, other):
        self.push_back(other)
        return self

    def __mul__(self, other):
        for _ in other:
            self.push_back(StackObj(_))
        return self

    def pop_back(self):
        if not self._top:
            return
        if self._top._next == None:
            x = self._top
            self._top = None
            return x
        last = self._top
        pre_last = self._top
        while last._next != None:
            pre_last = last
            last = last._next
        x = pre_last._next
        pre_last._next = None
        return x



