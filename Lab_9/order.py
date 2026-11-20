from product import Product
from order_line import OrderLine


class Order:
    def __init__(self, order_id: str) -> None:
        self._order_id: str = order_id
        self._order_lines: list[OrderLine] = []

    def get_order_id(self) -> str:
        return self._order_id

    def get_order_lines(self) -> list[OrderLine]:
        return self._order_lines.copy()

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self._order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> bool:
        for order_line in self._order_lines:
            if order_line.get_product().get_id() == product_id:
                self._order_lines.remove(order_line)
                return True
        return False

    def calculate_total(self) -> float:
        total = 0.0
        for order_line in self._order_lines:
            total += order_line.calculate_subtotal()
        return total

    def display_order(self) -> None:
        print(f"\nOrder ID: {self._order_id}")
        print("-" * 50)
        for order_line in self._order_lines:
            product = order_line.get_product()
            print(f"{product.get_name()} x {order_line.get_quantity()}")
            print(f"Subtotal: ${order_line.calculate_subtotal():.2f}")
        print("-" * 50)
        print(f"Total: ${self.calculate_total():.2f}")
