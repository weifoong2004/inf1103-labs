import csv
from inventory import Inventory
from supplier import Supplier
from product_factory import ProductFactory

def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Please enter a number greater than zero.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number, e.g. 12.50")


def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    loaded = 0

    try:
        file = open(path, newline="", encoding="utf-8-sig")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    else:
        with file:
            reader = csv.reader(file)
            next(reader, None)

            for row_number, row in enumerate(reader, start=2):
                try:
                    product_type, product_id, name, price, stock = row

                    product = ProductFactory.create(
                        product_type,
                        product_id,
                        name,
                        float(price),
                        int(stock),
                        supplier
                    )

                    inventory.add_product(product)
                    loaded += 1

                except ValueError as error:
                    print(f"Skipping row {row_number}: {error}")

        print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished.")
