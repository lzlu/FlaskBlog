# -*- coding:utf-8 -*-
from flask.ext.pagedown.fields import PageDownField
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

__author__ = 'lulizhou'


class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class PostForm(Form):
    tag = StringField(validators=[DataRequired()])
    title = StringField(validators=[DataRequired()])
    body = PageDownField(validators=[DataRequired()])
    submit = SubmitField('发表')