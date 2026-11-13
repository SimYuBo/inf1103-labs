from product import Product
from supplier import Supplier
from can_be_shipped import CanBeShipped

BASE_SHIPPING_COST = 5.0   # flat fee
COST_PER_KG = 2.0          # per kilogram

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier, weight: float):
        super().__init__(product_id, name, price, stock, supplier)
        self.weight: float = weight

    def get_weight(self) -> float:
        return self.weight

    def display_info(self) -> None:
        super().display_info()
        print(f"Weight: {self.weight} kg")

    def get_fulfillment_info(self) -> str:
        return "Physical Product: Requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return BASE_SHIPPING_COST + (COST_PER_KG * self.weight)

    def to_record(self) -> dict:
        record = super().to_record()
        record["type"] = "physical"
        record["weight"] = self.weight
        return record
