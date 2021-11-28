import os
from posix import EX_TEMPFAIL

from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.security import check_password_hash
from werkzeug.utils import secure_filename

from app import app, login, db
from app.models import User, Resume


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html', title='home')


@app.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user and password1 != password2:
            #flash("Somthing's wrong. please try again.")
            return redirect(url_for('sign_up'))
        user = User(email=email)
        user.set_password(password1)
        db.session.add(user)
        db.session.commit()
        #flash('Your are now ready to sign in! have fun.')
        return redirect(url_for('sign_in'))
    return render_template('sign_up.html', title='home')


@app.route('/sign-in', methods=['POST', 'GET'])
def sign_in():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user and not user.check_password(password):
            #flash("Somthing's wrong. please try again.")
            return redirect(url_for('sign_in'))
        login_user(user)
        #flash("You logged in to your account.", category="success")
        return redirect(url_for('profile'))
    return render_template('sign_in.html', title='home')


@app.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('home'))


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/profile', methods=['POST', 'GET'])
@login_required
def profile():
    if request.method == 'POST':
        img = request.files['img']
        filename = secure_filename(img.filename)
        if filename != '':
            img.save(os.path.join(app.config["UPLOAD_PATH"], filename))
        img_url = os.path.join("/images", filename)
        print(img_url)
        user = User.query.filter_by(id=current_user.id).first()
        if user:
            user.image=img_url
            user.fname=request.form.get('fname')
            user.lname=request.form.get('lname')
            user.phone=request.form.get('phone')
            user.title=request.form.get('title')
            user.age=request.form.get('age')
            user.identifi_number=request.form.get('identifi')
            user.marital_status=request.form.get('marital')
            user.about=request.form.get('about')
        if request.form.get('gender') == 'other':
            user.gender = request.form.get('gender-text')
        else:
            user.gender = request.form.get('gender')
        db.session.commit()
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