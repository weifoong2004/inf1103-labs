"""
INF1103 Lab 6 - Object-Oriented Programming
Inventory class

Single Responsibility: manage a COLLECTION of Product objects.
This class does not know how to load/save files, and it does not
print menus or read user input - it only stores products and lets
you add, search and display them.
"""


class Inventory:
    def __init__(self):
        self.__products = []

    # -------------------------------------------------------------
    # add_product(product): store a Product object in the collection
    # -------------------------------------------------------------
    def add_product(self, product):
        if self.search_product(product.get_id()) is not None:
            print(f"Error: Product ID '{product.get_id()}' already exists. "
                  f"Product not added.")
            return False
        self.__products.append(product)
        return True

    # -------------------------------------------------------------
    # search_product(product_id): find and return a Product, or None
    # -------------------------------------------------------------
    def search_product(self, product_id):
        for product in self.__products:
            if product.get_id() == product_id:
                return product
        return None

    # -------------------------------------------------------------
    # display_all(): ask every Product to describe itself
    # -------------------------------------------------------------
    def display_all(self):
        print("Current Inventory")
        print("-" * 50)
        if not self.__products:
            print("No products in inventory.")
        for product in self.__products:
            product.display_information()
        print("-" * 50)

    # -------------------------------------------------------------
    # get_all_products(): hands back the list so the main program can,
    # e.g., convert it to dicts for saving. Inventory still owns the
    # actual list; this is a read-only view for other code to use.
    # -------------------------------------------------------------
    def get_all_products(self):
        return self.__products