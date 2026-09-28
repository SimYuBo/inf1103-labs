# Global constants
MAX_CAPACITY = 500
TAX_RATE = 0.10
INVENTORY_FILE = "inventory.txt"

# Inventory item structure
ITEM_FIELDS = {
    "id": 0,
    "name": 1,
    "quantity": 2,
    "transaction_history": 3
}

FIELD_SEPARATOR = ","
HISTORY_SEPARATOR = "|"

def get_valid_input():
    userInput = input("Enter stock quantity (or 'quit' to finish): ").strip()
    if userInput.lower() == "quit":
        return "quit"
    elif not userInput.isdigit():
        print("Error: '" + userInput + "' is not a valid whole number. Please try again.")
        return None
    quantity = int(userInput)
    if quantity < 0:
        print("Error: Negative stock quantities are not allowed.")
        return None
    return quantity

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * TAX_RATE

def generate_report(total_units, failed_attempts):
    print("\n--- Inventory Audit Report ---")
    print("Total Deliveries Processed: " + str(total_units))
    print("Number of Failed/Rejected Entries: " + str(failed_attempts))

def load_inventory():
    inventory = []
    transaction_history = {}
    try:
        with open(INVENTORY_FILE, "r") as f:
            lines = f.read().splitlines()
    except FileNotFoundError:
        return inventory, transaction_history

    for line in lines:
        if not line.strip():
            continue
        parts = line.split(FIELD_SEPARATOR)
        if len(parts) != len(ITEM_FIELDS):
            continue
        try:
            item_id = int(parts[ITEM_FIELDS["id"]])
            name = parts[ITEM_FIELDS["name"]]
            quantity = int(parts[ITEM_FIELDS["quantity"]])
            history = [int(x) for x in parts[ITEM_FIELDS["transaction_history"]].split(HISTORY_SEPARATOR) if x]
        except ValueError:
            continue
        inventory.append([item_id, name, quantity])
        transaction_history[item_id] = history

    return inventory, transaction_history

inventory, transaction_history = load_inventory()
failedEntries = 0
deliveriesProcessed = 0
while True:
    quantity = get_valid_input()
    if quantity == "quit":
        print("\nQuitting...")
        break
    elif quantity == None:
        failedEntries += 1
        continue
    inventory = process_delivery(inventory, quantity)
    tax = calculate_tax(quantity)
    deliveriesProcessed += 1
    print("Accepted. Current total inventory: " + str(inventory) + ", Tax: " + str(tax))
    if inventory > MAX_CAPACITY:
        print("ALERT: Overstock detected! Total inventory (" + str(inventory) + ") exceeds " + str(MAX_CAPACITY) + " units.")
        break
    elif inventory == MAX_CAPACITY:
        print("Notice: Inventory has reached exactly the " + str(MAX_CAPACITY) + " unit limit.")
    else:
        pass

generate_report(deliveriesProcessed, failedEntries)