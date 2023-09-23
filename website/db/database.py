import uuid

from website.db import db
from website.db.converters import *
from website.db.models import Product, User
from website.db.models import ProductSchema, UserSchema

product_schema = ProductSchema()
user_schema = UserSchema()

class Query:
    def __init__(self):
        pass

    def add_item(self, payload):
        self.id = uuid.uuid4()
        for key, value in payload.items():
            print(f"{key}:{value}, {self.id}")

    def get_items(self):
        pass

    def __enter__(self):
        db.session.begin()

    def __exit__(self):
        db.session.close()
