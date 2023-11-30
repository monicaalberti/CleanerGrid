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

class EnergyUseForm(FlaskForm):
    choices = ["lighting", "heating", "landry", "entertainment equipments", "fridge", "cooking facilities"]
    
    selections = SelectMultipleField('Make a selection of the equipment you have done to day at home:',
                                     choices=choices, validators =[DataRequired()])
    
    submit = SubmitField('Submit')
