from product import Product

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, download_size: float):
        super().__init__(product_id, name, price, stock)
        self.download_size = download_size

    def display_info(self):
        super().display_info()
        print(f"Download Size: {self.download_size} MB")