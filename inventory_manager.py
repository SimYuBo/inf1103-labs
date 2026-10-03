import json

INVENTORY_FILE = "inventory.json"

def load_inventory():
    with open(INVENTORY_FILE, "r") as f:
        inventory = json.load(f)
    return inventory

def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f, indent=4)

def display_all(inventory):
    print("\nCurrent Inventory")
    print("-----------------")
    for item in inventory:
        print(f"ID: {item['id']} | Name: {item['name']} | Price: ${item['price']:.2f} | Stock: {item['stock']}")
    print("-----------------")

def add_product(inventory):
    print("\nAdd New Product")
    print("-----------------")
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
    save_inventory(inventory)
    print(f"Product '{name}' added successfully.")

def update_stock(inventory):
    print("\nUpdate Stock")
    print("-----------------")
    item_id = input("Enter product ID to update: ")
    item = next((item for item in inventory if item['id'] == item_id), None)
    
    if item is None:
        print(f"Error: Product ID '{item_id}' not found.")
        return
    
    new_stock = int(input(f"Enter new stock quantity for '{item['name']}': "))
    item['stock'] = new_stock
    save_inventory(inventory)
    print(f"Stock for '{item['name']}' updated to {new_stock} successfully.")
