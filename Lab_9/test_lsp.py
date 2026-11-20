
from product import Product
from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from inventory import Inventory


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


supplier = Supplier("S001", "ABC Electronics", "abc@gmail.com")

physical = PhysicalProduct("P001", "Laptop", 1200.0, 10, 2.5, supplier)
digital = DigitalProduct("D001", "Software", 50.0, 100, 500.0, supplier)

print("Testing PhysicalProduct:")
show_product_details(physical)

print("\nTesting DigitalProduct:")
show_product_details(digital)

inventory = Inventory()
inventory.add_product(physical)
inventory.add_product(digital)

print("\nTesting both products in Inventory:")
inventory.display_all()
