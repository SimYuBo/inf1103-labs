import json

INVENTORY_FILE = "inventory.json"

class FileHandling:
    def __init__(self):
        self._file_path = INVENTORY_FILE

    def load_inventory(self) -> list[dict]:
        with open(self._file_path, "r") as f:
            inventory = json.load(f)
            print("Inventory loaded successfully.")
        return inventory

    def save_inventory(self, data) -> None:
        print("Saving inventory to file...")
        with open(self._file_path, "w") as f:
            json.dump(data, f, indent=4)
            print("Inventory saved successfully.")