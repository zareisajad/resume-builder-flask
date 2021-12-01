import os
import datetime

from flask import render_template, redirect, url_for, request, flash
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.utils import secure_filename

from app import app, login, db
from app.forms import ProfileForm
from app.models import User, Profile


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html', title='home')


@app.route('/sign-up', methods=['POST', 'GET'])
def sign_up():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user and password1 != password2:
            #flash("Somthing's wrong. please try again.")
            return redirect(url_for('sign_up'))
        user = User(fname=fname, lname=lname, email=email)
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
        if not user or not user.check_password(password):
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
    form = ProfileForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            img = form.photo.data
            filename = secure_filename(img.filename)
            if filename != '':
                img.save(os.path.join(app.config["UPLOAD_PATH"], filename))
            img_url = os.path.join("/images", filename)
            if not current_user.profile:
                profile = Profile(
                    photo=img_url,
                    title=form.title.data,
                    phone=form.phone.data,
                    about=form.about.data,
                    age=form.age.data,
                    city=form.city.data,
                    identifi_number=form.identifi_number.data,
                    marital_status=form.marital_status.data,
                    gender=form.gender.data,
                    user_id=current_user.id
                )
                if form.gender.data == 'other':
                    profile.gender = form.gender_text.data
                db.session.add(profile)
                db.session.commit()
                return redirect(url_for('profile'))
            else:
                p = Profile.query.filter_by(user_id=current_user.id).first()
                p.title=form.title.data,
                p.phone=form.phone.data,
                p.about=form.about.data,
                p.age=form.age.data,
                p.city=form.city.data,
                p.identifi_number=form.identifi_number.data,
                p.marital_status=form.marital_status.data,
                p.gender=form.gender.data,
                db.session.commit()
                return redirect(url_for('profile'))
    else:
        if current_user.profile:
            form.photo.data = current_user.profile[0].photo
            form.title.data = current_user.profile[0].title
            form.phone.data = current_user.profile[0].phone
            form.about.data = current_user.profile[0].about
            form.age.data = current_user.profile[0].age
            form.city.data = current_user.profile[0].city
            form.identifi_number.data = current_user.profile[0].identifi_number
            form.gender.data = current_user.profile[0].gender
    return render_template('resume-forms/profile.html', title='Profile', form=form)


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