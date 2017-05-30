from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config


bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    from wdsauth.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from wdsauth.epicenter import epicenter as epicenter_blueprint
    app.register_blueprint(epicenter_blueprint)

    return app
