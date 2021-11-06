# store database models
from datetime import datetime
from time import time
import re

from sqlalchemy.sql.schema import PrimaryKeyConstraint

from . import db
from flask_login import UserMixin
from flask_security import UserMixin, RoleMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    roles = db.relationshipo('Role', secondary=roles_users, backref=db.backref('users'), lazy='dynamic')
    
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

roles_users = db.Table('roles_users', 
                       db.Column('user_id', db.Integer,
                        db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer,
                        db.ForeignKey('role.id'))
)
    


# class Details(db.Model):
#     grade = db.Column(db.String(150), default="")
#     major = db.Column(db.String(150), default="")


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    slug = db.Column(db.String(150), unique=True)
    body = db.Column(db.Text)
    create = db.Column(db.DateTime, default=datetime.now())

    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
        else:
            self.slug = (str(int(time())))

    def __repr__(self):
        return f'<Post id: {self.id}, title: {self.title}'
