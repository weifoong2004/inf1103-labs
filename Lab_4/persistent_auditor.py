MAX_CAPACITY = 500
TAX_RATE = 0.10
INVENTORY_FILE = "inventory.txt"

def load_inventory(filename):
    total = 0
    history = []
 
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
 
        if lines:
            # First line holds the running total
            total = int(lines[0].strip())
            # Every following line is one past transaction amount
            history = [int(line.strip()) for line in lines[1:] if line.strip()]
 
        print(f"Loaded previous inventory from '{filename}': "
              f"total = {total}, {len(history)} past transaction(s).")
 
    except FileNotFoundError:
        print(f"No existing '{filename}' found. Starting with an empty inventory.")
    except (ValueError, IndexError):
        # File exists but is corrupted/unreadable - fail safe rather than crash
        print(f"Warning: '{filename}' was unreadable. Starting with an empty inventory.")
        total, history = 0, []
 
    return total, history


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

def generate_report(total_units, failed_attempts, deliveries=0, total_tax=0.0, history=None):
    history = history or []
    print("\n====== Inventory Audit Report ======")
    print("Total Deliveries Processed:", deliveries)
    print("Total Units in Inventory:", total_units)
    print("Total Tax Collected:", round(total_tax, 2))
    print("Number of Failed/Rejected Entries:", failed_attempts)
    print("Transaction History (all-time):", history)
    print("====================================")

def main():

    total_inventory, history = load_inventory(INVENTORY_FILE)
    deliveries_processed = 0
    failed_entries = 0
    total_tax = 0.0

    print("== Smart Inventory System ==")
    print("Enter a stock quantity, or type 'quit' to finish.\n")

    while True:
        entry = get_valid_input()

        if entry == "quit":
            generate_report(total_inventory, failed_entries,
                deliveries_processed, total_tax, history)
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

if __name__ == "__main__":
    main()