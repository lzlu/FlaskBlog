# -*- coding:utf-8 -*-
from datetime import datetime
from flask import redirect, url_for, render_template, session, request, flash, abort, current_app
from . import main
from flask.ext.login import current_user, login_required
from app import db
from .forms import NameForm, PostForm
from ..models import User, Role, Permission, Post, Tags

__author__ = 'lulizhou'


@main.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.last_modified.desc()).paginate(page,
                                                                         per_page=current_app.config[
                                                                             'FLASKY_POSTS_PER_PAGE'],
                                                                         error_out=False)
    posts = pagination.items
    return render_template("index.html", posts=posts, pagination=pagination)


@main.route("/post/add_post", methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if current_user.can(Permission.WRITE_ARTICLES) and form.validate_on_submit():
        post = Post(body=form.body.data, title=form.title.data,
                    author=current_user._get_current_object())
        post.addTag(form.tag.data)
        db.session.add(post)
        flash("发布成功!")
        return redirect(url_for('.index'))
    return render_template("add_post.html", form=form)


@main.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    post = Post.query.filter_by(id=id).first()
    tags = post.tags.all()
    return render_template('post.html', post=post, tags=tags)


@main.route('/delete', methods=['GET', 'POST'])
@login_required
def delete():
    if request.args is None:
        flash("参数错误！")
        return redirect(url_for('.index'))
    else:
        current_auther = current_user.get_id()
        post_auther = Post.query.filter_by(id=request.args['id']).first()
        if post_auther.author_id == int(current_auther) or current_user.is_administrator():
            print("这里的标签啊是%s" % post_auther.getTagByArry())
            post_auther.delTag(post_auther.getTagByArry())
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
        # print("传过来的标签有：%s" % form.tag.data)
        post.updateTag(form.tag.data)
        db.session.add(post)
        flash("The post has been Update!")
        return redirect(url_for('.index'))
    form.title.data = post.title
    form.body.data = post.body
    form.tag.data = post.getTagByString()
    return render_template('edit_post.html', form=form)


@main.route('/sortout', methods=['GET', 'POST'])
def sortout():
    allTags = Tags.query.order_by(Tags.id.desc())
    for allTag in allTags:
        print("便签名字是%s,有%s个" % (allTag.tag_name, allTag.tag_count))
    return render_template('sortout.html', allTags=allTags)


@main.route('/sortout/<string:tag_name>', methods=['GET', 'POST'])
def tag_name(tag_name):
    thisTags = Tags.query.filter_by(tag_name=tag_name).first()
    posts = thisTags.posts.all()
    return render_template("index.html", posts=posts)