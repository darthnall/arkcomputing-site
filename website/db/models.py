from website.db import db, ma

# Production Database schema
class User(db.Model):
    id            = db.Column(db.String(32),  primary_key=True)
    name          = db.Column(db.String(32),  unique=False, nullable=False)
    username      = db.Column(db.String(16),  unique=True,  nullable=False)
    email         = db.Column(db.String(120), unique=False, nullable=False)
    address       = db.Column(db.String(32),  unique=False, nullable=True)
    is_subscribed = db.Column(db.Boolean,     unique=False, nullable=False, default=False)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_fk = True


class Product(db.Model):
    id            = db.Column(db.String(32), primary_key=True)
    name          = db.Column(db.String(32), unique=False, nullable=False)
    price         = db.Column(db.Float(12),  unique=False, nullable=False)
    qty           = db.Column(db.Integer, unique=False, nullable=True)
    dop           = db.Column(db.DateTime,   unique=True,  nullable=True)
    is_hot        = db.Column(db.Boolean,    unique=False, nullable=True, default=False)
    category      = db.Column(db.String(12), unique=False, nullable=True, default="")

class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        include_fk = True


# Future inventory stuff
