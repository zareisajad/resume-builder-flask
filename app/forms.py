from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from wtforms import StringField, DateField, SelectField


class ProfileForm(FlaskForm):
    photo = FileField(
        render_kw={'accept': 'image/*'},
        validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])]
    )
    fname = StringField(
        render_kw={'placeholder': 'first name'}, validators=[DataRequired()]
    )
    lname = StringField(
        render_kw={'placeholder': 'last name'}, validators=[DataRequired()]
    )
    phone = StringField(
        render_kw={'placeholder': 'phone'}, validators=[DataRequired()]
    )
    age = DateField()
    email = StringField(
        render_kw={'placeholder': 'email'},
        validators=[DataRequired(),
        Email(check_deliverability=True,message='Invalid Email!')]
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
        choices = [('single', 'Single'), ('married', 'Married')]
    )
    gender = SelectField(
        choices = [
            ('male', 'Male'), ('female', 'Female'),
            ('not-say', 'I\'d rather not to say'), ('other', 'Other')]
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