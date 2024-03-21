from config import db, ForeignKey, relationship
from flask_login import UserMixin


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(20))
    firstname = db.Column(db.String(20))
    email = db.Column(db.String(30))
    password = db.Column(db.String(30))
    age = db.Column(db.Integer())
    birthday = db.Column(db.Date)

