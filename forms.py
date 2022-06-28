from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,RadioField)
from wtforms.validators import InputRequired, Length
from flask_wtf import FlaskForm


class UserCreating(FlaskForm):
    task_nomer = StringField('Номер Задачи', validators=[InputRequired(), Length(min=1, max=20)])

    user_name = StringField('Имя пользователя', validators=[InputRequired(), Length(min=3, max=20)])

    user_surname = StringField('Фамилия Пользователя', validators=[InputRequired(), Length(min=3, max=20)])

    callway_number = StringField('Фамилия Пользователя', validators=[InputRequired(), Length(min=3, max=20)])

    #level = RadioField('Level', choices=['Beginner', 'Intermediate', 'Advanced'], validators=[InputRequired()])

    deskcontrol = BooleanField('DeskControl', default='None')

    gorodok = BooleanField('Учетная Система ГородОК', default='None')

    email = BooleanField('Почта', default='None')

    smartbox = BooleanField('SmartBox', default='None')

    vpn = BooleanField('VPN', default='None')

