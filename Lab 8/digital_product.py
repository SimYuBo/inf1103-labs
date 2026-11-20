from product import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int,
                 supplier: Supplier, download_size: float):
        super().__init__(product_id, name, price, stock, supplier)
        self.download_size: float = download_size

    def get_download_size(self) -> float:
        return self.download_size

    def display_info(self) -> None:
        super().display_info()
        print(f"Download Size: {self.download_size} MB")

    def get_fulfillment_info(self) -> str:
        return "Digital Product: Can be downloaded directly from the website."

    def to_record(self) -> dict:
        record = super().to_record()
        record["type"] = "digital"
        record["download_size"] = self.download_size
        return record
