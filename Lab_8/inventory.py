from product import Product

class Inventory:
    def __init__(self):
        self._products: list[Product] = []
    # -------------------------------------------------------------
    # add_product(product): store a Product object in the collection
    # -------------------------------------------------------------
    def add_product(self, product):
        if self.search_product(product.get_id()) is not None:
            print(f"Error: Product ID '{product.get_id()}' already exists. "
                  f"Product not added.")
            return False
        self._products.append(product)
        return True

    # -------------------------------------------------------------
    # search_product(product_id): find and return a Product, or None
    # -------------------------------------------------------------
    def search_product(self, product_id):
        for product in self._products:
            if product.get_id() == product_id:
                return product
        return None

        # -------------------------------------------------------------
    # find_product(product_id): find and return a Product, or None
    # -------------------------------------------------------------
    def find_product(self, product_id: str) -> Product | None:
        for product in self._products:
            if product.get_id() == product_id:
                return product
        return None


    # -------------------------------------------------------------
    # display_all(): ask every Product to describe itself
    # -------------------------------------------------------------
    def display_all(self):
        print("Current Inventory")
        print("-" * 50)
        if not self._products:
            print("No products in inventory.")
        for product in self._products:
            product.display_information()
        print("-" * 50)

    # -------------------------------------------------------------
    # add_product(): add Product to inventory
    # -------------------------------------------------------------

    def add_product(self, product: Product) -> bool:
        if self.search_product(product.get_id()) is not None:
            print(f"Error: Product ID '{product.get_id()}' already exists. "
                f"Product not added.")
            return False

        self._products.append(product)
        return True

    # -------------------------------------------------------------
    # remove_product(product_id): remove a Product from inventory
    # -------------------------------------------------------------
    def remove_product(self, product_id: str) -> bool:
        product = self.find_product(product_id)

        if product is not None:
            self._products.remove(product)
            return True

        return False



    # -------------------------------------------------------------
    # get_all_products(): hands back the list so the main program can,
    # -------------------------------------------------------------
    def get_all_products(self):
        return self._products