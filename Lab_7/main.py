import json
import os

from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INVENTORY_FILE = os.path.join(SCRIPT_DIR, "inventory.json")

DEFAULT_PRODUCTS = [
    {"type": "physical", "id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15, "weight": 2.2},
    {"type": "physical", "id": "P002", "name": "Mouse", "price": 25.50, "stock": 40, "weight": 0.15},
    {"type": "physical", "id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25, "weight": 0.8},
    {"type": "digital", "id": "P004", "name": "Antivirus Software", "price": 39.99, "stock": 100, "download_size": 250},
]


def create_product_from_dict(data):
    product_type = data.get("type")

    if product_type == "physical":
        return PhysicalProduct(data["id"], data["name"], data["price"],
                                data["stock"], data["weight"])
    elif product_type == "digital":
        return DigitalProduct(data["id"], data["name"], data["price"],
                               data["stock"], data["download_size"])
    else:
        raise ValueError(f"Unknown product type: {product_type!r}")


def load_inventory(filename):
    inventory = Inventory()

    if os.path.exists(filename):
        print(f"{filename} found.")
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            for item in data:
                inventory.add_product(create_product_from_dict(item))
            print("Inventory loaded successfully.")
            return inventory
        except (json.JSONDecodeError, ValueError, KeyError) as e:
            print(f"Warning: {filename} is corrupted or invalid ({e}). "
                  f"Starting with default inventory.")
    else:
        print(f"{filename} not found. Starting with default inventory.")

    for item in DEFAULT_PRODUCTS:
        inventory.add_product(create_product_from_dict(item))
    return inventory


def save_inventory(filename, inventory):
    data = [product.to_dict() for product in inventory.get_all_products()]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Inventory saved successfully to {filename}.")


def add_product_flow(inventory):
    print("Add New Product")
    print("1. Physical Product")
    print("2. Digital Product")
    type_choice = input("Select product type (1 or 2): ").strip()

    if type_choice not in ("1", "2"):
        print("Error: Invalid product type selected. Product not added.")
        return

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

    if type_choice == "1":
        try:
            weight = float(input("Weight (kg): ").strip())
        except ValueError:
            print("Error: Weight must be a number. Product not added.")
            return
        if weight < 0:
            print("Error: Weight cannot be negative. Product not added.")
            return
        product = PhysicalProduct(product_id, name, price, stock, weight)

    else:  # type_choice == "2"
        try:
            download_size = float(input("Download Size (MB): ").strip())
        except ValueError:
            print("Error: Download size must be a number. Product not added.")
            return
        if download_size < 0:
            print("Error: Download size cannot be negative. Product not added.")
            return
        product = DigitalProduct(product_id, name, price, stock, download_size)

    if inventory.add_product(product):
        print("Product added successfully!")
        print(product.get_fulfilment_info())


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
    print(product.get_fulfilment_info())           

    if isinstance(product, CanBeShipped):
        print(f"Estimated Shipping Cost: ${product.calculate_shipping_cost():.2f}")
    print("-" * 50)


# display_menu()
def display_menu():
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


# main()
def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM (OOP + Inheritance)")
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