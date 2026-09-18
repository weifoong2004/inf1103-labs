MAX_CAPACITY = 500
TAX_RATE = 0.10

def get_valid_input():
    user_input = input("Enter stock quantity: ").strip()
 
    if user_input.lower() == "quit":
        return "quit"
 
    if not user_input.isdigit():
        if user_input.startswith("-") and user_input[1:].isdigit():
            print("Error: Number cannot be negative. Please try again.")
        else:
            print("Error: Invalid input. Please enter a valid integer.")
        return None
 
    return int(user_input)

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * TAX_RATE

def is_over_capacity(total):
    return total > MAX_CAPACITY

def generate_report(total_units, failed_attempts, deliveries=0, total_tax=0.0):
    print("\n====== Inventory Audit Report ======")
    print("Total Deliveries Processed:", deliveries)
    print("Total Units in Inventory:", total_units)
    print("Total Tax Collected:", round(total_tax, 2))
    print("Number of Failed/Rejected Entries:", failed_attempts)
    print("====================================")

def main():
    total_inventory = 0
    deliveries_processed = 0
    failed_entries = 0
    total_tax = 0.0

    print("== Smart Inventory System ==")
    print("Enter a stock quantity, or type 'quit' to finish.\n")

    while True:
        entry = get_valid_input()

        if entry == "quit":
            generate_report(total_inventory, failed_entries,
                deliveries_processed, total_tax)
            break

        if entry is None:
            failed_entries += 1
            continue

        total_inventory = process_delivery(total_inventory, entry)
        tax = calculate_tax(entry)
        total_tax += tax
        deliveries_processed += 1

        if is_over_capacity(total_inventory):
            print("Warning: Total inventory exceeds", MAX_CAPACITY, "units.")
            break
        elif total_inventory == MAX_CAPACITY:
            print("Notice: Total inventory at max capacity (500 units).")
        else:
            pass

        print(f"Accepted {entry} units | Tax: {round(tax, 2)} | "
                f"Total inventory: {total_inventory}")


if __name__ == "__main__":
    main()