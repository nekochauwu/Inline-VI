from flask_wtf  import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import InputRequired, Email


class UserForm(FlaskForm):
    first_name = StringField('First Name', validators=[InputRequired('Please enter your first name')])
    last_name = StringField('Last Name')
    email = StringField('Email', validators=[InputRequired('Enter your email address'), Email('Enter a valid email address')])
    submit = SubmitField('Submit')