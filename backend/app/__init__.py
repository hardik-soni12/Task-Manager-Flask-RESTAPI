from flask import Flask
from .extensions import db, bcrypt, jwt, migrate
from backend.config import Config_dict


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config_dict[config_name])

    # Initialize extentions
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    migrate.init_app(app, db)

    return app