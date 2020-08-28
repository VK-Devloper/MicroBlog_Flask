import os

from flask_admin import Admin

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment

app = Flask(__name__)
admin = Admin(app)
moment = Moment()
login = LoginManager()
login.login_view = 'login'

app.secret_key = 'vaibhav'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
migrate = Migrate(app, db)

from app import routes, models
