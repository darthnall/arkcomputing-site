from website.db import db, ma

# Production Database schema
class User(db.Model):
    id            = db.Column(db.String(32), primary_key=True)
    name          = db.Column(db.String(32))
    username      = db.Column(db.String(16))
    email         = db.Column(db.String(120))
    address       = db.Column(db.String(32))
    is_subscribed = db.Column(db.String(32))

class UserSchema(ma.SQLAlchemyAutoSchema):
    pass

class Product(db.Model):
    id            = db.Column(db.String(32), primary_key=True)
    name          = db.Column(db.String(32), unique=False, nullable=True)
    unit_price    = db.Column(db.Float(12),  unique=False, nullable=True)
    is_hot        = db.Column(db.Boolean,    unique=False, nullable=True, default=False)
    category      = db.Column(db.String(12), unique=False, nullable=True, default="")
    tags          = db.Column(db.List(db.String(12), unique=False, nullable=True, default=["test_tag"]))

class ProductSchema(ma.SQLAlchemyAutoSchema):
    pass

# Future inventory stuff
class Report(db.Model):
    #id: Mapped[int] = mapped_column(Integer, primary_key=True)
    #date: Mapped[DateTime] = mapped_column(DateTime, unique=False, nullable=True)
    start_date = db.Column(db.String(12), unique=False, nullable=False)
    end_date = db.Column(db.String(12), unique=False, nullable=False)
    prices = db.relationship('Build', back_populates='build')

class Manufacturer(db.Model):
    #id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name = db.Column(db.String, unique=False,   nullable=False)
    partner = db.Column(db.Boolean, nullable=False, default=False)
    sponsor = db.Column(db.Boolean, nullable=False, default=False)

class Build(db.Model):
    #id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name = db.Column(db.String, unique=False, nullable=False)
