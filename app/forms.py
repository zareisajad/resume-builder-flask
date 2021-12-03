from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.fields.simple import TextAreaField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from wtforms import StringField, SelectField, IntegerField


class ProfileForm(FlaskForm):
    photo = FileField(
        render_kw={'accept': 'image/*'},
        validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'])]
    )
    phone = StringField(
        render_kw={'placeholder': 'phone'}, validators=[DataRequired()]
    )
    birthday_year = IntegerField(
        render_kw={'placeholder': 'your birthday year'}, validators=[DataRequired()]
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
    )
    about = TextAreaField(
        render_kw={
            'placeholder': 'Tell somthig about yourself...',
            'cols':'30', 'rows':'5'
        },
        validators=[DataRequired()]
    )