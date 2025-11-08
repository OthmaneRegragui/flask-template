# ./app/extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# 1. Create extension instances
# These are not yet attached to any specific Flask application.
db = SQLAlchemy()
migrate = Migrate()

# You would add other extensions here as well, for example:
# from flask_login import LoginManager
# login_manager = LoginManager()