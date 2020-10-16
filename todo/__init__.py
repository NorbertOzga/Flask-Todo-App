from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    CORS(app)

    register_blueprints(app)

    return app


def register_blueprints(app):
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp, url_prefix='/')
