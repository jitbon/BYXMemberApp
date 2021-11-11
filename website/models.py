# Group 5
# Jason Kim (jason.j.kim@vanderbilt.edu)
# Blaine Mitchell (blaine.z.mitchell@vanderbilt.edu)
# Bo Peng (bo.peng@vanderbilt.edu)
# Paul Woo (paul.woo@vanderbilt.edu)
# Homework 3

# store database models

from . import db
from datetime import datetime
from time import time
import re

from sqlalchemy.sql.schema import PrimaryKeyConstraint


from flask_login import UserMixin
from flask_security import UserMixin, RoleMixin
from sqlalchemy.sql import func

# Standard user model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    
# Roles for each user, relationship with User
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)

#Table holding the user and their role
roles_users = db.Table('roles_users', 
                       db.Column('user_id', db.Integer,
                        db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer,
                        db.ForeignKey('role.id'))
)
    


# class Details(db.Model):
#     grade = db.Column(db.String(150), default="")
#     major = db.Column(db.String(150), default="")

#slugifying is for creating unique urls that will be formed when an announcement is made by a member. Clicking on an announcement takes them to a unique page with that announcement. 
def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)

# Model for an announcement that will be stored to the database
class Announcement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    slug = db.Column(db.String(150), unique=True) # unique url for the announcement that will take the user to the announcement page
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
