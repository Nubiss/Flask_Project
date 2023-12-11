from app import repository
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from .repository import *


#class UserNameForm(FlaskForm):
    #UserNameField = StringField('UserNameField', validators=[DataRequired()])
    #UserSurNameField = StringField('UserSurNameField', validators=[DataRequired()])
    #UserEmailField = StringField('UserEmailField', validators=[DataRequired()])
    
    # class CredentialsForm(FlaskForm):
#     loginField = StringField('loginField', validators=[DataRequired()])
#     passwordField= StringField('passwordField', validators=[DataRequired()])

class RegistrationForm(FlaskForm):
    loginField = StringField('loginField', validators=[DataRequired(), Length(min=6, max=30)])
    passwordField= PasswordField('passwordField', validators=[DataRequired(), Length(min=8, max=30), EqualTo('passwordConfirmField', message="Пароли должны совпадать")])
    passwordConfirmField= PasswordField('passwordConfirmField', validators=[DataRequired(), Length(min=8, max=30), EqualTo('passwordField', message="Пароли должны совпадать")])
    
class AuthorizationForm(FlaskForm):
    loginField = StringField('loginField', validators=[DataRequired(), Length(min=6, max=30)])
    passwordField= StringField('passwordField', validators=[DataRequired(), Length(min=8, max=30)])
    
    
