import unittest
import tempfile
import sys
from pathlib import Path
from unittest.mock import patch
from io import StringIO

# Allow imports from the main project folder
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from supplier import Supplier
from inventory import Inventory
from product_factory import ProductFactory
from discount_strategy import (
    NoDiscount,
    PercentageDiscount,
    BulkDiscount,
    StudentDiscount
)
from order import Order
from csv_loader import get_positive_float, load_products


class Lab9Tests(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001", "ABC Supplies", "abc@example.com"
        )

        self.product = ProductFactory.create(
            "physical", "P001", "Lamp", 25, 10,
            self.supplier, weight=2
        )

    def test_factory(self):
        self.assertEqual(self.product.get_name(), "Lamp")

        digital = ProductFactory.create(
            "digital", "D001", "App", 50, 5,
            self.supplier, download_size=100
        )

        self.assertEqual(digital.get_download_size(), 100)

    def test_unknown_type(self):
        with self.assertRaises(ValueError):
            ProductFactory.create(
                "service", "S001", "Service", 30, 5,
                self.supplier
            )

    def test_validation(self):
        for price, stock in [(0, 1), (-1, 1), (5, -1)]:
            with self.assertRaises(ValueError):
                ProductFactory.create(
                    "physical", "P002", "Bad",
                    price, stock, self.supplier
                )

        order = Order("O001")

        with self.assertRaises(ValueError):
            order.add_order_line(self.product, 0)

    def test_discounts(self):
        order = Order("O001")
        order.add_order_line(self.product, 10)

        self.assertEqual(order.calculate_total(), 250)

        order.set_discount(BulkDiscount(200, 20))
        self.assertEqual(order.calculate_total(), 230)

        order.set_discount(PercentageDiscount(10))
        self.assertEqual(order.calculate_total(), 225)

        order.set_discount(StudentDiscount())
        self.assertEqual(order.calculate_total(), 237.5)

        order.set_discount(NoDiscount())
        self.assertEqual(order.calculate_total(), 250)

    def test_positive_float_retry(self):
        with patch(
            "builtins.input",
            side_effect=["abc", "-5", "12.50"]
        ):
            with patch("sys.stdout", new_callable=StringIO):
                result = get_positive_float("Price: ")

        self.assertEqual(result, 12.5)

    def test_csv_skips_bad_rows(self):
        csv_text = (
            "product_type,product_id,name,price,stock_quantity\n"
            "physical,P001,Lamp,25,10\n"
            "service,S001,Service,30,5\n"
            "physical,P002,Chair,abc,3\n"
            "digital,D001,App,49.9,100\n"
        )

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "products.csv"
            path.write_text(csv_text)

            inventory = Inventory()

            with patch("sys.stdout", new_callable=StringIO) as output:
                load_products(str(path), inventory, self.supplier)

            self.assertEqual(
                len(inventory.get_all_products()), 2
            )
            self.assertIn(
                "2 products loaded.", output.getvalue()
            )

    def test_missing_csv(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "missing.csv"

            with patch("sys.stdout", new_callable=StringIO) as output:
                load_products(
                    str(path), Inventory(), self.supplier
                )

            self.assertIn(
                "Products file not found:",
                output.getvalue()
            )
            self.assertIn(
                "Load attempt finished.",
                output.getvalue()
            )


if __name__ == "__main__":
    unittest.main()
