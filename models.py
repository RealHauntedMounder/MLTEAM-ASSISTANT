from config import db, ForeignKey, relationship
from flask_login import UserMixin


user_organisation = db.Table('user_organisation',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('organisation_id', db.Integer, db.ForeignKey('organisation.id'), primary_key=True)
)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lastname = db.Column(db.String(20))
    firstname = db.Column(db.String(20))
    email = db.Column(db.String(30))
    password = db.Column(db.String(30))
    age = db.Column(db.Integer())
    birthday = db.Column(db.Date())
    phone = db.Column(db.String(20))
    address = db.Column(db.String(50))
    education = db.Column(db.String(50))
    experience = db.Column(db.Integer())
    qualities = db.Column(db.String(50))

    organisations = db.relationship('Organisation', secondary=user_organisation, backref=db.backref('users', lazy='dynamic'))

class Organisation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    address = db.Column(db.String(50))
    email = db.Column(db.String(30))
    phone = db.Column(db.String(20))
    description = db.Column(db.Text())


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisation.id'))
    organisation = db.relationship('Organisation', backref=db.backref('departments', lazy='dynamic'))


class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    description = db.Column(db.Text())

class Permission_user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    permission_id = db.Column(db.Integer, db.ForeignKey('permission.id'))
    permission = db.relationship('Permission', backref=db.backref('permission_users', lazy='dynamic'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('permission_users', lazy='dynamic'))
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisation.id'))
    organisation = db.relationship('Organisation', backref=db.backref('permission_users', lazy='dynamic'))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    department = db.relationship('Department', backref=db.backref('permission_users', lazy='dynamic'))




