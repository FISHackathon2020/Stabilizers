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
    app = Flask(__name__)
    app.config.from_object(Config)

    db = SQLAlchemy(app)

    return db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from project.auth.routes import auth
    from project.social.routes import social
    app.register_blueprint(auth)
    app.register_blueprint(social)

    return app