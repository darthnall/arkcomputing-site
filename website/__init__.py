from flask import Flask
from .db import db, db_url
import os

global app
app = Flask(__name__, template_folder=os.path.abspath('./templates'))
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

db.init_app(app)

from website.public.routes import client_bp
app.register_blueprint(client_bp, url_prefix='')

with app.app_context():
    db.create_all()
