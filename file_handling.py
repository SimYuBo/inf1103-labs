import json

class FileHandling:
    INVENTORY_FILE = "inventory.json"
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