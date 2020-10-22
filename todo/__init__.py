from flask import Flask
from flask_cors import CORS

from .routes import bp as routes_bp
from .extension import migrate, database, marshmallow
from todo.config import ProdConfig, Config


def create_app(config_object: Config = ProdConfig) -> Flask:
    """Create Flask app, register blueprints and extensions.

    Args:
         config_object: Configuration object.

    Returns:
        Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)

    CORS(app)

    register_blueprints(app)
    register_extensions(app)

    app.app_context().push()

    from todo.models.user import User
    from todo.models.task import Task

    return app


def register_blueprints(app: Flask) -> None:
    """Register blueprints in application.

    Args:
        app: Flask application.

    Returns:
        None.
    """
    app.register_blueprint(routes_bp, url_prefix='/')


def register_extensions(app: Flask) -> None:
    """Register extensions in application.

    Args:
         app: Flask application.

    Returns:
        None.
    """
    database.init_app(app)
    migrate.init_app(app, database)
    marshmallow.init_app(app)
