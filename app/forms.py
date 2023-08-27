from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired



class UserNameForm(FlaskForm):
    UserNameField = StringField('UserNameField', validators=[DataRequired()])
    UserSurNameField = StringField('UserSurNameField', validators=[DataRequired()])
    UserEmailField = StringField('UserEmailField', validators=[DataRequired()])
    
class CredentialsForm(FlaskForm):
    loginField = StringField('loginField', validators=[DataRequired()])
    passwordField= StringField('passwordField', validators=[DataRequired()])