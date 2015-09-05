# -*- coding:utf-8 -*-
from datetime import datetime
from flask import redirect, url_for, render_template, session, request, flash
from . import main
from flask.ext.login import current_user
from app import db
from .forms import NameForm, PostForm
from ..models import User, Role, Permission, Post

__author__ = 'lulizhou'


@main.route('/', methods=['GET', 'POST'])
def index():
    form = PostForm()
    if current_user.can(Permission.WRITE_ARTICLES) and form.validate_on_submit():
        post = Post(body=form.body.data, title=form.title.data,
                    author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('.index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template("index.html", form=form, posts=posts)


@main.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.args is None:
        flash("参数错误！")
        return redirect(url_for('.index'))
    else:
        current_auther = current_user.get_id()
        post_auther = Post.query.filter_by(id=request.args['id']).first()
        if post_auther.author_id == int(current_auther):
            db.session.delete(post_auther)
            flash("删除成功!")
        else:
            flash("你不能删！")
        return redirect(url_for('.index'))