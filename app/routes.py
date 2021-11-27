from flask import render_template, redirect, url_for, request
#from flask_login import current_user, login_required, login_user, logout_user
from app import app


@app.route('/profile', methods=['POST', 'GET'])
def profile():
    return render_template('profile.html', title='Profile')


@app.route('/profile/employment', methods=['POST', 'GET'])
def career_info():
    return render_template('career_info.html', title='Career Information')


@app.route('/profile/background', methods=['POST', 'GET'])
def career_background():
    return render_template('career_background.html', title='Career Background')


@app.route('/profile/skills', methods=['POST', 'GET'])
def skills():
    return render_template('skills.html', title='Skills')


@app.route('/profile/projects', methods=['POST', 'GET'])
def projects():
    return render_template('projects.html', title='Projects')


@app.route('/profile/links', methods=['POST', 'GET'])
def links():
    return render_template('links.html', title='Links')