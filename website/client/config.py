import os

class Client:
    def __init__(self, name):
        self._fullname = name.title() + " LLC"
        self._homepage = f"https://{''.join(name.split(' ')).lower()}.net/"
        self._brand = name.title()
        self._staff = []
        stafflist = os.environ[f"{'_'.join(name.upper().split(' '))}_STAFF"]
        for i in stafflist.split(" "):
            self._staff.append(i)

    def fullname(self) -> str | None:
        if self._fullname is not None:
            return str(self._fullname)
        else:
            return None

    def homepage(self) -> str | None:
        if self._homepage is not None:
            return str(self._homepage)
        else:
            return None

    def brand(self) -> str | None:
        if self._brand is not None:
            return str(self._brand)
        else:
            return None

    def staff(self) -> list | None:
        if self._staff is not None:
            return list(self._staff)
        else:
            return None

class Product:
    def __init__(self, id):
        price = 999.999
        self._id = id
        self._name = "Example Product"
        self._price = f"${price:.2f}"
        self._dop = "04-21-2023"
        self._purchased_by = "Mark Thude"
        self._build_id = 0

    def id(self) -> str | None:
        if self._id is not None:
            return str(self._id)
        else:
            return None

    def name(self) -> str | None:
        if self._name is not None:
            return str(self._name)
        else:
            return None

    def price(self) -> str | None:
        if self._price is not None:
            return str(self._price)
        else:
            return None

    def dop(self) -> str | None:
        if self._dop is not None:
            return str(self._dop)
        else:
            return None

    def purchased_by(self) -> str | None:
        if self._purchased_by is not None:
            return str(self._purchased_by)
        else:
            return None

    def build_id(self) -> str | None:
        if self._build_id is not None:
            return str(self._build_id)
        else:
            return None
