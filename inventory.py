from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

class Inventory:
    def __init__(self):
        self._products: dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        product_id = product.get_product_id()
        if product_id in self._products:
            raise ValueError(f"Product ID '{product_id}' already exists.")
        self._products[product_id] = product.copy()

    def search_product(self, product_id: str) -> Product | None:
        product = self._products.get(product_id)
        if product is None:
            return None
        return product.copy()

    def update_stock(self, product_id: str, quantity: int) -> None:
        product = self._products.get(product_id)
        if product is None:
            raise ValueError(f"Product ID '{product_id}' not found.")
        product.update_stock(quantity)
        print(f"Stock for '{product.get_name()}' updated to {product.get_stock()} successfully.")

    def display_all(self) -> tuple[Product, ...]:
        return tuple(product.copy() for product in self._products.values())

    def to_records(self) -> list[dict]:
        return [product.to_record() for product in self._products.values()]

    def load_records(self, records: list[dict]) -> None:
        self._products = {}
        for record in records:
            self.add_product(self._create_product(record))

    @staticmethod
    def _create_product(record: dict) -> Product:
        product_type = record.get("type")
        if product_type == "physical":
            return PhysicalProduct(record["id"], record["name"], record["price"],
                                   record["stock"], record["weight"])
        if product_type == "digital":
            return DigitalProduct(record["id"], record["name"], record["price"],
                                  record["stock"], record["download_size"])
        raise ValueError(f"Unknown product type: {product_type!r}")