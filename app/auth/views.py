# -*- coding:utf-8 -*-
from flask.ext.login import login_user, login_required, logout_user
from app import db
from ..models import User
from .forms import LoginForm, RegistrationForm

__author__ = 'lulizhou'
from flask import render_template, redirect, request, url_for, flash
from . import auth


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('邮箱或者密码错误!')

    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash("你已经登出")
    return redirect(url_for('main.index'))
# 用户注册路由
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        flash('注册成功!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)