from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

database = SQLAlchemy()
marshmallow = Marshmallow()
migrate = Migrate()
jwt = JWTManager()
