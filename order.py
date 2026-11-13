from product import Product
from order_line import OrderLine

class Order:
    def __init__(self, order_id: str):
        self._order_id: str = order_id
        self._order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        self._order_lines.append(OrderLine(product, quantity))

    def remove_order_line(self, product_id: str) -> None:
        for line in self._order_lines:
            if line.get_product().get_product_id() == product_id:
                self._order_lines.remove(line)
                return
        raise ValueError(f"No order line for product '{product_id}' in order '{self._order_id}'.")
 
    def get_order_lines(self) -> tuple[OrderLine, ...]:
        return tuple(self._order_lines)

    def calculate_total(self) -> float:
        return sum(order_line.calculate_subtotal() for order_line in self._order_lines)

    def display_info(self) -> None:
        print(f"Order {self._order_id}")
        for line in self._order_lines:
            line.display_info()
        print(f"Total: ${self.calculate_total():.2f}")