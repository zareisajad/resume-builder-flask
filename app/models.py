from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app import db


class Resume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_status = db.Column(db.String(120))
    desired_type_job = db.Column(db.String(120))
    expected_salary = db.Column(db.String(100))
    military_service = db.Column(db.String(80))
    fav_technologies = db.Column(db.String(200))
    user = db.relationship('User', backref='user')


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    image = db.Column(db.String(150))
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    phone = db.Column(db.String(80))
    email = db.Column(db.String(150), index=True, unique=True)
    age = db.Column(db.String(150))
    title = db.Column(db.String(150))
    city = db.Column(db.String(80))
    Identification_number = db.Column(db.String(80))
    marital_status = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    about = db.Column(db.String(700))
    password = db.Column(db.String(150))
    resume_id = db.Column(db.Integer, db.ForeignKey('resume.id'))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)