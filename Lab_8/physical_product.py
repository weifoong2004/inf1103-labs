from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier

SHIPPING_RATE_PER_KG = 2.50  # simple rule: $2.50 per kilogram


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float,
                stock: int, weight: float, supplier: Supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self._weight = weight

    def get_weight(self):
        return self._weight

    # Method overriding: reuse the parent's display first (common
    # info), then add what's unique to a physical product.
    def display_information(self):
        super().display_information()
        print(f"Weight: {self._weight} kg")

    # Implements Product's abstract method
    def get_fulfilment_info(self):
        return f"{self.get_name()} requires physical shipping."

    # Implements CanBeShipped's abstract method
    def calculate_shipping_cost(self):
        return round(self._weight * SHIPPING_RATE_PER_KG, 2)

    # Extend the parent's to_dict() with this type's own data
    def to_dict(self):
        data = super().to_dict()
        data["type"] = "physical"
        data["weight"] = self._weight
        return data