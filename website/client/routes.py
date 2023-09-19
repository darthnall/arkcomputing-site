from flask import Blueprint, render_template
import os

client_bp = Blueprint("client", __name__)

brand = os.environ["BRAND"]

@client_bp.route("/")
def home():
    return render_template('home.html', brand=brand)

@client_bp.route("/store")
@client_bp.route("/shop")
def shop():
    return render_template("store.html", brand=brand, title="Store")
