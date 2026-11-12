
import json
import os

from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory
from supplier import Supplier


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
INVENTORY_FILE = os.path.join(SCRIPT_DIR, "inventory.json")

# Default supplier for products saved before Lab 8
DEFAULT_SUPPLIER = {
    "supplier_id": "S000",
    "name": "Unknown Supplier",
    "contact_email": "unknown@example.com"
}

DEFAULT_PRODUCTS = [
    {"type": "physical", "id": "P001", "name": "Laptop",
     "price": 1200.00, "stock": 15, "weight": 2.2},

    {"type": "physical", "id": "P002", "name": "Mouse",
     "price": 25.50, "stock": 40, "weight": 0.15},

    {"type": "physical", "id": "P003", "name": "Keyboard",
     "price": 45.00, "stock": 25, "weight": 0.8},

    {"type": "digital", "id": "P004", "name": "Antivirus Software",
     "price": 39.99, "stock": 100, "download_size": 250},
]


# -------------------------------------------------------------
# create_supplier_from_dict(): Convert JSON data to Supplier
# -------------------------------------------------------------
def create_supplier_from_dict(data: dict) -> Supplier:
    return Supplier(
        data["supplier_id"],
        data["name"],
        data["contact_email"]
    )


# -------------------------------------------------------------
# create_product_from_dict(): Convert JSON data to Product
# -------------------------------------------------------------
def create_product_from_dict(data: dict) -> Product:
    product_type = data.get("type")

    supplier_data = data.get("supplier", DEFAULT_SUPPLIER)
    supplier = create_supplier_from_dict(supplier_data)

    if product_type == "physical":
        return PhysicalProduct(
            data["id"],
            data["name"],
            data["price"],
            data["stock"],
            data["weight"],
            supplier
        )

    elif product_type == "digital":
        return DigitalProduct(
            data["id"],
            data["name"],
            data["price"],
            data["stock"],
            data["download_size"],
            supplier
        )

    else:
        raise ValueError(f"Unknown product type: {product_type!r}")


# -------------------------------------------------------------
# load_inventory(): Load inventory from JSON
# -------------------------------------------------------------
def load_inventory(filename: str) -> Inventory:
    inventory = Inventory()

    if os.path.exists(filename):
        print(f"{filename} found.")

        try:
            with open(filename, "r") as f:
                data = json.load(f)

            for item in data:
                product = create_product_from_dict(item)
                inventory.add_product(product)

            print("Inventory loaded successfully.")
            return inventory

        except (json.JSONDecodeError, ValueError, KeyError, TypeError) as e:
            print(
                f"Warning: {filename} is corrupted or invalid ({e}). "
                "Starting with default inventory."
            )

            inventory = Inventory()

    else:
        print(f"{filename} not found. Starting with default inventory.")

    for item in DEFAULT_PRODUCTS:
        inventory.add_product(create_product_from_dict(item))

    return inventory


# -------------------------------------------------------------
# save_inventory(): Save products and suppliers to JSON
# -------------------------------------------------------------
def save_inventory(filename: str, inventory: Inventory) -> None:
    data = []

    for product in inventory.get_all_products():
        product_data = product.to_dict()

        supplier = product.get_supplier()

        product_data["supplier"] = {
            "supplier_id": supplier.get_supplier_id(),
            "name": supplier.get_name(),
            "contact_email": supplier.get_contact_email()
        }

        data.append(product_data)

    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Inventory saved successfully to {filename}.")


# -------------------------------------------------------------
# add_product_flow(): Add a new product with Supplier
# -------------------------------------------------------------
def add_product_flow(inventory: Inventory) -> None:
    print("Add New Product")
    print("1. Physical Product")
    print("2. Digital Product")

    type_choice = input("Select product type (1 or 2): ").strip()

    if type_choice not in ("1", "2"):
        print("Error: Invalid product type selected. Product not added.")
        return

    product_id = input("Product ID: ").strip()
    name = input("Product Name: ").strip()

    if not product_id or not name:
        print("Error: Product ID and name cannot be empty.")
        return

    try:
        price = float(input("Price: ").strip())
        stock = int(input("Stock Quantity: ").strip())

    except ValueError:
        print("Error: Price/Stock must be numbers. Product not added.")
        return

    if price < 0 or stock < 0:
        print("Error: Price and stock cannot be negative.")
        return

    # Get Supplier information
    print("\nEnter Supplier Information")

    supplier_id = input("Supplier ID: ").strip()
    supplier_name = input("Supplier Name: ").strip()
    supplier_email = input("Supplier Email: ").strip()

    if not supplier_id or not supplier_name or not supplier_email:
        print("Error: Supplier information cannot be empty.")
        return

    supplier = Supplier(
        supplier_id,
        supplier_name,
        supplier_email
    )

    # Create PhysicalProduct
    if type_choice == "1":
        try:
            weight = float(input("Weight (kg): ").strip())

        except ValueError:
            print("Error: Weight must be a number.")
            return

        if weight < 0:
            print("Error: Weight cannot be negative.")
            return

        product = PhysicalProduct(
            product_id,
            name,
            price,
            stock,
            weight,
            supplier
        )

    # Create DigitalProduct
    else:
        try:
            download_size = float(
                input("Download Size (MB): ").strip()
            )

        except ValueError:
            print("Error: Download size must be a number.")
            return

        if download_size < 0:
            print("Error: Download size cannot be negative.")
            return

        product = DigitalProduct(
            product_id,
            name,
            price,
            stock,
            download_size,
            supplier
        )

    if inventory.add_product(product):
        print("Product added successfully!")
        print(product.get_fulfilment_info())


# -------------------------------------------------------------
# update_stock_flow(): Update Product stock
# -------------------------------------------------------------
def update_stock_flow(inventory: Inventory) -> None:
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


# -------------------------------------------------------------
# search_product_flow(): Search for a Product
# -------------------------------------------------------------
def search_product_flow(inventory: Inventory) -> None:
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

    # Display Supplier information
    print("\nSupplier Information:")
    product.get_supplier().display_information()

    if isinstance(product, CanBeShipped):
        print(
            f"Estimated Shipping Cost: "
            f"${product.calculate_shipping_cost():.2f}"
        )

    print("-" * 50)


# -------------------------------------------------------------
# display_menu(): Display menu options
# -------------------------------------------------------------
def display_menu() -> None:
    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


# -------------------------------------------------------------
# main(): Main program
# -------------------------------------------------------------
def main() -> None:
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM (LAB 8)")
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
