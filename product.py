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

    def display_info(self):
        print(f"Product ID: {self._id}")
        print(f"Name: {self._name}")
        print(f"Price: ${self._price:.2f}")
        print(f"Stock: {self._stock} units")

    def to_record(self) -> dict:
        return {
            "product_id": self._id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock
        }
