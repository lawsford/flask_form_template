from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    user_id = StringField("User ID", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")


class MainForm(FlaskForm):
    mandatory_string_field = StringField("text_field", validators=[DataRequired()])
    optional_string_field = StringField("text_field", validators=[])
    submit = SubmitField("SUBMIT")