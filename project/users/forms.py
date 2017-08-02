from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email

class LoginForm(FlaskForm):
    email = StringField("электр. почта:",  validators=[InputRequired("Пожалуйста введите ваш почтовый адрес."), Email("Это поле должно содержать корректный почтовый адрес.")])
    password = PasswordField("пароль:",  validators=[InputRequired("Пожалуйста введите ваш пароль."),])
    #remember_me = BooleanField("")
    submit = SubmitField("войти")
    