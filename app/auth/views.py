# -*- coding:utf-8 -*-
from datetime import datetime
import os
from app.auth.utils import mkdirbydate, mkdir
from app.main.forms import PostForm, PhotoForm
from flask import abort, current_app
from flask.ext.login import login_user, login_required, logout_user, current_user
from app import db
from ..models import User, Post, Permission, ImgDir
from .forms import LoginForm, RegistrationForm
from werkzeug.utils import secure_filename

__author__ = 'lulizhou'
from flask import render_template, redirect, request, url_for, flash
from . import auth


@auth.route("/login", methods=['GET', 'POST'])
def login():
    logout_user()
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(request.args.get('next') or url_for('.post'))
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


# 获取该用户发布的文章
@auth.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    current_author = current_user.get_id()
    if current_author is None:
        abort(403)
    posts = Post.query.filter_by(author_id=current_author).order_by(Post.last_modified.desc())
    return render_template("auth/post.html", posts=posts)


# 新增文章
@auth.route('/post/add_new', methods=['GET', 'POST'])
@login_required
def add_post():
    form = PostForm()
    if current_user.can(Permission.WRITE_ARTICLES) and form.validate_on_submit():
        post = Post(body=form.body.data, title=form.title.data,
                    author=current_user._get_current_object())
        post.addTag(form.tag.data)
        db.session.add(post)
        flash("发布成功!")
        return redirect(url_for('.post'))
    return render_template("auth/add_post.html", form=form)


# 删除用户发布的文章
@auth.route('/post/delete?<int:id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    post_auther = Post.query.get_or_404(id)
    current_auther = current_user.get_id()
    if post_auther.author_id == int(current_auther) or current_user.is_administrator():
        post_auther.delTag(post_auther.getTagByArry())
        db.session.delete(post_auther)
        flash("删除成功!")
    return redirect(url_for('.post'))


# 编辑用户发布的文章
@auth.route('/post/edit?<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    post = Post.query.get_or_404(id)
    if current_user != post.author and not current_user.can(Permission.ADMINISTER):
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.body = form.body.data
        post.last_modified = datetime.utcnow()
        # print("传过来的标签有：%s" % form.tag.data)
        post.updateTag(form.tag.data)
        db.session.add(post)
        flash("The post has been Update!")
        return redirect(url_for('.post'))
    form.title.data = post.title
    form.body.data = post.body
    form.tag.data = post.getTagByString()
    return render_template('auth/edit_post.html', form=form)


# 上传图片
@auth.route('/post/upload', methods=('GET', 'POST'))
@login_required
def upload():
    form = PhotoForm()
    if form.validate_on_submit():
        safe_filename = secure_filename(form.photo.data.filename)
        # 七牛
        # data = form.photo.data
        # ret, info = qiniu_store.save(data, filename)
        upload_url = mkdir(current_app.config['UPLOADDIR'])
        picture_path = mkdirbydate(upload_url)
        save_path = os.path.join(picture_path[0], safe_filename)
        img_url = os.path.join(picture_path[1], safe_filename)
        form.photo.data.save(save_path)
        if not ImgDir.query.filter_by(img_dir=img_url).first():
            db.session.add(ImgDir(img_dir=img_url))
    filenames = ImgDir.query.order_by(ImgDir.add_time.desc()).all()
    return render_template('auth/upload.html', form=form, filenames=filenames)


@auth.route('/post/upload/delete?<int:id>', methods=('GET', 'POST'))
@login_required
def img_del(id):
    imgdir = ImgDir.query.get_or_404(id)
    uploadsdir = mkdir(current_app.config['UPLOADDIR'])
    img_url = os.path.join(uploadsdir, imgdir.img_dir)
    if os.path.exists(img_url):
        os.remove(img_url)
        db.session.delete(imgdir)
        flash("删除成功!")
    else:
        flash("图片不存在!%s\n%s\n%s" % (imgdir.img_dir, appdir, img_url))
    return redirect(url_for('auth.upload'))
