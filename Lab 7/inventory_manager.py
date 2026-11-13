from file_handling import FileHandling
from product import Product
from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped

class Main:
    def __init__(self):
        self._inventory = Inventory()
        self._file_handler = FileHandling()
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
        product.display_info()
        print(product.get_fulfillment_info())
        if isinstance(product, CanBeShipped):
            print(f"Shipping Cost: ${product.calculate_shipping_cost():.2f}")
        print("------------------")
 
    def _display_all(self) -> None:
        print("\nCurrent Inventory")
        print("-----------------")
        for p in self._inventory.display_all():
            p.display_info()
            print("-----------------")

    def _add_product(self) -> None:
        print("\nAdd New Product")
        print("-----------------")
        print("Choose product type:")
        print("1. Physical Product")
        print("2. Digital Product")
        while True:
            product_type = input("Enter your choice (1 or 2): ")
            if product_type in ("1", "2"):
                break
            print("Invalid choice. Please enter 1 or 2.")
        product_id = input("Enter product ID: ")
        name = input("Enter name: ")
        price = self._read_non_negative_float("Enter price: ")
        stock = self._read_non_negative_int("Enter stock quantity: ")
        if product_type == "1":
            weight = self._read_non_negative_float("Enter weight (kg): ")
            product = PhysicalProduct(product_id, name, price, stock, weight)
        else:
            download_size = self._read_non_negative_float("Enter download size (MB): ")
            product = DigitalProduct(product_id, name, price, stock, download_size)
        
        try:
            self._inventory.add_product(product)
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

if __name__ == "__main__":
    Main().run()