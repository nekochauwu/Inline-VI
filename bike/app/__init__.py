import os, yagmail
from pathlib import PurePath
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

from app import config

db = SQLAlchemy(app)

from app import models

if not os.path.exists(PurePath(__file__).parents[0] / 'instance'):
    with app.app_context():
        db.create_all()

mail = yagmail.SMTP("mail.inline.six@gmail.com","uyfvlkcscovelznw")

from app import routes