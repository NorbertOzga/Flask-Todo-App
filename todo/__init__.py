from flask import Flask
from flask_cors import CORS

from .extension import migrate, db, ma
from ..config import ProdConfig, Config


def create_app(config: Config = ProdConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    CORS(app)

    register_blueprints(app)
    register_extensions(app)

    return app


def register_blueprints(app):
    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp, url_prefix='/')


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
