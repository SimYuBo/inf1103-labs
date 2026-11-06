from product import Product

class PhysicalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, weight: float):
        super().__init__(product_id, name, price, stock)  # Assuming stock is not directly relevant for physical products
        self.weight = weight

    def display_info(self):
        super().display_info()
        print(f"Weight: {self.weight} kg")