from flask import abort
from flask import render_template
from flask import request
from flask import Blueprint
import os

client_bp = Blueprint("client", __name__)

brand = os.environ["BRAND"]

# Static routes
@client_bp.route("/")
def home():
    return render_template('home.html', brand=brand)

@client_bp.route("/store", methods = ["POST", "GET"])
@client_bp.route("/shop",  methods = ["POST", "GET"])
def store():
    if request.method == "POST":
        searchword = request.args.get("product")
        return render_template("store/details.html", searchword=searchword, brand=brand, title="Store")
    return render_template("store/home.html", brand=brand, title="Store")

# Static routes
@client_bp.route("/store")
def product(id=str(0)):
    return render_template('product.html', brand=brand, title=id)
