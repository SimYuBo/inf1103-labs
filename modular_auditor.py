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
    return amount * 0.10

inventory = 0
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
    if inventory > 500:
        print("ALERT: Overstock detected! Total inventory (" + str(inventory) + ") exceeds 500 units.")
        break
    elif inventory == 500:
        print("Notice: Inventory has reached exactly the 500 unit limit.")
    else:
        pass

print("\n--- Inventory Audit Report ---")
print("Total Deliveries Processed: " + str(deliveriesProcessed))
print("Number of Failed/Rejected Entries: " + str(failedEntries))