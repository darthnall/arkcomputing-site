from website import app

# DB imports
from flask_marshmallow import Marshmallow
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
from website.db import Product, User
from website.db import ProductSchema, UserSchema

db = SQLAlchemy()
ma = Marshmallow(app)
db_url = "sqlite:///site.db"
square_client = SquareClient(access_token=environ['SQUARE_ACCESS_TOKEN'], environment='sandbox')
