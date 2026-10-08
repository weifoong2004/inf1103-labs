import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INVENTORY_FILE = os.path.join(SCRIPT_DIR, "inventory.json")

DEFAULT_INVENTORY = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
]

def load_inventory(filename):
    """Load inventory from a JSON file, or fall back to default data."""
    if os.path.exists(filename):
        print(f"{filename} found.")
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            print("Inventory loaded successfully.")
            return data
        except (json.JSONDecodeError, ValueError):
            print(f"Warning: {filename} is corrupted. Starting with default inventory.")
            return [product.copy() for product in DEFAULT_INVENTORY]
    else:
        print(f"{filename} not found. Starting with default inventory.")
        return [product.copy() for product in DEFAULT_INVENTORY]


def display_all(inventory):
    print("Current Inventory")
    print("-" * 50)
    if not inventory:
        print("No products in inventory.")
    for product in inventory:
        print(f"ID: {product['id']} | Name: {product['name']} | "
              f"Price: ${product['price']:.2f} | Stock: {product['stock']}")
    print("-" * 50)


def add_product(inventory):
    print("Add New Product")
 
    product_id = input("Product ID: ").strip()
 
    # Prevent duplicate IDs, which would break search_product/update_stock
    if any(product["id"] == product_id for product in inventory):
        print(f"Error: Product ID '{product_id}' already exists. Product not added.")
        return inventory
 
    name = input("Product Name: ").strip()
 
    try:
        price = float(input("Price: ").strip())
        stock = int(input("Stock Quantity: ").strip())
    except ValueError:
        print("Error: Price/Stock must be numbers. Product not added.")
        return inventory
 
    if price < 0 or stock < 0:
        print("Error: Price and stock cannot be negative. Product not added.")
        return inventory
 
    new_product = {"id": product_id, "name": name, "price": price, "stock": stock}
    inventory.append(new_product)
    print("Product added successfully!")
    return inventory

def update_stock(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()
 
    for product in inventory:
        if product["id"] == product_id:
            print("Product Found:")
            print(f"Name: {product['name']}")
            print(f"Current Stock: {product['stock']}")
 
            new_stock = input("New Stock Quantity: ").strip()
            if not new_stock.isdigit():
                print("Error: Invalid stock quantity. Update cancelled.")
                return inventory
 
            product["stock"] = int(new_stock)
            print("Stock updated successfully!")
            return inventory
 
    print("Product not found.")
    return inventory
 
 
def search_product(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ").strip()
 
    for product in inventory:
        if product["id"] == product_id:
            print("Product Found")
            print("-" * 50)
            print(f"ID: {product['id']}")
            print(f"Name: {product['name']}")
            print(f"Price: ${product['price']:.2f}")
            print(f"Stock: {product['stock']}")
            print("-" * 50)
            return product
 
    print("Product not found.")
    return 0

def save_inventory(filename, inventory):
    with open(filename, "w") as f:
        json.dump(inventory, f, indent=4)
    print(f"Inventory saved successfully to {filename}.")



def display_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory(INVENTORY_FILE)

    while True:
        display_menu()
        choice = input("Enter option: ").strip()
 
        if choice == "1":
            display_all(inventory)
 
        elif choice == "2":
            inventory = add_product(inventory)

        elif choice == "3":
            inventory = update_stock(inventory)
 
        elif choice == "4":
            search_product(inventory)

        elif choice == "5":
            print("\nSaving inventory...")
            save_inventory(INVENTORY_FILE, inventory)

        elif choice == "6":
            print("\nSaving inventory before exit...")
            save_inventory(INVENTORY_FILE, inventory)
            print("\nThank you for using Inventory Management System.")
            print("Program terminated.")
            break 

        else:
            print("Invalid option. Please choose a number between 1 and 6.")
 
 
if __name__ == "__main__":
    main()
 
