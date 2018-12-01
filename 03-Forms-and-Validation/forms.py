from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    income = StringField('Income',
                        validators=[DataRequired()])
    amt= IntegerField("Amount Of Loan", validators=[DataRequired()])
    Inc_rate= DecimalField("INC rate", validators=[DataRequired()])
    PMT= DecimalField("PMT", validators=[DataRequired()])
    Rate= DecimalField("Rate ", validators=[DataRequired()])
    LTV= DecimalField(" LTV", validators=[DataRequired()])


    submit = SubmitField('Sign Up')



class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
