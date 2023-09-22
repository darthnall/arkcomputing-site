# Form validation imports
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

# Type imports
from dataclasses import dataclass, field

# Generic imports
from datetime import datetime

# Dataclasses for front-end
#
# These classes are purely for the front-end,
# and they call the Database class for their data.

@dataclass(init=True, repr=True)
class Product:
    id: int
    name: str
    price: float
    qty: int
    dop: datetime

    def __str__(self):
        return f"ID: {self.id} -> {self.name}\nQTY: {self.qty}\nUNIT PRICE: ${self.price}\nTOTAL VALUE: ${self.price * self.qty:.2f}"

@dataclass
class Client:
    id: int = field(repr=False, default=0)
    name: str = field(default="Ark Computing")
    ext: str = field(default="LLC")
    staff: list = field(default=["mark", "noah", "blake"])

    def fullname(self, name, ext) -> str:
        return f"{name} {ext}"
