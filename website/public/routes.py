from flask import render_template
from flask import request
from flask import Blueprint
from flask import redirect
from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError

from website.public import Client
from website.db.database import Query

# Eventually, this dictionary will be created by Client
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
    return render_template('home.html', client=client)

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

@client_bp.route("/add_item", methods=["POST"])
def add_item():
    name = request.form.get("name", "")
    price = request.form.get("price", "0")
    qty = request.form.get("qty", "0")
    is_hot = request.form.get("is_hot", "")
    dop = request.form.get("dop", "0")

    if not name or not dop:
        return "Name and Date of Purchase are required fields. Please try again."

    payload = {
            "name": name,
            "price": price,
            "qty": qty,
            "is_hot": is_hot,
            "dop": dop,
            }

    #try:
    #    with Query() as query:
    #        query.add_item(payload=payload)
    #except SQLAlchemyError:
    #    redirect("/")

    return jsonify(payload)
