# -*- coding:utf-8 -*-
from flask.ext.pagedown.fields import PageDownField
from flask.ext.wtf import Form
from flask.ext.wtf.file import FileRequired, FileAllowed, FileField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

__author__ = 'lulizhou'


class NameForm(Form):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


class PostForm(Form):
    title = StringField(validators=[DataRequired()])
    tag = StringField(validators=[DataRequired()])
    body = PageDownField(validators=[DataRequired()])
    submit = SubmitField('发表')

class PhotoForm(Form):
    photo = FileField("上传图片!", validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'gif'], '只能传jpg,png,gif')
    ])
    submit = SubmitField('上传')