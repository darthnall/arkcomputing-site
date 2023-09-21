from flask import render_template
from flask import request
from flask import Blueprint
from ..client import Client
from ..db import Product
import os

position = {
        "mark": "president",
        "noah": "vice president",
        "blake": "chief technical officer",
        }

client_bp = Blueprint("client", __name__)

client = Client(name=os.environ["CLIENT_NAME"])
staff = client.staff()

# Static routes
@client_bp.route("/")
def home():
    return render_template('home.html', client=client, title="Home")

@client_bp.route("/about")
def about():
    return render_template("about/home.html", client=client, staff=staff, position=position)

# Dynamic routes
@client_bp.route("/store", methods = ["POST", "GET"])
@client_bp.route("/shop",  methods = ["POST", "GET"])
def store():
    if request.method == "POST":
        product = Product(id=0)
        searchword = request.args.get("product")
        return render_template("store/product.html", searchword=searchword, client=client, title=product.name, product=product)
    product = Product(id=0)
    return render_template("store/details.html", client=client, product=product, title="Store")
