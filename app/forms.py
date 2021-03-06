import hashlib
from flask_wtf import Form
from wtforms import PasswordField
from wtforms import StringField
from wtforms.validators import DataRequired
from .models import User


class LoginForm(Form):
    user = StringField('user', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

    def get_user(self):
        return User.query.filter_by(user=self.user.data.lower(), password=hashlib.md5(
            self.password.data.encode('utf-8')).hexdigest()).first()


class RegisterForm(Form):
    user = StringField('user', validators=[DataRequired()])
    key = PasswordField('key', validators=[DataRequired()])
    email = StringField('email')