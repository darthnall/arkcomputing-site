from flask import abort
from flask import render_template
from flask import request
from flask import Blueprint
from .config import Client
import os

client_bp = Blueprint("client", __name__)

client = Client(name=os.environ["CLIENT_NAME"])
staff = client.staff()

# Static routes
@client_bp.route("/")
def home():
    return render_template('home.html', client=client, title="Home")

@client_bp.route("/store", methods = ["POST", "GET"])
@client_bp.route("/shop",  methods = ["POST", "GET"])
def store():
    error = None
    if request.method == "POST":
        searchword = request.args.get("product")
        return render_template("product.html", searchword=searchword, client=client, title="Store")
    return render_template("store.html", client=client, title="Store")

# Static routes
@client_bp.route("/about")
def about():
    return render_template("about/home.html", client=client, staff=staff, position={"mark":"president",
                                                                                    "noah":"vice president",
                                                                                    "blake": "chief technical officer",
                                                                                    })
