import json
import os

from product import Product
from inventory import Inventory

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INVENTORY_FILE = os.path.join(SCRIPT_DIR, "inventory.json")

DEFAULT_PRODUCTS = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
]


# ---------------------------------------------------------------
# File Handling: load_inventory(filename)
# In : the file path to read from
# Out: an Inventory object, populated with Product objects
# ---------------------------------------------------------------
def load_inventory(filename):
    inventory = Inventory()

    if os.path.exists(filename):
        print(f"{filename} found.")
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            for item in data:
                inventory.add_product(Product.from_dict(item))
            print("Inventory loaded successfully.")
            return inventory
        except (json.JSONDecodeError, ValueError, KeyError):
            print(f"Warning: {filename} is corrupted. Starting with default inventory.")
    else:
        print(f"{filename} not found. Starting with default inventory.")

    # Fresh start / corrupted file: fall back to the default products
    for item in DEFAULT_PRODUCTS:
        inventory.add_product(Product.from_dict(item))
    return inventory


# ---------------------------------------------------------------
# File Handling: save_inventory(filename, inventory)
# In : the file path, the Inventory object
# Out: nothing (writes to disk)
# ---------------------------------------------------------------
def save_inventory(filename, inventory):
    data = [product.to_dict() for product in inventory.get_all_products()]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Inventory saved successfully to {filename}.")


# ---------------------------------------------------------------
# add_product_flow(inventory): gets input, builds a Product, adds it
# ---------------------------------------------------------------
def add_product_flow(inventory):
    print("Add New Product")

    product_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()

    try:
        price = float(input("Price: ").strip())
        stock = int(input("Stock Quantity: ").strip())
    except ValueError:
        print("Error: Price/Stock must be numbers. Product not added.")
        return

    if price < 0 or stock < 0:
        print("Error: Price and stock cannot be negative. Product not added.")
        return

    product = Product(product_id, name, price, stock)
    if inventory.add_product(product):
        print("Product added successfully!")


# ---------------------------------------------------------------
# update_stock_flow(inventory): finds a product, asks for new stock,
# and lets the Product itself validate and apply the change
# ---------------------------------------------------------------
def update_stock_flow(inventory):
    print("Update Stock")
    product_id = input("Enter Product ID: ").strip()

    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")

    new_stock = input("New Stock Quantity: ").strip()
    if not new_stock.isdigit():
        print("Error: Invalid stock quantity. Update cancelled.")
        return

    if product.update_stock(int(new_stock)):
        print("Stock updated successfully!")


# ---------------------------------------------------------------
# search_product_flow(inventory): finds and displays a single product
# ---------------------------------------------------------------
def search_product_flow(inventory):
    print("Search Product")
    product_id = input("Enter Product ID: ").strip()

    product = inventory.search_product(product_id)
    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print("-" * 50)
    product.display_information()
    print("-" * 50)


# ---------------------------------------------------------------
# display_menu(): prints the menu options
# ---------------------------------------------------------------
def display_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


# ---------------------------------------------------------------
# main(): owns the menu loop and delegates to Inventory/Product
# ---------------------------------------------------------------
def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM (OOP)")
    print("=" * 40)

    inventory = load_inventory(INVENTORY_FILE)

    while True:
        display_menu()
        choice = input("Enter option: ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            add_product_flow(inventory)

        elif choice == "3":
            update_stock_flow(inventory)

        elif choice == "4":
            search_product_flow(inventory)

        elif choice == "5":
            print("Saving inventory...")
            save_inventory(INVENTORY_FILE, inventory)

        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(INVENTORY_FILE, inventory)
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please choose a number between 1 and 6.")


if __name__ == "__main__":
    main()