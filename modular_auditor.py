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

inventory = 0
failedEntries = 0
while True:
    quantity = get_valid_input()
    if quantity == "quit":
        print("\nQuitting...")
        break
    elif quantity == None:
        failedEntries += 1
        continue
    inventory += quantity
    print("Accepted. Current total inventory: " + str(inventory))
    if inventory > 500:
        print("ALERT: Overstock detected! Total inventory (" + str(inventory) + ") exceeds 500 units.")
        break
    elif inventory == 500:
        print("Notice: Inventory has reached exactly the 500 unit limit.")
    else:
        pass

print("\n--- Inventory Audit Report ---")
print("Total Units Processed: " + str(inventory))
print("Number of Failed/Rejected Entries: " + str(failedEntries))