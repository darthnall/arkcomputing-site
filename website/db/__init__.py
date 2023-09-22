from flask_sqlalchemy import SQLAlchemy
from square.client import Client as SquareClient
from os import environ

db = SQLAlchemy()
square_client = SquareClient(access_token=environ['SQUARE_ACCESS_TOKEN'], environment='sandbox')

class Product:
    def __init__(self, id):
        # query = query_db(db)
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
