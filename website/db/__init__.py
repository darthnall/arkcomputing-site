from website import app

# DB imports
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from square.client import Client as SquareClient

# Global imports
from os import environ

# Initialize database
db = SQLAlchemy()
ma = Marshmallow(app)

db_url = "sqlite:///site.db"
square_client = SquareClient(access_token=environ['SQUARE_ACCESS_TOKEN'], environment='sandbox')

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
db.init_app(app)

with app.app_context():
    db.create_all()
