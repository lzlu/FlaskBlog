# -*- coding:utf-8 -*-
from datetime import datetime
import bleach
from flask.ext.login import UserMixin, AnonymousUserMixin
from markdown import markdown
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from . import login_manager
from flask import current_app

__author__ = 'lulizhou'


class Permission:
    FOLLOW = 0x01
    COMMENT = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_COMMENTS = 0x08
    ADMINISTER = 0x80


# 权限类
class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    user = db.relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.FOLLOW |
                     Permission.COMMENT |
                     Permission.WRITE_ARTICLES, True),
            'Moderator': (Permission.FOLLOW |
                          Permission.COMMENT |
                          Permission.WRITE_ARTICLES, False),
            'Administrator': (0xff, False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()


# 用户类
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.role is None:
            if self.email == current_app.config['FLASKY_ADMIN']:
                self.role = Role.query.filter_by(permissions=0xff).first()
            if self.role is None:
                self.role = Role.query.filter_by(default=True).first()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 验证密码是否正确
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    def can(self, permissions):
        print(self.role.name)
        return self.role is not None and (self.role.permissions & permissions) == permissions

    # 判断是否有admin权限
    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def __repr__(self):
        return '<User %r>' % self.username


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False


login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# 关联表
Post_Tages = db.Table(
    'Post_Tages',
    db.Column('Post_id', db.Integer, db.ForeignKey('posts.id')),
    db.Column('Tage_id', db.Integer, db.ForeignKey('tags.id')),
)

# 文章类
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True)
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    last_modified = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    body_html = db.Column(db.Text)
    body_slug = db.Column(db.String(200))
    tags = db.relationship('Tags',
                           secondary=Post_Tages,
                           backref=db.backref('posts', lazy='dynamic'),
                           lazy='dynamic')

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        alowed_tages = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code', 'em',
                        'i', 'li', 'ol', 'pre', 'strong', 'ul', 'h1', 'h2', 'h3', 'p','div']
        target.body_html = bleach.linkify(bleach.clean(markdown(value, output_format='html'),
                                                       tags=alowed_tages, strip=True))
        target.body_slug = target.body_html[:200]

    @staticmethod
    def generate_fake(count=100):
        from random import seed, randint
        import forgery_py

        seed()
        user_count = User.query.count()
        for i in range(count):
            time = forgery_py.date.date(True)
            u = User.query.offset(randint(0, user_count - 1)).first()
            p = Post(body=forgery_py.lorem_ipsum.sentences(randint(1, 3)),
                     timestamp=time,
                     last_modified=time,
                     title=forgery_py.lorem_ipsum.title(),
                     author=u)
            db.session.add(p)
            db.session.commit()
    # 增加标签
    def addTag(self, tags):
        if type(tags) != type(set()):
            tags = tags.split(",")
        for tag in tags:
            now_Tag = Tags.query.filter_by(tag_name=tag).first()

            if not now_Tag:
                self.tags.append(Tags(tag_name=tag, tag_count=1))
            else:
                now_Tag.tag_count += 1
                self.tags.append(now_Tag)

    # 更新标签
    def updateTag(self, data):
        old = self.getTagByArry()
        new_tags = data.split(",")
        del_tags = {item for item in old if item not in new_tags}
        add_tags = {item for item in new_tags if item not in old}
        print("old=%s,new_tags=%s,del_tage=%s,add_tags=%s" % (old, new_tags, del_tags, add_tags))
        if del_tags is not None:
            self.delTag(del_tags)
        if add_tags is not None:
            self.addTag(add_tags)
    # 删除标签
    def delTag(self, data):
        for del_tag in data:
                remove_tag = Tags.query.filter_by(tag_name=del_tag).first()
                remove_tag.tag_count -= 1
                print("remove_tags=%s" % remove_tag.tag_name)
                if remove_tag is not None:
                    self.tags.remove(remove_tag)

    def getTagByArry(self):
        tags = self.tags.all()
        return tuple(tags[i].tag_name for i in range(len(tags)))

    def getTagByString(self):
        tags = self.tags.all()
        return ",".join(tags[i].tag_name for i in range(len(tags)))


db.event.listen(Post.body, 'set', Post.on_changed_body)


class Tags(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(64), index=True)
    tag_count = db.Column(db.Integer, default=0)
