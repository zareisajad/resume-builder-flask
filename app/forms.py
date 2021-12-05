from flask.app import Flask
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from wtforms import StringField, SelectField, IntegerField, BooleanField


class ProfileForm(FlaskForm):
    photo = FileField(
        render_kw={'accept': 'image/*'},
        validators=[FileAllowed(['jpg', 'png', 'jpeg'])]
    )
    phone = StringField(
        render_kw={'placeholder': 'phone'},
        validators=[DataRequired()]
    )
    birthday_year = IntegerField(
        render_kw={'placeholder': 'your birthday year'},
        validators=[DataRequired()]
    )
    title = StringField(
        render_kw={'placeholder': 'Example(Full stack flask developer, etc...)'},
        validators=[DataRequired()]
    )
    city = StringField(
        render_kw={'placeholder': 'city'},
        validators=[DataRequired()]
    )
    identifi_number = StringField(
        render_kw={'placeholder': 'your identification number'},
        validators=[DataRequired()]
    )
    marital_status = SelectField(
        choices = [('single', 'Single'), ('married', 'Married')],
        validators=[DataRequired()]
    )
    gender = SelectField(
        choices = [
            ('male', 'Male'), ('female', 'Female'),
            ('not-say', 'I\'d rather not to say'), ('other', 'Other')],
        validators=[DataRequired()]
    )
    gender_text = StringField(
        render_kw={'placeholder': 'your gender'},
        validators=[DataRequired()]
    )
    about = TextAreaField(
        render_kw={
            'placeholder': 'Tell somthig about yourself...',
            'cols':'30', 'rows':'5'
        },
        validators=[DataRequired()]
    )


class JobInfoForm(FlaskForm):
    job_status = SelectField(
        choices = [
            ('active', 'in active search'),
            ('interested', 'interested in a new job'),
            ('not-looking', 'not looking for a job')
        ],
        validators=[DataRequired()]
    )
    job_type = SelectField(
        choices = [
            ('full-time', 'full-time'),
            ('part-time', 'part-time'),
            ('projects', 'i like do some projects')
        ],
        validators=[DataRequired()]
    )
    military_service = SelectField(
        choices = [
            ('completed', 'completed'), ('subject', 'subject')
        ],
        validators=[DataRequired()]
    )
    expected_salary = StringField(
        render_kw={'placeholder': 'example: 8000'},
        validators=[DataRequired()]
    )
    work_tech = StringField(
        render_kw={'placeholder': 'example: python,javascript,flask, etc...'},
        validators=[DataRequired()]
    )


class CreerBackForm(FlaskForm):
    job_title = StringField(
        render_kw={'placeholder': 'job title'},
        validators=[DataRequired()]
    )
    company_name = StringField(
        render_kw={'placeholder': 'company name'},
        validators=[DataRequired()]
    )
    employment_date = StringField(
        render_kw={'placeholder': 'employment date'},
        validators=[DataRequired()]
    )
    quit_date = StringField(
        render_kw={'placeholder': 'date you quit the job', 'id':'quitJob'},
        validators=[DataRequired()]
    )

    about_job = TextAreaField(
        render_kw={
            'placeholder': 'Tell more about this job...',
            'cols':'30', 'rows':'5'
        },
        validators=[DataRequired()]
    )