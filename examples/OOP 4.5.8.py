from abc import ABC, abstractmethod


class StackInterface:
    @abstractmethod
    def push_back(self, obj):
        pass

    @abstractmethod
    def pop_back(self):
        raise TypeError

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
            return
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

st = Stack()

obj_top = StackObj("obj")
st.push_back(obj_top)

obj = StackObj("obj")
st.push_back(obj)

n = 0
h = st._top


del_obj = st.pop_back()
assert del_obj == obj, "метод pop_back возвратил неверный объект"

del_obj = st.pop_back()
assert del_obj == obj_top, "метод pop_back возвратил неверный объект"

assert st._top is None, "неверное значение атрибута _top"