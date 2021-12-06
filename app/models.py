from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.String(150), nullable=False ,default='images/default.png')
    fname = db.Column(db.String(200))
    lname = db.Column(db.String(200))
    email = db.Column(db.String(150), index=True, unique=True)
    password = db.Column(db.String(150))
    profile = db.relationship('Profile', backref='profile', uselist=False)
    background = db.relationship('Background', backref='background')
    skills = db.relationship('Skills', backref='skills')
    projects = db.relationship('Projects', backref='projects')
    links = db.relationship('Links', backref='links')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


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
    job_status = db.Column(db.String(150))
    job_type = db.Column(db.String(150))
    excepted_salary = db.Column(db.String(150))
    military_service = db.Column(db.String(150))
    work_tech = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Background(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(150))
    company_name = db.Column(db.String(100))
    employment_date = db.Column(db.String(80))
    quit_date = db.Column(db.String(80))
    about_job = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Skills(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(200))
    level = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Projects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    url = db.Column(db.String(100))
    tech = db.Column(db.String(100))
    about = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class Links(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200))
    link_type = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))