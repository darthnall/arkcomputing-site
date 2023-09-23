from flask import render_template
from flask import request
from flask import Blueprint
from flask import redirect

from website.public import Client

position = {
        "mark": "president",
        "noah": "vice president",
        "blake": "chief technical officer",
        }

client_bp = Blueprint("client", __name__)
client = Client(id=0, name="Ark Computing", ext="LLC", staff=["mark", "noah", "blake"])

# Static routes
@client_bp.route("/")
def home():
    return render_template('home.html', client=client, title="Home")

@client_bp.route("/about")
def about():
    return render_template("about/home.html", client=client, staff=client.staff, position=position)

# Dynamic routes
@client_bp.route("/store", methods = ["POST", "GET"])
@client_bp.route("/shop",  methods = ["POST", "GET"])
def store():
    return render_template("store/details.html", title="Store")

@client_bp.route("/submit", methods=["GET", "POST"])
def submit():
    return render_template("home.html")
