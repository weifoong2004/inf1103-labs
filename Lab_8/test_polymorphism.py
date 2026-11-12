
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory

# Create supplier
supplier = Supplier("S001", "ABC Electronics", "abc@gmail.com")

# Create different product types
physical = PhysicalProduct("P001", "Laptop", 1200.0, 10, 2.5, supplier)
digital = DigitalProduct("D001", "Software", 50.0, 100, 500.0, supplier)

# Create inventory
inventory = Inventory()

# Add both products
inventory.add_product(physical)
inventory.add_product(digital)

# Test polymorphism
print("Testing Polymorphism")
print("-" * 50)

for product in inventory.get_all_products():
    product.display_information()
    print(product.get_fulfilment_info())
    print("-" * 50)
