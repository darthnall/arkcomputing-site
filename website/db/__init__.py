# DB imports
from flask_sqlalchemy import SQLAlchemy
from square.client import Client as SquareClient
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

# Global imports
from os import environ
from typing import Any
from returns.result import Failure, Success, Result, safe

# Local imports
from .models import Product

db = SQLAlchemy()
db_url = "sqlite:///site.db"
square_client = SquareClient(access_token=environ['SQUARE_ACCESS_TOKEN'], environment='sandbox')

class Database:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    @safe
    def get_all_products(self):
        products = self.session.query(Product).all()
        return products

    @safe
    def add_product(self, product):
        self.session.add(product)
        self.session.commit()

    @safe
    def rm_product(self, id):
        product = self.session.query(Product).get(id)
        if product:
            self.session.delete(product)
            self.session.commit()
        else:
            raise ValueError(f"Product with ID {id} was not found.")

    def __enter__(self):
        self.session = self.Session()
        return self.session

    def __exit__(self, type, value, traceback):
        if type is not None:
            self.session.rollback()
        self.session.close()

if __name__ == "__main__":
    with Database(db_url) as session:
        product = Product(name="Test Product Name")
        session.add(product)
        session.commit()
