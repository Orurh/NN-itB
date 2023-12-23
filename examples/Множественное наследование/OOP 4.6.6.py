class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self):
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self):
        return self._id


class ShopGenericView:
    ''' без переопределения итератора'''
    def __init__(self):
        pass

    def __str__(self):
        return '\n'.join(f'{i}: {j}' for i, j in self.__dict__.items())


class ShopUserView:
    ''' с переопределением итератора'''
    def __init__(self):
        pass

    def __repr__(self):
        return '\n'.join(self.__next__())

    def __next__(self):
        for i, j in self.__dict__.items():
            if i != '_id':
                yield f'{i}: {j}'

class Book(ShopItem, ShopUserView):
    def __init__(self, title, author, year):
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


book = Book("Python ООП", "Балакирев", 2022)
print(book)
