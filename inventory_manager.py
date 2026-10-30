import json
from product import Product

INVENTORY_FILE = "inventory.json"

class Inventory:
    def __init__(self):
        self._products = dict[str, Product] = {}

    def add_product(self, product) -> None:
        product_id = product.get_product_id()
        if product_id in self._products:
            raise ValueError(f"Product ID '{product_id}' already exists.")
        self._products[product_id] = product.copy()
        print(f"Product '{product.get_name()}' added successfully.")

    def search_product(self, product_id: str) -> Product | None:
        product = self._products.get(product_id)
        if product is None:
            print(f"Error: Product ID '{product_id}' not found.")
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

'''
def add_product(inventory):
    
    item_id = input("Enter product ID: ")
    name = input("Enter name: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock quantity: "))
    
    new_item = {
        "id": item_id,
        "name": name,
        "price": price,
        "stock": stock
    }
    
    inventory.append(new_item)
    print(f"Product '{name}' added successfully.")
    return inventory

    def search_product(self, product_id: str) -> Product[0_1]:
        print("\nSearch Product")
        print("-----------------")
        item_id = input("Enter product ID to search: ")
        item = next((item for item in inventory if item['id'] == item_id), None)
        
        if item is None:
            print(f"Error: Product ID '{item_id}' not found.")
            return
        
        print("Product Found:\n------------------")
        print(f"ID: {item['id']}\nName: {item['name']}\nPrice: ${item['price']:.2f}\nStock: {item['stock']}")
        print("------------------")

            def display_all(self, inventory):
        print("\nCurrent Inventory")
        print("-----------------")
        for item in inventory:
            print(f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}")
        print("-----------------")

        
def update_stock(inventory):
    print("\nUpdate Stock")
    print("-----------------")
    item_id = input("Enter product ID to update: ")
    item = next((item for item in inventory if item['id'] == item_id), None)
    
    if item is None:
        print(f"Error: Product ID '{item_id}' not found.")
        return

    print(f"Current stock for '{item['name']}': {item['stock']}")
    new_stock = int(input(f"Enter new stock quantity for '{item['name']}': "))
    item['stock'] = new_stock
    print(f"Stock for '{item['name']}' updated to {new_stock} successfully.")
    return inventory
'''
    
inventory = Inventory() # creating the inventory object from the Inventory class 
product1 = Product("P001", "Laptop", 1200.00, 15) # creating product from Product class, via init 
product2 = Product("P002", "Mouse", 25.50, 40) 
inventory.add_product(product1) # pass the product to inventory class to store in a list 
inventory.add_product(product2)

def main():
    print("========================")
    print("Inventory Management System")
    print("========================")
    inventory = FileHandling.load_inventory()
    
    while True:
        print("\n----------MENU----------")
        print("1. Display All Products")
        print("2. Add New Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save inventory")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            inventory.display_all()
        elif choice == '2':
            print("\nAdd New Product")
            print("-----------------")
            inventory = add_product(inventory)
        elif choice == '3':
            inventory = update_stock(inventory)
        elif choice == '4':
            print("\nSearch Product")
            print("-----------------")
            product_id = input("Enter product ID to search: ")
            product =inventory.search_product(product_id)
            print("Product Found:\n------------------")
            print(f"ID: {product.get_product_id()}\nName: {product.get_name()}\nPrice: ${product.get_price():.2f}\nStock: {product.get_stock()}")
            print("------------------")
        elif choice == '5':
            FileHandling.save_inventory(inventory)
        elif choice == '6':
            print("Saving inventory before exiting...")
            FileHandling.save_inventory(inventory)
            print("Thank you for using Inventory Management System.\nProgram terminated.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()