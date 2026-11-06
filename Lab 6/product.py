class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self._id = product_id
        self._name = name
        self._price = price
        self._stock = stock

    def get_product_id(self) -> str:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    def get_stock(self) -> int:
        return self._stock

    def update_stock(self, quantity: int):
        self._stock = quantity

    def copy(self) -> "Product":
        return Product(self._id, self._name, self._price, self._stock)