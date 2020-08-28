from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fjidoaspfhnsduiopfbdwuifnioapsfhjasd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///static/todo.db'

db = SQLAlchemy(app)