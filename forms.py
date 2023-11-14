from flask_wtf import FlaskForm 
from wtforms import IntegerField, StringField, PasswordField , SubmitField,SelectField,DecimalField,FloatField,SelectMultipleField,RadioField,EmailField,FileField
from wtforms.validators import InputRequired, EqualTo

class RegistrationForm(FlaskForm):
    user_id = StringField("User id :", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    password2 = PasswordField("Confirm Password:", validators=[InputRequired(),EqualTo("password")])
    submit = SubmitField("Register")
    
class UserLoginForm(FlaskForm):
    user_id = StringField("User id :", validators=[InputRequired()])
    password = PasswordField("Password:", validators=[InputRequired()])
    submit = SubmitField("Login")
