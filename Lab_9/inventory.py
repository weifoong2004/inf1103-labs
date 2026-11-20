from product import Product


class Inventory:
    def __init__(self) -> None:
        self._products: list[Product] = []

    def add_product(self, product: Product) -> bool:
        if self.search_product(product.get_id()) is not None:
            print(f"Error: Product ID '{product.get_id()}' already exists. "
                  f"Product not added.")
            return False
        self._products.append(product)
        return True

    def find_product(self, product_id: str) -> Product | None:
        for product in self._products:
            if product.get_id() == product_id:
                return product
        return None

    def search_product(self, product_id: str) -> Product | None:
        return self.find_product(product_id)

    def remove_product(self, product_id: str) -> bool:
        product = self.find_product(product_id)
        if product is None:
            return False
        self._products.remove(product)
        return True

    def display_all(self) -> None:
        print("Current Inventory")
        print("-" * 50)
        if not self._products:
            print("No products in inventory.")
        for product in self._products:
            product.display_information()
        print("-" * 50)

    def display_all_products(self) -> None:
        self.display_all()

    def get_all_products(self) -> list[Product]:
        return self._products
