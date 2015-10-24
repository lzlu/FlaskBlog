# -*- coding:utf-8 -*-
from datetime import datetime
from flask import redirect, url_for, render_template, session, request, flash, abort, current_app, jsonify
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
    post = Post.query.get_or_404(id)
    tags = post.tags.all()
    return render_template('blog/post.html', post=post, tags=tags)


@main.route('/sortout', methods=['GET', 'POST'])
def sortout():
    allTags = Tags.query.order_by(Tags.id.desc())
    return render_template('blog/sortout.html', allTags=allTags)


@main.route('/sortout/<string:tag_name>', methods=['GET', 'POST'])
def tag_name(tag_name):
    thisTags = Tags.query.filter_by(tag_name=tag_name).first()
    if thisTags is None:
        abort(404)
    posts = thisTags.posts.all()
    return render_template("blog/sortout_index.html", posts=posts)


# 简历
@main.route('/about', methods=['GET', 'POST'])
def about():
    return render_template("resume/resume.html")


# 归档api
@main.route('/archives', methods=['GET', 'POST'])
def archives():
    return render_template('blog/sortout.html')


@main.route('/get_archives', methods=['GET', 'POST'])
def get_archives():
    # year = int(request.args.get('year', datetime.now().strftime('%Y'), type=int))
    page = int(request.args.get('page'))
    # year_stamp = datetime(year, 1, 1)
    # year_stamp_after = datetime(year + 1, 1, 1)
    Posts = Post.query.order_by(Post.timestamp.desc()).paginate(page, per_page=current_app.config['FLASKY_POSTS_PER_PAGE'], error_out=False).items
    # return render_template('blog/sortout.html', Posts=Posts, Year=year)
    print(Posts)
    if Posts:
        return jsonify({'result': 1, 'posts': [post.to_json4archives() for post in Posts]})
    else:
        return jsonify({'result': 0})
