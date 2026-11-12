from abc import ABC, abstractmethod
from supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float,
                stock: int, supplier: Supplier):
        self._product_id = product_id
        self._name = name
        self._price = price
        self._stock = stock
        self._supplier: Supplier = supplier
    # -------------------------------------------------------------
    # Getters: controlled, read-only access to the attributes
    # -------------------------------------------------------------
    def get_id(self):
        return self._product_id

    def get_name(self):
        return self._name

    def get_price(self):
        return self._price

    def get_stock(self):
        return self._stock

    def get_supplier(self) -> Supplier:
        return self._supplier

    def update_stock(self, quantity):
        if not isinstance(quantity, int):
            print("Error: Stock quantity must be an integer.")
            return False
        if quantity < 0:
            print("Error: Stock quantity cannot be negative.")
            return False
        self._stock = quantity
        return True

    def display_information(self) -> None:
        print(f"ID: {self._product_id} | Name: {self._name} | "
            f"Price: ${self._price:.2f} | Stock: {self._stock}")
        print(f"Supplier: {self._supplier.get_name()}")

    @abstractmethod
    def get_fulfilment_info(self):
        pass

    def to_dict(self):
        return {
            "id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock,
        }