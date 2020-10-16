from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

database = SQLAlchemy()
marshmallow = Marshmallow()
migrate = Migrate()
