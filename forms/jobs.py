import datetime
import sqlalchemy
from flask_wtf import FlaskForm
from sqlalchemy import orm
from wtforms import EmailField, PasswordField, BooleanField, SubmitField, SelectField, StringField, DateField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    job = StringField('Описание работы')
    work_size = StringField('Объем работы')
    collaborators = StringField('Соучастники')
    start_date = DateField('Начало работы')
    end_date = DateField('Конец работы')
    is_finished = BooleanField('Работа закончена')
    submit = SubmitField('Логин')
