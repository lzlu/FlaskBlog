# -*- coding:utf-8 -*-
from datetime import datetime
from flask import redirect, url_for, render_template, session, request, flash, abort, current_app
from . import main
from flask.ext.login import current_user, login_required
from app import db, qiniu_store
from .forms import NameForm, PostForm, PhotoForm
from ..models import User, Role, Permission, Post, Tags
from werkzeug.utils import secure_filename

__author__ = 'lulizhou'


@main.route('/', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Post.query.order_by(Post.last_modified.desc()).paginate(page,
                                                                         per_page=current_app.config[
                                                                             'FLASKY_POSTS_PER_PAGE'],
                                                                         error_out=False)
    posts = pagination.items
    return render_template("blog/index.html", posts=posts, pagination=pagination)


@main.route('/post/<int:id>', methods=['GET', 'POST'])
def post(id):
    post = Post.query.filter_by(id=id).first()
    tags = post.tags.all()
    return render_template('blog/post.html', post=post, tags=tags)


@main.route('/sortout', methods=['GET', 'POST'])
def sortout():
    allTags = Tags.query.order_by(Tags.id.desc())
    for allTag in allTags:
        print("便签名字是%s,有%s个" % (allTag.tag_name, allTag.tag_count))
    return render_template('blog/sortout.html', allTags=allTags)


@main.route('/sortout/<string:tag_name>', methods=['GET', 'POST'])
def tag_name(tag_name):
    thisTags = Tags.query.filter_by(tag_name=tag_name).first()
    posts = thisTags.posts.all()
    return render_template("blog/index.html", posts=posts)


@main.route('/upload/', methods=('GET', 'POST'))
def upload():
    form = PhotoForm()
    if form.validate_on_submit():
        filename = secure_filename(form.photo.data.filename)
        # 七牛
        # data = form.photo.data
        # ret, info = qiniu_store.save(data, filename)
        form.photo.data.save('app/static/uploads/' + filename)
        filenames = '/static/uploads/'+filename
        flash(filenames)
        return render_template('blog/upload.html', form=form, filenames=filenames)
    else:
        filename = None
        filenames = None
    return render_template('blog/upload.html', form=form, filenames=filenames)

