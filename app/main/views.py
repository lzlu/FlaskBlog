# -*- coding:utf-8 -*-
from datetime import datetime
from flask import redirect, url_for, render_template, session, request, flash, abort, current_app
from . import main
from flask.ext.login import current_user, login_required
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
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.last_modified.desc()).paginate(page,
                                                                     per_page=current_app.config[
                                                                         'FLASKY_POSTS_PER_PAGE'],
                                                                     error_out=False)
    posts = pagination.items
    return render_template("index.html", form=form, posts=posts, pagination=pagination)


@main.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    post = Post.query.filter_by(id=id).first()
    return render_template('post.html', post=post)


@main.route('/delete', methods=['GET', 'POST'])
@login_required
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


@main.route('/edit/<int:id>', methods=['GET', 'POST'])
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
        db.session.add(post)
        flash("The post has been Update!")
        return redirect(url_for('.index'))
    form.title.data = post.title
    form.body.data = post.body
    return render_template('edit_post.html', form=form)