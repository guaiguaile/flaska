# project/__init__.py
from flask import Flask

def create_app():
    from . import common, routes, services
    app = Flask(__name__)
    common.init_app(app)
    routes.init_app(app)
    services.init_app(app)
    return app