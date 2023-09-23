from flask import Flask
import os

global app
app = Flask(__name__, template_folder=os.path.abspath('./templates'))

from .db import db, db_url
db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = db_url

from website.public.routes import client_bp
app.register_blueprint(client_bp, url_prefix='')

with app.app_context():
    db.create_all()
