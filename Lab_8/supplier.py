class Supplier:
    def __init__(self, supplier_id: str, name: str, contact_email: str) -> None:
        self._supplier_id: str = supplier_id
        self._name: str = name
        self._contact_email: str = contact_email

    def get_supplier_id(self) -> str:
        return self._supplier_id

    def get_name(self) -> str:
        return self._name

    def get_contact_email(self) -> str:
        return self._contact_email

    def display_information(self) -> None:
        print(f"Supplier ID: {self._supplier_id}")
        print(f"Name: {self._name}")
        print(f"Contact Email: {self._contact_email}")
