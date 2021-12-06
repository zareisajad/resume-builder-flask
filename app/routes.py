import os
from datetime import datetime

from flask import render_template, redirect, url_for, request, flash, abort
from flask_login import current_user, login_required, login_user, logout_user
from werkzeug.utils import secure_filename
from flask_weasyprint import HTML, render_pdf

from app import app, login, db
from app.forms import ProfileForm, JobInfoForm, BackgroundForm, SkillForm, ProjectsForm, LinksForm
from app.models import Background, Skills, User, Profile, Projects, Links


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
            return redirect(url_for('sign_up'))
        user = User(fname=fname, lname=lname, email=email)
        user.set_password(password1)
        db.session.add(user)
        db.session.commit()
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
        if not current_user.profile:
            # create profile for user
            profile = Profile(
                title=form.title.data, phone=form.phone.data, age=age,
                about=form.about.data, city=form.city.data,
                identifi_number=form.identifi_number.data,
                marital_status=form.marital_status.data,
                user_id=current_user.id, gender=form.gender.data,
            )
            if form.photo.data:
                current_user.photo = upload_img(form.photo.data)
            db.session.add(profile)
            db.session.commit()
            return redirect(url_for('profile'))
        else:
            # updating profile information
            p = current_user.profile
            p.title=form.title.data
            p.phone=form.phone.data
            p.about=form.about.data
            p.age=age
            p.city=form.city.data
            p.identifi_number=form.identifi_number.data
            p.marital_status=form.marital_status.data
            p.gender=form.gender.data
            if form.photo.data:
                current_user.photo = upload_img(form.photo.data)
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


@app.route('/profile/job-info', methods=['POST', 'GET'])
@login_required
def job_info():
    form = JobInfoForm()
    if not current_user.profile:
        abort(404)
    if form.validate_on_submit():
        p = current_user.profile   
        p.job_status = form.job_status.data
        p.job_type = form.job_type.data
        p.excepted_salary = form.expected_salary.data
        p.military_service = form.military_service.data
        p.work_tech = form.work_tech.data
        db.session.commit()
        return redirect(url_for('job_info'))
    else:
        if current_user.profile:
            form.job_status.data = current_user.profile.job_status
            form.job_type.data = current_user.profile.job_type
            form.expected_salary.data = current_user.profile.excepted_salary
            form.military_service.data = current_user.profile.military_service
            form.work_tech.data = current_user.profile.work_tech
    return render_template(
        'resume-forms/job_info.html', title='Job Information', form=form
        )


@app.route('/profile/background', methods=['POST', 'GET'])
@login_required
def career_background():
    form = BackgroundForm()
    if form.validate_on_submit():
        background = Background(
            job_title=form.job_title.data,
            company_name=form.company_name.data,
            employment_date=form.employment_date.data,
            quit_date=form.quit_date.data,
            about_job=form.about_job.data,
            user_id=current_user.id
        )
        if not background.quit_date:
            background.quit_date = 'present'
        db.session.add(background)
        db.session.commit()
        return redirect(url_for('career_background'))
    jobs = current_user.background
    return render_template(
        'resume-forms/background.html',title='Career Background',form=form, jobs=jobs
    )


@app.route('/profile/background/delete/<id>', methods=['POST', 'GET'])
def delete_job(id):
    job = Background.query.filter_by(id=id).first()
    db.session.delete(job)
    db.session.commit()
    return redirect(url_for('career_background'))


@app.route('/profile/skills', methods=['POST', 'GET'])
@login_required
def skills():
    form = SkillForm()
    if form.validate_on_submit():
        skill = Skills(
            skill=form.skill.data,
            level=form.level.data,
            user_id=current_user.id
        )
        db.session.add(skill)
        db.session.commit()
    skills = current_user.skills
    return render_template(
        'resume-forms/skills.html', title='Skills', form=form, skills=skills
    )


@app.route('/profile/skills/delete/<id>', methods=['POST', 'GET'])
def delete_skill(id):
    skill = Skills.query.filter_by(id=id).first()
    db.session.delete(skill)
    db.session.commit()
    return redirect(url_for('skills'))


@app.route('/profile/projects', methods=['POST', 'GET'])
@login_required
def projects():
    form = ProjectsForm()
    if form.validate_on_submit():
        project = Projects(
            title=form.project_title.data,
            url=form.url.data,
            tech=form.tech.data,
            about=form.about.data,
            user_id=current_user.id
        )
        db.session.add(project)
        db.session.commit()
        return redirect(url_for('projects'))
    projects = current_user.projects
    return render_template(
        'resume-forms/projects.html', title='Projects', form=form, projects=projects
    )


@app.route('/profile/links', methods=['POST', 'GET'])
@login_required
def links():
    form = LinksForm()
    if form.validate_on_submit():
        link = Links(
            url=form.url.data,
            link_type=form.link_type.data,
            user_id=current_user.id
        )
        db.session.add(link)
        db.session.commit()
        return redirect(url_for('links'))
    links = current_user.links
    return render_template(
        'resume-forms/links.html', title='Links', form=form, links=links
    )


@app.route('/profile/resume', methods=['POST', 'GET'])
@login_required
def resume():
    html = render_template('resume.html')
    return render_pdf(HTML(string=html))
    # return render_template('resume.html')