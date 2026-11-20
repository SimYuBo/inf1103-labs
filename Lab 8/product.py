from abc import ABC, abstractmethod
from copy import copy as shallow_copy
from supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier):
        self._id: str = product_id
        self._name: str = name
        self._price: float = price
        self._stock: int = stock
        self._supplier: Supplier = supplier

    def get_product_id(self) -> str:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    def get_stock(self) -> int:
        return self._stock

    def get_supplier(self) -> Supplier:
        return self._supplier

    def update_stock(self, quantity: int) -> None:
        self._stock = quantity

    def copy(self) -> "Product":
        return shallow_copy(self)

    def display_info(self) -> None:
        print(f"Product ID: {self._id}")
        print(f"Name: {self._name}")
        print(f"Price: ${self._price:.2f}")
        print(f"Stock: {self._stock} units")
        self._supplier.display_information()

    def to_record(self) -> dict:
        return {
            "id": self._id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock,
            "supplier": self._supplier.to_record()
        }

    @abstractmethod
    def get_fulfillment_info(self) -> str:
        pass