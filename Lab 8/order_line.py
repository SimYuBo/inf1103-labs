from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self.product: Product = product
        self.quantity: int = quantity

    def get_product(self) -> Product:
        return self.product

    def get_quantity(self) -> int:
        return self.quantity

    def calculate_subtotal(self) -> float:
        return self.product.get_price() * self.quantity

    def display_info(self) -> None:
        print(f"{self._product.get_name()} ({self._product.get_product_id()}) "
              f"x {self._quantity} @ ${self._product.get_price():.2f} "
              f"= ${self.calculate_subtotal():.2f}")