import json
import os


INVENTORY_FILE = "inventory.json"

DEFAULT_INVENTORY = [
    {"id": "P001", "name": "Laptop", "price": 1200.00, "stock": 15},
    {"id": "P002", "name": "Mouse", "price": 25.50, "stock": 40},
    {"id": "P003", "name": "Keyboard", "price": 45.00, "stock": 25},
]


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

    inventory = [product.copy() for product in DEFAULT_INVENTORY] 
 
    while True:
        display_menu()
        choice = input("Enter option: ").strip()
 
        if choice == "1":
            display_all(inventory)
 
        elif choice == "2":
            inventory = add_product(inventory)

        elif choice == "6":
            print("Exiting. Goodbye!")
            break
  
        else:
            print("Invalid option. Please choose a number between 1 and 6.")
 
 
if __name__ == "__main__":
    main()
 
