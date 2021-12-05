from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db


class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.String(80))
    about = db.Column(db.String(700))
    age = db.Column(db.Integer)
    title = db.Column(db.String(150))
    city = db.Column(db.String(80))
    identifi_number = db.Column(db.String(80))
    marital_status = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(150), nullable=False ,default='default.png')
    fname = db.Column(db.String(200))
    lname = db.Column(db.String(200))
    email = db.Column(db.String(150), index=True, unique=True)
    password = db.Column(db.String(150))

    profile = db.relationship('Profile', backref='profile', uselist=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)