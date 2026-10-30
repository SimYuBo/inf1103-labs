import json
from product import Product

INVENTORY_FILE = "inventory.json"

class Inventory:
    def __init__(self):
        self._products: dict[str, Product] = {}

    def add_product(self, product) -> None:
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
        return [
            {
                "id": product.get_product_id(),
                "name": product.get_name(),
                "price": product.get_price(),
                "stock": product.get_stock()
            }
            for product in self._products.values()
        ]

    def load_records(self, records: list[dict]) -> None:
        self._products = {}
        for record in records:
            product = Product(
                product_id=record["id"],
                name=record["name"],
                price=record["price"],
                stock=record["stock"]
            )
            self.add_product(product)

#Class FileHandling:

class FileHandling:
    def __init__(self, file_path: str = INVENTORY_FILE):
        self._file_path = file_path

    def load_inventory(self):
        with open(self._file_path, "r") as f:
            inventory = json.load(f)
            print("Inventory loaded successfully.")
        return inventory

    def save_inventory(self, data):
        print("Saving inventory to file...")
        with open(self._file_path, "w") as f:
            json.dump(data, f, indent=4)
            print("Inventory saved successfully.")

class Main:
    def __init__(self):
        self._file = INVENTORY_FILE
        self._inventory = Inventory()
        self._file_handler = FileHandling(self._file)
        self._inventory.load_records(self._file_handler.load_inventory())

    @staticmethod
    def _read_non_negative_int(prompt: str) -> int:
        while True:
            try:
                value = int(input(prompt))
                if value >= 0:
                    return value
                print("Please enter a non-negative number.")
            except ValueError:
                print("Please enter a whole number.")
 
    @staticmethod
    def _read_non_negative_float(prompt: str) -> float:
        while True:
            try:
                value = float(input(prompt))
                if value >= 0:
                    return value
                print("Please enter a non-negative number.")
            except ValueError:
                print("Please enter a number.")

    @staticmethod
    def _show_product(product: Product) -> None:
        print("Product Found:\n------------------")
        print(f"ID: {product.get_product_id()}")
        print(f"Name: {product.get_name()}")
        print(f"Price: ${product.get_price():.2f}")
        print(f"Stock: {product.get_stock()}")
        print("------------------")
 
    def _display_all(self) -> None:
        print("\nCurrent Inventory")
        print("-----------------")
        for p in self._inventory.display_all():
            print(
                f"ID: {p.get_product_id()} | Name: {p.get_name()} | "
                f"Price: ${p.get_price():.2f} | Stock: {p.get_stock()}"
            )
        print("-----------------")

    def _add_product(self) -> None:
        print("\nAdd New Product")
        print("-----------------")
        product_id = input("Enter product ID: ")
        name = input("Enter name: ")
        price = self._read_non_negative_float("Enter price: ")
        stock = self._read_non_negative_int("Enter stock quantity: ")
        try:
            self._inventory.add_product(Product(product_id, name, price, stock))
            print(f"Product '{name}' added successfully.")
        except ValueError as e:
            print(f"Error: {e}")
 
    def _update_stock(self, product_id: str, quantity: int) -> None:
        try:
            self._inventory.update_stock(product_id, quantity)
            print(f"Stock for '{product_id}' updated to {quantity} successfully.")
        except ValueError as e:
            print(f"Error: {e}")

    def _search_product(self, product_id: str) -> None:
        product = self._inventory.search_product(product_id)
        if product is None:
            print(f"Error: Product ID '{product_id}' not found.")
        else:
            self._show_product(product)
 
    def _save(self) -> None:
        self._file_handler.save_inventory(self._inventory.to_records())

    def run(self) -> None:
        print("========================")
        print("Inventory Management System")
        print("========================")
 
        while True:
            print("\n----------MENU----------")
            print("1. Display All Products")
            print("2. Add New Product")
            print("3. Update Stock")
            print("4. Search Product")
            print("5. Save inventory")
            print("6. Exit")
 
            choice = input("Enter your choice (1-6): ")
 
            if choice == "1":
                self._display_all()
            elif choice == "2":
                self._add_product()
            elif choice == "3":
                print("\nUpdate Stock")
                print("-----------------")
                product_id = input("Enter product ID to update: ")
                quantity = self._read_non_negative_int("Enter new stock quantity: ")
                self._update_stock(product_id, quantity)
            elif choice == "4":
                print("\nSearch Product")
                print("-----------------")
                self._search_product(input("Enter product ID to search: "))
            elif choice == "5":
                self._save()
            elif choice == "6":
                print("Saving inventory before exiting...")
                self._save()
                print("Thank you for using Inventory Management System.\nProgram terminated.")
                break
            else:
                print("Invalid choice. Please try again.")
    
inventory = Inventory() # creating the inventory object from the Inventory class 
product1 = Product("P001", "Laptop", 1200.00, 15) # creating product from Product class, via init 
product2 = Product("P002", "Mouse", 25.50, 40) 
inventory.add_product(product1) # pass the product to inventory class to store in a list 
inventory.add_product(product2)

if __name__ == "__main__":
    Main().run()