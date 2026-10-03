import json

INVENTORY_FILE = "inventory.json"

def load_inventory():
    with open(INVENTORY_FILE, "r") as f:
        inventory = json.load(f)
    return inventory

def save_inventory(inventory):
    with open(INVENTORY_FILE, "w") as f:
        json.dump(inventory, f, indent=4)

