from flask import Flask
from flask_cors import CORS

from ad_manager import ppc, api

app = Flask(__name__)

cors=CORS(app, resources={r"/*": {"origins": ["*"]}})

from ad_manager.ppc.routes import mod
from ad_manager.api.routes import mod

app.register_blueprint(ppc.routes.mod)
app.register_blueprint(api.routes.mod, url_prefix='/api')
