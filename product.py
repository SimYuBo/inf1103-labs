class Product:
    def __init__(self, product_id, name, price, stock):
        self.id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, new_stock):
        self.stock = new_stock

    def display_all(self):
        print(f"ID: {self.id} | Name: {self.name} | Price: ${self.price:.2f} | Stock: {self.stock}")

    def add_product(self, inventory):
        new_item = {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }
        inventory.append(new_item)
        print(f"Product '{self.name}' added successfully.")
        return inventory

    def search_product(self, inventory):
        item = next((item for item in inventory if item['id'] == self.id), None)
        if item is None:
            print(f"Error: Product ID '{self.id}' not found.")
            return
        print("Product Found:\n------------------")
        print(f"ID: {item['id']}\nName: {item['name']}\nPrice: ${item['price']:.2f}\nStock: {item['stock']}")
        print("------------------")

    