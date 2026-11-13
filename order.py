from product import Product
from order_line import OrderLine

class Order:
    def __init__(self, order_id: str):
        self._order_id: str = order_id
        self._order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        self._order_lines.append(OrderLine(product, quantity))

    def calculate_total(self) -> float:
        return sum(order_line.calculate_subtotal() for order_line in self._order_lines)