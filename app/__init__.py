from flask import Flask
from .config import Config
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

app.config['SECRET_KEY'] = 'abc876'

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://wdwazwnycsykht:8bb3c26492762ddc44aa51b434f9a2d01ff10385e3f952d242f22fecb4c1982a@ec2-54-164-22-242.compute-1.amazonaws.com:5432/dai6q5vj9arafj'

from app import views, models
