from flask import Flask
from flask_cors import CORS

from ..config import ProdConfig, Config


def create_app(config: Config = ProdConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    CORS(app)

    register_blueprints(app)

    return app


def register_blueprints(app):
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp, url_prefix='/')
