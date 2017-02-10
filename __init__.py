from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import os

app = Flask(__name__)
app.secret_key = "\x92M-\x16\xaf&\x883<?d\x11\x8b' \x04K\xac\xbdL\xc1\x16\xd0I"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
db = SQLAlchemy(app)

#configuration authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.init_app(app)




