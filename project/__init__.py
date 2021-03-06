from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from project.config import Config

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

def create_database(config_class=Config):
    global db

    app = Flask(__name__)
    app.config.from_object(Config)

    db = SQLAlchemy(app)

    db.create_all()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.app_context().push()
    db.create_all()

    from project.auth.routes import auth
    from project.social.routes import social
    app.register_blueprint(auth)
    app.register_blueprint(social)

    return app

from project import models
