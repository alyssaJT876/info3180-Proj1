from flask import Flask
from .config import Config
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

app.config['SECRET_KEY'] = 'abc876'

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://project1:Password123@localhost/project1'

from app import views, models
