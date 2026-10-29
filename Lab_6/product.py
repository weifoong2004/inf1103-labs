"""
INF1103 Lab 6 - Object-Oriented Programming
Product class

Single Responsibility: represent and manage ONE product's own data.
This class knows nothing about files, menus, or the rest of the
inventory - it only knows how to look after itself.
"""


class Product:
    def __init__(self, product_id, name, price, stock):
        # "Private" attributes (by convention - the double underscore
        # triggers Python's name mangling). External code is expected
        # to go through the public methods below rather than touching
        # these directly.
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    # -------------------------------------------------------------
    # Getters: controlled, read-only access to the private attributes
    # -------------------------------------------------------------
    def get_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    # -------------------------------------------------------------
    # update_stock(quantity): the ONLY way outside code should change
    # stock. Because it's a method rather than a direct assignment,
    # the Product gets to validate the value before accepting it -
    # that's what encapsulation buys us.
    # -------------------------------------------------------------
    def update_stock(self, quantity):
        if not isinstance(quantity, int):
            print("Error: Stock quantity must be an integer.")
            return False
        if quantity < 0:
            print("Error: Stock quantity cannot be negative.")
            return False
        self.__stock = quantity
        return True

    # -------------------------------------------------------------
    # display_information(): the Product knows how to describe itself
    # -------------------------------------------------------------
    def display_information(self):
        print(f"ID: {self.__product_id} | Name: {self.__name} | "
              f"Price: ${self.__price:.2f} | Stock: {self.__stock}")

    # -------------------------------------------------------------
    # to_dict() / from_dict(): conversion helpers so a Product can be
    # written to / read from JSON. Saving/loading FILES is still not
    # this class's job (that stays in main.py), but knowing how to
    # turn itself into a plain dict is reasonably "about the product
    # itself," so it stays here.
    # -------------------------------------------------------------
    def to_dict(self):
        return {
            "id": self.__product_id,
            "name": self.__name,
            "price": self.__price,
            "stock": self.__stock,
        }

    @staticmethod
    def from_dict(data):
        return Product(data["id"], data["name"], data["price"], data["stock"])