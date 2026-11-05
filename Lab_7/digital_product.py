from product import Product


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)  # reuse Product's constructor
        self._download_size = download_size

    def get_download_size(self):
        return self._download_size

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self._download_size} MB")

    def get_fulfilment_info(self):
        return f"{self.get_name()} is delivered digitally via download."

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "digital"
        data["download_size"] = self._download_size
        return data