from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from typing import Any
from returns.result import Failure, Success, Result, safe

from website.db.models import Product, User
from website.db.models import ProductSchema, UserSchema

# This is where the db logic will go
print("Hello from database.py")
