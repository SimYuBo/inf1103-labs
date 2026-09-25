MAX_CAPACITY = 500
TAX_RATE = 0.10
INVENTORY_FILE = "inventory.txt"

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
    try:
        with open(INVENTORY_FILE, "r") as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0
    except ValueError:
        print("Error: Inventory file is corrupted. Starting with 0 inventory.")
        return 0

inventory = load_inventory()
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