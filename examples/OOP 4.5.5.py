class ShopInterface:
    def get_id(self):
        raise NotImplementedError('в классе не переопределен метод get_id')


class ShopItem(ShopInterface):
    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price
        self._id = id(self)

    def get_id(self):
        return self._id, hash(self)

item1 = ShopItem("имя1", "вес1", "100")
item2 = ShopItem("имя2", "вес2", "200")
print(item1.get_id())
print(item2.get_id())