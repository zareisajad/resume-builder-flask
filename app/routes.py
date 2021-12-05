import os
from datetime import datetime

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
            return redirect(url_for('sign_in'))
        login_user(user)
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
    if form.validate_on_submit():
        age = calculate_age(form.birthday_year.data)
        img = upload_img(form.photo.data)
        if not current_user.profile:
            # create profile for user
            profile = Profile(
                title=form.title.data, phone=form.phone.data, age=age,
                about=form.about.data, city=form.city.data,
                identifi_number=form.identifi_number.data,
                marital_status=form.marital_status.data,
                user_id=current_user.id, gender=form.gender.data,
            )
            current_user.photo = img
            db.session.add(profile)
            db.session.commit()
            return redirect(url_for('profile'))
        else:
            # updating profile information
            p = Profile.query.filter_by(user_id=current_user.id).first()
            p.title=form.title.data
            p.phone=form.phone.data
            p.about=form.about.data
            p.age=age
            p.city=form.city.data
            p.identifi_number=form.identifi_number.data
            p.marital_status=form.marital_status.data
            p.gender=form.gender.data
            current_user.photo = img  
            db.session.commit()
            return redirect(url_for('profile'))
    else:
        if current_user.profile:        
            form.title.data = current_user.profile.title
            form.phone.data = current_user.profile.phone
            form.about.data = current_user.profile.about
            form.birthday_year.data = current_user.profile.age
            form.city.data = current_user.profile.city
            form.identifi_number.data = current_user.profile.identifi_number
            form.gender.data = current_user.profile.gender
    return render_template('resume-forms/profile.html', title='Profile', form=form)


def calculate_age(year):
    """
    get profileform birthday_year field submited data
    and calculate current age,
    then return age
    """
    birthday_year = year
    today = datetime.now()
    date = today.date()
    current_year = date.strftime("%Y")
    age = int(current_year) - birthday_year
    return age


def upload_img(img_file):
    """
    get img file, secure its name and save it in static/images,
    then return its url to save in db.
    """
    img = img_file
    filename = img.filename
    if filename != '':
        img_name = filename.split('.')
        img_name[0] = current_user.fname + str(current_user.id) + '.'
        name = ''.join(img_name)
        filename = secure_filename(name)
        img.save(os.path.join(app.config["UPLOAD_PATH"], filename))
    img_url = os.path.join("/images", filename)
    return img_url


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