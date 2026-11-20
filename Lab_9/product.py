from abc import ABC, abstractmethod
from supplier import Supplier


class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, supplier: Supplier) -> None:
        self._product_id: str = product_id
        self._name: str = name
        self._price: float = price
        self._stock: int = stock
        self._supplier: Supplier = supplier

    def get_id(self) -> str:
        return self._product_id

    def get_name(self) -> str:
        return self._name

    def get_price(self) -> float:
        return self._price

    def get_stock(self) -> int:
        return self._stock

    def get_supplier(self) -> Supplier:
        return self._supplier

    def update_stock(self, quantity: int) -> bool:
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
    def get_fulfilment_info(self) -> str:
        pass

    def to_dict(self) -> dict[str, str | float | int | dict[str, str]]:
        return {
            "id": self._product_id,
            "name": self._name,
            "price": self._price,
            "stock": self._stock,
            "supplier": {
                "supplier_id": self._supplier.get_supplier_id(),
                "name": self._supplier.get_name(),
                "contact_email": self._supplier.get_contact_email(),
            },
        }
