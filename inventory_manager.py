import json

INVENTORY_FILE = "inventory.json"

def load_inventory():
    with open(INVENTORY_FILE, "r") as f:
        inventory = json.load(f)
        print("Inventory loaded successfully.")
    return inventory

def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as f:
        print("Saving inventory to file...")
        json.dump(inventory, f, indent=4)
        print("Inventory saved successfully.")

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
    print(f"Product '{name}' added successfully.")
    return inventory

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

def search_product(inventory):
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

def main():
    print("========================")
    print("Inventory Management System")
    print("========================")
    inventory = load_inventory()
    
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
            display_all(inventory)
        elif choice == '2':
            inventory = add_product(inventory)
        elif choice == '3':
            inventory = update_stock(inventory)
        elif choice == '4':
            search_product(inventory)
        elif choice == '5':
            save_inventory(inventory)
        elif choice == '6':
            print("Saving inventory before exiting...")
            save_inventory(inventory)
            print("Thank you for using Inventory Management System.\nProgram terminated.")
            break
        else:
            print("Invalid choice. Please try again.")

main()