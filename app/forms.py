from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired



class UserNameForm(FlaskForm):
    UserNameField = StringField('UserNameField', validators=[DataRequired()])
    UserSurNameField = StringField('UserSurNameField', validators=[DataRequired()])
    UserEmailField = StringField('UserEmailField', validators=[DataRequired()])