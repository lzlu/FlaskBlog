# -*- coding:utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from app.models import User

__author__ = 'lulizhou'

# 定义登录表单
class LoginForm(Form):
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 64), Email()])

    password = PasswordField("密码", validators=[DataRequired()])
    remember_me = BooleanField("记住我")
    submit = SubmitField('登录')


# 定义用户注册表单
class RegistrationForm(Form):
    email = StringField("邮箱", validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField("用户名", validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                    '用户名只能包含字母数字点下划线')])
    password = PasswordField("密码", validators=[DataRequired(), EqualTo('password2', message='密码不匹配!')])

    password2 = PasswordField("再次确认密码", validators=[DataRequired()])
    submit = SubmitField('确认注册')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱被注册')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名被注册')

