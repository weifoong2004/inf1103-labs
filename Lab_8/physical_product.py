from product import Product
from supplier import Supplier
from can_be_shipped import CanBeShipped

SHIPPING_RATE_PER_KG: float = 2.50


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float,
                 stock: int, weight: float, supplier: Supplier) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self._weight: float = weight

    def get_weight(self) -> float:
        return self._weight

    def display_information(self) -> None:
        super().display_information()
        print(f"Weight: {self._weight} kg")

    def get_fulfilment_info(self) -> str:
        return f"{self.get_name()} requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return round(self._weight * SHIPPING_RATE_PER_KG, 2)

    def to_dict(self) -> dict[str, str | float | int | dict[str, str]]:
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self._weight
        return data
