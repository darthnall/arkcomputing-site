from flask import Flask
import os

global app
app = Flask(__name__, template_folder=os.path.abspath('./templates'))


from website.public.routes import client_bp
app.register_blueprint(client_bp, url_prefix='')
