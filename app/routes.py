from flask import render_template, redirect, url_for, request
from flask_login import current_user, login_required, login_user, logout_user

from app import app, login
from app.models import User, Resume


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html', title='home')


@app.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    return render_template('sign_up.html', title='home')


@app.route('/sign-in', methods=['POST', 'GET'])
def sign_in():
    return render_template('sign_in.html', title='home')


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    return render_template('resume-forms/profile.html', title='Profile')


@app.route('/profile/employment', methods=['POST', 'GET'])
@login_required
def career_info():
    return render_template('resume-forms/career_info.html', title='Career Information')


@app.route('/profile/background', methods=['POST', 'GET'])
@login_required
def career_background():
    return render_template('resume-forms/career_background.html', title='Career Background')


@app.route('/profile/skills', methods=['POST', 'GET'])
@login_required
def skills():
    return render_template('resume-forms/skills.html', title='Skills')


@app.route('/profile/projects', methods=['POST', 'GET'])
@login_required
def projects():
    return render_template('resume-forms/projects.html', title='Projects')


@app.route('/profile/links', methods=['POST', 'GET'])
@login_required
def links():
    return render_template('resume-forms/links.html', title='Links')


@app.route('/profile/resume', methods=['POST', 'GET'])
@login_required
def resume():
    #resume = Resume.query.all()
    return render_template('resume.html')