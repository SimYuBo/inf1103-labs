from product import Product

BASE_SHIPPING_COST = 5.0   # flat fee
COST_PER_KG = 2.0          # per kilogram

class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float):
        super().__init__(product_id, name, price, stock)  # Assuming stock is not directly relevant for physical products
        self.weight = weight

    def get_weight(self) -> float:
        return self.weight

    def display_info(self):
        super().display_info()
        print(f"Weight: {self.weight} kg")

    def get_fulfillment_info(self) -> dict:
        return "Physical Product: Requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return BASE_SHIPPING_COST + (COST_PER_KG * self.weight)

    def to_record(self) -> dict:
        record = super().to_record()
        record["type"] = "physical"
        record["weight"] = self.weight
        return record