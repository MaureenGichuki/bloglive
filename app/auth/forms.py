from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User
from wtforms import ValidationError



class RegistrationForm(FlaskForm):
    email = StringField('Enter Email Address',validators=[DataRequired(),Email()])
    username = StringField('Enter username',validators = [DataRequired()])
    password = PasswordField('Password',validators = [DataRequired(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Password',validators = [DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
            if User.query.filter_by(email =data_field.data).first():
                raise ValidationError('This email is already taken')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('This username is taken')


class LoginForm(FlaskForm):
    email = StringField('Enter your Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Enter your Password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')