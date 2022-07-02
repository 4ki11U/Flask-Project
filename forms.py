from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,RadioField)
from wtforms.validators import InputRequired, Length


class CourseForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(),
                                             Length(min=10, max=100)])
    description = TextAreaField('Course Description',
                                validators=[InputRequired(),
                                            Length(max=200)])
    price = IntegerField('Price', validators=[InputRequired()])
    level = RadioField('Level',
                       choices=['Beginner', 'Intermediate', 'Advanced'],
                       validators=[InputRequired()])
    available = BooleanField('Available', default='checked')


class UserCreate(FlaskForm):
    task_number = StringField('Номер задачи', validators=[InputRequired(), Length(min=1, max=35)])

    user_name = StringField('Имя пользователя', validators=[InputRequired(), Length(min=3, max=35)])

    user_surname = StringField('Фамилия пользователя', validators=[InputRequired(), Length(min=3, max=35)])

    callway_number = IntegerField('Логин CallWay', validators=[InputRequired()])

    project = RadioField('В каком проекте нужно создать ?',choices=['ЖКХ (20.120)', 'КВК\КТЕ (20.26)', 'ЖКХ + КВК'],
                         validators=[InputRequired()])

    DeskControl = BooleanField('DeskControl', default='')

    gorodok = BooleanField('ГородОК', default='')

    mail = BooleanField('Почти', default='')

    SmartBox = BooleanField('SmartBox', default='')

    VPN = BooleanField('VPN', default='')