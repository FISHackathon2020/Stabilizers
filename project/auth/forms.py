from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from project.models import Student, Representative

class RegistrationForm(FlaskForm):
    pass

class LoginForm(FlaskForm):
    pass