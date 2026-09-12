total_inventory = 0
units_processed = 0
failed_entries = 0

print("== Smart Inventory System ==")
print("Enter a stock quantity, or type 'quit' to finish.\n")

while True:
    user_input = input("Enter stock quantity: ")

    if user_input.lower() == 'quit':
        print("\nInventory processing complete.")
        print("Total units processed:", units_processed)
        print("Total inventory:", total_inventory)
        print("Failed entries:", failed_entries)
        break

    try:
        quantity = int(user_input)
        if quantity < 0:
            print("Error: Number cannot be negative. Please try again.")
            failed_entries += 1
            continue
        total_inventory += quantity
        units_processed += 1
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        failed_entries += 1
    if total_inventory > 500:
        print("Warning: Total inventory exceeds 500 units.")
        break
    elif total_inventory == 500:
        print("Notice: Total inventory at max capacity (500 units).")
    else:
        pass

