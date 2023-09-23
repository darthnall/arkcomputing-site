from dataclasses import dataclass, field
from datetime import datetime


# Back-end creates these objects, the front-end calls them after creation.
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
    homepage: str = field(default="https://arkcomputing.net/")
    staff: list[str] = field(default_factory=list)

    def fullname(self) -> str:
        return f"{self.name}, {self.ext}"
