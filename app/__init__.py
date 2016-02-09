from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_compress import Compress

from config import config

compress = Compress()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    compress.init_app(app)

    # attach routes and custom error pages here

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app