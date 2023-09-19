from flask import Blueprint, render_template

client_bp = Blueprint('client', __name__)

@client_bp.route('/')
def home():
    return render_template('bookmark.html', brand="?BRAND_NAME?")
