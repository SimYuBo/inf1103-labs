# Global constants
MAX_CAPACITY = 500
TAX_RATE = 0.10
INVENTORY_FILE = "inventory.txt"
FIELD_SEPARATOR = ","
HISTORY_SEPARATOR = "|"

# Inventory item structure
ITEM_FIELDS = {
    "id": 0,
    "name": 1,
    "quantity": 2,
    "transaction_history": 3
}

def get_valid_input(prompt):
    userInput = input(prompt).strip()
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
        parts = line.split(FIELD_SEPARATOR)
        item = [None] * len(ITEM_FIELDS)
        item[ITEM_FIELDS["id"]] = parts[ITEM_FIELDS["id"]]
        item[ITEM_FIELDS["name"]] = parts[ITEM_FIELDS["name"]]
        item[ITEM_FIELDS["quantity"]] = int(parts[ITEM_FIELDS["quantity"]])
        
        history_text = parts[ITEM_FIELDS["transaction_history"]]
        history = [int(x) for x in history_text.split(HISTORY_SEPARATOR) if x]
        item[ITEM_FIELDS["transaction_history"]] = history

        inventory.append(item)
        transaction_history[item[ITEM_FIELDS["id"]]] = history

    return inventory, transaction_history

def save_inventory(inventory, transaction_history):
    with open(INVENTORY_FILE, "w") as f:
        for item in inventory:
            item_id = item[ITEM_FIELDS["id"]]
            history = HISTORY_SEPARATOR.join(str(x) for x in transaction_history.get(item_id, []))
            f.write(FIELD_SEPARATOR.join([
                str(item_id),
                item[ITEM_FIELDS["name"]],
                str(item[ITEM_FIELDS["quantity"]]),
                history
            ]) + "\n")

def find_item(inventory, item_id):
    for item in inventory:
        if item[ITEM_FIELDS["id"]] == item_id:
            return item
    return None           

inventory, transaction_history = load_inventory()
failed_entries = 0
deliveries_processed = 0
while True:
    id_input = get_valid_input("Enter item ID (or 'quit' to finish): ")
    if id_input == "quit":
        print("\nQuitting...")
        break
    if id_input is None:
        failed_entries += 1
        continue

    item = find_item(inventory, str(id_input))
    if item is None:
        print("Error: Item ID " + str(id_input) + " not found.")
        failed_entries += 1
        continue

    quantity = get_valid_input("Enter delivery quantity for " + item[ITEM_FIELDS["name"]] + " (or 'quit'): ")
    if quantity == "quit":
        print("\nQuitting...")
        break
    if quantity is None:
        failed_entries += 1
        continue

    item[ITEM_FIELDS["quantity"]] = process_delivery(item[ITEM_FIELDS["quantity"]], quantity)
    item_id = item[ITEM_FIELDS["id"]]
    transaction_history.setdefault(item_id, []).append(quantity)
    item[ITEM_FIELDS["transaction_history"]] = transaction_history[item_id]

    tax = calculate_tax(quantity)
    deliveries_processed += 1

    total_inventory = sum(i[ITEM_FIELDS["quantity"]] for i in inventory)
    print("Accepted. " + item[ITEM_FIELDS["name"]] + " now at " + str(item[ITEM_FIELDS["quantity"]])
          + ", Total inventory: " + str(total_inventory) + ", Tax: " + str(tax))

    if total_inventory > MAX_CAPACITY:
        print("ALERT: Overstock detected! Total inventory (" + str(total_inventory)
              + ") exceeds " + str(MAX_CAPACITY) + " units.")
        break
    elif total_inventory == MAX_CAPACITY:
        print("Notice: Inventory has reached exactly the " + str(MAX_CAPACITY) + " unit limit.")

save_inventory(inventory, transaction_history)
generate_report(deliveries_processed, failed_entries)