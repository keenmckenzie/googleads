from flask import Flask

from ad_manager import ppc

app = Flask(__name__)

from ad_manager.ppc.routes import mod

app.register_blueprint(ppc.routes.mod)
